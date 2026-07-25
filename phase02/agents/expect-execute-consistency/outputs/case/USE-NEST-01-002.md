# USE-NEST-01-002

- 标题: workflow_call 嵌套 2 层时应正常执行
- 维度: 易用性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-NEST-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-026
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      workflow_call 嵌套 2 层时应正常执行

前置条件:
  - 仓库存在 2 层嵌套的 reusable workflow

操作步骤:
  1. 主 workflow 调用 A，A 调用 B

预期结果:
  运行成功完成，无嵌套层数报错

验证点:
  - [正向] 运行成功完成
  - [负向] 不应报嵌套超限错误

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | call reusable (caller) | ./.gitcode/workflows/reusable-level1.yml | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 运行成功完成 | 覆盖 | status assertion: COMPLETED |
| 不应报嵌套超限错误 | 未覆盖 | 缺少负向断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | COMPLETED | CONSISTENT | status assertion: COMPLETED |

### 问题

- 验证点 `不应报嵌套超限错误` → 未覆盖: 缺少负向断言

---
