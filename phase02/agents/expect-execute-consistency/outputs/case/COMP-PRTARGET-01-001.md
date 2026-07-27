# COMP-PRTARGET-01-001

- **标题**: pull_request_target 默认使用 base 分支 workflow 版本
- **维度**: 完备性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**pull_request_target 默认使用 base 分支 workflow 版本**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-014

通过标准：
1. type=positive, target=run_logs, contains="BASE_VERSION_MARKER"
2. type=negative, target=run_logs

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo base version marker | `echo "BASE_VERSION_MARKER"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches:
      - main
jobs:
  verify:
    name: Verify base workflow version
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo base version marker
        run: |
          echo "BASE_VERSION_MARKER"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_target` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains=BASE_VERSION_MARKER | ❌ VACUOUS | BASE_VERSION_MARKER: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

### 问题

**断言 1 — VACUOUS**❌: BASE_VERSION_MARKER: VACUOUS (步骤仅 echo，未执行功能)

---