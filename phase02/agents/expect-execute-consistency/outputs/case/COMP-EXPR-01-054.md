# COMP-EXPR-01-054

- 标题: 字符串函数 contains startsWith endsWith 边界行为
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 step 的 if 条件或 env 中使用 contains / startsWith / endsWith 函数
2. 覆盖空串、不匹配、边界匹配等场景

预期结果:
- contains 子串匹配正确，startsWith 前缀匹配正确，endsWith 后缀匹配正确，区分大小写

验证点:
- [正向] contains 匹配子串返回真
- [正向] startsWith 匹配前缀返回真
- [正向] endsWith 匹配后缀返回真
- [负向] 大小写不匹配返回假

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Contains match | if: ${{ contains(atomgit.ref_name, 'main') }}，echo "contains_passed" | 是 |
| 2 | StartsWith match | if: ${{ startsWith(atomgit.ref, 'refs/heads/') }}，echo "startswith_passed" | 是 |
| 3 | EndsWith match | if: ${{ endsWith(atomgit.ref_name, 'ain') }}，echo "endswith_passed" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-EXPR-01-054
dimensions: [completeness]
dimension: completeness
priority: P1
title: 字符串函数 contains startsWith endsWith 边界行为
intent_ref: KEEP-TC-180~182
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
      name: Verify string functions boundary
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Contains match
          if: ${{ contains(atomgit.ref_name, 'main') }}
          run: |
            echo "contains_passed"
        - name: StartsWith match
          if: ${{ startsWith(atomgit.ref, 'refs/heads/') }}
          run: |
            echo "startswith_passed"
        - name: EndsWith match
          if: ${{ endsWith(atomgit.ref_name, 'ain') }}
          run: |
            echo "endswith_passed"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: contains_passed
  - type: positive
    target: run_logs
    must_contain: startswith_passed
  - type: positive
    target: run_logs
    must_contain: endswith_passed
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
| [正向] contains 匹配子串返回真 | ✅ COVERED | if: ${{ contains(atomgit.ref_name, 'main') }}，断言 contains_passed |
| [正向] startsWith 匹配前缀返回真 | ✅ COVERED | if: ${{ startsWith(atomgit.ref, 'refs/heads/') }}，断言 startswith_passed |
| [正向] endsWith 匹配后缀返回真 | ✅ COVERED | if: ${{ endsWith(atomgit.ref_name, 'ain') }}，断言 endswith_passed |
| [负向] 大小写不匹配返回假 | ❌ UNVERIFIABLE | 无步骤测试大小写不匹配场景；无法从单次 dispatch 证明未匹配的否定行为 |

### 问题

- 大小写不匹配返回假：需额外步骤测试大小写差异场景（如 contains(ref_name, 'MAIN')），当前无此测试

---
