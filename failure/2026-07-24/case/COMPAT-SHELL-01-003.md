## 失败分诊 · COMPAT-SHELL-01-003 · Windows runner 默认 shell 差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 1 — Runner 标签格式
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  runs-on: [windows-latest, x64, small]

  # 应改为（使用平台支持的 OS 标签）:
  runs-on: [ubuntu-latest, x64, small]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 1: "`runs-on` 中列出的所有标签必须同时存在于 Runner 的标签集合中。" `windows-latest` 不在 GitCode Runner 标签集中，调度器无法匹配 Runner。

**置信度**: 高（平台 Runner 标签集不包含 windows-latest，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 Runner 匹配，用例无法调度执行
- **静默性**: 🟢明确报错 — 调度器返回标签不匹配错误
- **影响面**: 所有期望在 Windows 环境测试 shell 行为的用例
- **综合**: GitCode 无 Windows Runner，`windows-latest` 标签无法调度
- **是否有规避手段**: 否 — 无法在不存在 Windows Runner 的平台上测试 Windows shell 行为

**建议**:
- 将 `runs-on` 改为 `[ubuntu-latest, x64, small]`；Windows shell 差异测试需等待平台支持 Windows Runner
