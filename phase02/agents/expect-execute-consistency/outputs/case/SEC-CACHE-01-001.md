# SEC-CACHE-01-001

- 标题: fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   SEC-CACHE-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-018
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      fork PR 写入的 cache 必须不可被主仓后续 workflow 读取

前置条件:
  - 仓库配置了 cache

操作步骤:
  1. 以 fork 贡献者身份提交一个写入 cache 的 workflow
  2. 在主仓提交一个读取相同 cache key 的 workflow

预期结果:
  - 主仓 workflow 的 cache restore 不应命中 fork PR 写入的缓存
  - 缓存键应带仓库级隔离前缀

验证点:
  - [负向] 主仓 workflow 在 fork PR 写入 cache 后，绝不应命中到该缓存
  - [非功能] 缓存命中率监控应显示跨仓库命中为 0

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write cache | uses: cache with path=./node_modules, key=test-cache-key | 是 |

<details><summary>完整 workflow YAML</summary>

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

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 主仓 workflow 在 fork PR 写入 cache 后，绝不应命中到该缓存 | ✅ COVERED | 步骤以 fork 贡献者身份真实写入 cache（uses: cache），断言 target=cache_restore, must_not_hit=fork_cache_key 可验证主仓不可读取 |
| [非功能] 缓存命中率监控应显示跨仓库命中为 0 | 🔄 UNVERIFIABLE | 监控指标为平台级可观测性度量，单次 workflow 步骤无法产出这类聚合监控数据 |

### 问题

- [非功能] 缓存命中率监控应显示跨仓库命中为 0: UNVERIFIABLE — 缓存命中率是平台级监控指标，不是单个 workflow 步骤能产出或验证的输出

## 5. 评级理由

两个验证点中一个 COVERED（步骤通过 uses: cache 真实写入缓存，为安全隔离断言的验证提供前提），一个 UNVERIFIABLE（监控指标不可通过步骤产出），评级为部分不符。
