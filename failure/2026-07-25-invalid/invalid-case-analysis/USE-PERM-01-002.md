## 失败分诊 · USE-PERM-01-002 · 使用 GitHub 权限域命名时报错应给出 GitCode 对照表

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 预期非法 (negative test)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L2:C13** — permissions.contents: unknown property


### 根因初判

**根因**: 需人工判断 — 未分类
**责任人**: 需人工判断

> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。

### 证据

- **维度**: usability | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: 使用 GitHub 权限域命名时报错应给出 GitCode 对照表
- **断言**: 0 positive / 1 negative

**Workflow 摘要**:
```yaml
permissions:
  contents: read
on:
  workflow_dispatch:
jobs:
  bad-perm:
    name: test github permission error
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: checkout
        uses: checkout
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   USE-PERM-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
标题:      使用 GitHub 权限域命名时报错应给出 GitCode 对照表
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/security-permissions/token-permissions.md`

### 影响评估

- **阻塞性**: 🔴阻塞 — YAML 无法通过校验，workflow 无法部署运行
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非阻塞：case 本身是 negative test，INVALID 是期望结果

**规避手段**: 无——此为有意测试，平台报错符合预期

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 保持 case 不变，确认平台对非法输入的报错行为符合预期

---
