## 失败分诊 · COMPAT-PATHS-01-001 · paths 过滤器 300 条边界测试

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.push.paths` 包含 300 条路径，平台可能对 paths 数量有限制或在边界行为上有差异
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 22（未知限制 — paths 数量超过平台允许上限）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      push:
        branches: [main]
        paths:                             # 300 条路径条目
          - 'path/001.txt'
          ...
          - 'path/300.txt'
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 6: "`on.push` 不能同时有 `paths` 和 `paths-ignore`"（当前只有 paths，合规）
  - 平台对 paths 数量有未文档化的上限，300 条可能超出限制

**置信度**: 中（paths 300 条边界值可能触发平台数量限制，但规则未明确记录具体上限值）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟡可能静默 — 具体错误信息取决于平台对 paths 数量上限的处理（拒绝 vs 截断）
- **影响面**: 所有 paths 条目过多的 workflow
- **综合**: paths 300 条边界值触发平台拒绝
- **是否有规避手段**: 是 — 减少 paths 条目数量至平台允许范围内（需实测确定上限值）

**建议**:
- 减少 paths 条目数至平台允许范围（如 100 条以内）
- 此用例的目标是测试 300 条边界，被拒绝后记录平台实际限制
- 在 spec-gap 中记录 paths 数量上限值
