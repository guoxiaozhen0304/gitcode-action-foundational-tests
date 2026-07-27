# USE-TYPE-01-001
- **标题**: 使用 GitCode types 命名时正常触发
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 GitCode types 命名时正常触发**
- 触发事件: `pull_request`
- 规格引用: INTENT-USE-009
通过标准：
1. PR 创建或更新时触发运行
2. 运行成功或至少进入执行态

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo event | `echo "event=${{ atomgit.event_name }}"` | 无 | 记录触发事件名 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | positive | `${{ atomgit.event_name }}` 表达式 + pull_request 触发 | ✅ GENUINE | pull_request 触发 + 表达式求值涉及平台真实行为 |
---
