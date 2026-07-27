# SEC-TOCTOU-01-003

- **标题**: 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载**

- 触发事件: `pull_request_comment`
- 规格引用: INTENT-SEC-043

通过标准：
1. type=positive, target=run_logs, equals=trigger_time_snapshot_consistent
2. type=negative, target=run_logs
3. type=nonfunctional, target=trigger_audit, equals=audit_comment_matches_trigger_time

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Snapshot trigger time com | `echo "COMMENT_SNAPSHOT: capturing trigger time comment content hash"` |  | ❌ VACUOUS |
| 2 | Window for edit race | `sleep 60 echo "POST_EDIT_READ: re checking comment content consistency"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_comment:
    types: [created, edited]
jobs:
  snapshot-check:
    name: Comment snapshot consistency check
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Snapshot trigger time comment hash
        run: |
          echo "COMMENT_SNAPSHOT: capturing trigger time comment content hash"
      - name: Window for edit race
        run: |
          sleep 60
          echo "POST_EDIT_READ: re checking comment content consistency"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_comment` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals=trigger_time_snapshot_consistent | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 3 | trigger_audit | nonfunctional | equals=audit_comment_matches_trigger_time | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---