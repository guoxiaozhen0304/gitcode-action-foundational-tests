# USE-RUN-01-001

- 标题: 使用三段式标签时 job 正常调度
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-RUN-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-006
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      使用三段式标签时 job 正常调度

前置条件:
  - 仓库有可用的 dedicate-hosted runner

操作步骤:
  1. 使用 runs-on: [dedicate-hosted, x64, large]

预期结果:
  job 被成功调度到匹配的 runner

验证点:
  - [正向] 运行成功完成
  - [正向] job 日志显示在对应 runner 上执行

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | check runner (test-runner) | echo "runner ok"  | VACUOUS |

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
| job 日志显示在对应 runner 上执行 | 覆盖 | status assertion: COMPLETED |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | COMPLETED | CONSISTENT | status assertion: COMPLETED |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
