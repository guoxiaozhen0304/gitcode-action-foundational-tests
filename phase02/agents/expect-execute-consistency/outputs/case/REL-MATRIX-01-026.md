# REL-MATRIX-01-026
- **标题**: matrix fail-fast=true——任意 job 实例失败应立即取消其余实例
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**matrix fail-fast=true——任意 job 实例失败应立即取消其余实例**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-026
通过标准：
1. 失败 job 状态 = failure
2. 其余未完成 jobs 状态 = cancelled

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
| 1 | job_status = failure | positive | — | ❌ IMPOSSIBLE | 工作流仅包含 `echo version=${{ matrix.version }}`，无 `exit 1` 或任何失败路径。文本描述要求"1 个实例故意失败"但 YAML 未实现 |
| 2 | cancelled_jobs_count = 8 | positive | — | ❌ IMPOSSIBLE | 矩阵仅 `version: [1,2,3]`（3 个组合），无失败源头可触发取消，且断言值 8 与 3 实例不匹配 |
### 问题
文本规格要求"含 3x3 matrix 且 fail-fast=true，其中 1 个实例故意失败"并断言 cancelled=8，但 YAML 中矩阵仅一维 `version: [1,2,3]`（3 实例），且所有实例均 echo 不会失败。YAML 既缺少失败注入步骤（exit 1），也缺少第二维矩阵变量使组合达到 9 个。
---
