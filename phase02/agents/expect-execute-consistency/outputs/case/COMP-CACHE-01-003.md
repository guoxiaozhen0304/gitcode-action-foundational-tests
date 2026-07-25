# COMP-CACHE-01-003

- 标题: fork PR 不应覆盖或污染主分支 cache
- 维度: 完备性 | 优先级: P0
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
- 主分支已存在 cache
- 存在一个来自 fork 的 PR

操作步骤:
1. fork PR 触发 workflow 并写入 cache
2. 主分支再次触发 workflow 读取同一 cache key

预期结果:
- 主分支 cache 未被 fork PR 覆盖
- 主分支读取到的仍是原有 cache 内容

验证点:
- [负向] fork PR 不应覆盖主分支 cache
- [正向] 主分支 cache 内容保持不变

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Cache write | uses: cache with path: cached.txt, key: shared-cache-key | 是 |
| 2 | Write poison | echo "poison" > cached.txt | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CACHE-01-003
dimensions: [completeness, security, reliability]
dimension: completeness
priority: P0
title: fork PR 不应覆盖或污染主分支 cache
intent_ref: INTENT-COMP-016

setup:
  repo_fixture: with-cache
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
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

trigger:
  event: pull_request
  as: untrusted_contributor
  params: {}

fault_injection: null

assertions:
  - type: negative
    target: cache_pollution
    equals: main_cache_overwritten
  - type: positive
    target: main_cache_content
    equals: original

teardown:
  reset: fixture
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo | with-cache |
| Secrets | (none) |
| 阻塞 | untrusted_contributor 实现需要第二个独立账号，当前测试环境缺乏多账号支持 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] fork PR 不应覆盖主分支 cache | ❌ BLOCKED | untrusted_contributor 身份依赖多账号模拟 fork PR 场景 |
| [正向] 主分支 cache 内容保持不变 | ❌ BLOCKED | 同上；需先以 untrusted_contributor 执行再以 maintainer 验证主分支 cache |

### 问题

- 触发身份为 untrusted_contributor，需要第二个独立账号 fork 仓库后发起 PR，测试环境无此能力

---
