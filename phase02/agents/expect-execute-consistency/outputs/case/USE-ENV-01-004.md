# USE-ENV-01-004
- **标题**: job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证）
- **维度**: usability
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-046
通过标准：
1. 表达式层 `${{ env.APP_ENV }}` 取到值 `prod`
2. shell 层 `$APP_ENV` 取到值 `prod`（文档承诺该 job 内所有 step 可见）
3. 若 shell 层为空，记文档承诺未兑现缺陷

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | read env both layers | `echo "shell=[$APP_ENV]"` / `echo "expr=[${{ env.APP_ENV }}]"` | 无 | shell 变量与表达式求值结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "expr=[prod]" | positive | 步骤含 `${{ env.APP_ENV }}` 表达式 | ✅ GENUINE | `${{ }}` 表达式求值，平台真实行为 |
| 2 | run_logs contains "shell=[prod]" | positive | 步骤 echo job env 变量 `$APP_ENV`，env 由平台注入 | ✅ GENUINE | shell 变量取自平台注入的真实 env，非硬编码 |
| 3 | documentation 确定性校验 | negative | 文档与行为矛盾检查 | ✅ COVERED | 确定性文档校验 |
---
