## 失败分诊 · SEC-PERM-01-002 · permissions 声明 read 时写操作被平台拒绝

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 13 — `permissions` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    perm-write-denied:
      name: Test write denied under read
      runs-on: [ubuntu-latest, x64, small]
      permissions:
        repository: read
      steps: [...]

  # 应改为（删除 permissions 块）:
  jobs:
    perm-write-denied:
      name: Test write denied under read
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 13: "GitCode 平台**完全不支持** `permissions` 字段——无论是 workflow 级还是 job 级。报 `jobs[id].permissions: unknown property`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有需要声明只读权限的 workflow
- **综合**: job 级 `permissions: repository: read` 不被平台支持
- **是否有规避手段**: 是 — 删除 `permissions` 块

**建议**:
- 删除 job 级 `permissions: repository: read`；权限控制通过平台项目设置配置
