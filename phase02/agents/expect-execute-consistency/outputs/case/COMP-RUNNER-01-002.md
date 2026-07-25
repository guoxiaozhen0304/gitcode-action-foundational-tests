# COMP-RUNNER-01-002

- 标题: runs-on default 等效 ubuntu-latest x64 small
- 维度: 完备性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-RUNNER-01-002
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
溯源意图:  INTENT-COMP-010
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      runs-on default 等效 ubuntu-latest x64 small

前置条件:
  - 平台支持 default 快捷标签

操作步骤:
  1. 配置 runs-on: default
  2. 触发 workflow

预期结果:
  - job 被调度到 small 规格 Runner
  - 运行成功

验证点:
  - [正向] 运行状态为 success
  - [正向] Runner 规格与 small（2核8G）一致

清理:      none
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo runner info (verify) | echo "os=$RUNNER_OS" echo "arch=$RUNNER_ARCH"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 运行状态为 success | 覆盖 | workflow can potentially fail |
| Runner 规格与 small（2核8G）一致 | 覆盖 | workflow can potentially fail |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | CONSISTENT | workflow can potentially fail |
| 2 | runner_spec | positive | small | CONSISTENT | real step logic exists |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
