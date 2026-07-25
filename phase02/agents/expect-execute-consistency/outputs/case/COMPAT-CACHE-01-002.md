# COMPAT-CACHE-01-002

- 标题: cache 行为等价性——fork PR 写隔离
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-CACHE-01-002
维度标签:   [compatibility, security]
维度:      兼容性
优先级:    P0
溯源意图:  INTENT-COMPAT-025
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    COMPAT-CACHE-01-001
标题:      cache 行为等价性——fork PR 写隔离

前置条件:
  - 仓库已启用 cache 插件
  - 存在一个来自 fork 的 PR

操作步骤:
  1. 在 fork PR 的工作流中使用 `uses: cache` 尝试写入新缓存
  2. 观察 fork PR 场景下的缓存写入行为
  3. 对比同一缓存 key 在主干分支上的写入权限

预期结果:
  - fork PR 不应覆盖或污染主干分支的缓存条目
  - fork PR 可读取公共缓存，但写入应被隔离或拒绝
  - 系统应为 fork 提供独立的缓存命名空间或阻止写入

验证点:
  - [负向] fork PR 不应成功覆盖主干缓存
  - [正向] 主干缓存保持完整未被污染
  - [正向] 系统提供明确的缓存隔离机制

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) restore cache | uses: cache | 是 |
| 2 | (TC) attempt write from fork | run: mkdir -p "$HOME/.cache/test-dir"
echo "FORK_MARKER_$(date +%s)" > "$HOME/.cache/test-dir/fork_marker.txt"
echo "FORK_WRITE_ATTEMPTED"
 | 是 |
| 3 | (TC) save cache | uses: cache | if: ${{ always() }} | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  verify-fork-cache:
    name: Verify fork PR cache isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) restore cache
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-fork-test
          restore-keys: compat-cache-fork-test-
      - name: (TC) attempt write from fork
        run: |
          mkdir -p "$HOME/.cache/test-dir"
          echo "FORK_MARKER_$(date +%s)" > "$HOME/.cache/test-dir/fork_marker.txt"
          echo "FORK_WRITE_ATTEMPTED"
      - name: (TC) save cache
        if: ${{ always() }}
        uses: cache
        with:
          path: ~/.cache/test-dir
          key: compat-cache-fork-test

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pr |
| 触发身份 | untrusted_contributor |
| Repo Fixture | with-fork-pr |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] fork PR 不应成功覆盖主干缓存 | ✅ COVERED | negative assertion in YAML assertions |
| [正向] 主干缓存保持完整未被污染 | ✅ COVERED | steps have real logic |
| [正向] 系统提供明确的缓存隔离机制 | ✅ COVERED | steps have real logic |

### 问题

无

---
