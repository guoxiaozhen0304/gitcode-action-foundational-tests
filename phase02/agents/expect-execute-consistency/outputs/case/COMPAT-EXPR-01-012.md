# COMPAT-EXPR-01-012

- 标题: fromJSON() 函数缺失时的降级行为
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-012
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-010
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    COMPAT-EXPR-01-011
标题:      fromJSON() 函数缺失时的降级行为

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow run 块中引用 GitHub 支持的 fromJSON() 表达式函数
  2. 提交并推送该 workflow
  3. 观察平台解析与运行行为

预期结果:
  - 平台对不支持的 fromJSON() 函数给出明确的校验错误或运行时错误
  - 错误信息应指明该函数在 GitCode 中不可用
  - 不应静默求值并返回意外结果

验证点:
  - [负向] 不支持函数不应静默通过并返回意外值
  - [正向] 错误信息应足够清晰，帮助迁移者识别函数缺失

清理:      fixture
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Test fromJSON function in run block (test-fromjson) | RESULT="${{ fromJSON('{\"a\": 1}').a }}" echo "fromjson-result=$RESULT"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不支持函数不应静默通过并返回意外值 | 覆盖 | log assertion without specific string check |
| 错误信息应足够清晰，帮助迁移者识别函数缺失 | 未覆盖 | 缺少正向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | CONSISTENT | log assertion without specific string check |
| 2 | error_message | nonfunctional | 若 fromJSON() 函数不可用，错误信息应明确指出函数缺失，而非 gene | LLM_DEPENDENT | LLM/nonfunctional assertion: 若 fromJSON() 函数不可用，错误信息应明确指出函数缺失，而非 generic 语法错误 |

### 问题

- 验证点 `错误信息应足够清晰，帮助迁移者识别函数缺失` → 未覆盖: 缺少正向断言

---
