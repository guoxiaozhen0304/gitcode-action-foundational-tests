# COMPAT-MATRIX-01-005

- 标题: matrix exclude 全排除不被支持时的差异
- 维度: 兼容性 | 优先级: P2
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-MATRIX-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-NEW-007
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      matrix exclude 全排除不被支持时的差异

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，配置 `strategy.matrix.exclude` 排除所有组合
  2. 提交并触发 workflow

预期结果:
  - GitHub 行为：exclude 全排除时应报矩阵为空错误或生成 0 个实例
  - GitCode 行为：可能不支持 exclude 全排除
  - 应明确记录差异

验证点:
  - [正向] 系统对空矩阵给出明确报错
  - [负向] 不通过 exclude 被静默忽略导致所有实例仍生成

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo matrix values (test-matrix-exclude) | echo "os=${{ matrix.os }}" echo "node=${{ matrix.node }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 系统对空矩阵给出明确报错 | 覆盖 | LLM/nonfunctional assertion: 系统对空矩阵给出明确报错（如 matrix is empty） |
| 不通过 exclude 被静默忽略导致所有实例仍生成 | 覆盖 | LLM/nonfunctional assertion: exclude 不应被静默忽略导致所有实例仍生成 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | positive | 系统对空矩阵给出明确报错（如 matrix is empty） | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统对空矩阵给出明确报错（如 matrix is empty） |
| 2 | run_status | negative | exclude 不应被静默忽略导致所有实例仍生成 | LLM_DEPENDENT | LLM/nonfunctional assertion: exclude 不应被静默忽略导致所有实例仍生成 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
