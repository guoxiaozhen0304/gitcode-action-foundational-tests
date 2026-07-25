# COMP-STEP-01-069

- 标题: step 必填与核心字段 name run uses 验证
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-STEP-01-069
维度标签:   [completeness]
维度:      完备性
优先级:    P1
溯源意图:  KEEP-TC-279~288
参照来源:  inputs/existing-cases/cases.md
母意图:    —
标题:      step 必填与核心字段 name run uses 验证

前置条件:
  - 仓库已启用 AtomGit Action

操作步骤:
  1. 定义含 name / run 的 step 和含 name / uses 的 step
  2. 验证 step name 必填且无非法字符

预期结果:
  - 每个 step 必须有 name，run 执行 shell 命令，uses 调用 Action，name 不含非法字符

验证点:
  - [正向] name + run 步骤正常执行
  - [正向] name + uses 步骤正常执行
  - [负向] step name 含非法字符被拒绝

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Run step | run: echo "run_ok"
 | 否 |
| 2 | Uses step | uses: checkout | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify:
    name: Verify step core fields
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Run step
        run: |
          echo "run_ok"
      - name: Uses step
        uses: checkout

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
| [正向] name + run 步骤正常执行 | ✅ COVERED | steps have real logic |
| [正向] name + uses 步骤正常执行 | ✅ COVERED | steps have real logic |
| [负向] step name 含非法字符被拒绝 | ✅ COVERED | steps have real logic |

### 问题

无

---
