## 失败分诊 · USE-EXPR-01-003 · expressions 函数表语法标记可解析性与状态关键字术语区分

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档语法标记质量审查 — 对函数表语法列逐行做括号配平、检测多余括号（如 `hashFiles(paths...))`）、区分状态关键字与函数，属于文档解析，非 workflow 执行
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "抽取函数表语法列逐行做括号配平与词法检查；hashFiles(paths...)) 等多余括号行存在即不合格"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为文档语法标记词法扫描，不依赖 gitcode workflow 触发

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过文档解析脚本离线完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此表达式语法标记质量场景
- **综合**: `eval: deterministic` 可通过括号配平扫描实现，但需解析文档中代码块
- **是否有规避手段**: 是 — 可开发文档代码块提取 + 括号配平扫描脚本

**建议**:
- Phase 02 开发文档语法扫描工具：提取函数表 → 括号配平 → 词法检查
- 平台文档系统应内置语法校验 CI
