# COMP-EXPR-01-055

- **标题**: hashFiles 函数边界行为
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**hashFiles 函数边界行为**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-055

通过标准：
1. type=positive, target=run_logs, must_contain="HASH_SINGLE="
2. type=positive, target=run_logs, must_contain="HASH_MULTI="
3. type=positive, target=run_logs, must_contain="HASH_NONE="

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Single file hash | `echo "HASH_SINGLE=${{ hashFiles('package.json') }}"` |  | ✅ GENUINE |
| 2 | Multi pattern hash | `echo "HASH_MULTI=${{ hashFiles('src/**', 'package.json') }}"` |  | ✅ GENUINE |
| 3 | No match hash | `echo "HASH_NONE=${{ hashFiles('nonexistent.xyz') }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify hashFiles boundary
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Single file hash
        run: |
          echo "HASH_SINGLE=${{ hashFiles('package.json') }}"
      - name: Multi pattern hash
        run: |
          echo "HASH_MULTI=${{ hashFiles('src/**', 'package.json') }}"
      - name: No match hash
        run: |
          echo "HASH_NONE=${{ hashFiles('nonexistent.xyz') }}"
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
| 1 | run_logs | positive | must_contain=HASH_SINGLE= | ✅ GENUINE | HASH_SINGLE=: GENUINE |
| 2 | run_logs | positive | must_contain=HASH_MULTI= | ✅ GENUINE | HASH_MULTI=: GENUINE |
| 3 | run_logs | positive | must_contain=HASH_NONE= | ✅ GENUINE | HASH_NONE=: GENUINE |

---