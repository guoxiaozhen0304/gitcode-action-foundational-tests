# USE-ACT-01-001
- **标题**: 使用裸插件名 checkout 时正常拉取官方 Action
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用裸插件名 checkout 时正常拉取官方 Action**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-007
通过标准：
1. checkout step 成功执行
2. 运行成功完成

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | - | action checkout 执行输出 |
| 2 | verify checkout | `ls -la` | - | 列出仓库文件 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: COMPLETED | ✅ GENUINE | 步骤使用 `uses: checkout` action + `ls -la` 真实命令，裸插件名引用可能成功或失败 |
---
