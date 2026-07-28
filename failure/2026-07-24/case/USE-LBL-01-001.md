## 失败分诊 · USE-LBL-01-001 · runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 1 — Runner 标签格式
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  runs-on: [nonexistent-os, x64, small]

  # 应改为（使用平台注册标签）:
  runs-on: [ubuntu-latest, x64, small]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 1: "`runs-on` 中列出的所有标签必须同时存在于 Runner 的标签集合中。" `nonexistent-os` 是不存在的标签，无法匹配任何 Runner，调度阶段报错。

**置信度**: 高（平台 Runner 标签集不含 nonexistent-os，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 Runner 匹配，用例无法调度执行
- **静默性**: 🟢明确报错 — 调度器返回标签不匹配错误
- **影响面**: 所有使用错误标签名的工作流
- **综合**: `nonexistent-os` 不在平台注册标签集中，调度失败
- **是否有规避手段**: 是 — 替换为 `[ubuntu-latest, x64, small]`

**建议**:
- 将 `runs-on` 改为 `[ubuntu-latest, x64, small]`；错误标签提示测试需在平台提供完整标签列表能力后执行
