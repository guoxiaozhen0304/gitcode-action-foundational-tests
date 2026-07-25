# COMP-CACHE-01-002

- 标题: restore-keys 前缀匹配兜底生效
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 之前运行已生成前缀匹配的 cache

操作步骤:
1. 触发 workflow，精确 key 不匹配但 restore-keys 前缀匹配

预期结果:
- restore-keys 前缀匹配成功，恢复最近同前缀缓存

验证点:
- [正向] cache 步骤通过 restore-keys 命中

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Cache test file | uses: cache with key: cache-test-v2-..., restore-keys: cache-test-v1-..., cache-test- | 是 |
| 2 | Use cache | cat cached.txt || echo "cache miss" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CACHE-01-002
dimensions: [completeness, security, reliability]
dimension: completeness
priority: P0
title: restore-keys 前缀匹配兜底生效
intent_ref: INTENT-COMP-016

setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default

workflow: |
  on:
    workflow_dispatch:
  jobs:
    verify:
      name: Verify restore keys fallback
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Cache test file
          uses: cache
          with:
            path: cached.txt
            key: cache-test-v2-${{ runner.os }}
            restore-keys: |
              cache-test-v1-${{ runner.os }}
              cache-test-
        - name: Use cache
          run: |
            cat cached.txt || echo "cache miss"

trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}

fault_injection: null

assertions:
  - type: positive
    target: cache_step
    equals: restore_hit

teardown:
  reset: none
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] cache 步骤通过 restore-keys 命中 | ✅ COVERED | 断言 cache_step=restore_hit，明确验证 restore-keys 兜底行为 |

### 问题

- 无

---
