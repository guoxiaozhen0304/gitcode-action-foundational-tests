## 失败分诊 · COMPAT-VARS-01-005 · vars 在条件表达式 if 中的可用性差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — jobs[test-vars-if].steps[1].if: if表达式无法解析 表达式：vars.ENABLE_FEATURE == 'true'第1位出现不支持的关键字


### 根因初判

**根因**: 用例问题 — GitHub 表达式函数 vs GitCode 关键字——vars 上下文不支持 if 条件
**责任人**: Phase 01

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: vars 在条件表达式 if 中的可用性差异
- **断言**: 1 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  test-vars-if:
    name: Test vars in if condition
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Step always runs
        run: |
          echo "always"
      - name: Step conditional on vars
        if: ${{ vars.ENABLE_FEATURE == 'true' }}
        run: |
          echo "feature_enabled"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-VARS-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
标题:      vars 在条件表达式 if 中的可用性差异
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

**综合**: 非预期拒绝：用例问题——GitHub 表达式函数 vs GitCode 关键字——vars 上下文不支持 if 条件

**规避手段**: 修正 YAML 语法

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 修正 case YAML 语法错误: GitHub 表达式函数 vs GitCode 关键字——vars 上下文不支持 if 条件
- 回流 Phase 01 评审 case 语法

---
