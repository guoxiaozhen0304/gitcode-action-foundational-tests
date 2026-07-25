# COMPAT-DIR-01-003

- 标题: .github/workflows 目录不应被识别且应给出迁移提示
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-DIR-01-003
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-029
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      .github/workflows 目录不应被识别且应给出迁移提示

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 在仓库中创建 `.github/workflows/test.yml` workflow 文件
  2. 提交并触发 push 事件
  3. 观察系统是否识别该 workflow

预期结果:
  - GitCode 行为：.github/workflows 下的 workflow 不应被识别
  - 系统应给出明确提示，说明 workflow 应放置在 .gitcode/workflows/ 目录下
  - 不应静默忽略导致用户误以为配置正确

验证点:
  - [负向] .github/workflows 下的 workflow 不应被触发
  - [正向] 系统给出迁移提示，说明正确的目录位置

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo hello (test-github-dir) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | push |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| .github/workflows 下的 workflow 不应被触发 | 覆盖 | LLM/nonfunctional assertion: .github/workflows 下的 workflow 不应被触发 |
| 系统给出迁移提示，说明正确的目录位置 | 覆盖 | LLM/nonfunctional assertion: 系统给出迁移提示，说明 workflow 应放置在 .gitcode/workflows/ 目录下 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | .github/workflows 下的 workflow 不应被触发 | LLM_DEPENDENT | LLM/nonfunctional assertion: .github/workflows 下的 workflow 不应被触发 |
| 2 | error_message | positive | 系统给出迁移提示，说明 workflow 应放置在 .gitcode/workf | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统给出迁移提示，说明 workflow 应放置在 .gitcode/workflows/ 目录下 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
