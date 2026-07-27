# COMPAT-LIMIT-01-001

- **标题**: 单次推送多个 tag 的事件生成上限行为（GitHub 超过 3 个不生成事件）
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**单次推送多个 tag 的事件生成上限行为（GitHub 超过 3 个不生成事件）**

- 触发事件: `tag`
- 规格引用: INTENT-COMPAT-052

通过标准：
1. type=positive, target=run_list, eval=llm_assisted
2. type=negative, target=run_list, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Mark tag triggered run | `echo "TAG_RUN_REF=${{ atomgit.ref }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    tags:
      - "v*"
jobs:
  probe:
    name: Probe batch tag push limit
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Mark tag triggered run
        run: |
          echo "TAG_RUN_REF=${{ atomgit.ref }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `tag` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_list | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---