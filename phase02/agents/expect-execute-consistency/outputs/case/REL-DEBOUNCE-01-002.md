# REL-DEBOUNCE-01-002
- **标题**: 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释**
- 触发事件: `tag`
- 规格引用: INTENT-REL-073
通过标准：
1. run 创建与 tag 事件 10/10 对账
2. 同一 tag 不触发 2 次

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | record ref step | `echo "trigger_ref=${{ atomgit.ref }}"` | - | 输出触发 tag 的 ref |

## 3. 触发与运行环境
| 触发事件 | tag |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | tag_event_run_reconciliation = 10/10_or_documented_debounce | positive | - | ✅ GENUINE | 步骤含 `${{ atomgit.ref }}` 动态表达式；harness 对账 |
| 2 | same_tag_duplicate_runs_count = 0 | positive | - | ✅ GENUINE | 平台去重 + harness 验证 |
| 3 | unexplained_run_loss_detected = true | negative | - | ✅ GENUINE | 负向验证无丢失 |
---
