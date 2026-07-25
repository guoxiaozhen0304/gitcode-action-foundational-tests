# USE-CTX-01-002

- 标题: 使用 github 上下文时报错应提示 atomgit 替代
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-CTX-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-002
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      使用 github 上下文时报错应提示 atomgit 替代

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 workflow 的 run 步骤中引用 ${{ github.ref }}

预期结果:
  YAML 校验或表达式求值阶段报错，提示应使用 atomgit 上下文

验证点:
  - [负向] 不应静默求值为空字符串
  - [非功能] 报错信息中应同时出现 github 与 atomgit 字样

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo github ref (bad-ctx) | echo "ref=${{ github.ref }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应静默求值为空字符串 | 覆盖 | negative status assertion |
| 报错信息中应同时出现 github 与 atomgit 字样 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须同时出现 github 与 atomgit 字样，并给出替换建议 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须同时出现 github 与 atomgit 字样，并给出替换建议 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
