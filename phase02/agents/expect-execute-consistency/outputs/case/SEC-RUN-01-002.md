# SEC-RUN-01-002

- **标题**: Runner 环境变量与共享目录必须跨 job 隔离
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner 环境变量与共享目录必须跨 job 隔离**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-021

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=isolated_as_expected

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Set env | `echo MY_SECRET_ENV=leaked >> $ATOMGIT_ENV echo leaked-data > /tmp/env-test.txt` |  | ✅ GENUINE |
| 2 | Check env clean | `if [ -n "$MY_SECRET_ENV" ] || [ -f /tmp/env-test.txt ]; then   echo "isolation b` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-a-env:
    name: Set env and tmp
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Set env
        run: |
          echo MY_SECRET_ENV=leaked >> $ATOMGIT_ENV
          echo leaked-data > /tmp/env-test.txt
  job-b-env:
    name: Check env isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check env clean
        run: |
          if [ -n "$MY_SECRET_ENV" ] || [ -f /tmp/env-test.txt ]; then
            echo "isolation broken"
            exit 1
          else
            echo "isolated as expected"
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
| 2 | run_logs | positive | equals=isolated_as_expected | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---