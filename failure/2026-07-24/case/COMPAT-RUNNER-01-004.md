## 失败分诊 · COMPAT-RUNNER-01-004 · 自定义特征标签不被支持时应给出可用标签列表

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 1 — Runner 标签格式
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  runs-on: [gpu, nvidia]

  # 应改为（使用平台可识别的标签组合）:
  runs-on: [ubuntu-latest, x64, small]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 1: "`runs-on` 中列出的所有标签必须同时存在于 Runner 的标签集合中。" `gpu`、`nvidia` 均为非平台注册标签，调度器无法匹配任何 Runner，导致 YAML 校验或调度阶段报错。

**置信度**: 高（平台 Runner 标签集不包含 gpu/nvidia，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 Runner 匹配，用例无法调度执行
- **静默性**: 🟢明确报错 — 调度器返回标签不匹配错误
- **影响面**: 所有依赖 GPU/NVIDIA 硬件的 CI 用例
- **综合**: `gpu`、`nvidia` 不在 GitCode Runner 标签集中，无法调度执行
- **是否有规避手段**: 是 — 使用平台注册的标签 `[ubuntu-latest, x64, small]`

**建议**:
- 将 `runs-on` 改为平台注册标签；GPU 相关测试需等待平台新增 GPU 标签后方可执行
