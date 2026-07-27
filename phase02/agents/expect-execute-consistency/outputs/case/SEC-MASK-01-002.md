# SEC-MASK-01-002

- **标题**: Secret 值在 step summary 和错误堆栈中必须被脱敏
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Secret 值在 step summary 和错误堆栈中必须被脱敏**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-004

通过标准：
1. type=negative, target=step_summary, must_not_contain_secret="API_KEY"
2. type=negative, target=error_stack, must_not_contain_secret="API_KEY"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write secret to summary | `echo "Key: ${{ secrets.API_KEY }}" >> $ATOMGIT_STEP_SUMMARY` |  | ✅ GENUINE |
| 2 | Intentionally fail | `echo "Failing with key ${{ secrets.API_KEY }}" exit 1` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  summary-mask:
    name: Test summary masking
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write secret to summary
        run: |
          echo "Key: ${{ secrets.API_KEY }}" >> $ATOMGIT_STEP_SUMMARY
      - name: Intentionally fail
        run: |
          echo "Failing with key ${{ secrets.API_KEY }}"
          exit 1
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['API_KEY']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_summary | negative | !secret=API_KEY | ✅ GENUINE | 步骤使用 API_KEY，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | error_stack | negative | !secret=API_KEY | ✅ GENUINE | 步骤使用 API_KEY，secret 脱敏断言有验证对象（故意暴露测试） |

---