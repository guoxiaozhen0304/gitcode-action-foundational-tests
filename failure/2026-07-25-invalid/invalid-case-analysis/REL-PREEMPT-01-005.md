## 失败分诊 · REL-PREEMPT-01-005 · preemption events 边界值——配置 10 个应正常解析

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L7:C13** — concurrency.preemption.events: 列表中存在非法值:[push] 允许值:[mr_id]


### 根因初判

**根因**: 文档缺失 — preemption events 取值限制
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: reliability | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: preemption events 边界值——配置 10 个应正常解析
- **断言**: 1 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
concurrency:
  max: 5
  exceed-action: QUEUE
  preemption:
    events: [push, pull_request, workflow_dispatch, schedule, tag, issue_comment, pull_request_comment, merge_requests, fork_pr, manual]
jobs:
  test:
    name: preempt boundary test
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: echo step
        run: |
          echo test
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   REL-PREEMPT-01-005
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
标题:      preemption events 边界值——配置 10 个应正常解析
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
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：文档缺失——preemption events 取值限制

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 平台团队更新文档以描述实际行为: preemption events 取值限制

---
