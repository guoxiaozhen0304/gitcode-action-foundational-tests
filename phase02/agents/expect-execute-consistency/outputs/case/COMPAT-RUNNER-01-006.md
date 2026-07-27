# COMPAT-RUNNER-01-006
- **标题**: Runner 未预装 Java 工具链与 GitHub 差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Runner 未预装 Java 工具链与 GitHub 差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-011
通过标准：
1. [正向] 系统对缺失的 Java 工具链给出明确提示
2. [正向] 提示应建议替代方案（如使用自定义 Runner 或预装环境）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check Java | `java -version \|\| true` → `mvn -version \|\| true` → `echo "done"` | - | java/mvn 版本或错误, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估命令输出中缺失提示 |
| 2 | error_message | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估替代方案建议 |

---
