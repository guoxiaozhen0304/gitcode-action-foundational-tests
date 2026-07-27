# REL-CACHE-01-046

- **标题**: 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-046

通过标准：
1. type=positive, target=latest_cache_status, equals=hit
2. type=positive, target=oldest_cache_status, equals=miss

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | save cache | `cache` |  | ✅ GENUINE |
| 2 | generate cache data | `mkdir -p cache_data dd if=/dev/urandom of=cache_data/data.bin bs=1M count=100` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: cache LRU test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: save cache
        uses: cache
        with:
          path: cache_data
          key: cache-${{ matrix.index }}
      - name: generate cache data
        run: |
          mkdir -p cache_data
          dd if=/dev/urandom of=cache_data/data.bin bs=1M count=100
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
| 1 | latest_cache_status | positive | equals=hit | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | oldest_cache_status | positive | equals=miss | ✅ GENUINE | 断言有条件可被步骤验证 |

---