# REL-LOG-01-040

- **标题**: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-040

通过标准：
1. type=positive, target=log_size_mb, equals=100
2. type=positive, target=log_download, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | generate 100MB log | `for i in $(seq 1 2500); do python3 -c "print('A'*40960)"; done` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: log size 100MB test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: generate 100MB log
        run: |
          for i in $(seq 1 2500); do python3 -c "print('A'*40960)"; done
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
| 1 | log_size_mb | positive | equals=100 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | log_download | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |

---