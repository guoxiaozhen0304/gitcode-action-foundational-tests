## 失败分诊 · COMPAT-ACTIONDEV-01-001 · action.yml 元数据校验与 GitHub 差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 2 条

### 诊断信息

1. **[Error] L0:C0** — jobs[test-action-meta].steps[1].uses: 格式错误：pluginname@version，其中 pluginname 为 1~50 位字母、数字、"-"、"_"，version（官方插件不填）为 00-99.00-99.00-99 三段两位数字

2. **[Error] L0:C0** — stages[default].jobs[test-action-meta]: 插件./.github/actions/my-action不存在


### 根因初判

**根因**: 用例问题 — uses 路径引用不存在的文件
**责任人**: Phase 01

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P2 | **触发器**: workflow_dispatch
- **标题**: action.yml 元数据校验与 GitHub 差异
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  test-action-meta:
    name: Test action metadata
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Checkout action repo
        uses: checkout
      - name: Use local action
        uses: ./.github/actions/my-action
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-ACTIONDEV-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
标题:      action.yml 元数据校验与 GitHub 差异
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

**综合**: 非预期拒绝：用例问题——uses 路径引用不存在的文件

**规避手段**: 修正 YAML 语法

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 修正 case YAML 语法错误: uses 路径引用不存在的文件
- 回流 Phase 01 评审 case 语法

---
