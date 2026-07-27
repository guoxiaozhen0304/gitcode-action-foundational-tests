# COMPAT-PR-01-004
- **标题**: PR types 含 merge 时不触发与 GitHub 行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**PR types 含 merge 时不触发与 GitHub 行为差异**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMPAT-NEW-003
通过标准：
1. [负向] 不通过仅产生 PUSH 运行而无 pull_request 运行
2. [正向] 若平台已修复，合并 PR 后应触发 pull_request 类型运行

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo trigger info | `echo "event_name=${{ atomgit.event_name }}"` → `echo "done"` | - | `event_name=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 PR merge 行为差异 |
| 2 | run_status | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估平台修复后行为 |

---
