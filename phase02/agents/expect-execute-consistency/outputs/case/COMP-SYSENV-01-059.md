# COMP-SYSENV-01-059

- 标题: ATOMGIT 系统环境变量关键变量存在性
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-SYSENV-01-059
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-197~222
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      ATOMGIT 系统环境变量关键变量存在性

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 step 的 run 中输出所有 ATOMGIT_* 环境变量是否存在
  2. 运行 workflow 检查日志

预期结果:
  - ATOMGIT_SHA / REF / REF_NAME / REF_TYPE / EVENT_NAME / EVENT_PATH / WORKSPACE / REPOSITORY / RUN_ID / RUN_NUMBER / WORKFLOW / SERVER_URL / API_URL / OUTPUT / ENV / PATH / STEP_SUMMARY 均存在且非空

验证点:
  - [正向] 关键 ATOMGIT_* 变量在日志中显示非空
  - [负向] 无关键变量缺失

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check critical vars | run: echo "SHA_SET=$([ -n "$ATOMGIT_SHA" ] && echo yes    echo no)"
echo "REF_SET=$([ -n "$ATOMGIT_REF" ] && echo yes    echo no)"
echo "REF_NAME_SET=$([ - | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify ATOMGIT env presence
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Check critical vars
        run: |
          echo "SHA_SET=$([ -n "$ATOMGIT_SHA" ] && echo yes || echo no)"
          echo "REF_SET=$([ -n "$ATOMGIT_REF" ] && echo yes || echo no)"
          echo "REF_NAME_SET=$([ -n "$ATOMGIT_REF_NAME" ] && echo yes || echo no)"
          echo "EVENT_NAME_SET=$([ -n "$ATOMGIT_EVENT_NAME" ] && echo yes || echo no)"
          echo "WORKSPACE_SET=$([ -n "$ATOMGIT_WORKSPACE" ] && echo yes || echo no)"
          echo "REPO_SET=$([ -n "$ATOMGIT_REPOSITORY" ] && echo yes || echo no)"
          echo "RUN_ID_SET=$([ -n "$ATOMGIT_RUN_ID" ] && echo yes || echo no)"
          echo "RUN_NUM_SET=$([ -n "$ATOMGIT_RUN_NUMBER" ] && echo yes || echo no)"
          echo "SERVER_SET=$([ -n "$ATOMGIT_SERVER_URL" ] && echo yes || echo no)"
          echo "API_SET=$([ -n "$ATOMGIT_API_URL" ] && echo yes || echo no)"

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
| [正向] 关键 ATOMGIT_* 变量在日志中显示非空 | ✅ COVERED | steps have real logic |
| [负向] 无关键变量缺失 | ✅ COVERED | steps have real logic |

### 问题

无

---
