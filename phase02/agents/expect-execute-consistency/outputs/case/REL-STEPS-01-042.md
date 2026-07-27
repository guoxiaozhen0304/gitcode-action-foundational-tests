# REL-STEPS-01-042
- **标题**: 超多 step——单 job 内 50 个 step 应全部串行执行无丢失
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**超多 step——单 job 内 50 个 step 应全部串行执行无丢失**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-042
通过标准：
1. 50 个 step 全部出现在运行详情页
2. 每个 step 日志包含唯一标识
3. 不应出现 step 丢失或顺序错乱

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1-50 | step 01 - step 50 | `echo step XX` | — | 每步输出唯一标识 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_count = 50 | positive | — | ⚠️ STATUS_GUARANTEED | 50 个 step 均为 `echo step XX`，无 if:/uses:/`${{ }}`/真实命令。每个 echo 必然成功，JOB 级别的 step 计数由 harness 统计。steps 本身为 VACUOUS 但平台需真实解析和执行 50 个 step |
| 2 | step_order = correct | positive | — | ✅ GENUINE | 50 个 step 按声明顺序串行执行，echo 输出携带递增序号，由 harness 验证顺序 |
### 问题
- 所有 50 个 step 为纯静态 echo（无 `${{ }}`、`uses:`、`if:`），执行结果无条件保证成功（STATUS_GUARANTEED 适用于 run_status）  
- step_count 和 step_order 由 harness 外部验证，非 step 自身产出
---
