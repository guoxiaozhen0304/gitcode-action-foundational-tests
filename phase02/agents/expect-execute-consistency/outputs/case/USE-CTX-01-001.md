# USE-CTX-01-001
- **标题**: 使用 atomgit 上下文时表达式正常求值
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 atomgit 上下文时表达式正常求值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-002
通过标准：
1. 日志中输出当前分支引用值
2. 运行成功完成

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo atomgit ref | `echo "ref=${{ atomgit.ref }}"` | - | 平台动态求值 atomgit.ref，输出 ref=refs/heads/xxx |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: "ref=refs/heads/" | ✅ GENUINE | 步骤使用 `${{ atomgit.ref }}` 表达式，值由平台上下文动态求值产生 |
---
