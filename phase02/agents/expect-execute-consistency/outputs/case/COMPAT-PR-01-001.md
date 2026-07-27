# COMPAT-PR-01-001
- **标题**: pull_request types 命名差异 - GitCode 合法 types 应被接受
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**pull_request types 命名差异 - GitCode 合法 types 应被接受**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-011
通过标准：
1. workflow 应被平台接受，不报错
2. PR 事件应按指定 types 触发 workflow
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo PR event | `echo "PR_EVENT_TYPE=${{ atomgit.event.action }}"` 后 `echo "PR_TYPES_OK"` | — | PR_EVENT_TYPE=<action>, PR_TYPES_OK |
## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | positive | — | ✅ GENUINE | step 使用 ${{ atomgit.event.action }} 真实上下文，若 GitCode types 不被接受或触发失败则非 success |
| 2 | run_logs must_contain "PR_TYPES_OK" | positive | — | ⚠️ STATUS_GUARANTEED | echo "PR_TYPES_OK" 是纯字面输出，无 if/uses/${{ }} |
### 问题
- 断言2 为 STATUS_GUARANTEED（纯 echo）
---
