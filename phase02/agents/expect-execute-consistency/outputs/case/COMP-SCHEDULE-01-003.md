# COMP-SCHEDULE-01-003

- 标题: cron 间隔短于 5 分钟时被拒绝或降级
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-SCHEDULE-01-003
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-005
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      cron 间隔短于 5 分钟时被拒绝或降级

前置条件:
  - 仓库具备提交 workflow 的权限

操作步骤:
  1. 配置 cron 间隔为 1 分钟
  2. 提交 workflow

预期结果:
  - 平台拒绝该 workflow 或将其降级为最短间隔

验证点:
  - [负向] 不应允许每分钟触发的 schedule
  - [非功能] 错误信息应说明最短间隔限制

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo scheduled | run: echo "should not run"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "*/1 * * * *"
jobs:
  verify:
    name: Verify short interval rejection
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo scheduled
        run: |
          echo "should not run"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 不应允许每分钟触发的 schedule | 🚫 BLOCKED | trigger=schedule |
| [非功能] 错误信息应说明最短间隔限制 | 🚫 BLOCKED | trigger=schedule |

### 问题

- [负向] 不应允许每分钟触发的 schedule: BLOCKED - trigger=schedule
- [非功能] 错误信息应说明最短间隔限制: BLOCKED - trigger=schedule

---
