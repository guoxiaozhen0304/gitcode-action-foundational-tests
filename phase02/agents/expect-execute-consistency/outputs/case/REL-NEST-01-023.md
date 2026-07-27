# REL-NEST-01-023
- **标题**: workflow_call 嵌套边界——2 层嵌套调用应成功执行
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_call 嵌套边界——2 层嵌套调用应成功执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-023
通过标准：
1. 运行状态 = completed(success)

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call level 1 workflow | `uses: ./.gitcode/workflows/level1.yml` | — | 触发嵌套 workflow 调用 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = completed(success) | positive | — | ✅ GENUINE | `uses: ./.gitcode/workflows/level1.yml` 使用 `uses:` 指令真实触发 workflow_call 嵌套调用（level1→level2），由平台执行嵌套解析与调度 |
---
