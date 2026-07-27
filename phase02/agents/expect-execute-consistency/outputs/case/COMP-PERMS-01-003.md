# COMP-PERMS-01-003

- **标题**: fork PR 的 pull_request 下声明 write 仍仅 read
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 的 pull_request 下声明 write 仍仅 read**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-013

通过标准：
1. [负向] 写操作应失败 —— 断言 run_status != success_with_write
2. [正向] 系统应强制 fork PR TOKEN 为 read-only —— 断言 run_logs contains "write failed as expected"

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write | `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $ATOMGIT_TOKEN" -X POST "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}/issues/1/comments" -d '{"body":"test"}' \|\| echo "write failed as expected"` | permissions: repository: write, as: untrusted_contributor | curl HTTP 状态码或 fail 字符串 |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success_with_write | ✅ GENUINE | `curl` 是真实 HTTP 请求，使用 `$ATOMGIT_TOKEN` 和 `${{ atomgit.api_url }}` 等上下文；fork PR 下 write 被平台拒绝 |
| 2 | run_logs | positive | contains: write failed as expected | ✅ GENUINE | curl 失败时通过 `\|\|` 触发 echo，仅在写操作被拒绝时输出 |

