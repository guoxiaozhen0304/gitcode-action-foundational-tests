# COMPAT-PR-01-010
- **标题**: 存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**存在合并冲突的 PR 的触发行为（GitHub 不触发）对齐确认**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-039
通过标准：
1. [正向] 冲突 PR 的触发行为得到确定结论并与 GitHub（不触发）比对
2. [负向] 若触发，其运行不应被当作正常 PR 验证结果且无差异说明

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark conflicted PR run | `echo "CONFLICT_PR_JOB_RAN"` | - | `CONFLICT_PR_JOB_RAN` |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | with-merge-conflict-pr |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估冲突 PR 是否产生运行 |
| 2 | run_list | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：触发策略回写 Parity Matrix |

---
