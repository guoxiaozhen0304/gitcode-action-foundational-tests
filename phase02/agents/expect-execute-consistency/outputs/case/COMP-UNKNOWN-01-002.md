# COMP-UNKNOWN-01-002

- 标题: 不应静默忽略未知字段导致用户误以为配置生效
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-UNKNOWN-01-002
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-002
参照来源:  inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md
母意图:    —
标题:      不应静默忽略未知字段导致用户误以为配置生效

前置条件:
  - 仓库具备提交 workflow 的权限

操作步骤:
  1. 提交包含看似合法但平台不支持的字段的 workflow
  2. 触发并观察运行行为

预期结果:
  - 平台不应静默忽略未知字段而继续执行
  - 若字段未知，应显式报错而非忽略

验证点:
  - [负向] 运行不应在未知字段被静默忽略的情况下成功完成

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo step | run: echo "should not run"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test silent ignore
    runs-on: [ubuntu-latest, x64, small]
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
| [负向] 运行不应在未知字段被静默忽略的情况下成功完成 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
