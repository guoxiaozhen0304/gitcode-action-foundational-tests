# COMP-UNKNOWN-01-001

- 标题: 包含未知顶层字段的 workflow 触发 YAML 校验失败
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-UNKNOWN-01-001
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-002
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      包含未知顶层字段的 workflow 触发 YAML 校验失败

前置条件:
  - 仓库具备提交 workflow 的权限

操作步骤:
  1. 提交包含未知顶层字段（如 unknown_field: true）的 workflow
  2. 尝试触发该 workflow

预期结果:
  - 平台在校验阶段报错，拒绝执行该 workflow
  - 错误信息应指明不支持的字段名或行号

验证点:
  - [正向] workflow 提交后触发校验失败
  - [非功能] 错误信息包含字段名及不支持语义

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo step | run: echo "should not run"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
unknown_field: true
on:
  workflow_dispatch:
jobs:
  test:
    name: Test unknown field
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo step
        run: |
          echo "should not run"

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
| [正向] workflow 提交后触发校验失败 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |
| [非功能] 错误信息包含字段名及不支持语义 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] workflow 提交后触发校验失败: PARTIAL - all steps are trivial echo
- [非功能] 错误信息包含字段名及不支持语义: PARTIAL - all steps are trivial echo

---
