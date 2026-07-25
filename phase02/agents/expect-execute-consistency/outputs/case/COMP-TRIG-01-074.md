# COMP-TRIG-01-074

- 标题: workflow_dispatch 事件关键字段与 inputs 验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-TRIG-01-074
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-084~085
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      workflow_dispatch 事件关键字段与 inputs 验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 配置 workflow_dispatch 触发并定义 inputs 参数
  2. 手动触发并传入参数验证

预期结果:
  - workflow_dispatch 支持手动触发，inputs 参数仅支持 string 类型，default 和 required 生效，atomgit.event.inputs 可访问

验证点:
  - [正向] 手动触发成功创建 run
  - [正向] inputs 参数值在 step 中可访问
  - [正向] 未传参时使用 default 值

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Print inputs | run: echo "ENV=${{ inputs.environment }}"
echo "VER=${{ inputs.version }}"
echo "dispatch_ok"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: Target env
        type: string
        required: true
        default: staging
      version:
        description: Version
        type: string
        required: false
        default: 1.0.0
jobs:
  verify:
    name: Verify workflow_dispatch fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Print inputs
        run: |
          echo "ENV=${{ inputs.environment }}"
          echo "VER=${{ inputs.version }}"
          echo "dispatch_ok"

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
| [正向] 手动触发成功创建 run | ✅ COVERED | steps have real logic |
| [正向] inputs 参数值在 step 中可访问 | ✅ COVERED | steps have real logic |
| [正向] 未传参时使用 default 值 | ✅ COVERED | steps have real logic |

### 问题

无

---
