# USE-DOC-01-003

- **标题**: trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾
- **维度**: 易用性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾**

- 触发事件: `schedule`
- 规格引用: INTENT-USE-033

通过标准：
1. type=negative, target=documentation, eval=deterministic
2. type=positive, target=validation_result, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | marker step | `echo "scheduled"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  schedule:
    - cron: "* * * * *"
jobs:
  probe:
    name: per-minute cron doc example
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: marker step
        run: |
          echo "scheduled"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `schedule` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |
| 2 | validation_result | positive | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---