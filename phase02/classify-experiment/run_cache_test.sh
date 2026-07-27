#!/usr/bin/env bash
# run_cache_test.sh — 两阶段 push 测试 CACHE 用例
#
# 用法:
#   ./run_cache_test.sh <case-yaml> <run-id>
#
# 策略（所有 case 改用 on: push）:
#   COMP-CACHE-01-001: Phase 1 写缓存 → Phase 2 读缓存 → CACHE_HIT=yes
#   COMP-CACHE-01-002: Phase 1 写 v1-key 缓存 → Phase 2 用 v2-key+restore-keys 读 → HIT_VIA_RESTORE_KEYS
#   SEC-CACHE-01-002:  Phase 1 fork push 写缓存 → Phase 2 主仓 push 读缓存 → CACHE_MISS=yes

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

source_env() {
    local envf="$1"
    if [ -f "$envf" ]; then
        while IFS='=' read -r key val; do
            key="${key#"${key%%[![:space:]]*}"}"
            key="${key%"${key##*[![:space:]]}"}"
            [[ -z "$key" || "$key" =~ ^# ]] && continue
            val="${val#\"}"; val="${val%\"}"; val="${val#\'}"; val="${val%\'}"
            val="${val%%[[:space:]]*#*}"
            val="${val%"${val##*[![:space:]]}"}"
            export "$key=$val"
        done < "$envf"
    fi
}
source_env "$REPO_DIR/.env"

# ── 配置 ──
TOKEN="${GITCODE_ACCESS_TOKEN:?}"
CONTRIB_TOKEN="${CONTRIBUTOR_GITCODE_TOKEN:?}"
EXECUTOR="${GITCODE_EXECUTOR:?}"
OWNER="ComputingActionTest"
REPO="foundational-tests"
BRANCH="main"
FORK_OWNER="teamfi"
FORK_REPO="foundational-tests"
API_V8="https://api.gitcode.com/api/v8"
TIMEOUT=600
POLL=10
TS="$(date +%s)"

CASE_YAML="$1"
RUN_ID="$2"
CASE_ID="$(python3 -c "
import yaml,sys
with open('$CASE_YAML') as f:
    d=yaml.safe_load(f)
print(d.get('id','unknown'))
")"
CASE_TITLE="$(python3 -c "
import yaml,sys
with open('$CASE_YAML') as f:
    d=yaml.safe_load(f)
print(d.get('title',''))
")"

WORKDIR="$(mktemp -d /tmp/cache-test-XXXXX)"
trap 'rm -rf "$WORKDIR"' EXIT

log() { echo "[$(date +%H:%M:%S)] $*" | ts '%H:%M:%S' 2>/dev/null || echo "[$(date +%H:%M:%S)] $*"; }

api_get() {
    local path="$1"
    local sep="&"
    [[ "$path" != *\?* ]] && sep="?"
    curl -sS "${API_V8}${path}${sep}access_token=${TOKEN}&executor=${EXECUTOR}" 2>/dev/null
}

# ── 核心函数: push workflow + poll + 收集日志 ──
# $1 = workflow file name  $2 = YAML content  $3 = repo url  $4 = working dir
push_and_collect() {
    local wf_name="$1"
    local wf_content="$2"
    local repo_url="$3"
    local workdir="$4"

    local repodir="$workdir/repo"
    git clone --depth 1 --branch "$BRANCH" "$repo_url" "$repodir" 2>&1 | tail -1

    mkdir -p "$repodir/.gitcode/workflows"
    echo "$wf_content" > "$repodir/.gitcode/workflows/$wf_name"
    git -C "$repodir" add .gitcode/workflows/
    git -C "$repodir" commit --allow-empty -m "test: $wf_name"
    git -C "$repodir" push origin "$BRANCH" 2>&1 | tail -1
    log "   Pushed $wf_name"

    local rid=""
    local t0=$SECONDS
    while (( SECONDS - t0 < TIMEOUT )); do
        local runs
        runs="$(api_get "/repos/${OWNER}/${REPO}/actions/runs?per_page=100")"
        rid="$(echo "$runs" | python3 -c "
import sys,json
for r in json.load(sys.stdin).get('workflow_runs',[]):
    if '$wf_name' in (r.get('file_path','')):
        if r.get('status')=='COMPLETED' or r.get('status')=='FAILED' or r.get('status')=='CANCELED':
            print(r['workflow_run_id']); break
")"
        [[ -n "$rid" ]] && break
        sleep "$POLL"
    done
    if [[ -z "$rid" ]]; then
        log "   TIMEOUT: no completed run for $wf_name"
        echo "TIMEOUT"
        return 1
    fi
    log "   Run ${rid:0:12}... done"

    # 收集日志
    local logs=""
    local detail
    detail="$(api_get "/repos/${OWNER}/${REPO}/actions/runs/${rid}")"
    # 从 stages 获取所有 job 日志
    logs="$(echo "$detail" | python3 -c "
import sys,json,urllib.request
d=json.load(sys.stdin)
result=''
for stage in (d.get('stages') or []):
    for j in (stage.get('jobs') or []):
        jid=j.get('id','')
        if jid:
            url='${API_V8}/repos/${OWNER}/${REPO}/actions/runs/${rid}/jobs/'+jid+'/download_log?access_token=${TOKEN}&executor=${EXECUTOR}'
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    result+=r.read().decode('utf-8',errors='replace')
            except: pass
print(result)
")"

    # 清理 workflow 文件
    rm -f "$repodir/.gitcode/workflows/$wf_name"
    git -C "$repodir" rm --cached ".gitcode/workflows/$wf_name" 2>/dev/null || true
    git -C "$repodir" commit --allow-empty -m "chore: rm $wf_name" 2>/dev/null || true
    git -C "$repodir" push origin "$BRANCH" 2>&1 | tail -1

    echo "$rid"
    echo "$logs"
    return 0
}

# ──────────────────────────────────────────────────
# COMP-CACHE-01-001: cache hit 时恢复缓存内容正确
# ──────────────────────────────────────────────────
test_001() {
    log "== COMP-CACHE-01-001: cache hit restores content =="
    local key="cache-001-${TS}"
    local wf_dir="$WORKDIR/001"; mkdir -p "$wf_dir"
    local repo_url="https://oauth2:${TOKEN}@gitcode.com/${OWNER}/${REPO}.git"

    # Phase 1: 写缓存
    log "Phase 1: Write cache"
    local write_wf="cache-001-write-${TS}.yml"
    local write_content
    read -r -d '' write_content <<'YAML' || true
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
          key: __KEY__
YAML
    write_content="${write_content/__KEY__/${key}}"

    local rid1 logs1
    local out1
    out1="$(push_and_collect "$write_wf" "$write_content" "$repo_url" "$wf_dir")" || true
    rid1="$(echo "$out1" | head -1)"
    logs1="$(echo "$out1" | tail -n +2)"
    log "   Phase 1 run: ${rid1:0:12}..."

    # Phase 2: 读缓存
    log "Phase 2: Read cache"
    sleep 5
    local wf_dir2="$WORKDIR/001b"; mkdir -p "$wf_dir2"
    local read_wf="cache-001-read-${TS}.yml"
    local read_content
    read -r -d '' read_content <<'YAML' || true
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
          key: __KEY__
      - name: verify
        run: |
          if [ -f mycache/data.txt ]; then
            echo "CACHE_HIT=yes"
            cat mycache/data.txt
          else
            echo "CACHE_MISS=yes"
          fi
YAML
    read_content="${read_content/__KEY__/${key}}"

    local out2
    out2="$(push_and_collect "$read_wf" "$read_content" "$repo_url" "$wf_dir2")" || true
    local rid2 logs2
    rid2="$(echo "$out2" | head -1)"
    logs2="$(echo "$out2" | tail -n +2)"

    local verdict="FAIL"
    if echo "$logs2" | grep -q "CACHE_HIT=yes"; then
        log "   CACHE_HIT=yes"
        if echo "$logs2" | grep -q "HELLO_FROM_CACHE_001"; then
            log "   Content verified: HELLO_FROM_CACHE_001"
            verdict="PASS"
        else
            log "   Content NOT found in cache"
        fi
    elif echo "$logs2" | grep -q "CACHE_MISS=yes"; then
        log "   CACHE_MISS=yes — cache not available"
    else
        log "   No CACHE_HIT/CACHE_MISS marker in logs"
    fi
    log "   Verdict: $verdict"
    write_result "COMP-CACHE-01-001" "$verdict" "$rid2" "$logs2"
}
test_001_oid="COMP-CACHE-01-001"
test_001_oid="${test_001_oid#COMP-CACHE-}"
test_001_oid="${test_001_oid#SEC-CACHE-}"

# ────────────────────────────────────────────────────
# COMP-CACHE-01-002: restore-keys 前缀匹配兜底生效
# ────────────────────────────────────────────────────
test_002() {
    log "== COMP-CACHE-01-002: restore-keys prefix fallback =="
    local key_v1="cache-002-v1-${TS}"
    local key_v2="cache-002-v2-${TS}"
    local prefix="cache-002-v1-${TS}"
    local wf_dir="$WORKDIR/002"; mkdir -p "$wf_dir"
    local repo_url="https://oauth2:${TOKEN}@gitcode.com/${OWNER}/${REPO}.git"

    # Phase 1: 用 v1 key 写缓存
    log "Phase 1: Write cache with v1 key"
    local write_wf="cache-002-write-${TS}.yml"
    local write_content
    read -r -d '' write_content <<'YAML' || true
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
          echo "V1_CONTENT" > mycache/data.txt
      - name: save cache
        uses: cache
        with:
          path: mycache
          key: __KEY_V1__
YAML
    write_content="${write_content/__KEY_V1__/${key_v1}}"

    push_and_collect "$write_wf" "$write_content" "$repo_url" "$wf_dir" > /dev/null
    log "   Phase 1 done"

    # Phase 2: 用 v2 key + restore-keys 前缀回退 v1
    log "Phase 2: Read with v2 key + restore-keys=v1 prefix"
    sleep 5
    local wf_dir2="$WORKDIR/002b"; mkdir -p "$wf_dir2"
    local read_wf="cache-002-read-${TS}.yml"
    local read_content
    read -r -d '' read_content <<'YAML' || true
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
          key: __KEY_V2__
          restore-keys: |
            __PREFIX__
      - name: verify
        run: |
          if [ -f mycache/data.txt ]; then
            echo "CACHE_HIT=yes"
            cat mycache/data.txt
          else
            echo "CACHE_MISS=yes"
          fi
YAML
    read_content="${read_content/__KEY_V2__/${key_v2}}"
    read_content="${read_content/__PREFIX__/${prefix}}"

    local out2
    out2="$(push_and_collect "$read_wf" "$read_content" "$repo_url" "$wf_dir2")" || true
    local rid2 logs2
    rid2="$(echo "$out2" | head -1)"
    logs2="$(echo "$out2" | tail -n +2)"

    local verdict="FAIL"
    if echo "$logs2" | grep -q "CACHE_HIT=yes"; then
        if echo "$logs2" | grep -q "V1_CONTENT"; then
            log "   restore-keys worked: v1 content restored via v2 key"
            verdict="PASS"
        else
            log "   Cache hit but content mismatch"
        fi
    elif echo "$logs2" | grep -q "CACHE_MISS=yes"; then
        log "   CACHE_MISS=yes — restore-keys fallback did NOT work"
    else
        log "   No CACHE_HIT/CACHE_MISS marker"
    fi
    log "   Verdict: $verdict"
    write_result "COMP-CACHE-01-002" "$verdict" "$rid2" "$logs2"
}

# ──────────────────────────────────────────────────
# SEC-CACHE-01-002: 主仓 cache restore 对 fork cache miss
# ──────────────────────────────────────────────────
test_sec_002() {
    log "== SEC-CACHE-01-002: fork cache isolation =="
    local key="sec-cache-002-${TS}"
    local fork_url="https://oauth2:${CONTRIB_TOKEN}@gitcode.com/${FORK_OWNER}/${FORK_REPO}.git"
    local main_url="https://oauth2:${TOKEN}@gitcode.com/${OWNER}/${REPO}.git"

    # Phase 1: 在 fork 里写缓存
    log "Phase 1: Fork ($FORK_OWNER/$FORK_REPO) write cache"
    local wf_dir_fork="$WORKDIR/sec-fork"; mkdir -p "$wf_dir_fork"
    local write_wf="sec-cache-fork-${TS}.yml"
    local write_content
    read -r -d '' write_content <<'YAML' || true
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
          key: __KEY__
YAML
    write_content="${write_content/__KEY__/${key}}"

    local fork_repodir="$wf_dir_fork/repo"
    git clone --depth 1 --branch "$BRANCH" "$fork_url" "$fork_repodir" 2>&1 | tail -1

    # Sync fork with upstream
    git -C "$fork_repodir" remote add upstream "$main_url" 2>/dev/null || true
    git -C "$fork_repodir" fetch upstream "$BRANCH" 2>&1 | tail -1
    git -C "$fork_repodir" reset --hard "upstream/$BRANCH" 2>&1 | tail -1
    git -C "$fork_repodir" push origin "$BRANCH" --force 2>&1 | tail -1

    mkdir -p "$fork_repodir/.gitcode/workflows"
    echo "$write_content" > "$fork_repodir/.gitcode/workflows/$write_wf"
    git -C "$fork_repodir" add .gitcode/workflows/
    git -C "$fork_repodir" commit --allow-empty -m "test: $write_wf"
    git -C "$fork_repodir" push origin "$BRANCH" 2>&1 | tail -1
    log "   Fork push done"

    # Poll for completion (using main repo API — workflows from fork push go to the executor's repo context)
    local rid_fork=""
    local t0=$SECONDS
    while (( SECONDS - t0 < TIMEOUT )); do
        local runs
        runs="$(api_get "/repos/${FORK_OWNER}/${FORK_REPO}/actions/runs?per_page=100")"
        rid_fork="$(echo "$runs" | python3 -c "
import sys,json
for r in json.load(sys.stdin).get('workflow_runs',[]):
    if '$write_wf' in (r.get('file_path','')):
        if r.get('status') in ('COMPLETED','FAILED','CANCELED'):
            print(r['workflow_run_id']); break
")"
        [[ -n "$rid_fork" ]] && break
        sleep "$POLL"
    done
    if [[ -n "$rid_fork" ]]; then
        log "   Fork run completed: ${rid_fork:0:12}..."
    else
        log "   Fork run TIMEOUT — continuing anyway"
    fi

    # Cleanup fork workflow
    rm -f "$fork_repodir/.gitcode/workflows/$write_wf"
    git -C "$fork_repodir" rm --cached ".gitcode/workflows/$write_wf" 2>/dev/null || true
    git -C "$fork_repodir" commit --allow-empty -m "chore: rm $write_wf" 2>/dev/null || true
    git -C "$fork_repodir" push origin "$BRANCH" 2>&1 | tail -1

    # Phase 2: 主仓读缓存（应该 miss）
    log "Phase 2: Main repo read cache (expect MISS)"
    sleep 5
    local wf_dir_main="$WORKDIR/sec-main"; mkdir -p "$wf_dir_main"
    local read_wf="sec-cache-main-${TS}.yml"
    local read_content
    read -r -d '' read_content <<'YAML' || true
on:
  push:
    branches: [main]
jobs:
  read-cache:
    name: read-cache-main
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: restore cache
        uses: cache
        with:
          path: mycache
          key: __KEY__
      - name: verify
        run: |
          if [ -f mycache/data.txt ]; then
            echo "CACHE_HIT=yes"
            echo "CONTENT: $(cat mycache/data.txt)"
          else
            echo "CACHE_MISS=yes"
          fi
YAML
    read_content="${read_content/__KEY__/${key}}"

    local out2
    out2="$(push_and_collect "$read_wf" "$read_content" "$main_url" "$wf_dir_main")" || true
    local rid2 logs2
    rid2="$(echo "$out2" | head -1)"
    logs2="$(echo "$out2" | tail -n +2)"

    local verdict="FAIL"
    if echo "$logs2" | grep -q "CACHE_MISS=yes"; then
        log "   CACHE_MISS=yes — fork cache isolated"
        verdict="PASS"
    elif echo "$logs2" | grep -q "CACHE_HIT=yes"; then
        log "   CACHE_HIT=yes — fork cache NOT isolated! (security issue)"
        if echo "$logs2" | grep -q "FORK_POISON"; then
            log "   Fork content LEAKED into main repo!"
        fi
    else
        log "   No CACHE_HIT/CACHE_MISS marker"
    fi
    log "   Verdict: $verdict"
    write_result "SEC-CACHE-01-002" "$verdict" "$rid2" "$logs2"
}

write_result() {
    local case_id="$1" verdict="$2" run_id="$3" logs="$4"
    local out_dir="$SCRIPT_DIR/runs/$RUN_ID/results"
    mkdir -p "$out_dir"
    local log_preview="${logs:0:1000}"
    python3 -c "
import json
result={
    'case_id':'$case_id',
    'verdict':'$verdict',
    'run_id':'$run_id',
    'run_url':'https://gitcode.com/${OWNER}/${REPO}/actions/runs/$run_id',
    'logs_preview':$(python3 -c "import json; print(json.dumps('''${log_preview}'''))")
}
with open('$out_dir/${case_id}.json','w') as f:
    json.dump(result,f,indent=2,ensure_ascii=False)
" 2>/dev/null
    log "   Result: $out_dir/${case_id}.json"
}

# ── main ──
case "$CASE_ID" in
    COMP-CACHE-01-001) test_001 ;;
    COMP-CACHE-01-002) test_002 ;;
    SEC-CACHE-01-002)   test_sec_002 ;;
    *) log "Unknown case: $CASE_ID"; exit 1 ;;
esac
