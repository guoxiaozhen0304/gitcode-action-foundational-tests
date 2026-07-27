# SEC-WFRUN-01-001
- **标题**: 不可信运行绝不应存在隐式拉起高权限后续运行的链式路径
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**不可信运行绝不应存在隐式拉起高权限后续运行的链式路径**
- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-044
通过标准：
1. 不可信（fork PR）运行绝不应隐式拉起高权限后续运行
2. 文档应明示 workflow_run 不支持及替代安全模式

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (无 workflow) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | must_not_contain: "implicit_privileged_run_after_fork_pr" | ❌ UNEXERCISED | workflow: null，无步骤产生 run_list 数据 |
| 2 | documentation | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 辅助判定文档内容 |

### 问题
**断言 1 — UNEXERCISED**: workflow 为 null，不存在任何步骤产生 run_list target 的输出。该断言完全依赖 harness 侧枚举运行列表。
---
