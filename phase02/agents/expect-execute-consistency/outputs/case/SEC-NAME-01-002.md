# SEC-NAME-01-002

- **标题**: 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secrets 时日志中必须保持脱敏**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-025

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="API_KEY"
2. type=positive, target=run_logs, equals=masked_or_not_found

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Run printenv | `printenv | grep API_KEY || echo not found` |  | ✅ GENUINE |
| 2 | Read proc environ | `cat /proc/self/environ | tr '\0' '\n' | grep API_KEY || echo not found` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  printenv-test:
    name: Test printenv masking
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Run printenv
        run: |
          printenv | grep API_KEY || echo not found
      - name: Read proc environ
        run: |
          cat /proc/self/environ | tr '\0' '\n' | grep API_KEY || echo not found
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
| 1 | run_logs | negative | !secret=API_KEY | ❌ UNEXERCISED | 断言 secret 不泄露但无步骤使用 API_KEY |
| 2 | run_logs | positive | equals=masked_or_not_found | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

### 问题

**断言 1 — UNEXERCISED**❌: 断言 secret 不泄露但无步骤使用 API_KEY

---