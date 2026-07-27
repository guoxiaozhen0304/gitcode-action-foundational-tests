# COMPAT-ISOLATE-01-001
- **标题**: Runner 环境隔离——跨 job 文件隔离
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**Runner 环境隔离——跨 job 文件隔离**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-028
通过标准：
1. job B 无法读取到 job A 的文件残留
2. 每个 job 获得独立的文件系统视图
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | job-write: write workspace marker | `echo "ISOLATION_MARKER_..."` | — | workspace_marker.txt |
| 2 | job-write: write tmp marker | `echo "ISOLATION_MARKER_TMP_..."` | — | /tmp/isolation_marker.txt |
| 3 | job-write: output marker names | echo to $ATOMGIT_OUTPUT | — | output 变量 |
| 4 | job-verify: verify workspace isolation | ls workspace_marker.txt → ISOLATION_BROKEN/WORKSPACE_ISOLATED_OK | — | 隔离结果 |
| 5 | job-verify: verify tmp isolation | ls /tmp/isolation_marker.txt → ISOLATION_BROKEN/TMP_ISOLATED_OK | — | 隔离结果 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | WORKSPACE_ISOLATED_OK 由 LLM 判定 |
| 2 | run_logs eval=llm_assisted | positive | — | 🔶 LLM_DEPENDENT | TMP_ISOLATED_OK 由 LLM 判定 |
| 3 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | ISOLATION_BROKEN_WORKSPACE 由 LLM 判定 |
| 4 | run_logs eval=llm_assisted | negative | — | 🔶 LLM_DEPENDENT | ISOLATION_BROKEN_TMP 由 LLM 判定 |
### 问题
虽然 workflow 步骤本身使用 real commands（ls, exit 1, bash 条件判断），具有真实行为，但全部 4 个断言均为 LLM_DEPENDENT，没有确定性 rule-based 断言
---
