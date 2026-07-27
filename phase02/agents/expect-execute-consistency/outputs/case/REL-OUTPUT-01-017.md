# REL-OUTPUT-01-017

- **标题**: step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**step output 越界值——ATOMGIT_OUTPUT 写入 1 MB+1 byte 应被拒绝或报错**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-017

通过标准：
1. type=positive, target=run_logs, contains="1MB"
2. type=positive, target=job_status, equals=failure

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | write 1MB+1 output | `python3 -c "print('A'*1048577)" > out.txt echo "data=$(cat out.txt)" >> $ATOMGIT` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: output over limit test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: write 1MB+1 output
        run: |
          python3 -c "print('A'*1048577)" > out.txt
          echo "data=$(cat out.txt)" >> $ATOMGIT_OUTPUT
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
| 1 | run_logs | positive | contains=1MB | ❌ MISSING_SOURCE | 1MB: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | job_status | positive | equals=failure | ✅ GENUINE | 平台级断言 job_status — 由 harness 在运行时观测 |

### 问题

**断言 1 — MISSING_SOURCE**❌: 1MB: MISSING_SOURCE (无步骤产出此字符串)

---