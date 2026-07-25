# COMPAT-MATRIX-01-003

- 标题: matrix 三维展开不被支持时的差异
- 维度: 兼容性 | 优先级: P2
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-MATRIX-01-003
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-NEW-007
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      matrix 三维展开不被支持时的差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，配置三维 matrix（如 os × node × browser）
  2. 提交并触发 workflow

预期结果:
  - GitHub 行为：三维 matrix 应正常展开为多个 job 实例
  - GitCode 行为：可能不支持三维展开
  - 应明确记录差异

验证点:
  - [正向] 系统对三维 matrix 给出明确响应（接受或拒绝）
  - [负向] 不通过静默忽略导致 matrix 配置失效

清理:      无


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo matrix values | run: echo "os=${{ matrix.os }}"
echo "node=${{ matrix.node }}"
echo "browser=${{ matrix.browser }}"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-3d-matrix:
    name: Test 3D matrix
    runs-on: [ubuntu-latest, x64, small]
    strategy:
      matrix:
        os: [ubuntu, macos]
        node: [16, 18]
        browser: [chrome, firefox]
    steps:
      - name: Echo matrix values
        run: |
          echo "os=${{ matrix.os }}"
          echo "node=${{ matrix.node }}"
          echo "browser=${{ matrix.browser }}"

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
| [正向] 系统对三维 matrix 给出明确响应（接受或拒绝） | ✅ COVERED | steps have real logic |
| [负向] 不通过静默忽略导致 matrix 配置失效 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
