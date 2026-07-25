# COMP-PRTARGET-01-001

- 标题: pull_request_target 默认使用 base 分支 workflow 版本
- 维度: 完备性 | 优先级: P0
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-PRTARGET-01-001
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-014
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      pull_request_target 默认使用 base 分支 workflow 版本

前置条件:
  - 存在一个来自 fork 的 PR
  - base 分支 workflow 与 fork 分支 workflow 内容不同

操作步骤:
  1. fork 贡献者修改 workflow 文件
  2. 触发 pull_request_target

预期结果:
  - 执行的 workflow 版本来自 base 分支
  - fork 修改的 workflow 不影响执行逻辑

验证点:
  - [正向] 执行的 step 内容与 base 分支 workflow 一致
  - [负向] 不应执行 fork 分支修改后的 workflow 逻辑

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo base version marker | run: echo "BASE_VERSION_MARKER"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches:
      - main
jobs:
  verify:
    name: Verify base workflow version
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo base version marker
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
| [正向] 执行的 step 内容与 base 分支 workflow 一致 | 🚫 BLOCKED | trigger=pull_request_target, trigger=pull_request_target |
| [负向] 不应执行 fork 分支修改后的 workflow 逻辑 | 🚫 BLOCKED | trigger=pull_request_target, trigger=pull_request_target |

### 问题

- [正向] 执行的 step 内容与 base 分支 workflow 一致: BLOCKED - trigger=pull_request_target, trigger=pull_request_target
- [负向] 不应执行 fork 分支修改后的 workflow 逻辑: BLOCKED - trigger=pull_request_target, trigger=pull_request_target

---
