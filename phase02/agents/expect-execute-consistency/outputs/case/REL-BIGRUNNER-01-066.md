# REL-BIGRUNNER-01-066
- **标题**: 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**xlarge/2xlarge 反复编译成功率**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-066
通过标准：
1. 成功率≥90%
2. 失败归因明确
3. 无 flaky

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | compile step (xlarge) | `echo compiling; sleep 30` | - | 文本 + 等待 |
| 2 | compile step (2xlarge) | `echo compiling; sleep 30` | - | 文本 + 等待 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | success_rate ge 90 | positive | - | ❌ STATUS_GUARANTEED | 步骤仅 `echo compiling; sleep 30`（纯 trivial），无条件失败路径；runs-on 实际为 `[ubuntu-latest, x64, small]` 而非 xlarge/2xlarge |
| 2 | failure_attribution = clear | positive | - | ❌ MISSING_SOURCE | 无任何失败归因步骤或失败场景——所有步骤必然成功 |
### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅 echo 和 sleep，无条件分支、无真实编译、无可能的失败路径。runs-on 标签为 small 而非宣称的 xlarge/2xlarge。success_rate≥90 永远为真——测试从未验证大规模资源调度。

**断言 2 — MISSING_SOURCE**: 所有步骤必然成功，无任何失败产生机制，因此不存在可观测的 failure_attribution 输出。
---
