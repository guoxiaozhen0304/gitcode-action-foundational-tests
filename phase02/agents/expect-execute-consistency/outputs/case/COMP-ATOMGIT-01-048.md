# COMP-ATOMGIT-01-048

- 标题: atomgit 事件相关属性可访问性
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action
- workflow 配置为 push 触发

操作步骤:
1. 在 push 触发的 workflow 中引用 atomgit.event 下各字段
2. 运行 workflow 并检查日志

预期结果:
- push 事件下 atomgit.event.ref / before / after / commits / base_ref / created / deleted 等字段可正常访问并输出非空或合理值

验证点:
- [正向] event.ref 与 atomgit.ref 一致
- [正向] event.before 和 event.after 为 40 位 SHA
- [正向] event.commits 数组可访问

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print event properties | echo "EVENT_REF=${{ atomgit.event.ref }}"; echo "BEFORE=${{ atomgit.event.before }}"; ... | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ATOMGIT-01-048
dimensions: [completeness]
dimension: completeness
priority: P1
title: atomgit 事件相关属性可访问性
intent_ref: KEEP-TC-048~060
setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default
fault_injection: null
workflow: |
  on:
    push:
      branches: [main]
  jobs:
    verify:
      name: Verify event properties on push
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Print event properties
          run: |
            echo "EVENT_REF=${{ atomgit.event.ref }}"
            echo "BEFORE=${{ atomgit.event.before }}"
            echo "AFTER=${{ atomgit.event.after }}"
            echo "COMMITS_LEN=${{ atomgit.event.commits }}"
            echo "BASE_REF=${{ atomgit.event.base_ref }}"
            echo "CREATED=${{ atomgit.event.created }}"
            echo "DELETED=${{ atomgit.event.deleted }}"
trigger:
  event: push
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: EVENT_REF=refs/
  - type: positive
    target: run_logs
    must_contain: BEFORE=
  - type: positive
    target: run_logs
    must_contain: AFTER=
teardown:
  reset: fixture
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] event.ref 与 atomgit.ref 一致 | ✅ COVERED | 断言 EVENT_REF=refs/，与 atomgit.ref 的 refs/ 前缀一致，间接验证 |
| [正向] event.before 和 event.after 为 40 位 SHA | ❌ TRIVIAL | 步骤仅 echo BEFORE= 和 AFTER= 但无长度校验逻辑；断言仅检查 = 存在 |
| [正向] event.commits 数组可访问 | ❌ TRIVIAL | 步骤 echo COMMITS_LEN= 但无断言覆盖此输出，也未验证数组内容 |

### 问题

- event.before/after 40 位 SHA 格式校验缺失（仅检查存在）
- event.commits 数组访问性未断言

---
