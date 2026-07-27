#!/usr/bin/env python3
"""
run_fork_pr.py — Fork repo, push workflow, create fork PR, poll
"""
import os, sys, json, re, time, tempfile, subprocess, requests

CASE_YAML = sys.argv[1] if len(sys.argv) > 1 else None
RUN_ID = sys.argv[2] if len(sys.argv) > 2 else "fork-pr"
if not CASE_YAML:
    print("Usage: run_fork_pr.py <case-yaml> <run-id>"); sys.exit(1)

# Load env
ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".env")
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            line = re.sub(r'\s+#.*$', '', line.strip())
            if not line or "=" not in line: continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k not in os.environ: os.environ[k] = v

OWNER = os.environ["GITCODE_OWNER"]
REPO = os.environ["GITCODE_REPO"]
BRANCH = os.environ.get("GITCODE_BRANCH", "main")
BOT_TOKEN = os.environ["GITCODE_ACCESS_TOKEN"]
CONTRIB_TOKEN = os.environ.get("CONTRIBUTOR_GITCODE_TOKEN", "")
EXECUTOR = os.environ.get("GITCODE_EXECUTOR", "ccijunk")
API_V5 = "https://api.gitcode.com/api/v5"
API_V8 = "https://api.gitcode.com/api/v8"

if not CONTRIB_TOKEN:
    print("ERROR: CONTRIBUTOR_GITCODE_TOKEN not set")
    sys.exit(1)

import yaml
with open(CASE_YAML) as f:
    case = yaml.safe_load(f)

CID = case["id"]
TITLE = case.get("title", "")
WF_NAME = CID.replace("_", "-").lower() + ".yml"
WF_PATH = f".gitcode/workflows/{WF_NAME}"
wf = case.get("workflow", "")
if "pull_request" not in wf:
    wf = wf.replace("on:", "on:\n  pull_request:\n    types: [open,update,reopen]\n    branches: [main]", 1)
if "workflow_dispatch" not in wf:
    wf = wf.replace("on:", "on:\n  workflow_dispatch:", 1)
wf += f"\n# fork-pr-{int(time.time())}"

FEAT_BRANCH = f"fork-test-{CID.replace('_','-').lower()}-{int(time.time())}"
wd = tempfile.mkdtemp()
log = lambda m: print(f"[{time.strftime('%H:%M:%S')}] {m}")

log(f"Case: {CID} — {TITLE}")

# ── 1. Push workflow to upstream main ──
log("Push workflow to upstream main...")
upstream_dir = f"{wd}/upstream"
subprocess.run(["git", "clone", f"https://oauth2:{BOT_TOKEN}@gitcode.com/{OWNER}/{REPO}.git", upstream_dir], capture_output=True)
os.makedirs(f"{upstream_dir}/.gitcode/workflows", exist_ok=True)
with open(f"{upstream_dir}/.gitcode/workflows/{WF_NAME}", "w") as f:
    f.write(wf)
subprocess.run(["git", "add", ".gitcode/workflows/"], cwd=upstream_dir)
subprocess.run(["git", "commit", "-m", f"wf: {CID}"], cwd=upstream_dir, capture_output=True)
subprocess.run(["git", "push", "origin", BRANCH], cwd=upstream_dir, capture_output=True)
log("Workflow pushed to main")

# ── 2. Use existing fork ──
fork_owner = "teamfi"
fork_repo = REPO
log(f"Fork: {fork_owner}/{fork_repo}")

# ── 3. Clone fork, sync with upstream, push branch ──
log(f"Cloning fork + pushing to {FEAT_BRANCH}...")
fork_dir = f"{wd}/fork"
r = subprocess.run(["git", "clone", f"https://oauth2:{CONTRIB_TOKEN}@gitcode.com/{fork_owner}/{fork_repo}.git", fork_dir],
    capture_output=True, text=True)
if r.returncode != 0:
    log(f"Clone failed: {r.stderr[-200:]}")
    sys.exit(1)
