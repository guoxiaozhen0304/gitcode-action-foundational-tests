#!/usr/bin/env bash
# run_smoke.sh — GitCode 每日冒烟测试执行入口
# 用法:
#   ./run_smoke.sh [run-id] [phase01-run-id] [src-dir]
# 例:
#   ./run_smoke.sh 2026-08-17-01 smoke phase01/runs/smoke/cases/yaml

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

RUN_ID="${1:-$(date +%Y-%m-%d-%H%M%S)}"
PHASE01_RUN_ID="${2:-smoke}"
SRC_DIR="${3:-phase01/runs/smoke/cases/yaml}"

# 探测 Python 命令
PYTHON=""
for cmd in python3 python py; do
    if command -v "$cmd" >/dev/null 2>&1; then
        PYTHON="$cmd"
        break
    fi
done
if [ -z "$PYTHON" ]; then
    echo "错误: 未找到 Python 解释器 (python3/python/py)"
    exit 1
fi

echo "=== GitCode 冒烟测试 ==="
echo "Run ID      : $RUN_ID"
echo "Phase01 ID  : $PHASE01_RUN_ID"
echo "用例目录    : $SRC_DIR"
echo "Python      : $PYTHON"
echo ""

# 1. Schema 校验
echo "[1/4] Schema 校验..."
$PYTHON phase02/scripts/schema_check.py "$PHASE01_RUN_ID" "$RUN_ID" --src-dir "$SRC_DIR"

# 2. 批量执行
echo "[2/4] 批量执行..."
$PYTHON phase02/scripts/run_batch.py "$RUN_ID"

# 3. 报告生成
echo "[3/4] 报告生成..."
$PYTHON phase02/scripts/report_builder.py "$RUN_ID"

# 4. 结果汇总
echo "[4/4] 完成。"
echo ""
echo "📄 Markdown 报告 : phase02/reports/$RUN_ID/report.md"
echo "📊 JSON 汇总     : phase02/runs/$RUN_ID/summary.json"
echo "📁 详细结果      : phase02/runs/$RUN_ID/results/"

# 可选：将最新报告链接到固定路径，方便 Jenkins 归档
mkdir -p phase02/reports/latest
rm -f phase02/reports/latest/report.md
ln -sf "../$RUN_ID/report.md" phase02/reports/latest/report.md 2>/dev/null || true
