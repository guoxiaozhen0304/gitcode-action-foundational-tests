#!/bin/bash
# run-case.sh — Phase 02 闭环执行脚本（dispatch 方式）
# Usage: ./run-case.sh <case-yaml-path> <run-id>
set -euo pipefail

CASE_YAML="${1:?Usage: $0 <case-yaml-path> <run-id>}"
RUN_ID="${2:?}"
: ${GITCODE_ACCESS_TOKEN:?请设置 GITCODE_ACCESS_TOKEN}
: ${GITCODE_COOKIE:?请设置 GITCODE_COOKIE（v2 dispatch API 必填）}
: ${GITCODE_EXECUTOR:="ccijunk"}
: ${GITCODE_API_BASE_URL:="https://api.gitcode.com"}
: ${GITCODE_WEB_API:="https://web-api.gitcode.com"}
: ${GITCODE_OWNER:="ComputingActionTest"}
: ${GITCODE_REPO:="foundational-tests"}
: ${GITCODE_BRANCH:="main"}
: ${TIMEOUT_SECONDS:=600}
: ${POLL_INTERVAL:=10}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RESULTS_DIR="${SCRIPT_DIR}/../runs/${RUN_ID}/results"
mkdir -p "$RESULTS_DIR"
VENV_PY="/tmp/phase02-venv/bin/python3"

_log() { echo "[$(date +%H:%M:%S)] $*"; }

# ── 1. Extract case fields ──────────────────────────────
_log "Loading case: $(basename $CASE_YAML)"

ENV_FILE="/tmp/case-env.sh"
$VENV_PY << PYEOF > "$ENV_FILE"
import yaml, json, re

def _fix_runs_on(m):
    indent = m.group(1)
    labels = re.findall(r'-\s+(\S+)', m.group(2))
    return f'{indent}runs-on: [{", ".join(labels)}]\n'

with open('${CASE_YAML}') as f:
    c = yaml.safe_load(f)
print(f'export CASE_ID="{c["id"]}"')
print(f'export CASE_TITLE="{c["title"]}"')
print(f'export CASE_DIM="{c["dimension"]}"')
print(f'export CASE_PRI="{c["priority"]}"')
print(f'export CASE_INTENT="{c["intent_ref"]}"')
print(f'export CASE_RESET="{c["teardown"]["reset"]}"')
print(f'export TRIGGER_EVENT="{c["trigger"]["event"]}"')
wf = c.get('workflow', '') or ''

# Normalize: ensure workflow_dispatch trigger exists + fix runs-on lists
if 'workflow_dispatch' not in (wf or ''):
    wf = re.sub(r'(on:\s*\n)', r'\1  workflow_dispatch:\n', wf)
wf = re.sub(r'^(\s+)runs-on:\s*\n((?:\s+-\s+\S+\n?)+)', _fix_runs_on, wf, flags=re.MULTILINE)

print(f'export WORKFLOW_FILE="/tmp/workflow-case.yml"')
with open('/tmp/workflow-case.yml', 'w') as wf_f:
    wf_f.write(wf)
print(f'export ASSERTIONS_FILE=\"/tmp/case-assertions.json\"')
with open('/tmp/case-assertions.json', 'w') as af:
    json.dump(c.get("assertions", []), af, ensure_ascii=False)
PYEOF

source "$ENV_FILE"
_log "CASE: $CASE_ID — $CASE_TITLE ($CASE_DIM/$CASE_PRI)"
START_TIME=$(date +%s)

# ── 2. Deploy workflow (push to register + trigger) ──────
_log "Deploying to ${GITCODE_OWNER}/${GITCODE_REPO}"
WORK_DIR=$(mktemp -d)
git clone "https://oauth2:${GITCODE_ACCESS_TOKEN}@gitcode.com/${GITCODE_OWNER}/${GITCODE_REPO}.git" "$WORK_DIR/repo" 2>&1 | tail -1
cd "$WORK_DIR/repo"
mkdir -p .gitcode/workflows

WF_NAME=$(echo "$CASE_ID" | tr '[:upper:]' '[:lower:]' | sed 's/_/-/g').yml

