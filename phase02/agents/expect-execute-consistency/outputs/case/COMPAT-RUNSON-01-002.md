# COMPAT-RUNSON-01-002
- **标题**: runs-on 标签体系——单标签字符串应报错
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runs-on 标签体系——单标签字符串应报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-027
通过标准：
1. [负向] 单标签字符串格式在解析/校验阶段报错
2. [正向] 错误信息应明确说明需使用数组格式
3. [负向] 不应静默调度到不匹配标签的 Runner

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | (TC) should not reach here | `echo "RUNSON_STRING_ACCEPTED"` | - | `RUNSON_STRING_ACCEPTED` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | workflow_parse | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估解析/校验阶段是否报错 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估错误信息是否提示数组格式 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认未出现 RUNSON_STRING_ACCEPTED |

---
