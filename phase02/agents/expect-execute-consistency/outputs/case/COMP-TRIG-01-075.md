# COMP-TRIG-01-075

- 标题: schedule 事件关键字段与 cron 格式验证
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-075
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-237~430
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      schedule 事件关键字段与 cron 格式验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 schedule 触发并定义 cron 表达式
  2. 验证数组格式和字段访问

预期结果:
  - schedule 必须为数组格式 [{cron: ...}]，cron 五段式正确，atomgit.event.schedule 可访问

验证点:
  - [正向] 数组格式 schedule 通过校验
  - [负向] 对象格式 schedule 被拒绝
  - [正向] event.schedule 非空

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print schedule | run: echo "SCHEDULE=${{ atomgit.event.schedule }}"
echo "schedule_ok"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule event fields
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Print schedule
        run: |
          echo "SCHEDULE=${{ atomgit.event.schedule }}"
          echo "schedule_ok"

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
| [正向] 数组格式 schedule 通过校验 | 🚫 BLOCKED | trigger=schedule |
| [负向] 对象格式 schedule 被拒绝 | 🚫 BLOCKED | trigger=schedule |
| [正向] event.schedule 非空 | 🚫 BLOCKED | trigger=schedule |

### 问题

- [正向] 数组格式 schedule 通过校验: BLOCKED - trigger=schedule
- [负向] 对象格式 schedule 被拒绝: BLOCKED - trigger=schedule
- [正向] event.schedule 非空: BLOCKED - trigger=schedule

---
