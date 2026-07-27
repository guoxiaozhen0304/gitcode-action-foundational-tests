# COMPAT-WCMD-01-005
- **标题**: debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-042
通过标准：
1. [正向] ::debug:: 默认可见性行为确定且被记录
2. [非功能] debug 门控机制差异进入迁移对照文档

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Emit debug command | `echo "::debug::demo debug message"` → `echo "DEBUG_PROBE_DONE"` | - | `::debug::demo debug message`, `DEBUG_PROBE_DONE` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain="DEBUG_PROBE_DONE" | ✅ GENUINE | 步骤先执行 `::debug::` 工作流命令（真实平台功能）再 echo 哨兵 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 debug message 默认可见性 |

---
