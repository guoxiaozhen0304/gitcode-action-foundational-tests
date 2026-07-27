# COMP-EXPR-01-056

- **标题**: toJson 函数边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**toJson 函数边界行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-056

通过标准：
1. type=positive, target=run_logs, must_contain="EVENT_JSON={"
2. type=positive, target=run_logs, must_contain="ENV_JSON={"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Serialize event | `echo "EVENT_JSON=${{ toJson(atomgit.event) }}"` |  | ✅ GENUINE |
| 2 | Serialize env context | `echo "ENV_JSON=${{ toJson(env) }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify toJson boundary
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Serialize event
        run: |
          echo "EVENT_JSON=${{ toJson(atomgit.event) }}"
      - name: Serialize env context
        env:
          TEST_KEY: test_value
        run: |
          echo "ENV_JSON=${{ toJson(env) }}"
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
| 1 | run_logs | positive | must_contain=EVENT_JSON={ | ❌ MISSING_SOURCE | EVENT_JSON={: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=ENV_JSON={ | ❌ MISSING_SOURCE | ENV_JSON={: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 1 — MISSING_SOURCE**❌: EVENT_JSON={: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: ENV_JSON={: MISSING_SOURCE (无步骤产出此字符串)

---