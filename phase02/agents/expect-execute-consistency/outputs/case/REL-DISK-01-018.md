# REL-DISK-01-018
- **标题**: Runner 磁盘边界——small runner 写入 49 GB 应成功
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**small runner 写入 49GB 文件应成功**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-018
通过标准：
1. job 状态=success
2. 应在 49GB 时不报磁盘满

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | write 49GB file | `fallocate -l 49G testfile \|\| dd if=/dev/zero of=testfile bs=1M count=50176` | - | 49GB 文件创建或 dd 写入结果 |
| 2 | verify disk space | `df -h . && test -f testfile` | - | 磁盘使用情况和文件存在性 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = success | positive | - | ✅ GENUINE | fallocate / dd 是真实的磁盘写入操作 |
---
