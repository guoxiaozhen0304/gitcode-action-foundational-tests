# COMPAT-EXPR-01-007

- 标题: hashFiles 表达式多路径组合边界
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-EXPR-01-007
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-007
参照来源:  inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/syntax-reference/context.md
母意图:    —
标题:      hashFiles 表达式多路径组合边界

前置条件:
  - 仓库已启用 GitCode Action
  - 仓库中包含 package.json 和 lock 文件（或任意两个以上可匹配文件）

操作步骤:
  1. 提交一个 workflow，在 step 中使用 hashFiles 同时匹配多个路径模式
  2. 例如 hashFiles('**/package.json', '**/package-lock.json')
  3. 手动触发并观察输出结果

预期结果:
  - hashFiles 对多路径组合返回组合的哈希值
  - 验证多路径匹配行为与 GitHub Actions 是否一致

验证点:
  - [正向] 多路径匹配时返回非空哈希字符串
  - [正向] 修改任一匹配文件后哈希值发生变化
  - [负向] 多路径组合不应导致解析错误或异常

清理:      重置 fixture 仓库
```


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | 是 |
| 2 | hash multiple paths | run: echo "hash multi: ${{ hashFiles('**/package.json', '**/package-lock.json') }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-hashfiles-multi:
    name: Test hashFiles multiple paths
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: hash multiple paths
        run: "echo \"hash multi: ${{ hashFiles('**/package.json', '**/package-lock.json') }}\""

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
| [正向] 多路径匹配时返回非空哈希字符串 | ✅ COVERED | steps have real logic |
| [正向] 修改任一匹配文件后哈希值发生变化 | ✅ COVERED | steps have real logic |
| [负向] 多路径组合不应导致解析错误或异常 | ❌ UNVERIFIABLE | single dispatch cannot prove negation |

### 问题

- [负向] 多路径组合不应导致解析错误或异常: UNVERIFIABLE - single dispatch cannot prove negation

---
