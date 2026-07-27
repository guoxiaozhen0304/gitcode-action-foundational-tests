# COMP-CACHE-01-003

- **标题**: fork PR 不应覆盖或污染主分支 cache
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 不应覆盖或污染主分支 cache**

- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-016

通过标准：
1. type=negative, target=cache_pollution, equals=main_cache_overwritten
2. type=positive, target=main_cache_content, equals=original

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Cache write | `cache` |  | ✅ GENUINE |
| 2 | Write poison | `echo "poison" > cached.txt` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches:
      - main
jobs:
  verify:
    name: Verify fork cache isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Cache write
        uses: cache
        with:
          path: cached.txt
          key: shared-cache-key
      - name: Write poison
        run: |
          echo "poison" > cached.txt
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
| 1 | cache_pollution | negative | equals=main_cache_overwritten | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | main_cache_content | positive | equals=original | ✅ GENUINE | 断言有条件可被步骤验证 |

---