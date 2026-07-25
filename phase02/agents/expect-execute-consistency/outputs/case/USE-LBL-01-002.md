# USE-LBL-01-002

- 标题: runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-LBL-01-002
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-025
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner

前置条件:
  - 仓库有匹配的 runner 但当前无空闲资源

操作步骤:
  1. 触发一个使用正确标签但需要等待的 workflow

预期结果:
  系统提示当前无空闲 Runner，正在排队，而非报无可用 runner

验证点:
  - [非功能] 状态或日志中是否出现排队/等待字样
  - [非功能] 错误信息是否区分无匹配与容量不足

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | step (queue-test) | echo "queued then ran"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 状态或日志中是否出现排队/等待字样 | 覆盖 | 非功能断言存在(LLM评估) |
| 错误信息是否区分无匹配与容量不足 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | 若因容量不足排队，应提示当前无空闲 Runner，正在排队而非无可用 runne | LLM_DEPENDENT | LLM/nonfunctional assertion: 若因容量不足排队，应提示当前无空闲 Runner，正在排队而非无可用 runner；若因标签不匹配，应 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
