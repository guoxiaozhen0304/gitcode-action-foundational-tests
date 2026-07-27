# USE-DIR-01-001

- **标题**: workflow 放置于 .gitcode/workflows/ 下可正常触发
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**workflow 放置于 .gitcode/workflows/ 下可正常触发**

- 触发事件: `push`
- 规格引用: INTENT-USE-001

通过标准：
1. type=positive, target=run_status, equals=COMPLETED

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | check directory | `echo "workflow triggered from .gitcode/workflows/"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
jobs:
  verify-dir:
    name: verify directory trigger
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: check directory
        run: |
          echo "workflow triggered from .gitcode/workflows/"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=COMPLETED | ❌ IMPOSSIBLE | 期望 !=success 但无步骤可能失败 |

### 问题

**断言 1 — IMPOSSIBLE**❌: 期望 !=success 但无步骤可能失败

---