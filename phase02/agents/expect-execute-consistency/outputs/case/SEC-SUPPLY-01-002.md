# SEC-SUPPLY-01-002
- **标题**: commit hash 不匹配时第三方 Action 应被拒绝执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**commit hash 不匹配时第三方 Action 应被拒绝执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-014
通过标准：
1. 错误 commit SHA 绝不应执行 Action
2. 返回明确的 Action 未找到或 SHA 不匹配错误

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use invalid hash action | uses: docker/build-push-action@0000000000000000000000000000000000000000 | - | action 解析失败，平台产生错误日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | must_not_equal: "success" | ✅ GENUINE | `uses:` 引用不存在的 hash，平台无法解析，运行不应成功 |
| 2 | run_logs | positive | equals: "action_not_found_or_sha_mismatch" | ✅ GENUINE | `uses:` action 解析失败产生错误日志，平台应输出拒绝信息 |
---
