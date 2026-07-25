# COMPAT-ENVIRON-01-002

- 标题: environment 字段绑定 secrets 的行为差异
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-ENVIRON-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-023
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      environment 字段绑定 secrets 的行为差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，job 声明 `environment: prod` 并引用环境 secret
  2. 提交并触发 workflow

预期结果:
  - GitHub 行为：environment 字段绑定环境，环境 secrets 经审批后可用
  - GitCode 行为：environment 字段不被识别，环境 secrets 不可用
  - 应明确报错或警告，不应静默忽略

验证点:
  - [负向] 不通过 environment 字段被静默忽略
  - [正向] 系统对 environment 字段给出明确报错或警告

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo env secret (test-environment) | echo "env_secret=${{ secrets.ENV_SECRET }}" echo "done"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不通过 environment 字段被静默忽略 | 覆盖 | LLM/nonfunctional assertion: environment 字段不应被静默忽略 |
| 系统对 environment 字段给出明确报错或警告 | 覆盖 | LLM/nonfunctional assertion: 系统对 environment 字段给出明确报错或警告 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | environment 字段不应被静默忽略 | LLM_DEPENDENT | LLM/nonfunctional assertion: environment 字段不应被静默忽略 |
| 2 | error_message | positive | 系统对 environment 字段给出明确报错或警告 | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统对 environment 字段给出明确报错或警告 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
