# COMPAT-ACTIONDEV-01-001

- 标题: action.yml 元数据校验与 GitHub 差异
- 维度: 兼容性 | 优先级: P2
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-ACTIONDEV-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-NEW-010
参照来源:  inputs/gitcode-spec/action-development/top-level-fields.md
母意图:    —
标题:      action.yml 元数据校验与 GitHub 差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 Action 仓库，包含 action.yml，使用 GitHub 风格元数据（如 `branding` 字段）
  2. 在 workflow 中引用该 Action
  3. 提交并触发 workflow

预期结果:
  - GitCode 对 action.yml 的校验规则可能与 GitHub 不同
  - 不支持的字段应被静默忽略或给出警告，不应导致 Action 无法引用

验证点:
  - [正向] 不支持的 action.yml 字段不导致 workflow 失败
  - [正向] 系统给出明确提示说明不支持的字段

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Checkout action repo (test-action-meta) | checkout | GENUINE |
| 2 | Use local action (test-action-meta) | ./.github/actions/my-action | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不支持的 action.yml 字段不导致 workflow 失败 | 覆盖 | LLM/nonfunctional assertion: 不支持的 action.yml 字段不导致 workflow 失败 |
| 系统给出明确提示说明不支持的字段 | 覆盖 | LLM/nonfunctional assertion: 不支持的 action.yml 字段不导致 workflow 失败 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 不支持的 action.yml 字段不导致 workflow 失败 | LLM_DEPENDENT | LLM/nonfunctional assertion: 不支持的 action.yml 字段不导致 workflow 失败 |
| 2 | error_message | positive | 系统对不支持的元数据字段给出明确提示 | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统对不支持的元数据字段给出明确提示 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
