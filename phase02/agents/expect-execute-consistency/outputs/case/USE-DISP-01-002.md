# USE-DISP-01-002
- **标题**: workflow_dispatch 未提供参数但存在 default 时应使用默认值运行
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_dispatch 未提供参数但存在 default 时应使用默认值运行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-030
通过标准：
1. 运行成功完成
2. 日志中输出 default 值

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo env | `echo "env=${{ inputs.environment }}"` | - | 平台将 inputs.environment 求值为 default 值 "staging" |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: "env=staging" | ✅ GENUINE | 步骤使用 `${{ inputs.environment }}` 表达式，值由平台按 default 求值，非字面量 echo |
---
