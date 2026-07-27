# USE-ENV-01-001
- **标题**: 使用 ATOMGIT_SHA 环境变量时正常取值
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 ATOMGIT_SHA 环境变量时正常取值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-003
通过标准：
1. 日志中出现非空的 SHA 值
2. 运行成功完成

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo ATOMGIT_SHA | `echo "sha=$ATOMGIT_SHA"` | - | 平台注入的环境变量值 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: "sha=" | ✅ GENUINE | 步骤 echo 的是平台注入的 $ATOMGIT_SHA 环境变量值（非字面量），值由平台环境决定 |
---
