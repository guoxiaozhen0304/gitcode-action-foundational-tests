# SEC-CACHE-01-002

- **标题**: 主仓 cache restore 对 fork cache miss
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**主仓 cache restore 对 fork cache miss**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-018

通过标准：
1. type=negative, target=cache_restore
2. type=positive, target=run_logs, equals=cache_miss

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Restore cache | `cache` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  cache-restore:
    name: Restore cache from main repo
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Restore cache
        uses: cache
        with:
          path: ./node_modules
          key: test-cache-key
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-cache` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore | negative |  | ✅ GENUINE | 通用断言匹配 |
| 2 | run_logs | positive | equals=cache_miss | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---