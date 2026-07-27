# COMP-SCHEDULE-01-001

- 标题: 合法 cron 在默认分支按时触发
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-SCHEDULE-01-001
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-005
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      合法 cron 在默认分支按时触发

前置条件:
  - workflow 位于默认分支
  - cron 表达式合法

操作步骤:
  1. 配置 schedule 触发 workflow
  2. 等待到达 cron 设定时间

预期结果:
  - workflow 在设定时间被触发
  - 运行成功完成

验证点:
  - [正向] 运行记录存在且 event 为 schedule
  - [正向] 触发时间与 cron 预期 UTC 时间一致

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo scheduled | run: echo "scheduled run" | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule trigger
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo scheduled
        run: |
          echo "scheduled run"

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
| [正向] 运行记录存在且 event 为 schedule | ⚠️ TRIVIAL | 步骤仅 echo 字面量 "scheduled run"，无 ${{ }} 表达式、无 if 条件、无 uses action、无实质命令 |
| [正向] 触发时间与 cron 预期 UTC 时间一致 | ❌ MISSING | 无任何步骤产出时间相关输出 |

### 问题

- [正向] 运行记录存在且 event 为 schedule: TRIVIAL — 步骤仅 echo 字面量，未执行任何验证逻辑
- [正向] 触发时间与 cron 预期 UTC 时间一致: MISSING — 无步骤产出或对比时间信息

## 5. 评级理由

两个验证点均为 TRIVIAL 或 MISSING，无任何步骤真实执行被测功能，评级为完全不符。
