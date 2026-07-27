# COMPAT-RUNNER-01-004
- **标题**: 自定义特征标签不被支持时应给出可用标签列表
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**自定义特征标签不被支持时应给出可用标签列表**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-NEW-008
通过标准：
1. [正向] 报错信息说明标签不匹配
2. [正向] 报错给出可用标签列表或标签格式指引

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo hello | `echo "hello"` | - | `hello` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估报错信息内容 |
| 2 | error_message | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估是否列出可用标签 |

---
