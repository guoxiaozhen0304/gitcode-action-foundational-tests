# REL-NEST-01-024
- **标题**: workflow_call 嵌套越界——3 层嵌套调用应被拒绝
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_call 嵌套越界——3 层嵌套调用应被拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-024
通过标准：
1. 运行状态 = completed(failure)
2. 日志含嵌套超限提示

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call level 1 workflow | `uses: ./.gitcode/workflows/level1_deep.yml` | — | 尝试 3 层嵌套调用 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = completed(failure) | positive | — | ✅ GENUINE | `uses:` 指令真实触发 3 层 workflow_call 嵌套（A→B→C→D），由平台执行嵌套深度校验并拒绝 |
| 2 | run_logs contains "嵌套" | positive | — | ✅ GENUINE | 平台解析嵌套超限时生成的错误信息，非脚本 echo，由 uses: 真实触发 |
---
