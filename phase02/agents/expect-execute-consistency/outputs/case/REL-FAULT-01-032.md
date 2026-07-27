# REL-FAULT-01-032
- **标题**: 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**upload-artifact 时网络分区应导致失败并报网络错误**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-032
通过标准：
1. upload-artifact step 状态=failure
2. 日志含 network 错误
3. 不应无限挂起

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate artifact file | `dd if=/dev/urandom of=artifact.bin bs=1M count=10` | - | 10MB 测试文件 |
| 2 | upload artifact step | `uses: upload-artifact` name=net-fault-artifact | - | action 输出（含网络错误） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | network_partition 30s at step 2 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status = failure | positive | - | ✅ GENUINE | upload-artifact 是 uses action + 网络分区故障注入 |
| 2 | run_logs contains "network" | positive | - | ✅ GENUINE | network_partition 导致 action 内部输出网络/连接错误 |
---
