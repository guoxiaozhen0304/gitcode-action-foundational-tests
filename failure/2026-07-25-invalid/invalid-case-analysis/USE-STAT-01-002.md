## 失败分诊 · USE-STAT-01-002 · 使用 success() 带括号时报错应提示 GitCode 括号差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 预期非法 (negative test)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — jobs[bad-stat].steps[0].if: if表达式无法解析 表达式：success()第1位出现不支持的函数


### 根因初判

**根因**: 需人工判断 — 未分类
**责任人**: 需人工判断

> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。

### 证据

- **维度**: usability | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: 使用 success() 带括号时报错应提示 GitCode 括号差异
- **断言**: 0 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  bad-stat:
    name: test success bracket error
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: step with brackets
        if: ${{ success() }}
        run: |
          echo "hello"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   USE-STAT-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
标题:      使用 success() 带括号时报错应提示 GitCode 括号差异
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/expressions.md`

> 文档描述了 if 条件表达式语法，但平台解析器不支持部分合法运算符。

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
