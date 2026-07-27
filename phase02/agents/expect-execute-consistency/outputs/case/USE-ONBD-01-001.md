# USE-ONBD-01-001
- **标题**: 新手快速开始路径端到端可复刻走查（判定方式：llm_assisted）
- **维度**: usability
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**新手快速开始路径端到端可复刻走查（判定方式：llm_assisted）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-050
通过标准：
1. 每步有可观察验证点
2. 不应存在文档假设用户知道但新手不知道的隐式前提
3. 全流程应在 30 分钟内可完成

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | workflow: null | 无 workflow 步骤 | — | 纯文档 / 人工走查 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation eval=llm_assisted | nonfunctional | LLM 模拟新手走查 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定新手卡壳点 |
| 2 | documentation 确定性校验：quick-start 前提清单含 Action 开通步骤 | negative | 确定性文档检查 | ✅ COVERED | 但仅有文档前置条件检查无法覆盖端到端走查主目标 |

### 问题
主目标为非功能 LLM 辅助走查，整体验证策略无法通过自动化分析判定。
---
