## 失败分诊 · SEC-PERM-01-002 · permissions 声明 read 时写操作被平台拒绝

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — jobs[perm-write-denied].permissions: unknown property


### 根因初判

**根因**: 平台缺陷 — job 级 permissions 不支持
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: security | **优先级**: P0 | **触发器**: workflow_dispatch
- **标题**: permissions 声明 read 时写操作被平台拒绝
- **断言**: 1 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
jobs:
  perm-write-denied:
    name: Test write denied under read
    runs-on: [dedicate-hosted, x64, large]
    permissions:
      repository: read
    steps:
      - name: Clone repo
        run: |
          git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git repo
      - name: Attempt push
        run: |
          cd repo
          echo test > test.txt
          git add test.txt
          git commit -m test
          git push origin main || echo push denied as expected
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   SEC-PERM-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
标题:      permissions 声明 read 时写操作被平台拒绝
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/security-permissions/token-permissions.md`

> 文档描述了 job 级 permissions 覆盖，但平台尚不支持 job 级 permissions 字段。

### 影响评估

- **阻塞性**: 🔴阻塞 — YAML 无法通过校验，workflow 无法部署运行
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：平台缺陷——job 级 permissions 不支持

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: job 级 permissions 不支持
- 等待平台修复后重新验证

---
