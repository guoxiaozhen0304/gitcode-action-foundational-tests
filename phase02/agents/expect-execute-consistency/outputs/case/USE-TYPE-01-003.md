# USE-TYPE-01-003
- **标题**: pull_request_comment 与 pr_comment 事件名双轨的文档说明
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request_comment 与 pr_comment 事件名双轨的文档说明**
- 触发事件: `pull_request_comment`
- 规格引用: INTENT-USE-036
通过标准：
1. 记录平台对别名事件名的识别情况
2. 文档只提一个事件名而样本用另一个且无任何说明即不合格

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | marker step | `echo "triggered via alias event name"` | 无 | 验证别名事件名是否触发 |

## 3. 触发与运行环境
| 触发事件 | pull_request_comment |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result 确定性记录平台对 pr_comment 别名的接受情况 | positive | workflow 使用 `on: pr_comment`，触发事件为 `pull_request_comment` | ✅ GENUINE | 事件别名接受性是平台真实行为 |
| 2 | documentation 确定性校验：trigger-events.md 应提及 pr_comment 别名 | negative | 确定性文档检查 | ✅ COVERED | 确定性文档校验 |
---
