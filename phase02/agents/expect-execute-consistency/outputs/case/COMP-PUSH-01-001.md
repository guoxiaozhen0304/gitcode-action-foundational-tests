# COMP-PUSH-01-001

- 标题: 匹配 branches 的 push 正确触发 workflow
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-PUSH-01-001
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-003
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      匹配 branches 的 push 正确触发 workflow

前置条件:
  - workflow 配置 branches: [main]

操作步骤:
  1. 向 main 分支推送代码
  2. 观察 workflow 是否触发

预期结果:
  - push 到 main 分支触发 workflow 运行

验证点:
  - [正向] 运行记录存在且 event 为 push
  - [正向] head_branch 为 main

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo triggered | run: echo "triggered on main"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches:
      - main
jobs:
  verify:
    name: Verify branch trigger
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo triggered
        run: |
          echo "triggered on main"

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
| [正向] 运行记录存在且 event 为 push | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] head_branch 为 main | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] 运行记录存在且 event 为 push: PARTIAL - all steps are trivial echo
- [正向] head_branch 为 main: PARTIAL - all steps are trivial echo

---
