# COMPAT-WCMD-01-004
- **标题**: 注解命令 error/warning/notice 的不中断降级行为
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**注解命令 error/warning/notice 的不中断降级行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-042
通过标准：
1. [正向] 输出注解命令后 workflow 仍按脚本逻辑成功结束
2. [负向] 注解命令不应截断后续日志或产生非预期副作用
3. [非功能] 与 GitHub 注解 UI 能力的差距进入差异清单

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Emit error warning notice commands | `echo "::error::demo error annotation"` → `echo "::warning::demo warning annotation"` → `echo "::notice::demo notice annotation"` | - | 三条注解命令 |
| 2 | Confirm subsequent commands run | `echo "AFTER_ANNOTATION_OK"` | - | `AFTER_ANNOTATION_OK` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 步骤使用 `::error::`、`::warning::`、`::notice::` 注解命令，测试命令是否导致 step 失败——有真实 failure 可能 |
| 2 | run_logs | positive | must_contain="AFTER_ANNOTATION_OK" | ✅ GENUINE | 第二步骤先输出注解命令（真实 workflow command 功能）再 echo 哨兵，测试后续命令是否被截断 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估日志是否被截断或有副作用 |

---
