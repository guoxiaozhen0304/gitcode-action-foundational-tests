# USE-NEST-01-002
- **标题**: workflow_call 嵌套 2 层时应正常执行
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_call 嵌套 2 层时应正常执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-026
通过标准：
1. 运行成功完成
2. 不应报嵌套超限错误

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call reusable | `uses: ./.gitcode/workflows/reusable-level1.yml` | 无 | 正常嵌套调用 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | positive | `uses:` 引用 reusable workflow，嵌套执行是平台真实行为 | ✅ GENUINE | `uses:` 调用涉及平台 reusable workflow 执行机制 |
---
