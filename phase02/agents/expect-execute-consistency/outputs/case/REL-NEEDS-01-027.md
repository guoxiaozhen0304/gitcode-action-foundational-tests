# REL-NEEDS-01-027
- **标题**: needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行
- **维度**: 稳定性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**needs 依赖 matrix job 部分失败——无 if 条件的下游 job 应 skipped 而非执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-069
通过标准：
1. jobB 聚合状态 = failure，失败实例数=1、成功实例数=2
2. jobA 状态 = skipped
3. jobA 不应为 success

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | maybe fail step (job_b) | `if [ "${{ matrix.version }}" = "2" ]; then exit 1; fi; echo "matrix_instance_ok=${{ matrix.version }}"` | — | version=2 时 exit 1 失败，其余成功 |
| 2 | should be skipped step (job_a) | `echo "this should not run"` | needs: job_b | 此步骤不应执行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_b_status = failure | positive | — | ✅ GENUINE | `if [ "${{ matrix.version }}" = "2" ]; then exit 1; fi` 真实使 1 个 matrix 实例失败（fail-fast=false 下其余 2 个继续），有真实失败路径 |
| 2 | job_a_status = skipped | positive | — | ✅ GENUINE | job_a 无 `if` 条件，通过 `needs: job_b` 依赖部分失败的 matrix，由平台聚合判定 |
| 3 | succeeded_instances_count = 2 | positive | — | ✅ GENUINE | fail-fast=false 下 version 1 和 3 应成功，由 harness 计数 |
| 4 | job_a_status = success | negative | — | ✅ GENUINE | 验证 job_a 不应成功执行 |
---
