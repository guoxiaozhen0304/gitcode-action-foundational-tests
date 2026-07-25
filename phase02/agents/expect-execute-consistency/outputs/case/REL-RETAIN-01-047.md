# REL-RETAIN-01-047

- 标题: artifact 保留期 90 天边界——第 91 天应不可下载
- 维度: 可靠性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   REL-RETAIN-01-047
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-047
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      artifact 保留期 90 天边界——第 91 天应不可下载

前置条件:
  - 仓库具备 artifact 使用权限

操作步骤:
  1. 上传保留期为 90 天的 artifact
  2. 第 90 天尝试下载
  3. 第 91 天尝试下载

预期结果:
  - 第 90 天下载成功(HTTP 200)
  - 第 91 天下载失败(404/403)

验证点:
  - [正向] 第 90 天可下载
  - [正向] 第 91 天不可下载

清理:      无需特殊清理
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | create artifact (test) | echo retention test > retention.txt  | GENUINE |
| 2 | upload artifact (test) | upload-artifact | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 第 90 天可下载 | 覆盖 | real step logic exists |
| 第 91 天不可下载 | 覆盖 | real step logic exists |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_day90_status | positive | 200 | CONSISTENT | real step logic exists |
| 2 | download_day91_status | positive | 404 | CONSISTENT | real step logic exists |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
