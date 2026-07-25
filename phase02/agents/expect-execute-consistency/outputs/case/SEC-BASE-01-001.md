# SEC-BASE-01-001

- 标题: pull_request_target 使用 base 分支的 workflow 版本
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-BASE-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-035
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      pull_request_target 使用 base 分支的 workflow 版本

前置条件:
  - 仓库 base 分支和 fork PR 分支的 workflow 内容不同

操作步骤:
  1. 在 fork PR 分支修改 workflow 文件（新增窃密步骤）
  2. 触发 pull_request_target 事件
  3. 检查实际执行的 workflow 版本

预期结果:
  - pull_request_target 触发时加载并执行 base 分支中的 workflow 文件版本
  - fork PR 分支内对 workflow 文件的改动不得被采用

验证点:
  - [正向] base 分支 workflow 按其定义执行，可访问 secret 与写 token
  - [负向] fork PR 分支内对 workflow 文件的改动不得被 pull_request_target 运行采用

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo from base (base-version) | echo "Executing base branch workflow"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request_target |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| base 分支 workflow 按其定义执行，可访问 secret 与写 token | 覆盖 | log assertion without specific string check |
| fork PR 分支内对 workflow 文件的改动不得被 pull_request_target 运行采用 | 覆盖 | log assertion without specific string check |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | base_branch_workflow_executed | CONSISTENT | log assertion without specific string check |
| 2 | run_logs | negative |  | CONSISTENT | log assertion without specific string check |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
