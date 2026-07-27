# SEC-CACHE-01-001

- **标题**: fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 写入的 cache 必须不可被主仓后续 workflow 读取**

- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-018

通过标准：
1. type=negative, target=cache_restore
2. type=positive, target=run_status, equals=completed

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write cache | `cache` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  cache-write:
    name: Write cache from fork
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write cache
        uses: cache
        with:
          path: ./node_modules
          key: test-cache-key
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-cache` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore | negative |  | ✅ GENUINE | 通用断言匹配 |
| 2 | run_status | positive | equals=completed | ✅ GENUINE | 状态断言 completed 可被步骤行为验证 |

---