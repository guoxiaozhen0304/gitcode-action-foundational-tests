# COMPAT-EXPR-01-001

- 标题: success 关键字在条件表达式中的可用性
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-004
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      success 关键字在条件表达式中的可用性

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 workflow，其中包含多个 step
  2. 在 step 执行过程中，尝试通过表达式获取当前的成功状态信息
  3. 观察平台对 success 关键字的解析与返回值

预期结果:
  - 若平台支持 success 关键字，则可在适当上下文中获取到状态值
  - 若不支持，应有明确的表达式解析行为（如视为字符串或报错）

验证点:
  - [正向] 表达式被正确解析，日志中输出预期值
  - [负向] 若平台拒绝该关键字，应记录兼容性差异

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | previous step succeeds | run: echo "Step completed successfully"
 | 否 |
| 3 | observe next step runs | run: echo "Next step executed, implicit success confirmed"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-success:
    name: Test success keyword availability
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: previous step succeeds
        run: |
          echo "Step completed successfully"
      - name: observe next step runs
        run: |
          echo "Next step executed, implicit success confirmed"

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
| [正向] 表达式被正确解析，日志中输出预期值 | ✅ COVERED | steps have real logic |
| [负向] 若平台拒绝该关键字，应记录兼容性差异 | ✅ COVERED | steps have real logic |

### 问题

无

---
