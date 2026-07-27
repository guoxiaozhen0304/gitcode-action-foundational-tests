# SEC-COMM-01-001

- 标题: issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   SEC-COMM-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-026
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过

前置条件:
  - 仓库配置了评论触发 workflow

操作步骤:
  1. 提交一个由 issue_comment 触发的 workflow，配置关键字过滤
  2. 提交一条将关键字伪装在 markdown 代码块中的评论

预期结果:
  - 伪装在代码块或注释中的关键字绝不应触发 workflow
  - 触发记录应包含评论原始内容哈希，用于审计

验证点:
  - [负向] 伪装在代码块或注释中的关键字绝不应触发 workflow
  - [非功能] 触发记录应包含评论原始内容哈希，用于审计

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check trigger | run: echo "Triggered by comment" | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  comment-filter:
    name: Test comment keyword filter
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check trigger
        run: |
          echo "Triggered by comment"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | issue_comment |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 伪装在代码块或注释中的关键字绝不应触发 workflow | 🔄 UNVERIFIABLE | 单次已触发的 workflow 运行无法证明被屏蔽的关键字未触发它；步骤仅为字面量 echo，无关键字过滤逻辑 |
| [非功能] 触发记录应包含评论原始内容哈希，用于审计 | ❌ MISSING | 无任何步骤生成评论内容哈希 |

### 问题

- **断言 1 — UNVERIFIABLE**: 该验证点是负向断言，要求证明"被屏蔽的关键字绝对不会触发 workflow"。但当前 workflow 已被触发并正在运行，单一执行实例无法证明否定行为。且步骤仅为 `echo "Triggered by comment"`（字面量字符串，无 `if:`、`${{ }}`、`uses:`），未实现任何关键字过滤检验逻辑。
- **断言 2 — MISSING**: 规格要求"触发记录应包含评论原始内容哈希"，但 workflow 中无任何步骤生成或输出评论内容哈希。

## 5. 评级理由

一个验证点为 UNVERIFIABLE（负向断言单次运行无法证明），一个为 MISSING（无步骤产出评论哈希）。判定为部分不符。
