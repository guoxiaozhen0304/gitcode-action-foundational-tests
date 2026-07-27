# SEC-TOCTOU-01-001
- **标题**: 审批后推送新 commit 不应被已授权特权运行执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**审批后推送新 commit 不应被已授权特权运行执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-031
通过标准：
1. 审批后推送的恶意代码绝不应被已授权特权运行执行
2. 特权运行执行的 commit 与审批时锁定的 SHA 一致

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check commit SHA | `echo "Running commit: ${{ atomgit.sha }}"` | - | 输出当前运行的 commit SHA |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: "unapproved_commit_executed" | ❌ MISSING_SOURCE | 无任何步骤产生该字符串。步骤仅 echo commit SHA |
| 2 | run_logs | positive | equals: "approved_sha_matched" | ❌ MISSING_SOURCE | 无任何步骤执行 SHA 比对逻辑或输出该字符串。步骤仅 echo `Running commit: <sha>` |

### 问题
**断言 1, 2 — MISSING_SOURCE**: 步骤仅 echo 当前 commit SHA（`${{ atomgit.sha }}`），未与审批 SHA 做任何比对，也不产生 "unapproved_commit_executed" 或 "approved_sha_matched" 字符串。workflow 未实现 TOCTOU 检测逻辑。
---
