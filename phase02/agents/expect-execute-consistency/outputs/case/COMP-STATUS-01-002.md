# COMP-STATUS-01-002

- 标题: 失败 step 的日志完整保留且可查看
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-STATUS-01-002
维度标签:   [completeness, usability]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-017
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      失败 step 的日志完整保留且可查看

前置条件:
  - workflow 包含会失败的 step

操作步骤:
  1. 触发 workflow
  2. 等待运行失败
  3. 通过 API 下载 job 日志

预期结果:
  - 失败 step 之前的日志完整保留
  - 失败 step 的错误输出可见

验证点:
  - [正向] 失败 step 前的输出存在于日志
  - [正向] 失败 step 的错误信息存在于日志

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Before failure | run: echo "BEFORE_FAILURE_MARKER"
 | 否 |
| 2 | Force failure | run: echo "ERROR_MARKER"
exit 1
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify failed step logs
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Before failure
        run: |
          echo "BEFORE_FAILURE_MARKER"
      - name: Force failure
        run: |
          echo "ERROR_MARKER"
          exit 1

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
| [正向] 失败 step 前的输出存在于日志 | ✅ COVERED | steps have real logic |
| [正向] 失败 step 的错误信息存在于日志 | ✅ COVERED | steps have real logic |

### 问题

无

---
