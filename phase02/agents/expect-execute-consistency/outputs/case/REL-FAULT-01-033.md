# REL-FAULT-01-033
- **标题**: 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**磁盘接近满时写入应失败并报磁盘满**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-033
通过标准：
1. job 状态=failure
2. 日志含 "No space left on device"

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | prefill disk | `fallocate -l 49.5G prefill.bin \|\| dd if=/dev/zero of=prefill.bin bs=1M count=50688` | - | 填充约 49.5GB |
| 2 | write additional 2GB | `dd if=/dev/zero of=extra.bin bs=1M count=2048` | - | 额外 2GB 写入触发磁盘满 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | disk_full at pre_job |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | - | ✅ GENUINE | 真实磁盘写满操作导致失败 |
| 2 | run_logs contains "No space left on device" | positive | - | ✅ GENUINE | dd 命令磁盘满时的标准错误输出 |
---
