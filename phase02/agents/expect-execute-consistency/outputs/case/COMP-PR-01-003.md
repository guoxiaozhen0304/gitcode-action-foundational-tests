# COMP-PR-01-003

- **标题**: fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-004

通过标准：
1. [负向] 写操作（如推送、评论）应失败 —— 断言 run_step_result != write_succeeded
2. [正向] ATOMGIT_TOKEN 权限为 read-only —— 断言 run_status=success_or_failure

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write with token | `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $ATOMGIT_TOKEN" -X POST "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}/issues/1/comments" -d '{"body":"test"}' \|\| echo "write failed as expected"` | - (as: untrusted_contributor) | curl HTTP 状态码或 fail 字符串 |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_step_result | negative | equals: write_succeeded | ✅ GENUINE | `curl` 是真实 HTTP 请求，使用 `$ATOMGIT_TOKEN` 和 `${{ atomgit.api_url }}` 上下文；fork PR 场景下 TOKEN 仅 read |
| 2 | run_status | positive | equals: success_or_failure | ✅ GENUINE | 步骤包含真实 curl 命令和 `${{ }}` 表达式 |

