# REL-DEBOUNCE-01-001
- **标题**: 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**同分支 10 秒内连续 5 次 push 的 run 记录与事件一一对账**
- 触发事件: `push`
- 规格引用: INTENT-REL-073
通过标准：
1. run 记录与 push 5/5 对账
2. 同一 sha 不重复触发

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | record sha step | `echo "trigger_sha=${{ atomgit.sha }}"` | - | 输出当前 push 的 commit sha |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | push_sha_run_mapping = 1:1_or_documented_debounce | positive | - | ✅ GENUINE | 步骤包含 `${{ atomgit.sha }}` 表达式，从平台上下文获取动态值；harness 对账 |
| 2 | same_sha_duplicate_runs_count = 0 | positive | - | ✅ GENUINE | 触发幂等性由平台控制，harness 校验 |
| 3 | unexplained_run_loss_detected = true | negative | - | ✅ GENUINE | 负向验证 run 无丢失 |
---
