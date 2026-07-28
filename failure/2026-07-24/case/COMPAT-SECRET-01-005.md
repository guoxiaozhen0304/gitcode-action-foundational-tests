## 失败分诊 · COMPAT-SECRET-01-005 · 环境级 secrets 不支持时应明确报错而非降级为项目级

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 16 — `environment` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    test-env-secret:
      name: Test environment level secret
      runs-on: [ubuntu-latest, x64, small]
      environment: prod

  # 应改为（删除 environment 块）:
  jobs:
    test-env-secret:
      name: Test environment level secret
      runs-on: [ubuntu-latest, x64, small]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 16: "GitCode 平台不支持 `jobs[id].environment` 字段，报 `jobs[id].environment: unknown property`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有使用环境级 secrets / 环境审批的工作流
- **综合**: `environment` 字段不被平台识别，YAML 校验阶段直接拒绝
- **是否有规避手段**: 是 — 删除 `environment` 字段，环境级 secrets 改为项目级配置

**建议**:
- 删除 `environment: prod` 行；环境级 secret 能力需等待平台支持后重新开放用例
