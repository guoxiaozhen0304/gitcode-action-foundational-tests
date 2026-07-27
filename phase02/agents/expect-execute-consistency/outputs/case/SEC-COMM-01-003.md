# SEC-COMM-01-003

- **标题**: 变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**变形伪装评论（大小写/多余空白/markdown 包裹）不得绕过 comments 过滤语义**

- 触发事件: `pull_request_comment`
- 规格引用: INTENT-SEC-042

通过标准：
1. type=positive, target=run_trigger, equals=exact_command_triggers
2. type=negative, target=run_trigger
3. type=nonfunctional, target=documentation, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Mark trigger | `echo "TRIGGERED_BY_COMMENT: command accepted"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_comment:
    types: [created]
    comments: ['^/deploy fixture-environment$']
jobs:
  comment-gate:
    name: Comment regex obfuscation check
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Mark trigger
        run: |
          echo "TRIGGERED_BY_COMMENT: command accepted"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_comment` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_trigger | positive | equals=exact_command_triggers | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_trigger | negative |  | ✅ GENUINE | 通用断言匹配 |
| 3 | documentation | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---