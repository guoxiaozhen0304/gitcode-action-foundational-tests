# COMP-PUSH-01-002

- 标题: 不匹配 branches 的 push 不触发 workflow
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-PUSH-01-002
维度标签:   [completeness]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-003
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      不匹配 branches 的 push 不触发 workflow

前置条件:
  - workflow 配置 branches: [main]

操作步骤:
  1. 向 develop 分支推送代码
  2. 观察 workflow 是否触发

预期结果:
  - push 到 develop 分支不触发 workflow

验证点:
  - [负向] 运行列表中不存在该 push 触发的运行

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo triggered | run: echo "should not run"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    branches:
      - main
jobs:
  verify:
    name: Verify branch skip
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo triggered
        run: |
          echo "should not run"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 运行列表中不存在该 push 触发的运行 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
