# COMP-ISOLATION-01-001

- 标题: 同一 workflow 先后 job 的文件系统相互隔离
- 维度: 完备性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- workflow 含两个串行 jobs

操作步骤:
1. job 1 写入文件到工作目录
2. job 2 尝试读取该文件

预期结果:
- job 2 无法看到 job 1 写入的文件

验证点:
- [负向] job 2 不应访问到 job 1 的文件
- [正向] 显式通过 artifact 传递后 job 2 可访问

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Create file | echo "secret data" > /tmp/isolation_test.txt | 是 |
| 2 | Attempt read | if [ -f /tmp/isolation_test.txt ]; then cat it; exit 1; else echo "file not found as expected"; fi | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-ISOLATION-01-001
dimensions: [completeness, reliability, security]
dimension: completeness
priority: P0
title: 同一 workflow 先后 job 的文件系统相互隔离
intent_ref: INTENT-COMP-011

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    job1:
      name: Write file
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Create file
          run: |
            echo "secret data" > /tmp/isolation_test.txt
    job2:
      name: Read file
      runs-on: [ubuntu-latest, x64, small]
      needs: job1
      steps:
        - name: Attempt read
          run: |
            if [ -f /tmp/isolation_test.txt ]; then
              echo "file exists"
              cat /tmp/isolation_test.txt
              exit 1
            else
              echo "file not found as expected"
            fi

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: run_status
    equals: success
  - type: negative
    target: run_logs
    must_not_contain: secret data

teardown:
  reset: none
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
| [负向] job 2 不应访问到 job 1 的文件 | ✅ COVERED | negative assertion: must_not_contain "secret data"，job2 的 bash 逻辑 exit 1 若文件存在 |
| [正向] 显式通过 artifact 传递后 job 2 可访问 | ❌ TRIVIAL | 当前 workflow 无 artifact 传递步骤，该正向验证点未实现 |

### 问题

- artifact 传递后的正向验证缺失：spec 要求验证"显式通过 artifact 传递后 job 2 可访问"，但 workflow 无 artifact 相关步骤

---
