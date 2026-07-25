# COMP-PRTARGET-01-002

- 标题: 显式 checkout head.sha 后执行不可信代码的风险可控
- 维度: 完备性 | 优先级: P0
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-PRTARGET-01-002
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-014
参照来源:  inputs/gitcode-spec/action-development/top-level-fields.md
母意图:    —
标题:      显式 checkout head.sha 后执行不可信代码的风险可控

前置条件:
  - 存在一个来自 fork 的 PR

操作步骤:
  1. 在 pull_request_target workflow 中显式 checkout head.sha
  2. 执行 head.sha 中的脚本

预期结果:
  - 平台允许此行为（设计如此）
  - 但 workflow 文件版本仍来自 base 分支

验证点:
  - [正向] checkout head.sha 成功
  - [正向] workflow 文件仍为 base 分支版本

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Checkout head sha | uses: checkout | 是 |
| 2 | Verify workflow still base | run: echo "BASE_VERSION_MARKER"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches:
      - main
jobs:
  verify:
    name: Verify checkout head sha
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Checkout head sha
        uses: checkout
        with:
          ref: ${{ atomgit.event.pull_request.head.sha }}
      - name: Verify workflow still base
        run: |
          echo "BASE_VERSION_MARKER"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] checkout head.sha 成功 | 🚫 BLOCKED | trigger=pull_request_target, trigger=pull_request_target |
| [正向] workflow 文件仍为 base 分支版本 | 🚫 BLOCKED | trigger=pull_request_target, trigger=pull_request_target |

### 问题

- [正向] checkout head.sha 成功: BLOCKED - trigger=pull_request_target, trigger=pull_request_target
- [正向] workflow 文件仍为 base 分支版本: BLOCKED - trigger=pull_request_target, trigger=pull_request_target

---
