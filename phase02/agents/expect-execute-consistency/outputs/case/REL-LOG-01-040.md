# REL-LOG-01-040
- **标题**: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**单 job 输出 100MB 日志应完整保留**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-040
通过标准：
1. 日志总大小≈100MB
2. 日志可下载

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate 100MB log | `for i in $(seq 1 2500); do python3 -c "print('A'*40960)"; done` | - | 约 100MB 的 A 重复日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_size_mb = 100 | positive | - | ✅ GENUINE | python3 真实生成 100MB stdout 输出 |
| 2 | log_download = success | positive | - | ✅ GENUINE | harness 下载日志验证完整性 |
---
