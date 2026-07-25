## 失败分诊 · SEC-SUPPLY-01-003 · 第三方 Action 来源应具备信任边界（typosquatting 限制）

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 2 条

### 诊断信息

1. **[Error] L0:C0** — jobs[typo-test].steps[0].uses: 格式错误：pluginname@version，其中 pluginname 为 1~50 位字母、数字、"-"、"_"，version（官方插件不填）为 00-99.00-99.00-99 三段两位数字

2. **[Error] L0:C0** — stages[default].jobs[typo-test]: 插件checkout-action@v1不存在


### 根因初判

**根因**: 用例问题 — uses 引用不存在的插件
**责任人**: Phase 01

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: security | **优先级**: P0 | **触发器**: workflow_dispatch
- **标题**: 第三方 Action 来源应具备信任边界（typosquatting 限制）
- **断言**: 1 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  typo-test:
    name: Test typosquatting rejection
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Use typo action
        uses: checkout-action@v1
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   SEC-SUPPLY-01-003
维度标签:   [security]
维度:      安全性
优先级:    P0
标题:      第三方 Action 来源应具备信任边界（typosquatting 限制）
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/writing-pipelines/configure-dependencies-order.md`

> 文档展示 stages array 和 map 两种格式，但平台只接受 map 格式。

### 影响评估

- **阻塞性**: ⚪无影响 — 用例本身有意测试非法输入
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟡同维度 — 影响同维度多个用例

**综合**: 非预期拒绝：用例问题——uses 引用不存在的插件

**规避手段**: 修正 YAML 语法

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 修正 case YAML 语法错误: uses 引用不存在的插件
- 回流 Phase 01 评审 case 语法

---
