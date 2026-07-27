# COMPAT-RUNNER-01-001
- **标题**: runner.os 在 Linux Runner 上应返回 Linux
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runner.os 在 Linux Runner 上应返回 Linux**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-018
通过标准：
1. [正向] 日志中 runner.os 的值为 Linux
2. [负向] 不应返回小写的 linux

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo runner os | `echo "runner_os=${{ runner.os }}"` → `echo "done"` | - | `runner_os=<value>`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 步骤含 `${{ runner.os }}` 表达式求值，run_status 非必然成功——表达式求值或标签匹配可能失败 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 验证 runner_os 值为 Linux 而非 linux |

---
