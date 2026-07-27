# COMP-SCHEDULE-01-002

- 标题: 非默认分支的 schedule workflow 不应触发
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-SCHEDULE-01-002
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-005
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      非默认分支的 schedule workflow 不应触发

前置条件:
  - workflow 仅存在于非默认分支

操作步骤:
  1. 在非默认分支创建 schedule workflow
  2. 等待到达 cron 设定时间

预期结果:
  - schedule 事件仅在默认分支生效
  - 非默认分支的 schedule workflow 不应触发

验证点:
  - [负向] 运行列表中不存在该 schedule 触发的运行

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo scheduled | run: echo "should not run" | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule non default branch
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo scheduled
        run: |
          echo "should not run"

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
| [负向] 运行列表中不存在该 schedule 触发的运行 | ❌ MISSING | 步骤仅 echo 字面量 "should not run"，无任何逻辑验证非默认分支上 schedule 是否触发；该负向断言依赖平台行为而非步骤可观测输出 |

### 问题

- [负向] 运行列表中不存在该 schedule 触发的运行: MISSING — 步骤仅 echo 字面量，无 ${{ }} 表达式、无 if 条件、无 uses action、无实质命令。该负向断言证明"某事未发生"，单次 workflow 运行无法通过步骤产出可验证的否定证据。

## 5. 评级理由

唯一验证点为 MISSING，步骤仅 echo 固定字符串，未执行任何实质逻辑，评级为完全不符。
