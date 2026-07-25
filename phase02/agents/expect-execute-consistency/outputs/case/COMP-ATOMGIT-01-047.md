# COMP-ATOMGIT-01-047

- 标题: atomgit 核心上下文属性可访问性
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action
- workflow 使用 workflow_dispatch 触发

操作步骤:
1. 在 workflow 的 step 中通过表达式引用 atomgit 核心属性
2. 运行 workflow 并检查日志输出

预期结果:
- atomgit.sha / ref / ref_name / ref_type / event_name / repository / run_number / run_attempt / workflow / server_url / api_url / workspace / actor / repositoryUrl / base_ref 均可正常访问并输出非空值

验证点:
- [正向] 各核心属性输出不为空
- [正向] atomgit.sha 长度为 40
- [正向] atomgit.ref 包含 refs/ 前缀
- [正向] atomgit.ref_name 不含 refs/ 前缀

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print core properties | echo "SHA=${{ atomgit.sha }}"; echo "REF=${{ atomgit.ref }}"; ... 共15个属性 | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ATOMGIT-01-047
dimensions: [completeness]
dimension: completeness
priority: P1
title: atomgit 核心上下文属性可访问性
intent_ref: KEEP-TC-017~057
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
      name: Verify atomgit core properties
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Print core properties
          run: |
            echo "SHA=${{ atomgit.sha }}"
            echo "REF=${{ atomgit.ref }}"
            echo "REF_NAME=${{ atomgit.ref_name }}"
            echo "REF_TYPE=${{ atomgit.ref_type }}"
            echo "EVENT=${{ atomgit.event_name }}"
            echo "REPO=${{ atomgit.repository }}"
            echo "RUN_NUM=${{ atomgit.run_number }}"
            echo "RUN_ATT=${{ atomgit.run_attempt }}"
            echo "WF=${{ atomgit.workflow }}"
            echo "SERVER=${{ atomgit.server_url }}"
            echo "API=${{ atomgit.api_url }}"
            echo "WORKSPACE=${{ atomgit.workspace }}"
            echo "ACTOR=${{ atomgit.actor }}"
            echo "REPO_URL=${{ atomgit.repositoryUrl }}"
            echo "BASE_REF=${{ atomgit.base_ref }}"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: SHA=
  - type: positive
    target: run_logs
    must_contain: REF=refs/
  - type: positive
    target: run_logs
    must_contain: REPO=
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
| [正向] 各核心属性输出不为空 | ✅ COVERED | 步骤1 echo 15个属性，断言 SHA=/REF=/REPO= 均有值 |
| [正向] atomgit.sha 长度为 40 | ❌ TRIVIAL | 步骤仅 echo ${{ atomgit.sha }} 不校验长度，断言仅检查 SHA= 存在；步长校验缺失 |
| [正向] atomgit.ref 包含 refs/ 前缀 | ✅ COVERED | 断言 must_contain: REF=refs/ |
| [正向] atomgit.ref_name 不含 refs/ 前缀 | ❌ TRIVIAL | 步骤 echo REF_NAME= 但无对应断言，也未做不含 refs/ 的校验逻辑 |

### 问题

- sha 长度 40 的校验缺失（仅检查 SHA= 存在）
- ref_name 不含 refs/ 前缀的校验缺失（无对应断言和比较逻辑）

---
