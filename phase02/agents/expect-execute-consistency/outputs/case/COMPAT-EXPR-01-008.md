# COMPAT-EXPR-01-008

- 标题: toJson 表达式输出格式差异（pretty-print vs compact）
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-008
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-008
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      toJson 表达式输出格式差异（pretty-print vs compact）

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow 中定义一个对象或数组
  2. 使用 toJson 表达式函数将其序列化并输出到日志
  3. 观察输出格式是否包含换行与缩进

预期结果:
  - toJson 输出应为合法 JSON
  - 若 GitCode 与 GitHub 行为一致，应输出 compact 单行 JSON
  - 若存在差异，应明确记录 pretty-print 与 compact 的行为分界

验证点:
  - [正向] toJson 输出合法 JSON
  - [非功能] 输出格式应与 GitHub Actions 行为一致或文档中明确说明差异

清理:      fixture
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Output object via toJson (test-tojson) | echo '${{ toJson({'key1': 'value1', 'key2': 'value2'}) }}'  | GENUINE |
| 2 | Output array via toJson (test-tojson) | echo '${{ toJson(['a', 'b', 'c']) }}'  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| toJson 输出合法 JSON | 覆盖 | real command in step 'Output object via toJson' contains string |
| 输出格式应与 GitHub Actions 行为一致或文档中明确说明差异 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | key1 | CONSISTENT | real command in step 'Output object via toJson' contains string |
| 2 | run_logs | nonfunctional | toJson 输出应为合法 JSON；若包含换行缩进则为 pretty-prin | LLM_DEPENDENT | LLM/nonfunctional assertion: toJson 输出应为合法 JSON；若包含换行缩进则为 pretty-print，若为单行则为 co |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
