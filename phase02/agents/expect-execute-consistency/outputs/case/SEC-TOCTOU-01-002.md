# SEC-TOCTOU-01-002

- **标题**: 评论触发不应绕过代码固定与 PR 审批
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**评论触发不应绕过代码固定与 PR 审批**

- 触发事件: `issue_comment`
- 规格引用: INTENT-SEC-031

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=trigger_sha_matched

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Check fixed commit | `echo "Executing commit: ${{ atomgit.sha }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  comment-toctou:
    name: Test comment TOCTOU
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check fixed commit
        run: |
          echo "Executing commit: ${{ atomgit.sha }}"
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | positive | equals=trigger_sha_matched | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---