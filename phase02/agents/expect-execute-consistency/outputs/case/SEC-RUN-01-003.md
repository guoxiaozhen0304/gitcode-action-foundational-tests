# SEC-RUN-01-003

- **标题**: 自托管 Runner 跨项目残留必须被隔离
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**自托管 Runner 跨项目残留必须被隔离**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-022

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=isolated_as_expected

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write temp | `echo project-a-secret > /tmp/project-a-temp.txt` |  | ❌ VACUOUS |
| 2 | Check no cross project le | `if [ -f /tmp/project-a-temp.txt ]; then   echo "cross project leak"   exit 1 els` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  project-a:
    name: Write project A data
    runs-on: [self-hosted, x64, large]
    steps:
      - name: Write temp
        run: |
          echo project-a-secret > /tmp/project-a-temp.txt
  project-b:
    name: Check project B isolation
    runs-on: [self-hosted, x64, large]
    steps:
      - name: Check no cross project leak
        run: |
          if [ -f /tmp/project-a-temp.txt ]; then
            echo "cross project leak"
            exit 1
          else
            echo "isolated as expected"
          fi
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `self-hosted-shared` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | positive | equals=isolated_as_expected | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---