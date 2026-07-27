# SEC-INJ-01-004

- **标题**: 不可信 commit message 不可直接插进 run 脚本导致命令注入
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**不可信 commit message 不可直接插进 run 脚本导致命令注入**

- 触发事件: `push`
- 规格引用: INTENT-SEC-012

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Inline commit message | `echo "Message is ${{ atomgit.event.commits[0].message }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  commit-inj:
    name: Test commit message injection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Inline commit message
        run: |
          echo "Message is ${{ atomgit.event.commits[0].message }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

---