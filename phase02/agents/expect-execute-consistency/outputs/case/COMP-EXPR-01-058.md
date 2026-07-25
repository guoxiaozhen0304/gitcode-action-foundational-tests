# COMP-EXPR-01-058

- 标题: 表达式运算符与优先级边界行为
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 if 条件中测试 == / != / ! / && / || / > / < / >= / <= 运算符及优先级组合
2. 验证求值结果正确

预期结果:
- 各运算符按正确优先级求值，逻辑与短路，逻辑或短路，比较运算符正确

验证点:
- [正向] == 和 != 运算正确
- [正向] ! 取反正确
- [正向] && 和 || 优先级正确
- [正向] 比较运算符 > < >= <= 正确

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Equality | if: ${{ atomgit.ref_name == 'main' \|\| true }}，echo "eq_passed" | 是 |
| 2 | Not equal | if: ${{ atomgit.ref_name != 'nonexistent' }}，echo "ne_passed" | 是 |
| 3 | Greater than | if: ${{ 5 > 3 }}，echo "gt_passed" | 是 |
| 4 | Logical combo | if: ${{ true && (false \|\| true) }}，echo "logic_passed" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-EXPR-01-058
dimensions: [completeness]
dimension: completeness
priority: P1
title: 表达式运算符与优先级边界行为
intent_ref: KEEP-TC-160~175
setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default
fault_injection: null
workflow: |
  on:
    workflow_dispatch:
  jobs:
    verify:
      name: Verify operator precedence
      runs-on: [dedicate-hosted, x64, large]
      steps:
        - name: Equality
          if: ${{ atomgit.ref_name == 'main' || true }}
          run: |
            echo "eq_passed"
        - name: Not equal
          if: ${{ atomgit.ref_name != 'nonexistent' }}
          run: |
            echo "ne_passed"
        - name: Greater than
          if: ${{ 5 > 3 }}
          run: |
            echo "gt_passed"
        - name: Logical combo
          if: ${{ true && (false || true) }}
          run: |
            echo "logic_passed"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: eq_passed
  - type: positive
    target: run_logs
    must_contain: ne_passed
  - type: positive
    target: run_logs
    must_contain: gt_passed
  - type: positive
    target: run_logs
    must_contain: logic_passed
teardown:
  reset: fixture
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] == 和 != 运算正确 | ✅ COVERED | 步骤1 == 运算，步骤2 != 运算，断言 eq_passed, ne_passed |
| [正向] ! 取反正确 | ❌ TRIVIAL | 无步骤测试纯 ! 取反运算；步骤1 eq 使用了 `\|\| true` 回避 true 场景 |
| [正向] && 和 \|\| 优先级正确 | ✅ COVERED | 步骤4 组合测试 `true && (false \|\| true)`，断言 logic_passed |
| [正向] 比较运算符 > < >= <= 正确 | ✅ COVERED | 步骤3 5 > 3 测试 >，但 < / >= / <= 未单独测试 |

### 问题

- ! 取反运算符未测试（缺独立步骤验证 `${{ !false }}` 或等价场景）
- < / >= / <= 比较运算符未单独覆盖（仅测试了 >）

---
