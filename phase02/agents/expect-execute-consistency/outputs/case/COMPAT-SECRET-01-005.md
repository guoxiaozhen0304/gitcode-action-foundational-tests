# COMPAT-SECRET-01-005
- **标题**: 环境级 secrets 不支持时应明确报错而非降级为项目级
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**环境级 secrets 不支持时应明确报错而非降级为项目级**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-002
通过标准：
1. [负向] 不通过静默降级（ENV_SECRET 不应返回 PROJECT_SECRET 的值）
2. [正向] 系统对环境级 secrets 的缺失给出明确提示
3. [正向] 项目级 secrets 正常注入

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check secrets | `echo "project_secret=${{ secrets.PROJECT_SECRET }}"` → `echo "env_secret=${{ secrets.ENV_SECRET }}"` → `echo "done"` | - | `project_secret=<value>`, `env_secret=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [PROJECT_SECRET] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 ENV_SECRET 是否被静默降级 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估项目级 secret 是否正常注入 |
| 3 | error_message | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估缺失提示内容 |

---
