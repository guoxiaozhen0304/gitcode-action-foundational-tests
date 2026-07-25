## 失败分诊 · COMPAT-RUNNER-01-005 · 内网环境 Runner 不支持时的差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — jobs[test-intranet].runs-on: runs-on以数组形式定义时，若为默认资源池则定义为['codearts-hosted',{os},{arch},{flavor}]，如['codearts-hosted','ubuntu-latest','x64','large']，其中'codearts-hosted'可省略；若为自定义资源池则定义为['self-hosted',{name},{label_1},{label_2},...,{label_n}]，如['self-hosted','my-private-pool','x64','region=cn-north-4']


### 根因初判

**根因**: 产品bug — runs-on 数组校验过严
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P2 | **触发器**: workflow_dispatch
- **标题**: 内网环境 Runner 不支持时的差异
- **断言**: 1 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  test-intranet:
    name: Test intranet runner
    runs-on: [intranet, x64]
    steps:
      - name: Echo hello
        run: |
          echo "hello"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-RUNNER-01-005
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
标题:      内网环境 Runner 不支持时的差异
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

**综合**: 非预期拒绝：产品bug——runs-on 数组校验过严

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: runs-on 数组校验过严
- 等待平台修复后重新验证

---
