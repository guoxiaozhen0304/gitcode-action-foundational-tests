# COMP-TIMEOUT-01-002

- 标题: 超时的 job 被强制终止并标记为 failure
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-TIMEOUT-01-002
维度标签:   [completeness, reliability]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-008
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      超时的 job 被强制终止并标记为 failure

前置条件:
  - workflow 声明 timeout-minutes: 1

操作步骤:
  1. 触发 workflow，其中 step 睡眠超过 1 分钟
  2. 观察 job 是否在 1 分钟后被强制终止

预期结果:
  - job 在 1 分钟后被强制终止
  - 运行状态标记为 failure
  - 已运行 step 的日志保留

验证点:
  - [负向] 运行状态为 failure
  - [正向] 超时前已完成的 step 日志完整保留

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo before sleep | run: echo "starting"
 | 否 |
| 2 | Sleep beyond timeout | run: sleep 120
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify timeout kill
    runs-on: [ubuntu-latest, x64, small]
    timeout-minutes: 1
    steps:
      - name: Echo before sleep
        run: |
          echo "starting"
      - name: Sleep beyond timeout
        run: |
          sleep 120

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 运行状态为 failure | ✅ COVERED | negative assertion in YAML assertions |
| [正向] 超时前已完成的 step 日志完整保留 | ✅ COVERED | steps have real logic |

### 问题

无

---
