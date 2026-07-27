# REL-LOG-01-041
- **标题**: 单 job 日志大小上限探测——500MB 带序号日志的完整保留或明确截断标识
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**500MB 日志完整保留或明确截断**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-077
通过标准：
1. 下载日志行号连续可判定完整/截断
2. 不应静默截断
3. 实测上限记录

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | emit numbered log step | `seq -f "LOG_LINE_%08.0f xxxxx" 8000000` | - | 约 500MB 带行号日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_downloadable = true | positive | - | ✅ GENUINE | seq 是真实命令输出大量带行号日志 |
| 2 | tail_integrity = complete_or_explicitly_marked_truncated | positive | - | ✅ GENUINE | 行号可供完整性校验 |
| 3 | silent_tail_loss_detected = true | negative | - | ✅ GENUINE | 负向验证无静默丢失 |
| 4 | measured_log_limit = recorded | nonfunctional | - | 🔶 LLM_DEPENDENT | 非功能指标 |
---
