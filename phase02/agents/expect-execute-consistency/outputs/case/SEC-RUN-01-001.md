# SEC-RUN-01-001
- **标题**: Job 结束后 workspace 与临时文件必须被彻底清理
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**job B 不应读取到 job A 残留的敏感文件**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-020
通过标准：
1. 日志不含 "residual found"
2. 日志含 "cleaned as expected"
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 (job-a) | Write temp secret | `echo sensitive-data > /tmp/sensitive-temp.txt` | — | 写入临时文件 |
| 2 (job-b) | Check no residual | `if [ -f /tmp/sensitive-temp.txt ]; then echo "residual found"; exit 1; else echo "cleaned as expected"; fi` | — | 检查结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 "residual found" | negative | run_logs must_not_contain | ✅ GENUINE | job-b 的 if 检查 + exit 1 → 真实行为；跨 job 文件隔离由平台 runner 清理决定 |
| 2 | cleaned as expected | positive | run_logs equals | ✅ GENUINE | job-b 有 if/exit 1；echo 输出 "cleaned as expected" 当清理正常时 |
### 问题
(无)
---
