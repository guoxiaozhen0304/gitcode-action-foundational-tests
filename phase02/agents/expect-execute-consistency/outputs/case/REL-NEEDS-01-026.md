# REL-NEEDS-01-026
- **标题**: needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行
- **维度**: 稳定性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**needs 依赖 matrix job 成功路径——matrix 全部成功后下游 job 应正常初始化执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-069
通过标准：
1. jobB 全部 matrix 实例状态 = success
2. jobA 状态 = success，日志中含 needs.jobB.result=success
3. jobA 不应为 skipped

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | matrix work step (job_b) | `echo "matrix_instance=${{ matrix.version }}"` | — | 输出实例标记 |
| 2 | read needs result step (job_a) | `echo "needs_result=${{ needs.job_b.result }}"` | needs: job_b | 输出 needs 聚合结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_b_status = success | positive | — | ✅ GENUINE | job_b 为 3 实例 matrix（fail-fast=false），所有实例 echo 含 `${{ }}` 表达式，真实矩阵调度 |
| 2 | job_a_status = success | positive | — | ✅ GENUINE | job_a 通过 `needs: job_b` 和 `echo "needs_result=${{ needs.job_b.result }}"` 真实测试 needs 对 matrix job 的聚合判定 |
| 3 | job_a_status = skipped | negative | — | ✅ GENUINE | 作为 negative 断言，验证 job_a 不应被跳过——由 needs job_b 真实聚合结果驱动 |
| 4 | downstream_start_delay_seconds ≤ 120 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
