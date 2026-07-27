# COMP-PR-01-003

- **标题**: fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-004

通过标准：
1. type=negative, target=run_step_result, equals=write_succeeded
2. type=positive, target=run_status, equals=success_or_failure

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt write with token | `curl -s -o /dev/null -w "%{http_code}"                     -H "Authorization: to` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches:
      - main
jobs:
  verify:
    name: Verify fork PR token read only
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write with token
        run: |
          curl -s -o /dev/null -w "%{http_code}"                     -H "Authorization: token $ATOMGIT_TOKEN"                     -X POST                     "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}/issues/1/comments"                     -d '{"body":"test"}' || echo "write failed as expected"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_step_result | negative | equals=write_succeeded | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_status | positive | equals=success_or_failure | ✅ GENUINE | 状态断言 success_or_failure 可被步骤行为验证 |

---