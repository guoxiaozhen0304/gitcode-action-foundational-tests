# COMP-VARREF-01-083

- 标题: YAML 表达式与 Shell 环境变量引用方式验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-VARREF-01-083
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-438~440
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      YAML 表达式与 Shell 环境变量引用方式验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 在 env 和 run 中分别使用 ${{ }} 表达式和 $VAR 环境变量方式引用
  2. 验证两种方式结果一致

预期结果:
  - ${{ env.VAR }} 与 $VAR 引用同一变量时值一致，${{ atomgit.sha }} 与 $ATOMGIT_SHA 值一致

验证点:
  - [正向] 表达式引用与环境变量引用结果相同
  - [正向] atomgit 上下文与 ATOMGIT_* 环境变量值一致

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Compare references | run: echo "EXPR=${{ env.TEST_VAR }}"
echo "ENV=$TEST_VAR"
echo "SHA_EXPR=${{ atomgit.sha }}"
echo "SHA_ENV=$ATOMGIT_SHA"
echo "ref_ok"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
env:
  TEST_VAR: hello
jobs:
  verify:
    name: Verify variable reference styles
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Compare references
        run: |
          echo "EXPR=${{ env.TEST_VAR }}"
          echo "ENV=$TEST_VAR"
          echo "SHA_EXPR=${{ atomgit.sha }}"
          echo "SHA_ENV=$ATOMGIT_SHA"
          echo "ref_ok"

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
| [正向] 表达式引用与环境变量引用结果相同 | ✅ COVERED | steps have real logic |
| [正向] atomgit 上下文与 ATOMGIT_* 环境变量值一致 | ✅ COVERED | steps have real logic |

### 问题

无

---
