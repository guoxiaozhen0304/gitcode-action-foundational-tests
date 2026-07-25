# COMP-WFLOW-01-061

- 标题: workflow name 与 on 字段必填与类型验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-WFLOW-01-061
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-366~401
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow name 与 on 字段必填与类型验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 name 和 on 的 workflow
  2. 验证 name 为可选但 on 为必填，on 必须为 map

预期结果:
  - workflow 可正常提交并触发，name 缺省时使用文件名，on 为 map 格式

验证点:
  - [正向] 含 name 的 workflow 被正确显示
  - [正向] on 为 map 时 workflow 可被触发
  - [负向] on 为数组时平台拒绝

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | run: echo "workflow_ok"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
name: Test workflow name and on
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify workflow fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo ok
        run: |
          echo "workflow_ok"

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
| [正向] 含 name 的 workflow 被正确显示 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [正向] on 为 map 时 workflow 可被触发 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [负向] on 为数组时平台拒绝 | ⚠️ PARTIAL | no real logic in steps |

### 问题

- [正向] 含 name 的 workflow 被正确显示: PARTIAL - all steps are trivial echo
- [正向] on 为 map 时 workflow 可被触发: PARTIAL - all steps are trivial echo
- [负向] on 为数组时平台拒绝: PARTIAL - no real logic in steps

---
