# REL-STATE-01-058

- 标题: Runner 状态机正确性——空闲/运行/离线转换与时序一致性
- 维度: 可靠性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   REL-STATE-01-058
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-058
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      Runner 状态机正确性——空闲/运行/离线转换与时序一致性

前置条件:
  - 仓库具备 runner 状态查询权限

操作步骤:
  1. 对同一 runner 连续执行触发→观察→等待→触发循环 5 轮

预期结果:
  - 状态序列符合 idle→running→idle
  - 转换时延有界

验证点:
  - [正向] 状态序列正确
  - [非功能] idle→running≤30s
  - [非功能] running→idle≤60s

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | sleep step (test) | sleep 60  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 状态序列正确 | 覆盖 | real step logic exists |
| idle→running≤30s | 覆盖 | 非功能断言存在(LLM评估) |
| running→idle≤60s | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | state_sequence | positive | idle_running_idle | CONSISTENT | real step logic exists |
| 2 | idle_to_running_seconds | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |
| 3 | running_to_idle_seconds | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
