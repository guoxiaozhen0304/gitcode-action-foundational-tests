# SEC-TOKEN-01-002
- **标题**: fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝**
- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-003
通过标准：
1. 写操作绝不应成功
2. 权限拒绝信息明确

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt push | `git clone ... && git push || echo "push denied"` | - | git 操作输出；push 失败时 echo "push denied" |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | equals: "push_denied_or_403" | ❌ MISSING_SOURCE | 步骤输出 "push denied"（push 失败时），与断言字符串 "push_denied_or_403" 不一致 |
| 2 | run_status | positive | equals: "completed" | ✅ GENUINE | 步骤含 `${{ atomgit.token }}` + 真实 git 操作，存在合理失败路径（clone 可能失败） |

### 问题
**断言 1 — MISSING_SOURCE**: 步骤在 push 失败时输出 "push denied"，而断言期望 "push_denied_or_403"，字符串不匹配。步骤行为真实但断言字符串与输出不一致。
---
