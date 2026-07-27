# USE-RUN-01-003
- **标题**: rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assisted）
- **维度**: usability
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**rerun 上限与 6 小时时限在 UI 的明示（判定方式：llm_assisted）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-049
通过标准：
1. 达到 3 次上限后按钮置灰且悬停提示已达最大重跑次数
2. 超过 6 小时的运行按钮置灰且悬停提示时限原因
3. 运行详情页应显示当前已重跑次数

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | fail step | `exit 1` | 无 | 制造失败运行（用于重跑按钮验证） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui eval=llm_assisted | nonfunctional | LLM 判定 UI 重跑按钮 tooltip 与详情页展示 | 🔶 LLM_DEPENDENT | 唯一断言为 LLM 辅助判定 UI 交互 |

### 问题
唯一断言为 nonfunctional + llm_assisted，步骤仅有 `exit 1` 制造失败运行，重跑行为判定完全依赖 LLM 对 UI 语义评估。
---
