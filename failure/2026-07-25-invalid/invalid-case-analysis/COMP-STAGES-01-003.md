## 失败分诊 · COMP-STAGES-01-003 · post.run_always true 时 workflow 失败仍执行 post

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 2 条

### 诊断信息

1. **[Error] L14:C5** — post.steps: unknown property

2. **[Error] L12:C15** — post.run_always: unknown property


### 根因初判

**根因**: 文档冲突 — post.steps/run_always 文档描述但平台拒
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: completeness | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: post.run_always true 时 workflow 失败仍执行 post
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  main:
    name: Main job fail
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Force failure
        run: |
          exit 1
post:
  run_always: true
  steps:
    - name: Post cleanup
      run: |
        echo "post executed"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMP-STAGES-01-003
维度标签:   [completeness]
维度:      completeness
优先级:    P1
标题:      post.run_always true 时 workflow 失败仍执行 post
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/core-concepts/workflow-job-step-action.md`

> 文档描述了 post 后处理阶段，但平台校验器报 unknown property。

### 影响评估

- **阻塞性**: 🔴阻塞 — YAML 无法通过校验，workflow 无法部署运行
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟡同维度 — 影响同维度多个用例

**综合**: 非预期拒绝：文档冲突——post.steps/run_always 文档描述但平台拒

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 平台团队更新文档以描述实际行为: post.steps/run_always 文档描述但平台拒

---
