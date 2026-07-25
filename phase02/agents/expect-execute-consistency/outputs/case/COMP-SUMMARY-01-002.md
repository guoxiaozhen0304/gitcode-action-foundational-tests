# COMP-SUMMARY-01-002

- 标题: summary 中不应暴露系统内部路径
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SUMMARY-01-002
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-018
参照来源:  inputs/gitcode-spec/syntax-reference/workflow-commands.md
母意图:    —
标题:      summary 中不应暴露系统内部路径

前置条件:
  - workflow 向 ATOMGIT_STEP_SUMMARY 写入内容

操作步骤:
  1. 触发 workflow
  2. 检查 summary 内容

预期结果:
  - summary 中不包含 Runner 内部绝对路径等敏感信息

验证点:
  - [负向] summary 中不出现 /tmp/runner-xxx 等内部路径

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write safe summary | run: echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify summary security
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write safe summary
        run: |
          echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"

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
| [负向] summary 中不出现 /tmp/runner-xxx 等内部路径 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
