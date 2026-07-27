# COMP-ISOLATION-01-001

- **标题**: 同一 workflow 先后 job 的文件系统相互隔离
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**同一 workflow 先后 job 的文件系统相互隔离**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-011

通过标准：
1. type=positive, target=run_status, equals=success
2. type=negative, target=run_logs

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create file | `echo "secret data" > /tmp/isolation_test.txt` |  | ❌ VACUOUS |
| 2 | Attempt read | `if [ -f /tmp/isolation_test.txt ]; then   echo "file exists"   cat /tmp/isolatio` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job1:
    name: Write file
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create file
        run: |
          echo "secret data" > /tmp/isolation_test.txt
  job2:
    name: Read file
    runs-on: [ubuntu-latest, x64, small]
    needs: job1
    steps:
      - name: Attempt read
        run: |
          if [ -f /tmp/isolation_test.txt ]; then
            echo "file exists"
            cat /tmp/isolation_test.txt
            exit 1
          else
            echo "file not found as expected"
          fi
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---