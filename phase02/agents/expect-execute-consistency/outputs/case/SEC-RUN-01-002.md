# SEC-RUN-01-002
- **标题**: Runner 环境变量与共享目录必须跨 job 隔离
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**job B 的环境变量和 /tmp 在启动时为干净状态，不继承 job A 的设置**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-021
通过标准：
1. 日志不含 "isolation broken"
2. 日志含 "isolated as expected"
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 (job-a-env) | Set env and tmp | `echo MY_SECRET_ENV=leaked >> $ATOMGIT_ENV; echo leaked-data > /tmp/env-test.txt` | — | 写入 env 和文件 |
| 2 (job-b-env) | Check env clean | `if [ -n "$MY_SECRET_ENV" ] \|\| [ -f /tmp/env-test.txt ]; then echo "isolation broken"; exit 1; else echo "isolated as expected"; fi` | — | 隔离检查结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 "isolation broken" | negative | run_logs must_not_contain | ✅ GENUINE | job-b 的 if 条件检查 + exit 1；跨 job 环境/文件隔离由平台 runner 清理决定 |
| 2 | isolated as expected | positive | run_logs equals | ✅ GENUINE | job-b 有 if/exit 1；echo "isolated as expected" 当隔离正常时输出 |
### 问题
(无)
---
