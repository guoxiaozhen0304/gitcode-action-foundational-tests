# COMPAT-YAML-01-001
- **标题**: YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为**
- 触发事件: `push`
- 规格引用: INTENT-COMPAT-049
通过标准：
1. [正向] 标准 on 写法被正确识别为触发配置而非布尔键
2. [负向] workflow 不应因 on 键被解析为布尔而静默不触发且无告警
3. [正向] env 中 on 字面值的取值类型行为确定

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo env literal value | `echo "DEBUG_FLAG=[$DEBUG_FLAG]"` → `echo "ON_KEY_OK"` | - | `DEBUG_FLAG=[on或true]`, `ON_KEY_OK` |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain="ON_KEY_OK" | ✅ GENUINE | step 先输出 `$DEBUG_FLAG`（平台 env 变量，env 值来自 YAML `DEBUG_FLAG: on`，测试 YAML 1.1 布尔陷阱实际行为）再 echo 哨兵，非纯 echo 字面量 |
| 2 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 push 后是否静默不触发 |
| 3 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 DEBUG_FLAG 取值类型 |

---
