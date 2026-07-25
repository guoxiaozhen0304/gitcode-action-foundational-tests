# SEC-DOS-01-001

- 标题: 大 artifact / 大 cache 必须受配额与边界限制
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-DOS-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-033
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      大 artifact / 大 cache 必须受配额与边界限制

前置条件:
  - 仓库支持 artifact 和 cache 上传

操作步骤:
  1. 提交一个 workflow，尝试上传超大 artifact 或写入超大 cache
  2. 触发 workflow 并查看上传结果

预期结果:
  - 超过大小上限的 artifact/cache 上传绝不应成功写入
  - 超限时应给出明确报错（大小限制值），不应静默截断或卡死

验证点:
  - [负向] 超过大小上限的 artifact/cache 上传绝不应成功写入
  - [非功能] 超限时应给出明确报错（大小限制值），不应静默截断或卡死

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Create large file (quota-test) | dd if=/dev/zero of=large.bin bs=1M count=1100  | GENUINE |
| 2 | Upload large artifact (quota-test) | upload-artifact | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 超过大小上限的 artifact/cache 上传绝不应成功写入 | 覆盖 | negative status assertion |
| 超限时应给出明确报错（大小限制值），不应静默截断或卡死 | 未覆盖 | 缺少非功能断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative |  | CONSISTENT | negative status assertion |
| 2 | run_logs | positive | size_limit_exceeded_error | CONSISTENT | log assertion without specific string check |

### 问题

- 验证点 `超限时应给出明确报错（大小限制值），不应静默截断或卡死` → 未覆盖: 缺少非功能断言

---
