# SEC-COMM-01-001

- **标题**: issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**issue_comment / pull_request_comment 触发关键字过滤必须不可被绕过**

- 触发事件: `issue_comment`
- 规格引用: INTENT-SEC-026

通过标准：
1. type=negative, target=run_status
2. type=positive, target=run_logs, equals=workflow_not_triggered

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Check trigger | `echo "Triggered by comment"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  comment-filter:
    name: Test comment keyword filter
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check trigger
        run: |
          echo "Triggered by comment"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `issue_comment` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative |  | ✅ GENUINE | 状态断言  可被步骤行为验证 |
| 2 | run_logs | positive | equals=workflow_not_triggered | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---