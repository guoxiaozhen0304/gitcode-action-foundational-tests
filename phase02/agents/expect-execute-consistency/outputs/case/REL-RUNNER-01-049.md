# REL-RUNNER-01-049

- 标题: Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值
- 维度: 可靠性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   REL-RUNNER-01-049
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-049
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      Runner 规格真实性——small/medium/large 实际 CPU/内存/磁盘 vs 声明值

前置条件:
  - 仓库具备多种 flavor runner 使用权限

操作步骤:
  1. 对 small/medium/large 各触发探针 job，读取 /proc/cpuinfo、free -m、df

预期结果:
  - 每种 flavor 实际资源不低于声明值的 90%
  - 各探针在 5 分钟内完成调度

验证点:
  - [正向] CPU/内存/磁盘最小比率≥0.9
  - [负向] 实际资源不应显著低于声明
  - [非功能] queued→running ≤5min

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | probe small (probe-small) | nproc free -m df -BG ${{RUNNER_TEMP}}  | GENUINE |
| 2 | probe medium (probe-medium) | nproc free -m df -BG ${{RUNNER_TEMP}}  | GENUINE |
| 3 | probe large (probe-large) | nproc free -m df -BG ${{RUNNER_TEMP}}  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| CPU/内存/磁盘最小比率≥0.9 | 覆盖 | real step logic exists |
| 实际资源不应显著低于声明 | 未覆盖 | 缺少负向断言 |
| queued→running ≤5min | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | resource_ratio | positive |  | CONSISTENT | real step logic exists |
| 2 | queued_to_running_minutes | nonfunctional |  | LLM_DEPENDENT | LLM/nonfunctional assertion:  |

### 问题

- 验证点 `实际资源不应显著低于声明` → 未覆盖: 缺少负向断言

---
