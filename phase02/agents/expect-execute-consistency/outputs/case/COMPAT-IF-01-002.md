# COMPAT-IF-01-002

- 标题: continue-on-error 标记后失败 step 不阻断后续执行
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-IF-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-003
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      continue-on-error 标记后失败 step 不阻断后续执行

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个包含两个 step 的 workflow
  2. 第一个 step 显式返回非零退出码，但设置 continue-on-error 为 true
  3. 第二个 step 输出一条消息
  4. 手动触发该 workflow

预期结果:
  - 第一个 step 虽失败，但因 continue-on-error 标记，后续 step 仍继续执行
  - job 整体状态可能为成功或特殊标记，但不因该失败而中断

验证点:
  - [正向] 第二个 step 成功执行并输出消息
  - [正向] 第一个 step 的失败后，后续 step 未被跳过
  - [正向] job 未在第一个 step 处中断

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | force failure with continue | run: exit 1
 | continue-on-error: true | 是 |
| 2 | should still run | run: echo "This should appear"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-continue:
    name: Test continue on error
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: force failure with continue
        continue-on-error: true
        run: |
          exit 1
      - name: should still run
        run: |
          echo "This should appear"

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
| [正向] 第二个 step 成功执行并输出消息 | ✅ COVERED | steps have real logic |
| [正向] 第一个 step 的失败后，后续 step 未被跳过 | ✅ COVERED | steps have real logic |
| [正向] job 未在第一个 step 处中断 | ✅ COVERED | steps have real logic |

### 问题

无

---
