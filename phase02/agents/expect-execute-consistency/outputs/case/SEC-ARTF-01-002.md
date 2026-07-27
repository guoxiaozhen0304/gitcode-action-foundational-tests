# SEC-ARTF-01-002
- **标题**: 跨仓库 artifact 下载返回 403 或 404
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**主仓尝试下载 fork PR 的 artifact ID 返回 403/404**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-019
通过标准：
1. 日志不含 HTTP 200
2. 日志返回 403 或 404
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt download fork artifact | `curl -s -o /dev/null -w "%{http_code}" "https://api.gitcode.com/api/v8/repos/${{ atomgit.repository }}/actions/artifacts/FORK_ARTIFACT_ID/zip?access_token=${{ atomgit.token }}"` | — | HTTP 状态码 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-artifacts |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 日志不含 "200" | negative | run_logs must_not_contain "200" | ✅ GENUINE | 步骤使用 ${{ }} 表达式执行 curl，依赖真实平台 API 响应 |
| 2 | 日志等于 "403_or_404" | positive | run_logs equals "403_or_404" | ❌ VACUOUS | 步骤输出 HTTP 状态码（数字如 "403"），但断言期望精确字符串 "403_or_404"；步骤从不输出该字面量字符串，仅靠外部判定器映射 |
### 问题
断言 2 VACUOUS：curl 输出的是 HTTP 状态码数字（如 "403"），并非字面量 "403_or_404"，该字符串仅存在于断言期望中。
---
