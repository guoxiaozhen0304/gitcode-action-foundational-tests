## 失败分诊 · COMPAT-CONCUR-01-001 · concurrency cancel-in-progress false 时应排队而非报错

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 2 条

### 诊断信息

1. **[Error] L0:C0** — concurrency.exceed-action: 值不能为空

2. **[Error] L0:C0** — concurrency.max: 值不能小于1


### 根因初判

**根因**: 产品bug — concurrency 字段语义与文档不符
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: concurrency cancel-in-progress false 时应排队而非报错
- **断言**: 2 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
concurrency:
  group: test-group-compat-034
  cancel-in-progress: false
jobs:
  concurrency-test:
    name: Test concurrency queue behavior
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: checkout source
        uses: checkout
      - name: long running step
        run: |
          echo "Starting long job"
          sleep 60
          echo "Job done"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-CONCUR-01-001
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
标题:      concurrency cancel-in-progress false 时应排队而非报错
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/writing-pipelines`

### 影响评估

- **阻塞性**: ⚪无影响 — 用例本身有意测试非法输入
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟡同维度 — 影响同维度多个用例

**综合**: 非预期拒绝：产品bug——concurrency 字段语义与文档不符

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: concurrency 字段语义与文档不符
- 等待平台修复后重新验证

---
