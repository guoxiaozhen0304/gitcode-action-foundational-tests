# REL-CACHEPERF-01-054

- **标题**: 缓存加速比——cache 命中 vs 未命中构建耗时对比
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**缓存加速比——cache 命中 vs 未命中构建耗时对比**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-054

通过标准：
1. type=nonfunctional, target=speedup_ratio
2. type=nonfunctional, target=restore_time_seconds

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | restore cache | `cache` |  | ✅ GENUINE |
| 2 | install deps | `npm ci || true` |  | ✅ GENUINE |
| 3 | save cache | `cache` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: cache speedup test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: restore cache
        uses: cache
        with:
          path: node_modules
          key: cache-deps-${{ matrix.run }}
      - name: install deps
        run: |
          npm ci || true
      - name: save cache
        uses: cache
        with:
          path: node_modules
          key: cache-deps-${{ matrix.run }}
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
| 1 | speedup_ratio | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | restore_time_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---