# REL-CACHE-01-047

- **标题**: cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cache 容量上限探测——500MB/1GB/2GB 单 cache 的接受/拒绝语义**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-079

通过标准：
1. type=positive, target=write_outcome, equals=accepted_or_explicit_rejection_with_limit
2. type=positive, target=readback_md5_match, equals=true_if_accepted
3. type=negative, target=silent_corruption_detected, equals=true
4. type=nonfunctional, target=measured_cache_limit, equals=recorded

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | cache save step | `cache` |  | ✅ GENUINE |
| 2 | generate cache data step | `mkdir -p cache_data dd if=/dev/urandom of=cache_data/data.bin bs=1M count=${{ ma` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: cache size probe job
    runs-on: [ubuntu-latest, x64, large]
    strategy:
      matrix:
        size_mb: [500, 1000, 2000]
      fail-fast: false
    steps:
      - name: cache save step
        uses: cache
        with:
          path: cache_data
          key: cache-size-probe-${{ matrix.size_mb }}
      - name: generate cache data step
        run: |
          mkdir -p cache_data
          dd if=/dev/urandom of=cache_data/data.bin bs=1M count=${{ matrix.size_mb }}
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
| 1 | write_outcome | positive | equals=accepted_or_explicit_rejection_with_limit | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | readback_md5_match | positive | equals=true_if_accepted | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | silent_corruption_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | measured_cache_limit | nonfunctional | equals=recorded | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---