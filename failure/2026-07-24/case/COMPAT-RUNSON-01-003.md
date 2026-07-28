## 失败分诊 · COMPAT-RUNSON-01-003 · 自托管 runs-on 对象式写法（type/group/labels）的实测仲裁

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 1 — Runner 标签格式 · 只用数组格式，禁止 `{}` 对象格式
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  runs-on: {type: self-hosted, group: default, labels: [linux, x64]}

  # 应改为（数组格式）:
  runs-on: [self-hosted, arch=arm, group=006]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 1: "只用数组格式，禁止 `{}` 对象格式。" `runs-on: {type, group, labels}` 是 GitHub Actions 的 YAML 对象写法，GitCode 平台仅接受数组格式 `[self-hosted, ...]`，对象格式直接报 `unknown property`。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有使用 GitHub 对象式 runs-on 的迁移工作流
- **综合**: `{}` 对象格式不被平台接受，必须改为数组格式
- **是否有规避手段**: 是 — 改为数组格式 `[self-hosted, arch=arm, group=006]`

**建议**:
- 将对象格式改为数组格式 `runs-on: [self-hosted, arch=arm, group=006]`
