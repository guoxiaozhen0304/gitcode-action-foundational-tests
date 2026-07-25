## 失败分诊 · COMPAT-CONCUR-01-004 · concurrency preemption events 越界时行为差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 3 条

### 诊断信息

1. **[Error] L0:C0** — concurrency.exceed-action: 值不能为空

2. **[Error] L0:C0** — concurrency.max: 值不能小于1

3. **[Error] L7:C13** — concurrency.preemption.events: 列表中存在非法值:[11] 允许值:[mr_id]


### 根因初判

**根因**: 文档缺失 — preemption events 取值限制
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: concurrency preemption events 越界时行为差异
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
concurrency:
  group: test-preemption-events
  preemption:
    enable: true
    events: 11
jobs:
  test-preemption-events:
    name: Test preemption events boundary
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo hello
        run: |
          echo "hello"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-CONCUR-01-004
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
标题:      concurrency preemption events 越界时行为差异
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

**综合**: 非预期拒绝：文档缺失——preemption events 取值限制

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 平台团队更新文档以描述实际行为: preemption events 取值限制

---
