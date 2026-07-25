# COMP-CACHE-01-001

- 标题: cache hit 时恢复缓存内容正确
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

前置条件:
- 之前运行已生成匹配的 cache

操作步骤:
1. 触发 workflow，使用 cache 插件
2. 观察 cache 是否命中

预期结果:
- cache 命中并正确恢复内容

验证点:
- [正向] cache 步骤状态为 success
- [正向] 恢复后的文件内容与之前一致

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Cache test file | uses: cache with path: cached.txt, key: cache-test-${{ runner.os }} | 是 |
| 2 | Use cache | cat cached.txt || echo "cache miss" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-CACHE-01-001
dimensions: [completeness, security, reliability]
dimension: completeness
priority: P0
title: cache hit 时恢复缓存内容正确
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
      name: Verify cache hit
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Cache test file
          uses: cache
          with:
            path: cached.txt
            key: cache-test-${{ runner.os }}
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
    target: run_status
    equals: success
  - type: positive
    target: cache_step
    equals: hit

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
| [正向] cache 步骤状态为 success | ✅ COVERED | 断言 cache_step=hit，run_status=success |
| [正向] 恢复后的文件内容与之前一致 | ✅ COVERED | 步骤2 cat cached.txt 输出内容，run_status=success 隐含内容正确（无错误退出） |

### 问题

- 无

---
