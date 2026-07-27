# SEC-MASK-01-005

- **标题**: Secret 日志脱敏不可通过多行值输出绕过
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Secret 日志脱敏不可通过多行值输出绕过**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-007

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="MULTI_LINE_SECRET"
2. type=positive, target=run_logs, equals=multiline_masked_with_asterisks

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Echo multiline secret | `echo "${{ secrets.MULTI_LINE_SECRET }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  multiline-mask:
    name: Test multiline masking
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo multiline secret
        run: |
          echo "${{ secrets.MULTI_LINE_SECRET }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['MULTI_LINE_SECRET']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=MULTI_LINE_SECRET | ✅ GENUINE | 步骤使用 MULTI_LINE_SECRET，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_logs | positive | equals=multiline_masked_with_asterisks | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---