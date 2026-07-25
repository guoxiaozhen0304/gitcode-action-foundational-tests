#!/usr/bin/env python3
"""
run_pr_case.py — Deploy workflow, create PR, wait for pull_request trigger
Usage: python3 run_pr_case.py <case-yaml> <run-id>
"""
import os, sys, json, time, tempfile, subprocess, requests, zipfile, io, yaml

CASE_YAML = sys.argv[1] if len(sys.argv) > 1 else None
RUN_ID = sys.argv[2] if len(sys.argv) > 2 else "pr-test"
if not CASE_YAML:
    print("Usage: run_pr_case.py <case-yaml> <run-id>")
    sys.exit(1)

# Load env
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".env")
if os.path.exists(ENV_PATH):
    import re
    with open(ENV_PATH) as f:
        for line in f:
            line = re.sub(r'\s+#.*$', '', line.strip())
            if not line or "=" not in line: continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k not in os.environ: os.environ[k] = v

OWNER = os.environ.get("GITCODE_OWNER", "ComputingActionTest")
REPO = os.environ.get("GITCODE_REPO", "foundational-tests")
BRANCH = os.environ.get("GITCODE_BRANCH", "main")
TOKEN = os.environ["GITCODE_ACCESS_TOKEN"]
EXECUTOR = os.environ.get("GITCODE_EXECUTOR", "ccijunk")
API_V8 = "https://api.gitcode.com/api/v8"
API_V5 = "https://api.gitcode.com/api/v5"
TIMEOUT = 600
POLL = 10

# Read case
with open(CASE_YAML) as f:
    case = yaml.safe_load(f)

CASE_ID = case["id"]
WF_NAME = CASE_ID.replace('_', '-').lower() + ".yml"
WF_PATH = f".gitcode/workflows/{WF_NAME}"

wf = case.get("workflow", "")

# Ensure pull_request trigger
if "pull_request" not in wf:
    wf = wf.replace("on:", "on:\n  pull_request:\n    branches: [main]", 1)
if "workflow_dispatch" not in wf:
    wf = wf.replace("on:", "on:\n  workflow_dispatch:", 1)
wf += f"\n# pr-test-{int(time.time())}"

BRANCH_NAME = f"pr-test-{CASE_ID.replace('_', '-').lower()}-{int(time.time())}"

print(f"[*] Case: {CASE_ID} ({case.get('title','')})")
print(f"[*] Branch: {BRANCH_NAME}")

# Clone, deploy workflow to main
wd = tempfile.mkdtemp()
repo_url = f"https://oauth2:{TOKEN}@gitcode.com/{OWNER}/{REPO}.git"
subprocess.run(["git", "clone", repo_url, f"{wd}/repo"], capture_output=True)
repo_dir = f"{wd}/repo"

# Write workflow to main
os.makedirs(f"{repo_dir}/.gitcode/workflows", exist_ok=True)
with open(f"{repo_dir}/.gitcode/workflows/{WF_NAME}", "w") as f:
    f.write(wf)
subprocess.run(["git", "add", ".gitcode/workflows/"], cwd=repo_dir)
subprocess.run(["git", "commit", "-m", f"test: {CASE_ID} workflow"], cwd=repo_dir)
subprocess.run(["git", "push", "origin", BRANCH], cwd=repo_dir, capture_output=True)
print("[*] Workflow pushed to main")

# Create feature branch with a dummy change
subprocess.run(["git", "checkout", "-b", BRANCH_NAME], cwd=repo_dir)
with open(f"{repo_dir}/dummy-{CASE_ID}.txt", "w") as f:
    f.write(f"PR test for {CASE_ID}")
subprocess.run(["git", "add", "."], cwd=repo_dir)
subprocess.run(["git", "commit", "-m", f"pr-test: {CASE_ID}"], cwd=repo_dir)
subprocess.run(["git", "push", "origin", BRANCH_NAME], cwd=repo_dir, capture_output=True)
print(f"[*] Branch {BRANCH_NAME} pushed")

