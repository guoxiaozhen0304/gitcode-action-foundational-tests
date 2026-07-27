# USE-ENV-01-002
- **标题**: 引用 GITHUB_SHA 时日志应给出环境变量映射提示
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**引用 GITHUB_SHA 时日志应给出环境变量映射提示**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-003
通过标准：
1. 不应静默输出空值后继续
2. 日志中是否出现 ATOMGIT 前缀的环境变量指引

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo GITHUB_SHA | `set -u; echo "sha=$GITHUB_SHA"` | - | $GITHUB_SHA 在 GitCode 不存在，set -u 导致错误退出 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定报错/警告文本是否包含环境变量映射指引 |

### 问题
(无 — 断言为 LLM_DEPENDENT。步骤使用 `set -u` + 未定义变量 $GITHUB_SHA 触发错误退出，runner 是否产生指引性错误消息需 LLM 判定。)
---
