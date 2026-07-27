# USE-ANNOT-01-001

- **标题**: workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-021

通过标准：
1. type=positive, target=run_logs, contains="::error file=src/main.js,line=10::Missing semicolon"
2. type=positive, target=run_logs, contains="::warning file=src/util.js,line=5::Deprecated function"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | emit error and warning | `echo "::error file=src/main.js,line=10::Missing semicolon" echo "::warning file=` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  annot-test:
    name: annotation command test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: emit error and warning
        run: |
          echo "::error file=src/main.js,line=10::Missing semicolon"
          echo "::warning file=src/util.js,line=5::Deprecated function"
          echo "::notice::General notice"
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
| 1 | run_logs | positive | contains=::error file=src/main.js,line= | ❌ VACUOUS | ::error file=src/main.js: VACUOUS (步骤仅 echo，未执行功能); line=10::Missing semicolon:  |
| 2 | run_logs | positive | contains=::warning file=src/util.js,lin | ❌ VACUOUS | ::warning file=src/util.js: VACUOUS (步骤仅 echo，未执行功能); line=5::Deprecated functio |

### 问题

**断言 1 — VACUOUS**❌: ::error file=src/main.js: VACUOUS (步骤仅 echo，未执行功能); line=10::Missing semicolon: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — VACUOUS**❌: ::warning file=src/util.js: VACUOUS (步骤仅 echo，未执行功能); line=5::Deprecated function: VACUOUS (步骤仅 echo，未执行功能)

---