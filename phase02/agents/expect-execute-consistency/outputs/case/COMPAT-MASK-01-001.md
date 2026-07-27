# COMPAT-MASK-01-001

- **标题**: 直接 echo secrets 值应在日志中被脱敏
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**直接 echo secrets 值应在日志中被脱敏**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-033

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="TEST_SECRET", eval=deterministic
2. type=positive, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | echo secret directly | `echo "Secret value: ${{ secrets.TEST_SECRET }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  mask-test:
    name: Test secret masking direct echo
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: echo secret directly
        run: |
          echo "Secret value: ${{ secrets.TEST_SECRET }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['TEST_SECRET']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=TEST_SECRET | ✅ GENUINE | 步骤使用 TEST_SECRET，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---