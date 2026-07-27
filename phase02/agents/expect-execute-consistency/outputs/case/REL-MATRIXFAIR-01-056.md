# REL-MATRIXFAIR-01-056
- **标题**: 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**矩阵调度公平性——20 实例 matrix 配 max-parallel=4 的无饿死验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-056
通过标准：
1. 20 实例全部完成
2. 最大/最小 queued 延迟比 ≤3（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | matrix step | `echo version=${{ matrix.version }}` | — | 输出矩阵变量值 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_jobs_count = 20 | positive | — | ✅ GENUINE | version[20] + max-parallel=4，step 使用 `${{ matrix.version }}`，真实触发平台 20 实例矩阵调度公平性 |
| 2 | queued_delay_ratio ≤ 3 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
