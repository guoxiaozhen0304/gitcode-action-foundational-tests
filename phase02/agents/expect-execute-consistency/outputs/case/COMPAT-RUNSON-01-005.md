# COMPAT-RUNSON-01-005
- **标题**: Runner OS 多样性探测：windows-latest 的调度结局（不支持应明确报错）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Runner OS 多样性探测：windows-latest 的调度结局（不支持应明确报错）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-054
通过标准：
1. [正向/记录] windows-latest 的调度结局逐字记录
2. [负向] 指定不支持 OS 的 job 不应无限 queued 无提示
3. [非功能] 结论回写 parity-matrix 新增 Runner OS 多样性能力行

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark if scheduled on windows | `echo "WINDOWS_RUNNER_SCHEDULED"` | - | `WINDOWS_RUNNER_SCHEDULED` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 windows-latest 调度结局 |
| 2 | run_status | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估是否无限 queued |
| 3 | run_status | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：结论回写 parity-matrix |

---
