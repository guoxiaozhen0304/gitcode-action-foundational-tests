# COMPAT-DIR-01-002

- 标题: 工作流目录差异——.github/workflows/ 不应被识别
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-DIR-01-002
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-029
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    COMPAT-DIR-01-001
标题:      工作流目录差异——.github/workflows/ 不应被识别

前置条件:
  - 仓库已创建 .github/workflows/ 目录
  - 该目录下存在工作流定义文件

操作步骤:
  1. 在 .github/workflows/ci.yml 中创建工作流定义
  2. 同时确保 .gitcode/workflows/ 下无同名工作流
  3. 提交并推送到仓库，触发对应事件
  4. 观察平台是否识别并执行 .github/workflows/ 下的工作流

预期结果:
  - .github/workflows/ 下的工作流文件不被 GitCode 平台识别
  - 对应事件触发时，该目录下的工作流不会执行
  - 平台优先且仅识别 .gitcode/workflows/ 目录

验证点:
  - [负向] .github/workflows/ 下的工作流不应被触发执行
  - [正向] 平台应仅识别 .gitcode/workflows/ 目录
  - [正向] 事件触发后不应出现来自 .github 目录的意外运行记录

清理:      fixture
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | (TC) echo if reached (verify-github-dir-ignored) | echo "GITHUB_DIR_WORKFLOW_RAN"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | push |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| .github/workflows/ 下的工作流不应被触发执行 | 覆盖 | LLM/nonfunctional assertion: .github/workflows/ 下的工作流不应被识别触发 |
| 平台应仅识别 .gitcode/workflows/ 目录 | 覆盖 | LLM/nonfunctional assertion: 仅 .gitcode/workflows/ 下的工作流应被触发，且无意外运行记录 |
| 事件触发后不应出现来自 .github 目录的意外运行记录 | 覆盖 | LLM/nonfunctional assertion: 仅 .gitcode/workflows/ 下的工作流应被触发，且无意外运行记录 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_discovery | negative | .github/workflows/ 下的工作流不应被识别触发 | LLM_DEPENDENT | LLM/nonfunctional assertion: .github/workflows/ 下的工作流不应被识别触发 |
| 2 | run_logs | negative | 不应出现 GITHUB_DIR_WORKFLOW_RAN | LLM_DEPENDENT | LLM/nonfunctional assertion: 不应出现 GITHUB_DIR_WORKFLOW_RAN |
| 3 | run_status | positive | 仅 .gitcode/workflows/ 下的工作流应被触发，且无意外运行记录 | LLM_DEPENDENT | LLM/nonfunctional assertion: 仅 .gitcode/workflows/ 下的工作流应被触发，且无意外运行记录 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
