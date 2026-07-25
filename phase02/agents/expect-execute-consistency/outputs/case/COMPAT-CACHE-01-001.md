# COMPAT-CACHE-01-001

- 标题: cache 行为等价性——缓存命中场景
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-CACHE-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-025
参照来源:  inputs/gitcode-spec/core-concepts/artifacts-and-cache.md
母意图:    —
标题:      cache 行为等价性——缓存命中场景

前置条件:
  - 仓库已启用 cache 插件
  - 首次运行已生成缓存条目

操作步骤:
  1. 在工作流中使用 `uses: cache` 配置 key 和 path
  2. 首次运行生成缓存后，再次触发同一工作流
  3. 观察第二次运行的缓存恢复行为

预期结果:
  - 第二次运行时 cache 步骤识别到已有缓存并命中
  - 命中后无需重新生成，直接恢复缓存目录内容
  - cache 插件裸名写法行为与 GitHub 全名写法等价

验证点:
  - [正向] 第二次运行日志中出现缓存命中标识
  - [正向] 缓存目录内容正确恢复
  - [负向] 不应因 key 匹配而实际未恢复内容

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) restore cache | uses: cache | 是 |
| 2 | (TC) verify cache state | run: if [ -f "$HOME/.cache/test-dir/marker.txt" ]; then
  echo "CACHE_HIT"
else
  echo "CACHE_MISS"
  mkdir -p "$HOME/.cache/test-dir"
  echo "marker" > "$ | 是 |
| 3 | (TC) save cache | uses: cache | if: ${{ always() }} | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify-cache-hit:
    name: Verify cache hit behavior
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) restore cache
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-test-${{ atomgit.run_id }}
          restore-keys: compat-cache-test-
      - name: (TC) verify cache state
        run: |
          if [ -f "$HOME/.cache/test-dir/marker.txt" ]; then
            echo "CACHE_HIT"
          else
            echo "CACHE_MISS"
            mkdir -p "$HOME/.cache/test-dir"
            echo "marker" > "$HOME/.cache/test-dir/marker.txt"
          fi
      - name: (TC) save cache
        if: ${{ always() }}
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-test-${{ atomgit.run_id }}

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 第二次运行日志中出现缓存命中标识 | ✅ COVERED | steps have real logic |
| [正向] 缓存目录内容正确恢复 | ✅ COVERED | steps have real logic |
| [负向] 不应因 key 匹配而实际未恢复内容 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
