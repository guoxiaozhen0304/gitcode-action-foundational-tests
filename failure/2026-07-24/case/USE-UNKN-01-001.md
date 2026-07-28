## 失败分诊 · USE-UNKN-01-001 · 未知字段如 run-name 不应被静默忽略而应给出警告或错误

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 18 — `run-name` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  run-name: Build by ${{ atomgit.actor }}
  name: unknown field test
  on:
    workflow_dispatch:
  jobs: [...]

  # 应改为（删除 run-name）:
  name: unknown field test
  on:
    workflow_dispatch:
  jobs: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 18: "GitCode 平台不支持 `run-name` 字段（GitHub Actions 特性），报 `run-name: unknown property`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有从 GitHub 迁移并使用 `run-name` 的工作流
- **综合**: `run-name` 是 GitHub Actions 特有字段，GitCode Schema 拒绝
- **是否有规避手段**: 是 — 删除 `run-name` 字段

**建议**:
- 删除 `run-name: Build by ${{ atomgit.actor }}` 行；workflow 运行名称通过 `name` 字段设置
