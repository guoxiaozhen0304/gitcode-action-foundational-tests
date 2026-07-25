# COMP-TRIG-01-079

- 标题: 触发事件 types 取值与过滤边界验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-079
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-234~560
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      触发事件 types 取值与过滤边界验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 pull_request 和 merge_requests 的 types
  2. 验证允许值和非法值处理

预期结果:
  - pull_request types 允许 merge / open / reopen / update，merge_requests types 允许 close / merge / open / reopen / update，非法 types 被平台拒绝

验证点:
  - [正向] 合法 types 通过校验
  - [负向] 非法 types 被平台拒绝
  - [正向] 默认 types 在未指定时生效

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | run: echo "types_boundary_ok"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify trigger types boundary
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo ok
        run: |
          echo "types_boundary_ok"

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
| [正向] 合法 types 通过校验 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [负向] 非法 types 被平台拒绝 | ⚠️ PARTIAL | no real logic in steps |
| [正向] 默认 types 在未指定时生效 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] 合法 types 通过校验: PARTIAL - all steps are trivial echo
- [负向] 非法 types 被平台拒绝: PARTIAL - no real logic in steps
- [正向] 默认 types 在未指定时生效: PARTIAL - all steps are trivial echo

---