cp "$WORKFLOW_FILE" ".gitcode/workflows/${WF_NAME}"
echo "" >> ".gitcode/workflows/${WF_NAME}"
echo "# trigger: $(date +%s)" >> ".gitcode/workflows/${WF_NAME}"

git add .gitcode/workflows/
git commit -m "test: ${CASE_ID}"
git push origin "$GITCODE_BRANCH" 2>&1 | tail -1
PUSH_SHA=$(git rev-parse HEAD)
_log "Pushed: ${PUSH_SHA:0:8}"

# ── 3. Dispatch via v2 API ───────────────────────────────
_log "Dispatching..."
sleep 3

WF_PATH=".gitcode/workflows/${WF_NAME}"

DISPATCH_OUT=$($VENV_PY "${SCRIPT_DIR}/dispatch_workflow.py" "${WF_PATH}" 2>&1)

if echo "$DISPATCH_OUT" | grep -q '^ERROR:'; then
    _log "$DISPATCH_OUT"
    RUN_ID_GC=""
else
    RUN_ID_GC="$DISPATCH_OUT"
    _log "Dispatched: ${RUN_ID_GC:0:12}"
fi

rm -rf "$WORK_DIR"

# ── 4. Poll for run completion ───────────────────────────
_log "Polling ${RUN_ID_GC:0:12}..."
ELAPSED=0
while [ $ELAPSED -lt $TIMEOUT_SECONDS ]; do
    DETAIL=$(curl -sS "${GITCODE_API_BASE_URL}/api/v8/repos/${GITCODE_OWNER}/${GITCODE_REPO}/actions/runs/${RUN_ID_GC}?access_token=${GITCODE_ACCESS_TOKEN}&executor=${GITCODE_EXECUTOR}")
    STATUS=$(echo "$DETAIL" | python3 -c "import sys,json; print(json.load(sys.stdin).get('status',''))" 2>/dev/null || echo "?")
    _log "  [$STATUS] ${ELAPSED}s"
    case "$STATUS" in COMPLETED|FAILED|CANCELED) break ;; esac
    sleep $POLL_INTERVAL; ELAPSED=$((ELAPSED + POLL_INTERVAL))
done

if [ -z "$RUN_ID_GC" ] || [ $ELAPSED -ge $TIMEOUT_SECONDS ]; then
    VERDICT="TIMEOUT"
    RUN_CONCLUSION="timeout"
    JOB_COUNT=0
    LOGS=""
    _log "TIMEOUT after ${TIMEOUT_SECONDS}s"
