# COMP-TRIG-01-078

- 标题: 多事件组合与分支路径过滤验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-078
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-423
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      多事件组合与分支路径过滤验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 push 和 workflow_dispatch 多事件组合
  2. 验证 push 时 branches 和 paths 过滤

预期结果:
  - 同一 workflow 可配置多个事件，push 的 branches 和 paths 同时过滤，paths 与 paths-ignore 互斥

验证点:
  - [正向] 多事件组合通过校验
  - [正向] push 到匹配分支且路径匹配时触发
  - [负向] paths 与 paths-ignore 同时存在时平台拒绝或只保留 paths

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | run: echo "multi_event_ok"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches: [main]
    paths:
      - "src/**"
      - "package.json"
  workflow_dispatch:
jobs:
  verify:
    name: Verify multi event and filters
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo ok
        run: |
          echo "multi_event_ok"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 多事件组合通过校验 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] push 到匹配分支且路径匹配时触发 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [负向] paths 与 paths-ignore 同时存在时平台拒绝或只保留 paths | ⚠️ PARTIAL | no real logic in steps |

### 问题

- [正向] 多事件组合通过校验: PARTIAL - all steps are trivial echo
- [正向] push 到匹配分支且路径匹配时触发: PARTIAL - all steps are trivial echo
- [负向] paths 与 paths-ignore 同时存在时平台拒绝或只保留 paths: PARTIAL - no real logic in steps

---