# Create PR
pr_resp = requests.post(
    f"{API_V5}/repos/{OWNER}/{REPO}/pulls",
    params={"access_token": TOKEN},
    headers={"Content-Type": "application/json"},
    json={"title": f"test: {CASE_ID}", "head": BRANCH_NAME, "base": BRANCH,
          "body": f"Automated PR test for {CASE_ID}"},
    timeout=15
)
if pr_resp.status_code != 200:
    print(f"[!] PR creation failed: {pr_resp.status_code} {pr_resp.text[:300]}")
    sys.exit(1)

pr_data = pr_resp.json()
pr_number = pr_data.get("object_id") or pr_data.get("id") or pr_data.get("number")
print(f"[*] PR created: #{pr_number}")
print(f"    URL: https://gitcode.com/{OWNER}/{REPO}/merge_requests/{pr_number}")

# Poll for pull_request triggered run
print(f"[*] Polling for PR-triggered run...")
elapsed = 0
run_id = None
while elapsed < TIMEOUT:
    resp = requests.get(
        f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs",
        params={"access_token": TOKEN, "executor": EXECUTOR, "per_page": 50, "pull_request_id": str(pr_number)},
        timeout=10
    )
    runs = resp.json().get("workflow_runs", [])
    for r in runs:
        if r.get("event") in ("MR", "PullRequest", "Pull_request") and r.get("file_path", "") == WF_PATH:
            run_id = r["workflow_run_id"]
            break
    if run_id:
        break
    time.sleep(POLL)
    elapsed += POLL
    if elapsed % 30 == 0:
        print(f"  [{elapsed}s] waiting...")

if not run_id:
    # Try broader search (no pull_request_id filter)
    resp = requests.get(
        f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs",
        params={"access_token": TOKEN, "executor": EXECUTOR, "per_page": 100, "branch": BRANCH},
        timeout=10
    )
    runs = resp.json().get("workflow_runs", [])
    for r in runs:
        if r.get("file_path", "") == WF_PATH and r.get("event") in ("MR", "PullRequest", "Pull_request"):
            run_id = r["workflow_run_id"]
            break

if not run_id:
    print("[!] No run found — PR may not have triggered workflow")
    sys.exit(1)

print(f"[*] Run: {run_id}")

# Poll for completion
while elapsed < TIMEOUT:
    resp = requests.get(
        f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs/{run_id}",
        params={"access_token": TOKEN, "executor": EXECUTOR},
        timeout=10
    )
    if resp.status_code != 200:
        time.sleep(POLL); elapsed += POLL
        continue
    status = resp.json().get("status", "")
    print(f"  [{elapsed}s] {status}")
    if status in ("COMPLETED", "FAILED", "CANCELED"):
        break
    time.sleep(POLL)
    elapsed += POLL

# Get logs
jresp = requests.get(
    f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs/{run_id}/jobs",
    params={"access_token": TOKEN, "executor": EXECUTOR},
    timeout=10
)
jobs = jresp.json().get("jobs", [])
for j in jobs[:2]:
    lresp = requests.get(
        f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs/{run_id}/jobs/{j['id']}/download_log",
        params={"access_token": TOKEN, "executor": EXECUTOR},
        timeout=15
    )
    try:
        z = zipfile.ZipFile(io.BytesIO(lresp.content))
        for n in z.namelist():
            log = z.read(n).decode("utf-8", errors="replace")
            print(f"\n=== LOG ({j.get('name','?')}) ===")
            print(log[-600:])
    except:
        pass

# Cleanup
subprocess.run(["git", "push", "origin", f":{BRANCH_NAME}"], cwd=repo_dir, capture_output=True)

# Write result
results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs", RUN_ID, "results")
os.makedirs(results_dir, exist_ok=True)
result = {
    "case_id": CASE_ID, "title": case.get("title", ""),
    "dimension": case.get("dimension", ""), "priority": case.get("priority", ""),
    "phase02_run": RUN_ID, "duration_seconds": elapsed,
    "verdict": "PASS" if status == "COMPLETED" else "FAIL",
    "gitcode_run_id": run_id, "run_status": status,
    "pr_number": pr_number
}
with open(f"{results_dir}/{CASE_ID}.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"\n=== RESULT: {CASE_ID} ===")
print(f"  Verdict: {result['verdict']}")
print(f"  Run: https://gitcode.com/{OWNER}/{REPO}/actions/runs/{run_id}")
print(f"  PR: https://gitcode.com/{OWNER}/{REPO}/merge_requests/{pr_number}")
