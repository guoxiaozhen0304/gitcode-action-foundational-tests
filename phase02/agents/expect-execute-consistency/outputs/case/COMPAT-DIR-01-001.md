# COMPAT-DIR-01-001

- 标题: 工作流目录差异——.gitcode/workflows/ 正常识别
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-DIR-01-001
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-029
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      工作流目录差异——.gitcode/workflows/ 正常识别

前置条件:
  - 仓库已创建 .gitcode/workflows/ 目录

操作步骤:
  1. 在 .gitcode/workflows/ci.yml 中创建工作流定义
  2. 提交并推送到仓库
  3. 触发对应事件，验证工作流被正确识别和执行

预期结果:
  - .gitcode/workflows/ 下的 .yml 文件被平台识别为有效工作流
  - 对应事件触发时工作流正常执行
  - 此行为与 GitCode 官方文档一致

验证点:
  - [正向] .gitcode/workflows/*.yml 被正确识别
  - [正向] 对应事件触发后工作流正常执行
  - [负向] 不应出现 .gitcode 目录下文件被忽略的情况

清理:      fixture
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | (TC) echo from gitcode dir (verify-gitcode-dir) | echo "GITCODE_DIR_RECOGNIZED_OK"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | push |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| .gitcode/workflows/*.yml 被正确识别 | 覆盖 | status assertion: completed_success |
| 对应事件触发后工作流正常执行 | 覆盖 | status assertion: completed_success |
| 不应出现 .gitcode 目录下文件被忽略的情况 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | completed_success | CONSISTENT | status assertion: completed_success |
| 2 | run_logs | positive | 日志中应出现 GITCODE_DIR_RECOGNIZED_OK | LLM_DEPENDENT | LLM/nonfunctional assertion: 日志中应出现 GITCODE_DIR_RECOGNIZED_OK |
| 3 | workflow_discovery | positive | .gitcode/workflows/ 下的工作流文件被正确识别 | LLM_DEPENDENT | LLM/nonfunctional assertion: .gitcode/workflows/ 下的工作流文件被正确识别 |

### 问题

- 验证点 `不应出现 .gitcode 目录下文件被忽略的情况` → 未覆盖: 缺少负向断言

---
