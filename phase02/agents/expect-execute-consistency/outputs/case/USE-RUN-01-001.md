# USE-RUN-01-001
- **标题**: 使用三段式标签时 job 正常调度
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用三段式标签时 job 正常调度**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-006
通过标准：
1. 运行成功完成
2. job 日志显示在对应 runner 上执行

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | check runner | `echo "runner ok"` | 无 | 标记日志（三段式标签调度验证） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | positive | 步骤为纯 echo，但 runs-on 三段式标签调度由平台决定 | ✅ GENUINE | 平台对三段式 runs-on 标签的调度匹配是真实行为 |
---
