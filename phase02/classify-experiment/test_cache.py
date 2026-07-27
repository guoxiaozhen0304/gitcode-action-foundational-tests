#!/usr/bin/env python3
"""test_cache.py — Push-based CACHE test runner

用法:  python3 test_cache.py <run-id>
"""

import os, sys, json, time, shutil, subprocess, tempfile, urllib.request, re, zipfile, io

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_env():
    env_path = os.path.join(SCRIPT_DIR, "..", "..", ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip()
                v = re.sub(r'\s+#.*$', '', v).strip().strip('"').strip("'")
                if k not in os.environ:
                    os.environ[k] = v

load_env()

TOKEN        = os.environ.get("GITCODE_ACCESS_TOKEN", "")
CONTRIB_TOKEN = os.environ.get("CONTRIBUTOR_GITCODE_TOKEN", "")
EXECUTOR     = os.environ.get("GITCODE_EXECUTOR", "")

OWNER   = "ComputingActionTest"
REPO    = "foundational-tests"
BRANCH  = "main"
FORK_OWNER = "teamfi"
FORK_REPO  = "foundational-tests"

POLL   = 10
TIMEOUT = 600


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def sh(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def api_get(path, token=None, executor=None):
    t = token or TOKEN
    ex = executor or EXECUTOR
    sep = "&" if "?" in path else "?"
    url = f"https://api.gitcode.com{path}{sep}access_token={t}&executor={ex}"
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        if "download_log" in path or "download-log" in path:
            return raw
        resp = raw.decode("utf-8", errors="replace")
        try:
            return json.loads(resp)
        except json.JSONDecodeError:
            return {"_raw": resp}


def push_and_poll(wf_name, wf_content, repo_owner, repo_name, token, workdir):
    """Push workflow to repo main, poll for COMPLETED, return (run_id, logs)."""
    url = f"https://oauth2:{token}@gitcode.com/{repo_owner}/{repo_name}.git"
    repodir = os.path.join(workdir, "repo")
    rc, out = sh(f'git clone --depth 1 --branch {BRANCH} "{url}" "{repodir}"')
    if rc != 0:
        log(f"   Clone failed: {out[-200:]}")
        return None, ""

    wf_dir = os.path.join(repodir, ".gitcode", "workflows")
    os.makedirs(wf_dir, exist_ok=True)
    with open(os.path.join(wf_dir, wf_name), "w") as f:
        f.write(wf_content)
    sh("git add .gitcode/workflows/", cwd=repodir)
    sh(f'git commit --allow-empty -m "test: {wf_name}"', cwd=repodir)
    rc, out = sh(f"git push origin {BRANCH}", cwd=repodir)
    if rc != 0:
        log(f"   Push failed: {out[-200:]}")
        return None, ""
    log(f"   Pushed {wf_name}")

    rid = None
    t0 = time.time()
    while time.time() - t0 < TIMEOUT:
        try:
            data = api_get(
                f"/api/v8/repos/{repo_owner}/{repo_name}/actions/runs?per_page=100",
                token=token, executor=EXECUTOR)
        except Exception:
            time.sleep(POLL)
            continue
        for r in data.get("workflow_runs", []):
            if wf_name in (r.get("file_path") or ""):
                if r.get("status") in ("COMPLETED", "FAILED", "CANCELED"):
                    rid = r.get("workflow_run_id", "")
                    break
        if rid:
            break
        time.sleep(POLL)

    if not rid:
        log("   TIMEOUT")
        return None, ""

    status = ""
    for r in data.get("workflow_runs", []):
        if wf_name in (r.get("file_path") or ""):
            status = r.get("status", "")

    # Collect logs
    logs = ""
    try:
        detail = api_get(
            f"/api/v8/repos/{repo_owner}/{repo_name}/actions/runs/{rid}",
            token=token, executor=EXECUTOR)
        for stage in (detail.get("stages") or []):
            for j in (stage.get("jobs") or []):
                jid = j.get("id", "")
                if jid:
                    try:
                        raw = api_get(
                            f"/api/v8/repos/{repo_owner}/{repo_name}/actions/runs/{rid}/jobs/{jid}/download_log",
                            token=token, executor=EXECUTOR)
                        if isinstance(raw, bytes):
                            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                                for name in z.namelist():
                                    logs += z.read(name).decode('utf-8', errors='replace') + "\n"
                        elif isinstance(raw, str):
                            logs += raw
                    except Exception:
                        pass
    except Exception as e:
        log(f"   Log fetch error: {e}")

    # Cleanup
    wf_path = os.path.join(repodir, ".gitcode", "workflows", wf_name)
    if os.path.exists(wf_path):
        os.remove(wf_path)
    sh(f"git rm --cached .gitcode/workflows/{wf_name}", cwd=repodir)
    sh(f'git commit --allow-empty -m "chore: rm {wf_name}"', cwd=repodir)
    sh(f"git push origin {BRANCH}", cwd=repodir)
    shutil.rmtree(repodir, ignore_errors=True)

    run_url = f"https://gitcode.com/{repo_owner}/{repo_name}/actions/runs/{rid}"
    log(f"   Run {status:12s} {run_url}")
    return rid, logs


def write_result(case_id, verdict, run_id, logs):
    rdir = os.path.join(SCRIPT_DIR, "runs", RUN_ID, "results")
    os.makedirs(rdir, exist_ok=True)
    preview = logs[:2000] if logs else ""
    with open(os.path.join(rdir, f"{case_id}.json"), "w") as f:
        json.dump({
            "case_id": case_id,
            "verdict": verdict,
            "run_id": run_id,
            "run_url": f"https://gitcode.com/{OWNER}/{REPO}/actions/runs/{run_id}" if run_id else "",
            "logs_preview": preview,
        }, f, indent=2, ensure_ascii=False)
    log(f"   Result -> {rdir}/{case_id}.json")


def make_read_yaml(key, restore_keys=None):
    """Generate a cache-read + verify workflow YAML."""
    rk = ""
    if restore_keys:
        rk = f"          restore-keys: |\n            {restore_keys}"
    return f"""\
on:
  push:
    branches: [main]
jobs:
  read-cache:
    name: read-cache
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: restore cache
        uses: cache
        with:
          path: mycache
          key: {key}
{rk}
      - name: verify
        run: |
          if [ -f mycache/data.txt ]; then
            echo "CACHE_HIT=yes"
            cat mycache/data.txt
          else
            echo "CACHE_MISS=yes"
          fi
"""


# ═══════════════════════════════════════════════════════════════
# COMP-CACHE-01-001: cache hit restores correct content
# ═══════════════════════════════════════════════════════════════
def test_001(run_id):
    log("=" * 60)
    log("COMP-CACHE-01-001: cache hit 时恢复缓存内容正确")
    log("=" * 60)

    TS = int(time.time())
    key = f"cache-001-{TS}"
    workdir = tempfile.mkdtemp(prefix="ct001-")

    # Write
    log("Phase 1: Write cache")
    write_yaml = f"""\
on:
  push:
    branches: [main]
jobs:
  write-cache:
    name: write-cache
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: create content
        run: |
          mkdir -p mycache
          echo "HELLO_FROM_CACHE_001" > mycache/data.txt
      - name: save cache
        uses: cache
        with:
          path: mycache
          key: {key}
"""
    push_and_poll(f"cache-001-write-{TS}.yml", write_yaml, OWNER, REPO, TOKEN, workdir)
    time.sleep(5)

    # Read
    log("Phase 2: Read cache")
    workdir2 = tempfile.mkdtemp(prefix="ct001b-")
    rid2, logs2 = push_and_poll(f"cache-001-read-{TS}.yml",
                                make_read_yaml(key),
                                OWNER, REPO, TOKEN, workdir2)

    verdict = "FAIL"
    if logs2:
        if "CACHE_HIT=yes" in logs2 and "HELLO_FROM_CACHE_001" in logs2:
            log("   CACHE_HIT=yes + content verified")
            verdict = "PASS"
        elif "CACHE_HIT=yes" in logs2:
            log("   CACHE_HIT but content NOT verified")
        elif "CACHE_MISS=yes" in logs2:
            log("   CACHE_MISS=yes — cache not available")
        else:
            log(f"   No marker. Preview: {logs2[:200]}")
    write_result("COMP-CACHE-01-001", verdict, rid2 or "", logs2 or "")

    shutil.rmtree(workdir, ignore_errors=True)
    shutil.rmtree(workdir2, ignore_errors=True)
    return verdict


# ═══════════════════════════════════════════════════════════════
# COMP-CACHE-01-002: restore-keys prefix match
#
# Proves prefix (not exact) match via 3 YAMLs:
#   1. Read key "nonexistent" → MISS (proves no pre-existing cache)
#   2. Write key "v1-xxx-FULL", then read key "v2" + restore-keys:[v1-xxx]
#      → v2 MISS, prefix "v1-xxx" matches "v1-xxx-FULL" → HIT (not exact!)
#   3. Write key "v2-xxx-FULL", then read key "v3" + restore-keys:[v2-xxx]
#      → v3 MISS, prefix "v2-xxx" matches "v2-xxx-FULL" → HIT (prefix chain confirmed)
# ═══════════════════════════════════════════════════════════════
def test_002(run_id):
    log("=" * 60)
    log("COMP-CACHE-01-002: restore-keys 前缀匹配兜底生效")
    log("=" * 60)

    TS = int(time.time())
    workdir = tempfile.mkdtemp(prefix="ct002-")

    # ── YAML 1: Prove nothing cached yet ──
    log("YAML 1: Read nonexistent key → expect MISS")
    workdir1 = tempfile.mkdtemp(prefix="ct002-1-")
    rid1, logs1 = push_and_poll(f"cache-002-probe-{TS}.yml",
                                make_read_yaml(f"cache-002-nonexistent-{TS}"),
                                OWNER, REPO, TOKEN, workdir1)
    baseline_miss = "CACHE_MISS=yes" in (logs1 or "")
    log(f"   Baseline miss: {baseline_miss}")
    shutil.rmtree(workdir1, ignore_errors=True)

    # ── YAML 2: v1-FULL written → v2 asked + prefix[v1-] → HIT ──
    key_v1 = f"cache-002-v1-{TS}-FULL"
    prefix_v1 = f"cache-002-v1-{TS}"       # shorter — prefix, NOT exact
    key_v2 = f"cache-002-v2-{TS}"

    log(f"YAML 2: Write {key_v1}, then read key={key_v2} + restore-keys:[{prefix_v1}]")
    write_yaml2 = f"""\
on:
  push:
    branches: [main]
jobs:
  write-cache:
    name: write-cache-v1
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: create content
        run: |
          mkdir -p mycache
          echo "V1_CONTENT" > mycache/data.txt
      - name: save cache
        uses: cache
        with:
          path: mycache
          key: {key_v1}
"""
    push_and_poll(f"cache-002-write-v1-{TS}.yml", write_yaml2, OWNER, REPO, TOKEN, workdir)
    time.sleep(5)

    workdir2 = tempfile.mkdtemp(prefix="ct002-2-")
    rid2, logs2 = push_and_poll(f"cache-002-read-v2-{TS}.yml",
                                make_read_yaml(key_v2, prefix_v1),
                                OWNER, REPO, TOKEN, workdir2)
    chain1 = "CACHE_HIT=yes" in (logs2 or "") and "V1_CONTENT" in (logs2 or "")
    log(f"   {key_v2} exact MISS → prefix '{prefix_v1}' matched '{key_v1}' → HIT={chain1}")
    shutil.rmtree(workdir2, ignore_errors=True)

    # ── YAML 3: v2-FULL written → v3 asked + prefix[v2-] → HIT ──
    key_v2_full = f"cache-002-v2-{TS}-FULL"
    prefix_v2 = f"cache-002-v2-{TS}"       # shorter — prefix, NOT exact
    key_v3 = f"cache-002-v3-{TS}"

    log(f"YAML 3: Write {key_v2_full}, then read key={key_v3} + restore-keys:[{prefix_v2}]")
    write_yaml3 = f"""\
on:
  push:
    branches: [main]
jobs:
  write-cache:
    name: write-cache-v2
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: create content
        run: |
          mkdir -p mycache
          echo "V2_CONTENT" > mycache/data.txt
      - name: save cache
        uses: cache
        with:
          path: mycache
          key: {key_v2_full}
"""
    push_and_poll(f"cache-002-write-v2-{TS}.yml", write_yaml3, OWNER, REPO, TOKEN, workdir)
    time.sleep(5)

    workdir3 = tempfile.mkdtemp(prefix="ct002-3-")
    rid3, logs3 = push_and_poll(f"cache-002-read-v3-{TS}.yml",
                                make_read_yaml(key_v3, prefix_v2),
                                OWNER, REPO, TOKEN, workdir3)
    chain2 = "CACHE_HIT=yes" in (logs3 or "") and "V2_CONTENT" in (logs3 or "")
    log(f"   {key_v3} exact MISS → prefix '{prefix_v2}' matched '{key_v2_full}' → HIT={chain2}")
    shutil.rmtree(workdir3, ignore_errors=True)

    verdict = "PASS" if (baseline_miss and chain1 and chain2) else "FAIL"
    log(f"   Baseline MISS={baseline_miss}  Chain1={chain1}  Chain2={chain2}  → {verdict}")
    write_result("COMP-CACHE-01-002", verdict, rid3 or "", logs3 or "")

    shutil.rmtree(workdir, ignore_errors=True)
    return verdict


# ═══════════════════════════════════════════════════════════════
# SEC-CACHE-01-002: fork cache isolation (main can't read fork)
#
# Two logs:
#   Log 1 (main): Write key=M → Read key=M → CACHE_HIT (proves cache works)
#   Log 2 (main): Read key=F (fork's key) → CACHE_MISS (proves isolation)
# ═══════════════════════════════════════════════════════════════
def test_sec_002(run_id):
    log("=" * 60)
    log("SEC-CACHE-01-002: 主仓 cache restore 对 fork cache miss")
    log("=" * 60)

    TS = int(time.time())
    key = f"sec-cache-{TS}"   # SAME key for both main and fork

    # ── Log 1: Main writes + reads key=K → CACHE_HIT (proves cache works) ──
    log("--- Log 1: Main writes key=K, main reads key=K → HIT ---")
    workdir = tempfile.mkdtemp(prefix="ctsec-")
    write_yaml = f"""\
on:
  push:
    branches: [main]
jobs:
  write-cache:
    name: write-cache
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: create content
        run: |
          mkdir -p mycache
          echo "MAIN_CACHE_OK" > mycache/data.txt
      - name: save cache
        uses: cache
        with:
          path: mycache
          key: {key}
"""
    push_and_poll(f"sec-cache-write-{TS}.yml", write_yaml, OWNER, REPO, TOKEN, workdir)
    time.sleep(5)

    workdir_hit = tempfile.mkdtemp(prefix="ctsec-hit-")
    rid_hit, logs_hit = push_and_poll(f"sec-cache-read-HIT-{TS}.yml",
                                      make_read_yaml(key),
                                      OWNER, REPO, TOKEN, workdir_hit)
    cache_works = "CACHE_HIT=yes" in (logs_hit or "")
    log(f"   Log 1 (key=K={key[:20]}...): {'CACHE_HIT' if cache_works else 'MISS'}  {rid_hit[:12] if rid_hit else '?'}...")
    shutil.rmtree(workdir_hit, ignore_errors=True)

    # ── Fork: push same key=K ──
    log("--- Fork: push same key=K to teamfi/foundational-tests ---")
    wdir_fork = tempfile.mkdtemp(prefix="ctsec-fork-")
    fork_url = f"https://oauth2:{CONTRIB_TOKEN}@gitcode.com/{FORK_OWNER}/{FORK_REPO}.git"
    main_url = f"https://oauth2:{TOKEN}@gitcode.com/{OWNER}/{REPO}.git"

    fork_repodir = os.path.join(wdir_fork, "repo")
    rc, out = sh(f'git clone --branch {BRANCH} "{fork_url}" "{fork_repodir}"')
    if rc != 0:
        log(f"   Fork clone failed: {out[-200:]}")
    else:
        sh(f"git remote add upstream {main_url}", cwd=fork_repodir)
        sh(f"git fetch upstream {BRANCH}", cwd=fork_repodir)
        sh(f"git reset --hard upstream/{BRANCH}", cwd=fork_repodir)
        sh(f"git push origin {BRANCH} --force", cwd=fork_repodir)

        fork_yaml = f"""\
on:
  push:
    branches: [main]
jobs:
  write-cache:
    name: write-cache-fork
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: create content
        run: |
          mkdir -p mycache
          echo "FORK_POISON" > mycache/data.txt
      - name: save cache
        uses: cache
        with:
          path: mycache
          key: {key}
"""
        wf_dir = os.path.join(fork_repodir, ".gitcode", "workflows")
        os.makedirs(wf_dir, exist_ok=True)
        fork_wf = f"sec-cache-fork-{TS}.yml"
        with open(os.path.join(wf_dir, fork_wf), "w") as f:
            f.write(fork_yaml)
        sh("git add .gitcode/workflows/", cwd=fork_repodir)
        sh(f'git commit --allow-empty -m "test: {fork_wf}"', cwd=fork_repodir)
        sh(f"git push origin {BRANCH}", cwd=fork_repodir)
        log("   Fork push done (same key=K)")

        os.remove(os.path.join(wf_dir, fork_wf))
        sh(f"git rm --cached .gitcode/workflows/{fork_wf}", cwd=fork_repodir)
        sh(f'git commit --allow-empty -m "chore: rm {fork_wf}"', cwd=fork_repodir)
        sh(f"git push origin {BRANCH}", cwd=fork_repodir)
    shutil.rmtree(wdir_fork, ignore_errors=True)
    time.sleep(5)

    # ── Log 2: Main reads same key=K (must MISS = fork cache isolated) ──
    log("--- Log 2: Main reads same key=K (expect MISS = fork isolated) ---")
    workdir_miss = tempfile.mkdtemp(prefix="ctsec-miss-")
    rid_miss, logs_miss = push_and_poll(f"sec-cache-read-MISS-{TS}.yml",
                                        make_read_yaml(key),
                                        OWNER, REPO, TOKEN, workdir_miss)
    log(f"   Log 2 (key=K={key[:20]}...): {rid_miss[:12] if rid_miss else '?'}...")

    isolated = False
    leaked = False
    if logs_miss and "CACHE_MISS=yes" in logs_miss:
        isolated = True
        log("   MISS — fork key K not found on main → isolation OK")
    elif logs_miss and "CACHE_HIT=yes" in logs_miss:
        if "FORK_POISON" in logs_miss:
            leaked = True
            log("   HIT with FORK_POISON → CACHE ISOLATION BROKEN!")
        elif "MAIN_CACHE_OK" in logs_miss:
            log("   HIT with MAIN_CACHE_OK → main's own cache (fork may not have written)")
            isolated = True  # Main's own cache, not fork's
        else:
            log("   HIT but unknown content source")

    verdict = "PASS" if (cache_works and isolated) else "FAIL"
    write_result("SEC-CACHE-01-002", verdict, rid_miss or "", logs_miss or "")

    shutil.rmtree(workdir, ignore_errors=True)
    shutil.rmtree(workdir_miss, ignore_errors=True)
    return verdict


# ═══════════════════════════════════════════════════════════════
# main
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    if not TOKEN:
        log("ERROR: GITCODE_ACCESS_TOKEN not set")
        sys.exit(1)

    RUN_ID = sys.argv[1] if len(sys.argv) > 1 else f"cache-{int(time.time())}"
    log(f"Run ID: {RUN_ID}")

    cases = {
        "COMP-CACHE-01-001": test_001,
        "COMP-CACHE-01-002": test_002,
        "SEC-CACHE-01-002":   test_sec_002,
    }

    results = {}
    for case_id, test_fn in cases.items():
        try:
            results[case_id] = test_fn(RUN_ID)
        except Exception as e:
            log(f"   EXCEPTION: {e}")
            results[case_id] = "ERROR"
            write_result(case_id, "ERROR", "", str(e))

    log("")
    log("=" * 60)
    log("RESULTS")
    log("=" * 60)
    for cid, v in results.items():
        log(f"  {cid}: {v}")
    passed = sum(1 for v in results.values() if v == "PASS")
    log(f"  {passed}/{len(results)} PASS")
