# USE-PERM-01-001
- **标题**: 使用 GitCode 权限域命名时正常生效
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 GitCode 权限域命名时正常生效**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-005
通过标准：
1. 运行成功完成
2. 权限声明未导致校验失败

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout | `uses: checkout` | 无 | checkout action 执行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | positive | `uses: checkout` 涉及 action 调用，permissions 字段由平台解析 | ✅ GENUINE | `uses:` 调用 + permissions 字段解析涉及平台真实行为 |
---
