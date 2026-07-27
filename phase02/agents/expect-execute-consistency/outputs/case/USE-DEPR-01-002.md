# USE-DEPR-01-002
- **标题**: 使用 ::set-output 时应给出弃用警告与替代示例
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 ::set-output 时应给出弃用警告与替代示例**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-010
通过标准：
1. 不应静默生效
2. 日志警告中应包含 deprecated/废弃/ATOMGIT_OUTPUT 字样

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | use deprecated set-output | `echo "::set-output name=mykey::myvalue"` | - | 发出已弃用的 workflow 命令 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定 runner 产生的弃用警告文本 |

### 问题
(无 — 断言为 LLM_DEPENDENT，跳过。步骤 echo 了 ::set-output 命令，runner 应产生弃用警告，但警告质量需 LLM 评估。)
---
