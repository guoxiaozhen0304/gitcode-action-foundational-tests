# REL-MATRIX-01-027
- **标题**: matrix max-parallel=4——9 个组合应最多同时运行 4 个
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**matrix max-parallel=4——9 个组合应最多同时运行 4 个**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-027
通过标准：
1. 峰值并发 ≤ 4
2. 9 个 jobs 全部 completed(success)

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
| 1 | max_concurrent_jobs ≤ 4 | positive | — | ✅ GENUINE | 3×3=9 实例 matrix + max-parallel=4 真实触发平台调度，由 harness 观测并发数。step 使用 `${{ matrix.version }}` 非纯静态 |
| 2 | run_status = completed(success) | positive | — | ✅ GENUINE | 9 实例 matrix 全部执行 echo（含 `${{ }}`），非纯静态，由平台真实调度完成 |
---
