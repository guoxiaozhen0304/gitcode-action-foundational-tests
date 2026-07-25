## 失败分诊 · COMPAT-PR-01-003 · PR types 配置后匹配类型不触发与 GitHub 行为差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — on.merge_requests: 列表长度超出限制，branches branches-ignore之和不能小于1或超过32


### 根因初判

**根因**: 平台缺陷 — 列表长度限制未在文档声明
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: pull_request
- **标题**: PR types 配置后匹配类型不触发与 GitHub 行为差异
- **断言**: 1 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  pull_request:
    types: [open, reopen, update]
jobs:
  test-pr-types:
    name: Test PR types trigger
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo trigger info
        run: |
          echo "event_name=${{ atomgit.event_name }}"
          echo "done"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-PR-01-003
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
标题:      PR types 配置后匹配类型不触发与 GitHub 行为差异
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/trigger-events.md`

### 影响评估

- **阻塞性**: ⚪无影响 — 用例本身有意测试非法输入
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：平台缺陷——列表长度限制未在文档声明

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: 列表长度限制未在文档声明
- 等待平台修复后重新验证

---
