# COMP-DIR-01-001

- 标题: .gitcode/workflows/ 下的 YAML 被正确识别并触发
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action
- 仓库 .gitcode/workflows/ 目录下存在 ci.yml

操作步骤:
1. 向默认分支推送代码变更
2. 观察 Actions 标签页是否出现新运行

预期结果:
- .gitcode/workflows/ci.yml 被识别为 workflow
- push 事件触发该 workflow 执行
- 运行状态最终变为 completed/success

验证点:
- [正向] 运行记录存在且 file_path 为 .gitcode/workflows/ci.yml
- [正向] 运行状态成功完成

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo verify | echo "workflow recognized" | 否 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-DIR-01-001
dimensions: [completeness]
dimension: completeness
priority: P1
title: .gitcode/workflows/ 下的 YAML 被正确识别并触发
intent_ref: INTENT-COMP-001

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    push:
      branches:
        - main
  jobs:
    verify:
      name: Verify directory recognition
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Echo verify
          run: |
            echo "workflow recognized"

trigger:
  event: push
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: run_status
    equals: success
  - type: positive
    target: run_file_path
    equals: .gitcode/workflows/ci.yml

teardown:
  reset: none
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
| [正向] 运行记录存在且 file_path 为 .gitcode/workflows/ci.yml | ✅ COVERED | 断言 run_file_path = .gitcode/workflows/ci.yml |
| [正向] 运行状态成功完成 | ✅ COVERED | 断言 run_status=success |

### 问题

- 无

---
