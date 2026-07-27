# USE-NEST-01-001
- **标题**: workflow_call 嵌套 3 层时报错应明确提示上限为 2 层
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**workflow_call 嵌套 3 层时报错应明确提示上限为 2 层**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-026
通过标准：
1. 不应静默失败或卡死
2. 报错中是否包含 workflow_call、嵌套、2 层、上限等关键词

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call reusable | `uses: ./.gitcode/workflows/reusable-level1.yml` | 无 | 平台校验/调度行为（嵌套深度检查） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | `uses:` 引用 reusable workflow，嵌套深度检测由平台执行 | ✅ GENUINE | `uses:` 调用真实 reusable workflow，平台嵌套限制是真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 判定报错关键词 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定报错内容 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
