# COMPAT-TOKEN-01-003
- **标题**: GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-020
通过标准：
1. [负向] GITHUB_TOKEN 不等于 ATOMGIT_TOKEN
2. [正向] GITHUB_TOKEN 为空或未定义
3. [负向] 不通过静默映射导致用户误用 GITHUB_TOKEN

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Compare tokens | `echo "GITHUB_TOKEN=$GITHUB_TOKEN"` → `echo "ATOMGIT_TOKEN=$ATOMGIT_TOKEN"` → `echo "done"` | - | `GITHUB_TOKEN=<value>`, `ATOMGIT_TOKEN=<value>`, `done` |
| 2 | Reference secrets GITHUB_TOKEN | `echo "secret_github_token=${{ secrets.GITHUB_TOKEN }}"` → `echo "done"` | - | `secret_github_token=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 对比 GITHUB_TOKEN 与 ATOMGIT_TOKEN 值 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 GITHUB_TOKEN 为空/未定义 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认未静默映射 |

---
