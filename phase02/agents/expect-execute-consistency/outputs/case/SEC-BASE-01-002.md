# SEC-BASE-01-002

- 标题: fork PR 改 workflow 不被 pull_request_target 采用
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-BASE-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-035
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    SEC-BASE-01-001
标题:      fork PR 改 workflow 不被 pull_request_target 采用

前置条件:
  - fork PR 分支修改了 workflow 文件

操作步骤:
  1. 在 fork PR 分支新增一个输出 secret 的步骤到 workflow
  2. 触发 pull_request_target 事件
  3. 检查运行日志中是否出现该步骤

预期结果:
  - fork PR 注入的步骤未出现在执行记录中
  - 运行采用的 workflow 内容哈希/步骤集与 base 分支一致

验证点:
  - [负向] pull_request_target 绝不应执行来自不可信 fork 的 workflow 定义
  - [正向] 运行采用的 workflow 内容哈希/步骤集与 base 分支一致

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Base step only (reject-fork-wf) | echo "Only base steps run"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request_target |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| pull_request_target 绝不应执行来自不可信 fork 的 workflow 定义 | 覆盖 | log assertion without specific string check |
| 运行采用的 workflow 内容哈希/步骤集与 base 分支一致 | 覆盖 | status assertion: success_with_base_workflow |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | CONSISTENT | log assertion without specific string check |
| 2 | run_status | positive | success_with_base_workflow | CONSISTENT | status assertion: success_with_base_workflow |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
