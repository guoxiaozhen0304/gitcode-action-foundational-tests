# REL-PREEMPT-01-005
- **标题**: preemption events 边界值——配置 10 个应正常解析
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**preemption events 边界值——配置 10 个应正常解析**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-005
通过标准：
1. workflow 保存成功并运行 completed(success)

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo step | `echo test` | — | 固定字符串输出 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = completed(success) | positive | — | ⚠️ STATUS_GUARANTEED | step 仅为 `echo test`。但真正被测的是 YAML 解析层：`concurrency.preemption.events: [push, pull_request, ..., manual]`（10 个事件）是否被成功解析。解析成功 + 纯 echo step → STATUS_GUARANTEED |
### 问题
- 断言通过纯 echo 成功 + YAML 解析通过来验证，本身逻辑上自洽（解析通过 → 能触发 → echo 成功 = 验证通过），但 step 内容不直接验证 preemption 语义
---
