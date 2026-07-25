## 失败分诊 · COMPAT-EXPR-01-013 · success() 带括号与不带括号的兼容性差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 2 条

### 诊断信息

1. **[Error] L0:C0** — jobs[test-success-paren].steps[0].if: if表达式无法解析 表达式：success()第1位出现不支持的函数

2. **[Error] L0:C0** — jobs[test-success-paren].steps[1].if: if表达式无法解析 表达式：success第1位出现不支持的关键字


### 根因初判

**根因**: 用例问题 — GitHub 表达式函数 vs GitCode 关键字——success 关键字未使用
**责任人**: Phase 01

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: success() 带括号与不带括号的兼容性差异
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  test-success-paren:
    name: Test success with/without parens
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Step with parens
        if: ${{ success() }}
        run: |
          echo "with_parens"
      - name: Step without parens
        if: ${{ success }}
        run: |
          echo "without_parens"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-EXPR-01-013
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
标题:      success() 带括号与不带括号的兼容性差异
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
- **影响面**: 🟡同维度 — 影响同维度多个用例

**综合**: 非预期拒绝：用例问题——GitHub 表达式函数 vs GitCode 关键字——success 关键字未使用

**规避手段**: 修正 YAML 语法

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 修正 case YAML 语法错误: GitHub 表达式函数 vs GitCode 关键字——success 关键字未使用
- 回流 Phase 01 评审 case 语法

---
