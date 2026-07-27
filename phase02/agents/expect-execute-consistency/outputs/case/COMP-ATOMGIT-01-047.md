# COMP-ATOMGIT-01-047

- **标题**: atomgit 核心上下文属性可访问性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**atomgit 核心上下文属性可访问性**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-047

通过标准：
1. type=positive, target=run_logs, must_contain="SHA="
2. type=positive, target=run_logs, must_contain="REF=refs/"
3. type=positive, target=run_logs, must_contain="REPO="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Print core properties | `echo "SHA=${{ atomgit.sha }}" echo "REF=${{ atomgit.ref }}" echo "REF_NAME=${{ a` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
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
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=SHA= | ✅ GENUINE | SHA=: GENUINE |
| 2 | run_logs | positive | must_contain=REF=refs/ | ❌ MISSING_SOURCE | REF=refs/: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=REPO= | ✅ GENUINE | REPO=: GENUINE |

### 问题

**断言 2 — MISSING_SOURCE**❌: REF=refs/: MISSING_SOURCE (无步骤产出此字符串)

---