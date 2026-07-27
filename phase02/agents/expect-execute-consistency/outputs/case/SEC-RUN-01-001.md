# SEC-RUN-01-001

- **标题**: Job 结束后 workspace 与临时文件必须被彻底清理
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Job 结束后 workspace 与临时文件必须被彻底清理**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-020

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=cleaned_as_expected

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write temp secret | `echo sensitive-data > /tmp/sensitive-temp.txt` |  | ❌ VACUOUS |
| 2 | Check no residual | `if [ -f /tmp/sensitive-temp.txt ]; then   echo "residual found"   exit 1 else   ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-a:
    name: Write sensitive file
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write temp secret
        run: |
          echo sensitive-data > /tmp/sensitive-temp.txt
  job-b:
    name: Check cleanup
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check no residual
        run: |
          if [ -f /tmp/sensitive-temp.txt ]; then
            echo "residual found"
            exit 1
          else
            echo "cleaned as expected"
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | positive | equals=cleaned_as_expected | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---