else
    RUN_CONCLUSION=$(echo "$DETAIL" | python3 -c "import sys,json; print(json.load(sys.stdin).get('status',''))" 2>/dev/null || echo "?")

    # ── 5. Collect logs ───────────────────────────────
    JOBS_RESP=$(curl -sS "${GITCODE_API_BASE_URL}/api/v8/repos/${GITCODE_OWNER}/${GITCODE_REPO}/actions/runs/${RUN_ID_GC}/jobs?access_token=${GITCODE_ACCESS_TOKEN}&executor=${GITCODE_EXECUTOR}")
    JOB_COUNT=$(echo "$JOBS_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); jobs=d.get('jobs',[]); print(len(jobs))" 2>/dev/null || echo "0")

    LOGS=""
    if [ "$JOB_COUNT" -gt 0 ]; then
        JOB_IDS=$(echo "$JOBS_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(','.join(str(j['id']) for j in d.get('jobs',[])))" 2>/dev/null)
        for jid in $(echo "$JOB_IDS" | tr ',' ' '); do
            JOB_LOG_ZIP="/tmp/job-${jid}-log.zip"
            curl -sS -L -o "$JOB_LOG_ZIP" "${GITCODE_API_BASE_URL}/api/v8/repos/${GITCODE_OWNER}/${GITCODE_REPO}/actions/runs/${RUN_ID_GC}/jobs/${jid}/download_log?access_token=${GITCODE_ACCESS_TOKEN}&executor=${GITCODE_EXECUTOR}" 2>/dev/null
            JOB_LOG=$($VENV_PY -c "
import zipfile
try:
    with zipfile.ZipFile('${JOB_LOG_ZIP}') as z:
        for name in z.namelist():
            print(z.read(name).decode('utf-8', errors='replace'))
except Exception as e:
    print(f'[LOG_ERROR: {e}]')
" 2>/dev/null || echo "")
            rm -f "$JOB_LOG_ZIP"
            LOGS="${LOGS}
=== JOB #${jid} ===
${JOB_LOG}"
        done
    fi
    _log "Collected ${JOB_COUNT} job(s), $(echo "$LOGS" | wc -l) log lines"

    # ── 6. Assert ─────────────────────────────────────
    LOGS_FILE="/tmp/case-logs-${CASE_ID}.txt"
    echo "$LOGS" > "$LOGS_FILE"
    ASSERT_RESULTS=$($VENV_PY << PYEOF
import json, sys
with open('${LOGS_FILE}', 'r') as f:
    logs = f.read()
conclusion = "${RUN_CONCLUSION}"
with open('${ASSERTIONS_FILE}', 'r') as f:
    assertions = json.load(f)

results = []
for a in assertions:
    atype = a.get('type', '')
    target = a.get('target', '')
    rubric = a.get('rubric', '')
    contained = a.get('contains', '')
    equals = a.get('equals', 'COMPLETED')
    passed = False

    if target == 'run_logs':
        if contained:
            passed = str(contained) in logs
        elif ruby:
            passed = rubric in logs
        elif a.get('must_not_contain_secret'):
            secret_val = a.get('must_not_contain_secret', '')
            passed = secret_val not in logs
        else:
            passed = conclusion == 'COMPLETED' and len(logs) > 100
    elif target == 'run_status':
        if atype == 'negative':
            passed = (conclusion != equals)
        else:
            passed = (conclusion == equals)
    else:
        passed = conclusion == 'COMPLETED'

    results.append({'type': atype, 'target': target, 'pass': passed, 'rubric': rubric})

all_pass = all(r['pass'] for r in results)
print(json.dumps({'verdict': 'PASS' if all_pass else 'FAIL', 'results': results}, ensure_ascii=False))
PYEOF
)
    rm -f "$LOGS_FILE"
    VERDICT=$(echo "$ASSERT_RESULTS" | python3 -c "import sys,json; print(json.load(sys.stdin).get('verdict','ERROR'))" 2>/dev/null || echo "ERROR")
    echo "$ASSERT_RESULTS" > /tmp/case-assert-results.json
fi

# ── 7. Write result ─────────────────────────────────────
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

$VENV_PY << PYEOF
import json
with open('/tmp/case-assert-results.json', 'r') as f:
    ar = json.load(f)
result = {
  'case_id': '${CASE_ID}',
  'title': '${CASE_TITLE}',
  'dimension': '${CASE_DIM}',
  'priority': '${CASE_PRI}',
  'intent_ref': '${CASE_INTENT}',
  'phase02_run': '${RUN_ID}',
  'start_time': ${START_TIME},
  'end_time': ${END_TIME},
  'duration_seconds': ${DURATION},
  'verdict': '${VERDICT}',
  'gitcode_run_id': '${RUN_ID_GC:-}',
  'run_conclusion': '${RUN_CONCLUSION:-}',
  'job_count': ${JOB_COUNT:-0},
  'assertion_results': ar.get('results', [])
}
with open('${RESULTS_DIR}/${CASE_ID}.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
PYEOF

# ── 8. Summary ──────────────────────────────────────────
_log ""
_log "═══════════════════════════════════════"
_log "RESULT: ${CASE_ID}"
_log "  Verdict: ${VERDICT}"
_log "  Duration: ${DURATION}s"
_log "  GitCode Run: #${RUN_ID_GC:-N/A}"
_log "  Result: ${RESULTS_DIR}/${CASE_ID}.json"
_log "═══════════════════════════════════════"

[ "$VERDICT" = "PASS" ]
