# SEC-TOCTOU-01-003
- **标题**: 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载**
- 触发事件: `pull_request_comment`
- 规格引用: INTENT-SEC-043
通过标准：
1. created 触发读取到触发时刻内容
2. 触发后编辑评论绝不应改变已排队/运行中 workflow 读到的事件负载
3. 审计中评论内容与触发时刻一致

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Snapshot trigger time comment hash | `echo "COMMENT_SNAPSHOT: capturing trigger time comment content hash"` | - | 仅 echo 标记文字 |
| 2 | Window for edit race | `sleep 60; echo "POST_EDIT_READ: re checking comment content consistency"` | - | 等待 60s 后 echo 标记文字 |

## 3. 触发与运行环境
| 触发事件 | pull_request_comment |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals: "trigger_time_snapshot_consistent" | ❌ MISSING_SOURCE | 无任何步骤产生该字符串。步骤仅 echo "COMMENT_SNAPSHOT:" 和 "POST_EDIT_READ:" |
| 2 | run_logs | negative | must_not_contain: "edited_content_adopted" | ❌ MISSING_SOURCE | 无任何步骤产生该字符串 |
| 3 | trigger_audit | nonfunctional | equals: "audit_comment_matches_trigger_time" | 🔶 LLM_DEPENDENT | 非功能断言，需外部审计判定 |

### 问题
**断言 1, 2 — MISSING_SOURCE**: 步骤仅 echo 标记字符串，未实际录制或比对评论内容哈希，也不产生 "trigger_time_snapshot_consistent" 或 "edited_content_adopted" 字符串。workflow 未实现快照比对逻辑。
---
