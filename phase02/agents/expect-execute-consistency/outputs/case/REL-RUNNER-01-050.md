# REL-RUNNER-01-050
- **标题**: 架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-074
通过标准：
1. x64 探针输出 = x86_64
2. arm64 探针输出 = aarch64
3. 架构错配次数 = 0

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | print arch step (x64) | `echo "declared=x64 actual=$(uname -m)"` | — | 输出实际架构 |
| 2 | print arch step (arm64) | `echo "declared=arm64 actual=$(uname -m)"` | — | 输出实际架构 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | x64_job_arch = x86_64 | positive | — | ✅ GENUINE | `$(uname -m)` 真实命令输出系统架构，`runs-on: [ubuntu-latest, x64, small]` 和 `[..., arm64, small]` 真实测试架构标签调度 |
| 2 | arm64_job_arch = aarch64 | positive | — | ✅ GENUINE | 同上 |
| 3 | arch_mismatch_count = 0 | positive | — | ✅ GENUINE | 由 harness 10 次采样统计错配，uname -m 产生真实数据 |
| 4 | x64_job_arch = aarch64 | negative | — | ✅ GENUINE | negative 断言确认 x64 job 不应输出 aarch64 |
| 5 | no_matching_runner_behavior = queued_or_explicit_error | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
