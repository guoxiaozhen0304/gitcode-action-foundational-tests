## 失败分诊 · COMP-UNKNOWN-01-001 · 包含未知顶层字段的 workflow 触发 YAML 校验失败

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L1:C16** — unknown_field: unknown property


### 根因初判

**根因**: 平台缺陷 — 未知字段静默拒绝
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: completeness | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: 包含未知顶层字段的 workflow 触发 YAML 校验失败
- **断言**: 1 positive / 0 negative

**Workflow 摘要**:
```yaml
unknown_field: true
on:
  workflow_dispatch:
jobs:
  test:
    name: Test unknown field
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo step
        run: |
          echo "should not run"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMP-UNKNOWN-01-001
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
标题:      包含未知顶层字段的 workflow 触发 YAML 校验失败
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

（未找到直接对应的规格文件）

### 影响评估

- **阻塞性**: 🔴阻塞 — YAML 无法通过校验，workflow 无法部署运行
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：平台缺陷——未知字段静默拒绝

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: 未知字段静默拒绝
- 等待平台修复后重新验证

---
