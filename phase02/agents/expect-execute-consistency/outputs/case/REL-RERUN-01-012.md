# REL-RERUN-01-012
- **标题**: rerun 越界值——尝试第 4 次重新运行应被系统拒绝
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**rerun 越界值——尝试第 4 次重新运行应被系统拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-012
通过标准：
1. 第 4 次 rerun 请求被拒绝

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
| 1 | rerun_request = rejected | positive | — | ❌ MISSING_SOURCE | 同 PREEMPT-01-006，断言 `rerun_request = rejected` 期望平台 API 层面拒绝第 4 次 rerun。此行为发生在 workflow 运行之前（UI/API 层面），不可由 workflow 内部步骤验证。需 harness 调用 rerun API 并捕获拒绝响应 |
### 问题
- 断言完全依赖外部 harness 行为，workflow 内的 `sleep 5` 不参与验证
---
