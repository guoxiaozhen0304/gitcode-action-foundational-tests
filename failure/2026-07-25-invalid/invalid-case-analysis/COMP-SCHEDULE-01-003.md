## 失败分诊 · COMP-SCHEDULE-01-003 · cron 间隔短于 5 分钟时被拒绝或降级

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 预期非法 (negative test)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L3:C13** — on.schedule[0].cron: 不是可识别的cron表达式


### 根因初判

**根因**: 需人工判断 — 未分类
**责任人**: 需人工判断

> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。

### 证据

- **维度**: completeness | **优先级**: P1 | **触发器**: schedule
- **标题**: cron 间隔短于 5 分钟时被拒绝或降级
- **断言**: 0 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  schedule:
    - cron: "*/1 * * * *"
jobs:
  verify:
    name: Verify short interval rejection
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo scheduled
        run: |
          echo "should not run"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMP-SCHEDULE-01-003
维度标签:   [completeness, compatibility]
维度:      completeness
优先级:    P1
标题:      cron 间隔短于 5 分钟时被拒绝或降级
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/trigger-events.md`

### 影响评估

- **阻塞性**: 🟡非阻塞 — workflow 仍可通过其他合法语法完成
- **静默性**: 🟡可察觉 — 平台报错信息不够清晰
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非阻塞：case 本身是 negative test，INVALID 是期望结果

**规避手段**: 无——此为有意测试，平台报错符合预期

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 保持 case 不变，确认平台对非法输入的报错行为符合预期

---
