# USE-STAT-01-001
- **标题**: 使用 always() 带括号时若被接受则正常执行
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 always() 带括号时若被接受则正常执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-004
通过标准：
1. step 日志出现执行记录
2. 运行成功完成

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | force fail | `exit 1` | 无 | 制造失败 |
| 2 | cleanup with always | `echo "cleanup executed"` | `if: ${{ always() }}` | 验证 always() 是否使 step 执行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "cleanup executed" | positive | `if: ${{ always() }}` 含 `${{ }}` 表达式 + `exit 1` 制造真实失败 | ✅ GENUINE | 表达式条件求值 + 失败路径涉及平台真实行为 |
---
