# USE-TYPE-01-003

- **标题**: pull_request_comment 与 pr_comment 事件名双轨的文档说明
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_comment 与 pr_comment 事件名双轨的文档说明**

- 触发事件: `pull_request_comment`
- 规格引用: INTENT-USE-036

通过标准：
1. type=positive, target=validation_result, eval=deterministic
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | marker step | `echo "triggered via alias event name"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pr_comment:
    types: [created]
jobs:
  probe:
    name: alias pr comment trigger
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: marker step
        run: |
          echo "triggered via alias event name"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_comment` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | eval=deterministic | ✅ GENUINE | 通用断言匹配 |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---