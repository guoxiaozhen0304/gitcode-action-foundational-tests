# COMPAT-CACHE-01-001

- **标题**: cache 行为等价性——缓存命中场景
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cache 行为等价性——缓存命中场景**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-025

通过标准：
1. type=positive, target=run_logs, eval=llm_assisted
2. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | (TC) restore cache | `cache` |  | ✅ GENUINE |
| 2 | (TC) verify cache state | `if [ -f "$HOME/.cache/test-dir/marker.txt" ]; then   echo "CACHE_HIT" else   ech` |  | ✅ GENUINE |
| 3 | (TC) save cache | `cache` | ${{ always() }} | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify-cache-hit:
    name: Verify cache hit behavior
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) restore cache
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-test-${{ atomgit.run_id }}
          restore-keys: compat-cache-test-
      - name: (TC) verify cache state
        run: |
          if [ -f "$HOME/.cache/test-dir/marker.txt" ]; then
            echo "CACHE_HIT"
          else
            echo "CACHE_MISS"
            mkdir -p "$HOME/.cache/test-dir"
            echo "marker" > "$HOME/.cache/test-dir/marker.txt"
          fi
      - name: (TC) save cache
        if: ${{ always() }}
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-test-${{ atomgit.run_id }}
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---