# COMPAT-SCHEDULE-01-002
- **标题**: schedule 不支持 timezone 字段差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**schedule 不支持 timezone 字段差异**
- 触发事件: `schedule`
- 规格引用: INTENT-COMPAT-013
通过标准：
1. [负向] 不应因 timezone 字段导致不可预期的行为
2. [正向] 错误信息应明确指出 timezone 字段不支持或文档说明忽略策略

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo schedule | `echo "SCHEDULE_TIMEZONE_OK"` | - | `SCHEDULE_TIMEZONE_OK` |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals=success (期望 NOT success) | ✅ COVERED | 平台验证型：YAML 含 `timezone` 字段（语义上可能不被支持），断言要求 run_status != success（平台应拒绝不接受该字段的工作流），属平台校验测试 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：需 LLM 评估 error_message 内容 |

---
