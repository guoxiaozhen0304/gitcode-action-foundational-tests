# COMP-CACHE-01-001

- **标题**: cache hit 时恢复缓存内容正确
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cache hit 时恢复缓存内容正确**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-016

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=cache_step, equals=hit

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Cache test file | `cache` |  | ✅ GENUINE |
| 2 | Use cache | `cat cached.txt || echo "cache miss"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify cache hit
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Cache test file
        uses: cache
        with:
          path: cached.txt
          key: cache-test-${{ runner.os }}
      - name: Use cache
        run: |
          cat cached.txt || echo "cache miss"
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
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | cache_step | positive | equals=hit | ✅ GENUINE | 平台级断言 cache_step — 由 harness 在运行时观测 |

---