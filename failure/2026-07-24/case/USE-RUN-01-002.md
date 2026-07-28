## 失败分诊 · USE-RUN-01-002 · 使用单标签 ubuntu-latest 时报错应给出三段式格式指引

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 1 — Runner 标签格式 · 只用数组格式，标签须完整匹配
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  runs-on: [ubuntu-latest]

  # 应改为（三段式标签）:
  runs-on: [ubuntu-latest, x64, small]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 1: "`runs-on` 中列出的所有标签必须同时存在于 Runner 的标签集合中。" GitCode Runner 标签集要求三段式完整描述（OS + 架构 + 规模），仅有 `ubuntu-latest` 无法匹配 `[ubuntu-latest, x64, small]` 等完整标签组合。

**置信度**: 高（平台 Runner 匹配需要完整标签组合，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 Runner 匹配，用例无法调度执行
- **静默性**: 🟢明确报错 — 调度器返回标签不完整或不匹配错误
- **影响面**: 所有使用 GitHub 风格单标签 `runs-on` 的迁移工作流
- **综合**: 单标签 `ubuntu-latest` 不足以匹配平台的三段式 Runner 标签体系
- **是否有规避手段**: 是 — 补充为 `[ubuntu-latest, x64, small]`

**建议**:
- 将 `runs-on: [ubuntu-latest]` 补充为 `runs-on: [ubuntu-latest, x64, small]`
