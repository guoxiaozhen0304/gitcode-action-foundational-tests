# COMPAT-FIELD-01-003

- 标题: 未知顶层字段不应被静默忽略而应给出警告
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-FIELD-01-003
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-021
参照来源:  inputs/gitcode-spec/
母意图:    —
标题:      未知顶层字段不应被静默忽略而应给出警告

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，包含一个 GitHub 特有的顶层字段（如 `concurrency.cancel-in-progress: true` 以外的未知字段，或自定义字段 `custom_field: value`）
  2. 提交并触发 workflow

预期结果:
  - 系统不应静默忽略未知字段
  - 应给出警告或错误，提示用户该字段不被支持

验证点:
  - [负向] 不通过未知字段被静默忽略
  - [正向] 系统给出警告或错误，提示未知字段

清理:      无


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo hello | run: echo "hello"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
custom_field: value
jobs:
  test-unknown-field:
    name: Test unknown top-level field
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo hello
        run: |
          echo "hello"

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
| [负向] 不通过未知字段被静默忽略 | ✅ COVERED | negative assertion in YAML assertions |
| [正向] 系统给出警告或错误，提示未知字段 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] 系统给出警告或错误，提示未知字段: PARTIAL - all steps are trivial echo

---
