# COMPAT-FIELD-01-002

- 标题: 含 services 字段的 job 应被报错或警告
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-FIELD-01-002
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-021
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    COMPAT-FIELD-01-001
标题:      含 services 字段的 job 应被报错或警告

前置条件:
  - 仓库已启用 Actions

操作步骤:
  1. 在 job 下添加 services 字段
  2. 提交并推送该 workflow
  3. 观察平台解析行为

预期结果:
  - 平台应在解析或保存阶段给出明确报错或警告
  - 不应被静默接受且服务未启动

验证点:
  - [负向] 不应被静默接受
  - [非功能] 报错信息应指明 services 字段不支持

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo hello | run: echo "hello"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test services field
    runs-on: [dedicate-hosted, x64, large]
    services:
      redis:
        image: redis:latest
        ports:
          - 6379:6379
    steps:
      - name: Echo hello
        run: |
          echo "hello"

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
| [负向] 不应被静默接受 | ❌ UNVERIFIABLE | single dispatch cannot prove negation |
| [非功能] 报错信息应指明 services 字段不支持 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [负向] 不应被静默接受: UNVERIFIABLE - single dispatch cannot prove negation
- [非功能] 报错信息应指明 services 字段不支持: PARTIAL - all steps are trivial echo

---
