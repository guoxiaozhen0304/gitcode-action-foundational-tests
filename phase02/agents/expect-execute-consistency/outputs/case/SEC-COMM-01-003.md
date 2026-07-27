# SEC-COMM-01-003
- **标题**: 变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**大小写/空白/markdown 变形评论不得绕过 comments 过滤**
- 触发事件: `pull_request_comment` (as untrusted_contributor)
- 规格引用: INTENT-SEC-042
通过标准：
1. 精确指令正常触发
2. 变形伪装不触发
3. 文档说明匹配语义
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark trigger | `echo "TRIGGERED_BY_COMMENT: command accepted"` | — | 触发标记 |

## 3. 触发与运行环境
| 触发事件 | pull_request_comment |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 精确指令触发 | positive | run_trigger equals | ❌ MISSING_SOURCE | target=run_trigger 非标准目标 |
| 2 | 变形不触发 | negative | run_trigger must_not_equal | ❌ MISSING_SOURCE | 同上 |
| 3 | 文档说明匹配语义 | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | llm 辅助判定 |
### 问题
非 LLM 断言均为 run_trigger（外部目标），workflow 步骤无法驱动。
---
