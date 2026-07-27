# REL-FLOOD-01-037
- **标题**: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**50 个并发 push 应全部创建且系统稳定**
- 触发事件: `push`
- 规格引用: INTENT-REL-037
通过标准：
1. 50 个运行均被创建
2. API/UI 无 5xx
3. 不应出现运行丢失

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 5` | - | 保持 job 运行 |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count = 50 | positive | - | ✅ GENUINE | sleep 是真实命令；harness 并发 push 50 次 |
| 2 | api_status = 200 | positive | - | ✅ GENUINE | harness 侧观察 API 响应 |
| 3 | api_status = 500 | negative | - | ✅ GENUINE | 负向验证无 5xx 错误 |
---
