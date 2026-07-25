# COMPAT-INPUTS-01-002

- 标题: workflow_dispatch inputs 类型限制 - string 正常通过
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-INPUTS-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-014
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    COMPAT-INPUTS-01-001
标题:      workflow_dispatch inputs 类型限制 - string 正常通过

前置条件:
  - 仓库已启用 Actions
  - 测试分支存在

操作步骤:
  1. 在 workflow 中定义 workflow_dispatch inputs 并指定 type: string
  2. 提交并推送该 workflow
  3. 触发 workflow 并传入参数

预期结果:
  - workflow 应被平台接受，不报错
  - string 类型的 input 应能正常接收和输出

验证点:
  - [正向] workflow 校验通过
  - [正向] string 类型 input 能正常传递和使用

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo input value | run: echo "ENV=${{ inputs.environment }}"
echo "STRING_INPUT_OK"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '部署目标环境'
        required: true
        default: 'staging'
        type: string
jobs:
  verify:
    name: Verify string input acceptance
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo input value
        run: |
          echo "ENV=${{ inputs.environment }}"
          echo "STRING_INPUT_OK"

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
| [正向] workflow 校验通过 | ✅ COVERED | steps have real logic |
| [正向] string 类型 input 能正常传递和使用 | ✅ COVERED | steps have real logic |

### 问题

无

---
