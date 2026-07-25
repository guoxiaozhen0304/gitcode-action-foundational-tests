## 失败分诊 · COMP-TRIG-01-075 · schedule 事件关键字段与 cron 格式验证

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L3:C13** — on.schedule[0].cron: 不是可识别的cron表达式


### 根因初判

**根因**: 产品bug — cron 表达式被拒 (合法语法)
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: completeness | **优先级**: P1 | **触发器**: schedule
- **标题**: schedule 事件关键字段与 cron 格式验证
- **断言**: 1 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  schedule:
    - cron: "0 2 * * *"
jobs:
  verify:
    name: Verify schedule event fields
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Print schedule
        run: |
          echo "SCHEDULE=${{ atomgit.event.schedule }}"
          echo "schedule_ok"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMP-TRIG-01-075
维度标签:   [completeness]
维度:      完备性
优先级:    P1
标题:      schedule 事件关键字段与 cron 格式验证
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/trigger-events.md`

> 文档描述了 schedule cron 触发方式，但平台 cron 解析器与标准 cron 语法不兼容。

### 影响评估

- **阻塞性**: 🟡非阻塞 — workflow 仍可通过其他合法语法完成
- **静默性**: 🟡可察觉 — 平台报错信息不够清晰
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：产品bug——cron 表达式被拒 (合法语法)

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: cron 表达式被拒 (合法语法)
- 等待平台修复后重新验证

---
