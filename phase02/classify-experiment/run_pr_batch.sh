#!/bin/bash
# run_pr_batch.sh — Push workflow to main, create PR, poll for trigger
set -euo pipefail
: ${GITCODE_ACCESS_TOKEN:?}
: ${GITCODE_EXECUTOR:="ccijunk"}
: ${GITCODE_OWNER:="ComputingActionTest"}
: ${GITCODE_REPO:="foundational-tests"}
: ${GITCODE_BRANCH:="main"}

PR_DIR="$(cd "$1" && pwd)"
RUN_ID="${2:-pr-run}"
ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
API_V5="https://api.gitcode.com/api/v5"
API_V8="https://api.gitcode.com/api/v8"
RESULTS="${ROOT_DIR}/phase02/runs/${RUN_ID}/results"
mkdir -p "$RESULTS"

_log() { echo "[$(date +%H:%M:%S)] $*"; }

for y in "$PR_DIR"/*.yaml; do
    [ -f "$y" ] || continue
    CID=$(python3 -c "import yaml; print(yaml.safe_load(open('$y'))['id'])")
    WF_NAME=$(echo "$CID" | tr '[:upper:]' '[:lower:]' | sed 's/_/-/g').yml
    WF_PATH=".gitcode/workflows/${WF_NAME}"
    TITLE=$(python3 -c "import yaml; print(yaml.safe_load(open('$y'))['title'])")
    _log "=== $CID: $TITLE ==="

    # Clone and deploy workflow to main
    WD=$(mktemp -d)
    git clone "https://oauth2:${GITCODE_ACCESS_TOKEN}@gitcode.com/${GITCODE_OWNER}/${GITCODE_REPO}.git" "$WD/repo" 2>&1 | tail -1
    cd "$WD/repo"
    mkdir -p .gitcode/workflows

    # Write workflow
    python3 -c "
import yaml, time
with open('$y') as f: c = yaml.safe_load(f)
wf = c.get('workflow','')
if 'pull_request' not in wf: wf = wf.replace('on:', 'on:\n  pull_request:\n    branches: [main]', 1)
if 'workflow_dispatch' not in wf: wf = wf.replace('on:', 'on:\n  workflow_dispatch:', 1)
wf += f'\n# pr-{int(time.time())}'
with open('.gitcode/workflows/${WF_NAME}', 'w') as f: f.write(wf)
"
    git add .gitcode/workflows/ && git commit -m "test: ${CID} workflow" && git push origin "${GITCODE_BRANCH}" 2>&1 | tail -1

    # Create branch with dummy change
    PR_BRANCH="pr-${CID}"  # reuse branch name
    git checkout -b "$PR_BRANCH" 2>/dev/null || git checkout "$PR_BRANCH"
    date > "dummy-${CID}.txt" 2>/dev/null || echo "pr-test" > "dummy-${CID}.txt"
    git add . && git commit -m "pr: ${CID}" 2>/dev/null || true
    git push origin "$PR_BRANCH" 2>&1 | tail -1

    # Create PR
    PR_NUM=$(curl -sS -X POST "${API_V5}/repos/${GITCODE_OWNER}/${GITCODE_REPO}/pulls?access_token=${GITCODE_ACCESS_TOKEN}" \
        -H "Content-Type: application/json" \
        -d "{\"title\":\"test: ${CID}\",\"head\":\"${PR_BRANCH}\",\"base\":\"${GITCODE_BRANCH}\"}" 2>/dev/null | \
        python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('iid',''))" 2>/dev/null)
    _log "PR: #${PR_NUM}"
    rm -rf "$WD"

    # Poll for run triggered by this PR
    sleep 5
    ELAPSED=0
    RUN_ID_GC=""
    while [ $ELAPSED -lt 300 ]; do
        RESP=$(curl -sS "${API_V8}/repos/${GITCODE_OWNER}/${GITCODE_REPO}/actions/runs?access_token=${GITCODE_ACCESS_TOKEN}&executor=${GITCODE_EXECUTOR}&per_page=50&pull_request_id=${PR_NUM}" 2>/dev/null)
        RUN_ID_GC=$(echo "$RESP" | python3 -c "
import sys,json
for r in json.load(sys.stdin).get('workflow_runs',[]):
    if r.get('file_path','')=='${WF_PATH}':
        print(r.get('workflow_run_id',''))
        break
" 2>/dev/null)
        [ -n "$RUN_ID_GC" ] && break
        sleep 10; ELAPSED=$((ELAPSED+10))
    done

    if [ -z "$RUN_ID_GC" ]; then
        _log "No run found for ${WF_PATH}"
        continue
    fi

    # Poll for completion
    _log "Run: ${RUN_ID_GC:0:12}"
    while [ $ELAPSED -lt 900 ]; do
        STATUS=$(curl -sS "${API_V8}/repos/${GITCODE_OWNER}/${GITCODE_REPO}/actions/runs/${RUN_ID_GC}?access_token=${GITCODE_ACCESS_TOKEN}&executor=${GITCODE_EXECUTOR}" | \
            python3 -c "import sys,json; print(json.load(sys.stdin).get('status','?'))" 2>/dev/null)
        _log "  [$STATUS] ${ELAPSED}s"
        case "$STATUS" in COMPLETED|FAILED|CANCELED) break ;; esac
        sleep 10; ELAPSED=$((ELAPSED+10))
    done

    # Write result
    python3 -c "
import json
result = {
    'case_id': '${CID}', 'title': '${TITLE}',
    'phase02_run': '${RUN_ID}',
    'verdict': '${STATUS}' == 'COMPLETED' and 'PASS' or 'FAIL',
    'gitcode_run_id': '${RUN_ID_GC}', 'run_status': '${STATUS}',
    'pr_number': ${PR_NUM:-0}
}
with open('${RESULTS}/${CID}.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f'  Verdict: {result[\"verdict\"]}')
"
    _log ""
done

_log "Done. Results: $RESULTS"
ls "$RESULTS" | wc -l