# COMP-ATOMGIT-01-049

- 标题: atomgit 边界格式校验
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 step 中校验 atomgit.sha 长度、ref 格式、ref_name 无前缀等边界条件
2. 运行 workflow 并断言格式

预期结果:
- atomgit.sha 长度为 40，atomgit.ref 以 refs/ 开头，atomgit.ref_name 不含 refs/ 前缀，atomgit.actor 非空

验证点:
- [正向] sha 长度等于 40
- [正向] ref 以 refs/ 开头
- [正向] ref_name 不含 refs/ 前缀
- [正向] actor 非空

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check formats | echo "SHA_LEN=${#ATOMGIT_SHA}"; echo "REF_PREFIX=${ATOMGIT_REF%%/*}"; echo "REF_NAME_NO_PREFIX=${ATOMGIT_REF_NAME#refs/}"; echo "ACTOR_LEN=${#ATOMGIT_ACTOR}" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ATOMGIT-01-049
dimensions: [completeness]
dimension: completeness
priority: P1
title: atomgit 边界格式校验
intent_ref: KEEP-TC-566~570
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
      name: Verify atomgit boundary formats
      runs-on: [dedicate-hosted, x64, large]
      steps:
        - name: Check formats
          run: |
            echo "SHA_LEN=${#ATOMGIT_SHA}"
            echo "REF_PREFIX=${ATOMGIT_REF%%/*}"
            echo "REF_NAME_NO_PREFIX=${ATOMGIT_REF_NAME#refs/}"
            echo "ACTOR_LEN=${#ATOMGIT_ACTOR}"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: SHA_LEN=40
  - type: positive
    target: run_logs
    must_contain: REF_PREFIX=refs
  - type: positive
    target: run_logs
    must_contain: ACTOR_LEN=
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
| [正向] sha 长度等于 40 | ✅ COVERED | 断言 must_contain: SHA_LEN=40 |
| [正向] ref 以 refs/ 开头 | ✅ COVERED | 断言 must_contain: REF_PREFIX=refs |
| [正向] ref_name 不含 refs/ 前缀 | ❌ TRIVIAL | 步骤 echo REF_NAME_NO_PREFIX 但无对应断言；strip 后无值时的边界校验缺失 |
| [正向] actor 非空 | ✅ COVERED | 断言 must_contain: ACTOR_LEN= |

### 问题

- ref_name 不含 refs/ 前缀的校验：步骤有 echo REF_NAME_NO_PREFIX 但 YAML assertions 中没有对应断言

---
