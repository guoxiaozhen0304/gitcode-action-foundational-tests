# COMPAT-IF-01-001

- 标题: step 失败后后续 step 默认跳过行为
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-IF-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-003
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      step 失败后后续 step 默认跳过行为

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个包含两个 step 的 workflow
  2. 第一个 step 显式返回非零退出码以模拟失败
  3. 第二个 step 输出一条消息
  4. 手动触发该 workflow

预期结果:
  - 第一个 step 失败后，第二个 step 被系统默认跳过
  - 整个 job 标记为失败状态

验证点:
  - [正向] 第二个 step 未执行，日志中无其输出
  - [正向] job 整体状态为失败
  - [负向] 第二个 step 不应在第一个 step 失败后仍运行

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | force failure | run: exit 1
 | 是 |
| 2 | should be skipped | run: echo "This should not appear"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-skip:
    name: Test step failure skip
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: force failure
        run: |
          exit 1
      - name: should be skipped
        run: |
          echo "This should not appear"

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
| [正向] 第二个 step 未执行，日志中无其输出 | ✅ COVERED | steps have real logic |
| [正向] job 整体状态为失败 | ✅ COVERED | steps have real logic |
| [负向] 第二个 step 不应在第一个 step 失败后仍运行 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
