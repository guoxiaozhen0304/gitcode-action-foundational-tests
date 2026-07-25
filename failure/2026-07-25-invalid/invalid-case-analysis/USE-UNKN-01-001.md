## 失败分诊 · USE-UNKN-01-001 · 未知字段如 run-name 不应被静默忽略而应给出警告或错误

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 预期非法 (negative test)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L1:C11** — run-name: unknown property


### 根因初判

**根因**: 需人工判断 — 未分类
**责任人**: 需人工判断

> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。

### 证据

- **维度**: usability | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: 未知字段如 run-name 不应被静默忽略而应给出警告或错误
- **断言**: 0 positive / 0 negative

**Workflow 摘要**:
```yaml
run-name: Build by ${{ atomgit.actor }}
name: unknown field test
on:
  workflow_dispatch:
jobs:
  bad:
    name: unknown field run-name
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: step
        run: |
          echo "hello"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   USE-UNKN-01-001
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
标题:      未知字段如 run-name 不应被静默忽略而应给出警告或错误
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

**综合**: 非阻塞：case 本身是 negative test，INVALID 是期望结果

**规避手段**: 无——此为有意测试，平台报错符合预期

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 保持 case 不变，确认平台对非法输入的报错行为符合预期

---
