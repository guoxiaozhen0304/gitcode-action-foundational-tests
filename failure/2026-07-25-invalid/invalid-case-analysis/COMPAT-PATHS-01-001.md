## 失败分诊 · COMPAT-PATHS-01-001 · paths 过滤器 300 条边界测试

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L3:C5** — on.push: 列表长度超出限制，paths paths-ignore之和不能小于1或超过32


### 根因初判

**根因**: 平台缺陷 — 列表长度限制未在文档声明
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: push
- **标题**: paths 过滤器 300 条边界测试
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  push:
    branches: [main]
    paths:
      - 'path/001.txt'
      - 'path/002.txt'
      - 'path/003.txt'
      - 'path/004.txt'
      - 'path/005.txt'
      - 'path/006.txt'
      - 'path/007.txt'
      - 'path/008.txt'
      - 'path/009.txt'
      - 'path/010.txt'
      - 'path/011.txt'
      - 'path/012.txt'
      - 'path/013.txt'
      - 'path/014.txt'
      - 'path/015.txt'
      - 'path/016.txt'
      - 'path/017.txt'
      - 'path/018.txt'
      - 'path/019.txt'
      - 'path/020.txt'
      - 'path/021.txt'
... (截断)
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-PATHS-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
标题:      paths 过滤器 300 条边界测试
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/trigger-events.md`

### 影响评估

- **阻塞性**: ⚪无影响 — 用例本身有意测试非法输入
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：平台缺陷——列表长度限制未在文档声明

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: 列表长度限制未在文档声明
- 等待平台修复后重新验证

---
