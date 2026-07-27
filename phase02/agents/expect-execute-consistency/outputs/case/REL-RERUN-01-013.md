# REL-RERUN-01-013
- **标题**: rerun 6 小时年龄限制——超期运行不可重新运行
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**rerun 6 小时年龄限制——超期运行不可重新运行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-013
通过标准：
1. rerun 请求被拒绝

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 5` | — | 持有 runner 5 秒 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_request = rejected | positive | — | ❌ MISSING_SOURCE | 同 REL-RERUN-01-012，验证 6 小时后 rerun API 拒绝需依赖外部时间窗口与 harness 调用，workflow 内 `sleep 5` 不参与 |
### 问题
- 断言依赖外部时间控制（等待 6 小时 1 分钟），workflow 内部步骤无关
---
