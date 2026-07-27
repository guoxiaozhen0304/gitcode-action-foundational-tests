# REL-RUNNER-01-049-V2
- **标题**: Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存/磁盘 vs 声明值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-049
通过标准：
1. CPU/内存/磁盘最小比率 ≥0.9
2. 失败时归因清晰

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | probe xlarge | `nproc; free -m; df -BG ${{RUNNER_TEMP}}` | — | 输出 xlarge runner 资源 |
| 2 | probe 2xlarge | `nproc; free -m; df -BG ${{RUNNER_TEMP}}` | — | 输出 2xlarge runner 资源 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio ≥ 0.9 | positive | — | ✅ GENUINE | `nproc`、`free -m`、`df -BG` 为真实系统命令。但两个探针 job 的 `runs-on` 标签全部为 `[ubuntu-latest, x64, small]`，未使用 xlarge 或 2xlarge 标签 |
| 2 | failure_attribution = clear | positive | — | ❌ VACUOUS | job 本身无失败路径，`failure_attribution` 无对应步骤产出 |
### 问题
- 同 REL-RUNNER-01-049，xlarge 和 2xlarge 探针 job 的 runs-on 标签实际为 `[ubuntu-latest, x64, small]`，无法测试对应规格
- failure_attribution 无对应步骤
---
