# COMPAT-CACHE-01-002

- **标题**: cache 行为等价性——fork PR 写隔离
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cache 行为等价性——fork PR 写隔离**

- 触发事件: `pr`
- 规格引用: INTENT-COMPAT-025

通过标准：
1. type=negative, target=run_logs, eval=llm_assisted
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_status, equals=leaked_cache_to_fork

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) restore cache | `cache` |  | ✅ GENUINE |
| 2 | (TC) attempt write from f | `mkdir -p "$HOME/.cache/test-dir" echo "FORK_MARKER_$(date +%s)" > "$HOME/.cache/` |  | ✅ GENUINE |
| 3 | (TC) save cache | `cache` | ${{ always() }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  verify-fork-cache:
    name: Verify fork PR cache isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) restore cache
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-fork-test
          restore-keys: compat-cache-fork-test-
      - name: (TC) attempt write from fork
        run: |
          mkdir -p "$HOME/.cache/test-dir"
          echo "FORK_MARKER_$(date +%s)" > "$HOME/.cache/test-dir/fork_marker.txt"
          echo "FORK_WRITE_ATTEMPTED"
      - name: (TC) save cache
        if: ${{ always() }}
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-fork-test
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pr` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-fork-pr` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_status | negative | equals=leaked_cache_to_fork | ✅ GENUINE | 状态断言 leaked_cache_to_fork 可被步骤行为验证 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---