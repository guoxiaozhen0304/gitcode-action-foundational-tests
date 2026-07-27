# COMP-VARREF-01-083

- **标题**: YAML 表达式与 Shell 环境变量引用方式验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**YAML 表达式与 Shell 环境变量引用方式验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-083

通过标准：
1. type=positive, target=run_logs, must_contain="EXPR=hello"
2. type=positive, target=run_logs, must_contain="ENV=hello"
3. type=positive, target=run_logs, must_contain="ref_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Compare references | `echo "EXPR=${{ env.TEST_VAR }}" echo "ENV=$TEST_VAR" echo "SHA_EXPR=${{ atomgit.` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
env:
  TEST_VAR: hello
jobs:
  verify:
    name: Verify variable reference styles
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare references
        run: |
          echo "EXPR=${{ env.TEST_VAR }}"
          echo "ENV=$TEST_VAR"
          echo "SHA_EXPR=${{ atomgit.sha }}"
          echo "SHA_ENV=$ATOMGIT_SHA"
          echo "ref_ok"
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
| 1 | run_logs | positive | must_contain=EXPR=hello | ❌ MISSING_SOURCE | EXPR=hello: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | positive | must_contain=ENV=hello | ❌ MISSING_SOURCE | ENV=hello: MISSING_SOURCE (无步骤产出此字符串) |
| 3 | run_logs | positive | must_contain=ref_ok | ✅ GENUINE | ref_ok: GENUINE |

### 问题

**断言 1 — MISSING_SOURCE**❌: EXPR=hello: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — MISSING_SOURCE**❌: ENV=hello: MISSING_SOURCE (无步骤产出此字符串)

---