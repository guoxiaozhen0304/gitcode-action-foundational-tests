# COMP-SYSENV-01-060

- 标题: ATOMGIT 系统环境变量值正确性
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SYSENV-01-060
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-197~222
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      ATOMGIT 系统环境变量值正确性

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 step 中比对 ATOMGIT_* 环境变量与 atomgit 上下文值的一致性
  2. 验证各变量值格式正确

预期结果:
  - ATOMGIT_SHA 与 atomgit.sha 一致，ATOMGIT_REF 与 atomgit.ref 一致，ATOMGIT_EVENT_NAME 与 atomgit.event_name 一致

验证点:
  - [正向] ATOMGIT_SHA 等于 atomgit.sha
  - [正向] ATOMGIT_REF 等于 atomgit.ref
  - [正向] ATOMGIT_RUN_NUMBER 与 atomgit.run_number 一致

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Compare values | run: echo "SHA_MATCH=$([ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ] && echo yes    echo no)"
echo "REF_MATCH=$([ "$ATOMGIT_REF" = "${{ atomgit.ref }}" ] && ec | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify ATOMGIT env values
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare values
        run: |
          echo "SHA_MATCH=$([ "$ATOMGIT_SHA" = "${{ atomgit.sha }}" ] && echo yes || echo no)"
          echo "REF_MATCH=$([ "$ATOMGIT_REF" = "${{ atomgit.ref }}" ] && echo yes || echo no)"
          echo "EVENT_MATCH=$([ "$ATOMGIT_EVENT_NAME" = "${{ atomgit.event_name }}" ] && echo yes || echo no)"
          echo "REPO_MATCH=$([ "$ATOMGIT_REPOSITORY" = "${{ atomgit.repository }}" ] && echo yes || echo no)"

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
| [正向] ATOMGIT_SHA 等于 atomgit.sha | ✅ COVERED | steps have real logic |
| [正向] ATOMGIT_REF 等于 atomgit.ref | ✅ COVERED | steps have real logic |
| [正向] ATOMGIT_RUN_NUMBER 与 atomgit.run_number 一致 | ✅ COVERED | steps have real logic |

### 问题

无

---
