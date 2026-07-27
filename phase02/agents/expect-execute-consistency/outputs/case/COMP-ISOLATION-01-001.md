# COMP-ISOLATION-01-001

- **标题**: 同一 workflow 先后 job 的文件系统相互隔离
- **维度**: completeness
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**同一 workflow 先后 job 的文件系统相互隔离**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-011

通过标准：
1. [负向] job 2 不应访问到 job 1 的文件 —— 断言 must_not_contain "secret data"
2. [正向] 运行状态成功 —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 (job1) | Create file | `echo "secret data" > /tmp/isolation_test.txt` | - | 创建文件 |
| 2 (job2) | Attempt read | `if [ -f /tmp/isolation_test.txt ]; then echo "file exists"; cat /tmp/isolation_test.txt; exit 1; else echo "file not found as expected"; fi` | - (needs: job1) | 检测跨 job 文件隔离 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | job2 使用真实 bash `if/elif/fi` 逻辑 + `exit 1`，跨 job 文件隔离失败时 workflow 会失败 |
| 2 | run_logs | negative | must_not_contain: secret data | ✅ GENUINE | 负向断言：若跨 job 隔离失败则 cat 会输出 "secret data" 且 exit 1；隔离成功则无此输出 |

