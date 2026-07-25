# COMP-WFLOW-01-063

- 标题: workflow concurrency 并发控制字段验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-WFLOW-01-063
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-289~293
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow concurrency 并发控制字段验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 workflow 级定义 concurrency 配置
  2. 验证 max / exceed-action / preemption.events 字段

预期结果:
  - concurrency 配置被平台接受，max >= 1，exceed-action 为 QUEUE 或 IGNORE，preemption.events 仅允许 mr_id

验证点:
  - [正向] 合法 concurrency 配置通过校验
  - [负向] max 小于 1 被拒绝
  - [负向] preemption.events 含非 mr_id 被拒绝

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | run: echo "concurrency_ok"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
concurrency:
  enable: true
  max: 2
  exceed-action: QUEUE
  preemption:
    enable: true
    events: [mr_id]
jobs:
  verify:
    name: Verify concurrency fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo ok
        run: |
          echo "concurrency_ok"

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
| [正向] 合法 concurrency 配置通过校验 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [负向] max 小于 1 被拒绝 | ⚠️ PARTIAL | no real logic in steps |
| [负向] preemption.events 含非 mr_id 被拒绝 | ⚠️ PARTIAL | no real logic in steps |

### 问题

- [正向] 合法 concurrency 配置通过校验: PARTIAL - all steps are trivial echo
- [负向] max 小于 1 被拒绝: PARTIAL - no real logic in steps
- [负向] preemption.events 含非 mr_id 被拒绝: PARTIAL - no real logic in steps

---
