# USE-INPT-01-001
- **标题**: 使用 string 类型 input 时正常通过校验
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 string 类型 input 时正常通过校验**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-008
通过标准：
1. YAML 校验通过，可手动触发
2. 输入参数正常传递

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo input | `echo "env=${{ inputs.env }}"` | 无 | 输出 inputs.env 的值 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | positive | 步骤含 `${{ inputs.env }}` 表达式 + 合法 input 定义 | ✅ GENUINE | `${{ }}` 表达式求值，input 解析由平台处理 |
---
