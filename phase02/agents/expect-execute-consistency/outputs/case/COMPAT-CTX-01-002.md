# COMPAT-CTX-01-002

- 标题: 使用 atomgit.ref 上下文应正确返回触发引用
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-CTX-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-016
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    COMPAT-CTX-01-001
标题:      使用 atomgit.ref 上下文应正确返回触发引用

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow 的 run 步骤中引用 ${{ atomgit.ref }}
  2. 提交并推送该 workflow
  3. 触发 workflow 运行

预期结果:
  - atomgit.ref 应正确返回触发事件的引用（如 refs/heads/main）

验证点:
  - [正向] 日志中 atomgit_ref 的值不为空且符合预期格式

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo atomgit ref | run: echo "atomgit_ref=${{ atomgit.ref }}"
echo "done"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test atomgit context reference
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo atomgit ref
        run: |
          echo "atomgit_ref=${{ atomgit.ref }}"
          echo "done"

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
| [正向] 日志中 atomgit_ref 的值不为空且符合预期格式 | ✅ COVERED | steps have real logic |

### 问题

无

---
