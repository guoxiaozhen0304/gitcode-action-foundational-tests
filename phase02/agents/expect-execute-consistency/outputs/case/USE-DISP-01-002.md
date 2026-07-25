# USE-DISP-01-002

- 标题: workflow_dispatch 未提供参数但存在 default 时应使用默认值运行
- 维度: 易用性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-DISP-01-002
维度标签:   ['usability', 'completeness']
维度:      usability/completeness
优先级:    P1
溯源意图:  INTENT-USE-030
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      workflow_dispatch 未提供参数但存在 default 时应使用默认值运行

前置条件:
  - workflow 配置了一个有 default 值的 input

操作步骤:
  1. 手动触发 workflow 不提供该参数

预期结果:
  workflow 使用默认值成功运行

验证点:
  - [正向] 运行成功完成
  - [正向] 日志中输出 default 值

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo env (test-default) | echo "env=${{ inputs.environment }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 运行成功完成 | 空洞 | no step produces 'env=staging' |
| 日志中输出 default 值 | 空洞 | no step produces 'env=staging' |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | env=staging | MISSING_SOURCE | no step produces 'env=staging' |

### 问题

- 验证点 `运行成功完成` → 空洞: no step produces 'env=staging'

- 验证点 `日志中输出 default 值` → 空洞: no step produces 'env=staging'

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'env=staging'

---
