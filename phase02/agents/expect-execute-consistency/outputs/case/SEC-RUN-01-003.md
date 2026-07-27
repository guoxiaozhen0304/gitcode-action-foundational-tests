# SEC-RUN-01-003
- **标题**: 自托管 Runner 跨项目残留必须被隔离
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**项目 B 的 job 不应读取到项目 A 残留的敏感文件**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-022
通过标准：
1. 日志不含 "cross project leak"
2. 日志含 "isolated as expected"
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 (project-a) | Write project A data | `echo project-a-secret > /tmp/project-a-temp.txt` | runs-on: [self-hosted, x64, large] | 写入文件 |
| 2 (project-b) | Check project B isolation | `if [ -f /tmp/project-a-temp.txt ]; then echo "cross project leak"; exit 1; else echo "isolated as expected"; fi` | runs-on: [self-hosted, x64, large] | 隔离检查结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | self-hosted-shared |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 "cross project leak" | negative | run_logs must_not_contain | ✅ GENUINE | project-b 有 if 检查 + exit 1；跨项目文件隔离由自托管 runner 清理决定 |
| 2 | isolated as expected | positive | run_logs equals | ✅ GENUINE | project-b 有 if/exit 1；echo "isolated as expected" 当隔离正常时输出 |
### 问题
(无)
---