subprocess.run(["git", "remote", "add", "upstream", f"https://oauth2:{BOT_TOKEN}@gitcode.com/{OWNER}/{REPO}.git"], cwd=fork_dir, capture_output=True)
subprocess.run(["git", "fetch", "upstream", BRANCH], cwd=fork_dir, capture_output=True)
subprocess.run(["git", "reset", "--hard", f"upstream/{BRANCH}"], cwd=fork_dir, capture_output=True)
subprocess.run(["git", "push", "origin", BRANCH, "--force"], cwd=fork_dir, capture_output=True)
subprocess.run(["git", "checkout", "-b", FEAT_BRANCH], cwd=fork_dir)
with open(f"{fork_dir}/dummy-{CID}.txt", "w") as f:
    f.write(f"Fork PR test for {CID}")
subprocess.run(["git", "add", "."], cwd=fork_dir)
subprocess.run(["git", "commit", "-m", f"fork-pr: {CID}"], cwd=fork_dir, capture_output=True)
subprocess.run(["git", "push", "origin", FEAT_BRANCH], cwd=fork_dir, capture_output=True)
log(f"Fork branch {FEAT_BRANCH} pushed")

# ── 4. Create fork PR ──
log("Creating fork PR...")
time.sleep(10)  # Wait for platform to register the workflow
pr_resp = requests.post(
    f"{API_V5}/repos/{OWNER}/{REPO}/pulls",
    params={"access_token": CONTRIB_TOKEN},
    headers={"Content-Type": "application/json"},
    json={"title": f"test: {CID}", "head": f"{fork_owner}:{FEAT_BRANCH}", "base": BRANCH,
          "body": f"Fork PR test for {CID}"},
    timeout=15
)
pr_data = pr_resp.json()
pr_number = pr_data.get("iid") or pr_data.get("number")
if not pr_number:
    # Try without fork_owner prefix
    pr_resp = requests.post(
        f"{API_V5}/repos/{OWNER}/{REPO}/pulls",
        params={"access_token": CONTRIB_TOKEN},
        headers={"Content-Type": "application/json"},
        json={"title": f"test: {CID}", "head": FEAT_BRANCH, "base": BRANCH},
        timeout=15
    )
    pr_data = pr_resp.json()
    pr_number = pr_data.get("iid") or pr_data.get("number")

if not pr_number:
    log(f"PR creation failed: {json.dumps(pr_data)[:300]}")
    sys.exit(1)

log(f"Fork PR: #{pr_number}")

# ── 5. Poll for run ──
log("Polling for run...")
time.sleep(5)
elapsed = 0; run_id = None
while elapsed < 300:
    resp = requests.get(f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs", params={
        "access_token": BOT_TOKEN, "executor": EXECUTOR,
        "per_page": 50, "pull_request_id": str(pr_number)
    }, timeout=10)
    runs = resp.json().get("workflow_runs", [])
    for r in runs:
        if r.get("file_path", "") == WF_PATH:
            run_id = r["workflow_run_id"]; break
    if run_id: break
    time.sleep(10); elapsed += 10

if not run_id:
    log("No run found")
    sys.exit(1)

log(f"Run: {run_id}")
while elapsed < 900:
    resp = requests.get(f"{API_V8}/repos/{OWNER}/{REPO}/actions/runs/{run_id}", params={
        "access_token": BOT_TOKEN, "executor": EXECUTOR}, timeout=10)
    status = resp.json().get("status", "?")
    log(f"  [{status}] {elapsed}s")
    if status in ("COMPLETED", "FAILED", "CANCELED"): break
    time.sleep(10); elapsed += 10

# ── 6. Result ──
results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs", RUN_ID, "results")
os.makedirs(results_dir, exist_ok=True)
result = {"case_id": CID, "title": TITLE, "phase02_run": RUN_ID, "verdict": "PASS" if status == "COMPLETED" else "FAIL", "gitcode_run_id": run_id, "run_status": status, "pr_number": pr_number}
with open(f"{results_dir}/{CID}.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

log(f"RESULT: {CID} — {result['verdict']}")
log(f"Run: https://gitcode.com/{OWNER}/{REPO}/actions/runs/{run_id}")
log(f"PR: https://gitcode.com/{OWNER}/{REPO}/merge_requests/{pr_number}")

# Cleanup
subprocess.run(["git", "push", "origin", f":{FEAT_BRANCH}"], cwd=fork_dir, capture_output=True)
subprocess.run(["rm", "-rf", wd])
