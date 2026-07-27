# SEC-TOCTOU-01-002
- **标题**: 评论触发不应绕过代码固定与 PR 审批
- **维度**: 安全性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**评论触发不应绕过代码固定与 PR 审批**
- 触发事件: `issue_comment`
- 规格引用: INTENT-SEC-031
通过标准：
1. 评论触发后推送的新 commit 绝不应被该次特权运行自动执行
2. 运行日志中的 commit SHA 与触发时刻一致

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check fixed commit | `echo "Executing commit: ${{ atomgit.sha }}"` | - | 输出当前运行的 commit SHA |

## 3. 触发与运行环境
| 触发事件 | issue_comment |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: "new_commit_after_trigger" | ❌ MISSING_SOURCE | 无任何步骤产生该字符串。步骤仅 echo commit SHA |
| 2 | run_logs | positive | equals: "trigger_sha_matched" | ❌ MISSING_SOURCE | 无任何步骤执行 SHA 比对或输出该字符串 |

### 问题
**断言 1, 2 — MISSING_SOURCE**: 步骤仅 echo 当前 commit SHA，未执行任何 SHA 比对逻辑，也不产生 "new_commit_after_trigger" 或 "trigger_sha_matched" 字符串。
---
