# COMPAT-RUNSON-01-003
- **标题**: 自托管 runs-on 对象式写法（type/group/labels）的实测仲裁
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**自托管 runs-on 对象式写法（type/group/labels）的实测仲裁**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-046
通过标准：
1. [正向] 对象式写法的调度或报错结局确定
2. [负向] 不应无限 queued 无提示

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark scheduling success | `echo "OBJECT_FORM_SCHEDULED"` | - | `OBJECT_FORM_SCHEDULED` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-self-hosted-runner |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估对象式写法调度结局 |
| 2 | run_status | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估是否无限 queued |

---
