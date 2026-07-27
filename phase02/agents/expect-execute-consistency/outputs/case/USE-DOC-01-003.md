# USE-DOC-01-003
- **标题**: trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾
- **维度**: 易用性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾**
- 触发事件: `schedule`
- 规格引用: INTENT-USE-033
通过标准：
1. 文档不应在最短间隔 5 分钟提示下方仍给出每分钟 cron 示例
2. 记录平台对该 cron 的接受/拒绝行为，与文档两处声明比对

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | marker step | `echo "scheduled"` | - | 仅 echo |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval: "deterministic" | ❌ MISSING_SOURCE | target=documentation，无 workflow 步骤产生 |
| 2 | validation_result | positive | eval: "deterministic" | ❌ MISSING_SOURCE | target=validation_result (deterministic)，无 workflow 步骤直接产生该 target 输出 |

### 问题
**断言 1 — MISSING_SOURCE**: target=documentation，纯静态文档扫描。
**断言 2 — MISSING_SOURCE**: target=validation_result (eval=deterministic)，平台 cron 策略的接受/拒绝行为需 harness 外部记录，workflow 仅作为 probe 存在。
---
