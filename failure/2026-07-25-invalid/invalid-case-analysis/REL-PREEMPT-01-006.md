## 失败分诊 · REL-PREEMPT-01-006 · preemption events 越界值——配置 11 个应被拒绝

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 预期非法 (negative test)
**诊断数**: 2 条

### 诊断信息

1. **[Error] L7:C13** — concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id]

2. **[Error] L7:C13** — concurrency.preemption.events: 列表长度必须在0到10之间


### 根因初判

**根因**: 需人工判断 — 未分类
**责任人**: 需人工判断

> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。

### 证据

- **维度**: reliability | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: preemption events 越界值——配置 11 个应被拒绝
- **断言**: 1 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
concurrency:
  max: 5
  exceed-action: QUEUE
  preemption:
    events: [push, pull_request, workflow_dispatch, schedule, tag, issue_comment, pull_request_comment, merge_requests, fork_pr, manual, pr]
jobs:
  test:
    name: preempt invalid test
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: echo step
        run: |
          echo test
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   REL-PREEMPT-01-006
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
标题:      preemption events 越界值——配置 11 个应被拒绝
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/writing-pipelines`

> 文档未声明 preemption events 仅支持 mr_id。

### 影响评估

- **阻塞性**: ⚪无影响 — 用例本身有意测试非法输入
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟡同维度 — 影响同维度多个用例

**综合**: 非阻塞：case 本身是 negative test，INVALID 是期望结果

**规避手段**: 无——此为有意测试，平台报错符合预期

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 保持 case 不变，确认平台对非法输入的报错行为符合预期

---
