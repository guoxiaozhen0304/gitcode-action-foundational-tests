# REL-MEM-01-021
- **标题**: Runner 内存越界——small runner 分配 9 GB 应被 OOM kill
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Runner 内存越界——small runner 分配 9 GB 应被 OOM kill**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-021
通过标准：
1. job 状态 = failure
2. 日志含 OOM 或 Killed

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | allocate 9GB | `python3 -c "a=bytearray(9216*1024*1024); print(len(a))"` | — | 尝试分配 9GB 内存，预期触发 OOM |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status = failure | positive | — | ✅ GENUINE | `python3 -c` 真实分配 9216*1024*1024 字节，超出 small runner 内存限制，由平台 OOM Killer 终止进程，有真实失败路径 |
| 2 | run_logs contains "Killed" | positive | — | ✅ GENUINE | OOM Killer 输出的 "Killed" 字符串来自系统真实行为，非脚本 echo |
---
