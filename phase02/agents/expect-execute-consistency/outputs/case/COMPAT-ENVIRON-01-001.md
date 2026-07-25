# COMPAT-ENVIRON-01-001

- 标题: 含 environment 字段的 job 应被报错或警告
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-ENVIRON-01-001
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-023
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      含 environment 字段的 job 应被报错或警告

前置条件:
  - 仓库已启用 Actions

操作步骤:
  1. 在 job 下添加 environment: production
  2. 提交并推送该 workflow
  3. 观察平台解析行为

预期结果:
  - 平台应在解析或保存阶段给出明确报错或警告
  - 不应被静默接受导致环境保护规则失效

验证点:
  - [负向] 不应被静默接受
  - [非功能] 报错信息应提示 environment 字段不支持及替代方案

清理:      fixture
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo hello (test) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应被静默接受 | 未覆盖 | 缺少负向断言 |
| 报错信息应提示 environment 字段不支持及替代方案 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | 平台应对 environment 字段给出明确报错或警告，不应静默忽略；信息应建 | LLM_DEPENDENT | LLM/nonfunctional assertion: 平台应对 environment 字段给出明确报错或警告，不应静默忽略；信息应建议使用其他方式配置部署 |

### 问题

- 验证点 `不应被静默接受` → 未覆盖: 缺少负向断言

---
