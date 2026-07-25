# COMPAT-INPUTS-01-001

- 标题: workflow_dispatch inputs 类型限制 - boolean 应报错
- 维度: 兼容性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-INPUTS-01-001
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-014
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      workflow_dispatch inputs 类型限制 - boolean 应报错

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow 中定义 workflow_dispatch inputs 并指定 type: boolean
  2. 提交并推送该 workflow
  3. 观察平台校验行为

预期结果:
  - 平台应对不支持的 boolean 类型给出明确的校验错误
  - 错误信息应提示仅支持 string 类型

验证点:
  - [负向] boolean 类型不应被静默接受
  - [正向] 错误信息应明确指出仅支持 string 类型

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo input | run: echo "INPUT_OK"
 | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      dry_run:
        description: '是否仅验证不部署'
        required: false
        default: false
        type: boolean
jobs:
  verify:
    name: Verify boolean input rejection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo input
        run: |
          echo "INPUT_OK"

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
| [负向] boolean 类型不应被静默接受 | ✅ COVERED | negative assertion in YAML assertions |
| [正向] 错误信息应明确指出仅支持 string 类型 | ⚠️ PARTIAL | steps exist but all trivial (echo only) |

### 问题

- [正向] 错误信息应明确指出仅支持 string 类型: PARTIAL - all steps are trivial echo

---
