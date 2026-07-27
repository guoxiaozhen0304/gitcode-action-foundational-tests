# COMP-SCRIPT-01-081

- **标题**: 仓库内脚本执行与路径验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**仓库内脚本执行与路径验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-081

通过标准：
1. type=positive, target=run_logs, must_contain="inline_script_ok"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Run inline script | `echo "inline_script_ok"` |  | ❌ VACUOUS |
| 2 | Run repo script | `./scripts/hello.sh || echo "script_fallback"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify in-repo script execution
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Run inline script
        run: |
          echo "inline_script_ok"
      - name: Run repo script
        run: |
          ./scripts/hello.sh || echo "script_fallback"
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
| 1 | run_logs | positive | must_contain=inline_script_ok | ❌ VACUOUS | inline_script_ok: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — VACUOUS**❌: inline_script_ok: VACUOUS (步骤仅 echo，未执行功能)

---