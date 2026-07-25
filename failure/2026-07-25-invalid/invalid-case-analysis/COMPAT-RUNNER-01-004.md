## 失败分诊 · COMPAT-RUNNER-01-004 · 自定义特征标签不被支持时应给出可用标签列表

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 预期非法 (negative test)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — jobs[test-custom-label].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['codearts-hosted','ubuntu-latest','x64','large']，其中'codearts-hosted'可省略；若为自定义资源池则定义为['self-hosted',{name},{label_1},{label_2},...,{label_n}]，如['self-hosted','my-private-pool','x64','region=cn-north-4']


### 根因初判

**根因**: 需人工判断 — 未分类
**责任人**: 需人工判断

> 此 case 为预期非法测试——YAML 有意包含非法输入，INVALID 是期望结果。平台报错行为符合预期。

### 证据

- **维度**: compatibility | **优先级**: P2 | **触发器**: workflow_dispatch
- **标题**: 自定义特征标签不被支持时应给出可用标签列表
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  test-custom-label:
    name: Test custom feature label
    runs-on: [gpu, nvidia]
    steps:
      - name: Echo hello
        run: |
          echo "hello"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-RUNNER-01-004
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
标题:      自定义特征标签不被支持时应给出可用标签列表
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/runner-images-tools.md`

> 文档描述 runs-on 数组格式，但平台校验器对合法标签组合也拒绝。

### 影响评估

- **阻塞性**: ⚪无影响 — 用例本身有意测试非法输入
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非阻塞：case 本身是 negative test，INVALID 是期望结果

**规避手段**: 无——此为有意测试，平台报错符合预期

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 保持 case 不变，确认平台对非法输入的报错行为符合预期

---
