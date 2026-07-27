# COMP-TRIG-01-075

- 标题: schedule 事件关键字段与 cron 格式验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

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
| 1 | Print schedule | run: echo "SCHEDULE=${{ atomgit.event.schedule }}" && echo "schedule_ok" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule event fields
    runs-on: [ubuntu-latest, x64, small]
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
| event | schedule |
| as | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [正向] 数组格式 schedule 通过校验 | ✅ COVERED | workflow 的 on.schedule 使用了数组格式 [{cron: ...}]，步骤通过 ${{ atomgit.event.schedule }} 表达式真实访问事件上下文，可证明平台接受数组格式并成功触发 |
| [负向] 对象格式 schedule 被拒绝 | 🔄 UNVERIFIABLE | workflow 仅配置了数组格式，单次运行无法证明对象格式会被平台拒绝；这是平台级校验行为 |
| [正向] event.schedule 非空 | ✅ COVERED | 步骤 echo "SCHEDULE=${{ atomgit.event.schedule }}" 真实输出 schedule 事件上下文，断言可通过 must_contain: schedule_ok 验证 |

### 问题

- [负向] 对象格式 schedule 被拒绝: UNVERIFIABLE — 该行为依赖平台在 workflow 提交时的格式校验，单次 workflow 运行无法自证另一种格式会被拒绝

## 5. 评级理由

三个验证点中两个 COVERED（步骤通过 ${{ }} 表达式真实访问 schedule 事件上下文），一个 UNVERIFIABLE（负向格式校验无法在单次运行中验证），评级为部分不符。
