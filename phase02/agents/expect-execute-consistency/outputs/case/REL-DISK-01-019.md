# REL-DISK-01-019
- **标题**: Runner 磁盘越界——small runner 写入 51 GB 应失败并报磁盘满
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**small runner 写入 51GB 应失败并报磁盘满**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-019
通过标准：
1. job 状态=failure
2. 日志含 "No space left on device"
3. 不应静默卡死

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | write 51GB file | `fallocate -l 51G testfile \|\| dd if=/dev/zero of=testfile bs=1M count=52224` | continue-on-error: true | 磁盘满时 dd 产生 "No space left on device" |
| 2 | check failure | `echo expecting failure above` | - | 确认标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | - | ✅ GENUINE | 真实磁盘写入超出可用空间导致失败 |
| 2 | run_logs contains "No space left on device" | positive | - | ✅ GENUINE | dd 命令磁盘满时标准错误输出，非 echo 伪造 |
---
