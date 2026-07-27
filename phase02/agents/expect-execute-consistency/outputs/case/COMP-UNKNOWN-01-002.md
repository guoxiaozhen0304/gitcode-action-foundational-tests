# COMP-UNKNOWN-01-002

- **标题**: 不应静默忽略未知字段导致用户误以为配置生效
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**不应静默忽略未知字段导致用户误以为配置生效**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-002

通过标准：
1. type=negative, target=run_status, equals=success_with_unknown_field_silently_ignored

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo step | `echo "should not run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test silent ignore
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo step
        run: |
          echo "should not run"
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
| 1 | run_status | negative | equals=success_with_unknown_field_silently_ignored | ✅ GENUINE | 状态断言 success_with_unknown_field_silently_ignored 可被步骤行为验证 |

---