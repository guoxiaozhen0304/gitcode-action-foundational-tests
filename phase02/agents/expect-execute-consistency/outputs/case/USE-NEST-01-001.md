# USE-NEST-01-001

- 标题: workflow_call 嵌套 3 层时报错应明确提示上限为 2 层
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-NEST-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-026
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      workflow_call 嵌套 3 层时报错应明确提示上限为 2 层

前置条件:
  - 仓库存在 3 层嵌套的 reusable workflow

操作步骤:
  1. 主 workflow 调用 A，A 调用 B，B 调用 C

预期结果:
  系统在校验或调度阶段报错，明确说明 workflow_call 嵌套层数超过 GitCode 上限 2 层

验证点:
  - [负向] 不应静默失败或卡死
  - [非功能] 报错中是否包含 workflow_call、嵌套、2 层、上限等关键词

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
| 不应静默失败或卡死 | 覆盖 | negative status assertion |
| 报错中是否包含 workflow_call、嵌套、2 层、上限等关键词 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含 workflow_call、嵌套、2 层、上限等关键词中的至少 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含 workflow_call、嵌套、2 层、上限等关键词中的至少两项 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
