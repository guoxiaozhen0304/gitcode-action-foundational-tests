# COMP-EXPR-01-056

- 标题: toJson 函数边界行为
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 run 中使用 toJson 序列化 atomgit.event 和 env 上下文
2. 验证输出为合法 JSON 字符串

预期结果:
- toJson 将对象序列化为合法 JSON 字符串，字符串含转义

验证点:
- [正向] toJson(atomgit.event) 输出以 { 开头
- [正向] toJson(env) 输出合法 JSON
- [正向] 嵌套对象可被正确序列化

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Serialize event | echo "EVENT_JSON=${{ toJson(atomgit.event) }}" | 是 |
| 2 | Serialize env context | echo "ENV_JSON=${{ toJson(env) }}" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-EXPR-01-056
dimensions: [completeness]
dimension: completeness
priority: P1
title: toJson 函数边界行为
intent_ref: KEEP-TC-187
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
      name: Verify toJson boundary
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Serialize event
          run: |
            echo "EVENT_JSON=${{ toJson(atomgit.event) }}"
        - name: Serialize env context
          env:
            TEST_KEY: test_value
          run: |
            echo "ENV_JSON=${{ toJson(env) }}"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: "EVENT_JSON={"
  - type: positive
    target: run_logs
    must_contain: "ENV_JSON={"
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
| [正向] toJson(atomgit.event) 输出以 { 开头 | ✅ COVERED | 断言 must_contain: EVENT_JSON={ |
| [正向] toJson(env) 输出合法 JSON | ✅ COVERED | 断言 must_contain: ENV_JSON={ |
| [正向] 嵌套对象可被正确序列化 | ❌ TRIVIAL | atomgit.event 本身为嵌套对象，但断言仅检查前缀 {，未验证嵌套结构完整性 |

### 问题

- 嵌套对象序列化验证不充分：断言仅检查 JSON 以 { 开头，未验证嵌套键值对的正确性

---
