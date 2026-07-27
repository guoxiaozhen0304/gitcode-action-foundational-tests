# COMPAT-TARGET-01-003
- **标题**: pull_request_target 默认 types 与 GitHub 差异
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request_target 默认 types 与 GitHub 差异**
- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMPAT-032
通过标准：
1. [正向] 默认 types 下 PR open 应触发 workflow
2. [正向] 默认 types 下 PR synchronize 应触发 workflow

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo trigger info | `echo "event_name=${{ atomgit.event_name }}"` → `echo "done"` | - | `event_name=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 PR open 是否触发 |
| 2 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 PR synchronize 是否触发 |

---
