# USE-ACT-01-004

- **标题**: 文档短名与市场名两种写法解析一致性验证
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**文档短名与市场名两种写法解析一致性验证**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-052

通过标准：
1. type=positive, target=validation_result, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | use cache short name | `cache` |  | ✅ GENUINE |
| 3 | use cache market name | `AtomgitCache` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  short-name:
    name: official short name reference
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: use cache short name
        uses: cache
        with:
          path: ~/.cache
          key: probe-cache-key
  market-name:
    name: market name reference
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: use cache market name
        uses: AtomgitCache
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
| 1 | validation_result | positive | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---