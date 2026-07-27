# REL-CACHE-01-048

- **标题**: cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**cache 同 key 并发写一致性——3 方并行写同一 key 不得产生混合/损坏内容**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-079

通过标准：
1. type=positive, target=cache_content_attribution, equals=single_writer_complete_or_explicit_conflict_error
2. type=negative, target=mixed_or_truncated_content_detected, equals=true
3. type=nonfunctional, target=concurrent_write_semantics, equals=recorded

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | cache write step | `cache` |  | ✅ GENUINE |
| 2 | write marker step | `mkdir -p shared_cache echo "writer_${{ matrix.writer_id }}_full_content_marker" ` |  | ✅ GENUINE |
| 3 | cache restore step | `cache` |  | ✅ GENUINE |
| 4 | check attribution step | `cat shared_cache/owner.txt || echo "cache_miss"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  writer:
    name: concurrent cache writer job
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        writer_id: [alpha, beta, gamma]
      fail-fast: false
    steps:
      - name: cache write step
        uses: cache
        with:
          path: shared_cache
          key: concurrent-same-key-probe
      - name: write marker step
        run: |
          mkdir -p shared_cache
          echo "writer_${{ matrix.writer_id }}_full_content_marker" > shared_cache/owner.txt
  verify:
    name: cache readback verify job
    runs-on: [ubuntu-latest, x64, small]
    needs: writer
    steps:
      - name: cache restore step
        uses: cache
        with:
          path: shared_cache
          key: concurrent-same-key-probe
      - name: check attribution step
        run: |
          cat shared_cache/owner.txt || echo "cache_miss"
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
| 1 | cache_content_attribution | positive | equals=single_writer_complete_or_explicit_conflict_error | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | mixed_or_truncated_content_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | concurrent_write_semantics | nonfunctional | equals=recorded | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---