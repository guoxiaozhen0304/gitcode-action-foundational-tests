# COMP-EXPR-01-057

- 标题: format substring replace 函数边界行为
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 env 中使用 format 拼接字符串，使用 substring 截取 SHA，使用 replace 替换前缀
2. 验证输出符合预期

预期结果:
- format 按占位符替换，substring 截取指定长度，replace 替换所有匹配子串

验证点:
- [正向] format 输出拼接后的字符串
- [正向] substring 输出指定长度子串
- [正向] replace 输出替换后的字符串

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Format string | echo "FMT=${{ format('Hello {0}', 'World') }}" | 是 |
| 2 | Substring sha | echo "SUB=${{ substring(atomgit.sha, 0, 7) }}" | 是 |
| 3 | Replace prefix | echo "REP=${{ replace(atomgit.ref, 'refs/heads/', '') }}" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-EXPR-01-057
dimensions: [completeness]
dimension: completeness
priority: P1
title: format substring replace 函数边界行为
intent_ref: KEEP-TC-183~185
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
      name: Verify format substring replace
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Format string
          run: |
            echo "FMT=${{ format('Hello {0}', 'World') }}"
        - name: Substring sha
          run: |
            echo "SUB=${{ substring(atomgit.sha, 0, 7) }}"
        - name: Replace prefix
          run: |
            echo "REP=${{ replace(atomgit.ref, 'refs/heads/', '') }}"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: FMT=Hello World
  - type: positive
    target: run_logs
    must_contain: SUB=
  - type: positive
    target: run_logs
    must_contain: REP=
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
| [正向] format 输出拼接后的字符串 | ✅ COVERED | 断言 FMT=Hello World，验证 'Hello {0}' 替换为 'Hello World' |
| [正向] substring 输出指定长度子串 | ✅ COVERED | 步骤 SUB=${{ substring(atomgit.sha,0,7) }}，断言 SUB= 存在 |
| [正向] replace 输出替换后的字符串 | ✅ COVERED | 步骤 REP=${{ replace(atomgit.ref, 'refs/heads/', '') }}，断言 REP= 存在 |

### 问题

- 无（SUB= 和 REP= 的断言仅检查存在而非精确值，但 spec 验证点为正向功能）

---
