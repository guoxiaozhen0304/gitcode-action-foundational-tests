# USE-LBL-01-001

- 标题: runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-LBL-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-025
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表

前置条件:
  - 仓库无匹配该标签组合的 runner

操作步骤:
  1. 使用完全不存在的标签组合如 [nonexistent-os, x64, small]

预期结果:
  系统在合理超时后失败，报错包含用户指定的标签和可用 runner 类型列表

验证点:
  - [负向] 不应无限 queued 且无提示
  - [非功能] 错误信息中是否包含用户指定的标签文本

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | step (bad) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应无限 queued 且无提示 | 覆盖 | negative status assertion |
| 错误信息中是否包含用户指定的标签文本 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含用户指定的 runs-on 标签原文；若因标签不匹配，应提示未找 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含用户指定的 runs-on 标签原文；若因标签不匹配，应提示未找到匹配标签的 Runn |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
