# COMPAT-SCHEDULE-01-003
- **标题**: schedule 在非默认分支不触发与 GitHub 差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**schedule 在非默认分支不触发与 GitHub 差异**
- 触发事件: `schedule`
- 规格引用: INTENT-COMPAT-013
通过标准：
1. [负向] develop 分支的 schedule workflow 不应触发
2. [正向] 默认分支的 schedule workflow 正常触发

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo branch | `echo "branch=${{ atomgit.ref_name }}"` → `echo "done"` | - | `branch=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估非默认分支是否触发 |
| 2 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估默认分支是否触发 |

---
