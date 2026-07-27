# REL-RUNNER-01-049
- **标题**: Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-049
通过标准：
1. CPU/内存/磁盘最小比率 ≥0.9
2. queued→running ≤5min（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | probe small | `nproc; free -m; df -BG ${{RUNNER_TEMP}}` | — | 输出 small runner 的 CPU 核数/内存/磁盘 |
| 2 | probe medium | `nproc; free -m; df -BG ${{RUNNER_TEMP}}` | — | 输出 medium runner 资源 |
| 3 | probe large | `nproc; free -m; df -BG ${{RUNNER_TEMP}}` | — | 输出 large runner 资源 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio ≥ 0.9 | positive | — | ✅ GENUINE | `nproc`、`free -m`、`df -BG` 为真实系统命令，输出实际硬件资源信息。但三个 job 全部使用 `runs-on: [ubuntu-latest, x64, small]`，并未区分 small/medium/large 标签——YAML 中 probe-medium 和 probe-large 的 runs-on 标签也是 small |
| 2 | queued_to_running_minutes ≤ 5 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
### 问题
- 三个探针 job（small/medium/large）的 `runs-on` 标签全部为 `[ubuntu-latest, x64, small]`，未使用 medium 或 large 标签。这导致三个 job 实际都在 small runner 上运行，无法验证 medium/large 规格真实性
---
