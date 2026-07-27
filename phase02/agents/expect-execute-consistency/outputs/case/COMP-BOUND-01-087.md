# COMP-BOUND-01-087

- **标题**: 步骤输出与跨 job 传递边界验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**步骤输出与跨 job 传递边界验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-087

通过标准：
1. type=positive, target=run_logs, must_contain="K1=val1"
2. type=positive, target=run_logs, must_contain="K2=val2"
3. type=positive, target=run_logs, must_contain="output_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write output | `echo "key1=val1" >> "$ATOMGIT_OUTPUT" echo "key2=val2" >> "$ATOMGIT_OUTPUT"` |  | ❌ VACUOUS |
| 2 | Read output | `echo "K1=${{ steps.writer.outputs.key1 }}" echo "K2=${{ steps.writer.outputs.key` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify output boundary
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write output
        id: writer
        run: |
          echo "key1=val1" >> "$ATOMGIT_OUTPUT"
          echo "key2=val2" >> "$ATOMGIT_OUTPUT"
      - name: Read output
        run: |
          echo "K1=${{ steps.writer.outputs.key1 }}"
          echo "K2=${{ steps.writer.outputs.key2 }}"
          echo "output_ok"
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
| 1 | run_logs | positive | must_contain=K1=val1 | ❌ MISSING_SOURCE | K1=val1: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=K2=val2 | ❌ MISSING_SOURCE | K2=val2: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=output_ok | ✅ GENUINE | output_ok: GENUINE |

### 问题

**断言 1 — MISSING_SOURCE**❌: K1=val1: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: K2=val2: MISSING_SOURCE (无步骤产出此字符串)

---