# COMPAT-YAML-01-001

- **标题**: YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为**

- 触发事件: `push`
- 规格引用: INTENT-COMPAT-049

通过标准：
1. type=positive, target=run_logs, must_contain="ON_KEY_OK"
2. type=negative, target=run_list, eval=llm_assisted
3. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo env literal value | `echo "DEBUG_FLAG=[$DEBUG_FLAG]" echo "ON_KEY_OK"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
env:
  DEBUG_FLAG: on
jobs:
  probe:
    name: Probe on key boolean trap
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo env literal value
        run: |
          echo "DEBUG_FLAG=[$DEBUG_FLAG]"
          echo "ON_KEY_OK"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=ON_KEY_OK | ❌ VACUOUS | ON_KEY_OK: VACUOUS (步骤仅 echo，未执行功能) |
| 2 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — VACUOUS**❌: ON_KEY_OK: VACUOUS (步骤仅 echo，未执行功能)

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---