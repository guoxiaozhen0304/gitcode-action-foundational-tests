# SEC-ARTF-01-002

- 标题: 跨仓库 artifact 下载返回 403 或 404
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-ARTF-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-019
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    SEC-ARTF-01-001
标题:      跨仓库 artifact 下载返回 403 或 404

前置条件:
  - fork PR 已上传 artifact

操作步骤:
  1. 在主仓 workflow 中尝试下载 fork PR 的 artifact ID
  2. 查看下载结果

预期结果:
  - 下载返回 404 或权限拒绝
  - 不应静默返回空包或成功

验证点:
  - [负向] 跨仓库 artifact 下载绝不应成功
  - [正向] 返回明确的 404 或 403 错误

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Attempt download fork artifact (artifact-download) | curl -s -o /dev/null -w "%{http_code}" \n            "https://api.gitcode.com/api/v8/repos/${{ atomg | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 跨仓库 artifact 下载绝不应成功 | 覆盖 | log assertion without specific string check |
| 返回明确的 404 或 403 错误 | 覆盖 | log assertion without specific string check |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | CONSISTENT | log assertion without specific string check |
| 2 | run_logs | positive | 403_or_404 | CONSISTENT | log assertion without specific string check |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
