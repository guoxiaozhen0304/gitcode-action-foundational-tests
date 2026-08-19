# Usability Intents · Run 2026-08-18-01

> Agent: usability agent（易用性 Agent）
> 维度标签: `usability`
> 输入版本: gitcode-spec/ 2026-08-18; risk-register.md 2026-08-18; parity-matrix.md 2026-08-18; case-base-detail.md 2026-07-20

---

## 缺失输入清单及退化影响

| 缺失输入 | 期望内容 | 退化影响 |
|---|---|---|
| `phase01/inputs/business-context/` | 迁移规模、改造点清单、已知摩擦记录 | 无法基于真实迁移项目体量估算摩擦高发路径；intent 场景偏向「通用语法迁移」而非「某业务线改造痛点」 |
| `phase01/inputs/workflow-samples/` | 真实 GitHub workflow 样本作迁移素材 | 无法引用具体业务 workflow 逐段对标；intent 以「假设性迁移」为主，缺少真实 YAML 断点 |

> 退化应对：以 `COMPAT-NOTES.md` 已识别的差异点为迁移场景骨架，以 `case-base-detail.md` 中 25 类已知 bug 为文档-行为不一致的实证来源，补全场景。

---

## Intent 列表

### INTENT-USE-001 — 迁移报错应指明路径差异（`.github/workflows/` → `.gitcode/workflows/`）

- **场景**：从 GitHub 迁移的开发者直接复制 workflow 文件到 `.github/workflows/`，提交后流水线未触发或报文件找不到。
- **用户视角**：用户不知道 GitCode 的 workflow 目录名不同，以为「文件明明在了为什么不跑」。
- **可理解性判据**：
  - 错误信息（或 UI 提示）必须同时包含：
    1. 未识别的路径 `.github/workflows/`（指出哪里错）；
    2. GitCode 的正确路径 `.gitcode/workflows/`（指出怎么改）；
    3. 平台名称 "AtomGit" 或 "GitCode"（让用户知道这是平台差异而非自己写错）。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §1 — 工作流目录差异。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-002 — 迁移报错应指明上下文命名差异（`github.*` → `atomgit.*`）

- **场景**：迁移的 workflow 中保留了 `${{ github.event_name }}`、`${{ github.sha }}` 等 GitHub 上下文引用，解析或运行时失败。
- **用户视角**：用户照抄 GitHub 文档里的表达式，报错信息若只说「未知上下文」则无法定位。
- **可理解性判据**：
  - 错误信息必须同时包含：
    1. 被识别为无效的上下文前缀 `github.`；
    2. 建议的替换前缀 `atomgit.`；
    3. 示例片段（如将 `${{ github.sha }}` 改为 `${{ atomgit.sha }}`）。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §2 — 上下文对象命名差异。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-003 — 迁移报错应指明令牌名称差异（`GITHUB_TOKEN` → `ATOMGIT_TOKEN`）

- **场景**：workflow 中引用 `$GITHUB_TOKEN`、`${{ secrets.GITHUB_TOKEN }}` 或 `github.token`。
- **用户视角**：CI 日志里出现空值或鉴权失败，用户不知道是令牌名变了。
- **可理解性判据**：
  - 当日志中出现 `GITHUB_TOKEN` 被引用但环境变量/secret 不存在时，平台应在日志或注解中输出提示，包含：
    1. `GITHUB_TOKEN` 不是本平台的系统变量名；
    2. 应使用 `ATOMGIT_TOKEN` / `secrets.ATOMGIT_TOKEN`；
    3. （可选）指向 secrets 配置页面的链接。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §2 — 系统环境变量前缀差异。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-004 — `runner.os` 文档值与实际返回值不一致的开发者困惑

- **场景**：文档声明 `runner.os` 返回 `"Linux"`，但实际返回 `"linux"`（case-base-detail.md 已知 bug TC-023/094）。用户按文档写 `if: ${{ runner.os == 'Linux' }}` 导致条件永远为假。
- **用户视角**：这不是「报错」，而是「静默不对」——最劝退的一类问题。用户无法区分是自己逻辑写错还是平台 bug。
- **可理解性判据**：
  - 下列至少满足其一即算通过：
    1. 平台修复后 `runner.os` 返回值与文档一致（`Linux` / `Windows` / `macOS`）；
    2. 或平台在检测到条件表达式中使用了文档值但运行时值为小写时，在日志中发出 warning，提示「实际返回值为小写，建议统一使用小写比较」。
  - 若均不满足，记为缺陷：文档与实现不一致且无提示。
- **是否需 llm_assisted**: 否（API/日志文本匹配可判定）。
- **关联的兼容性差异**: case-base-detail.md NEEDS-UPDATE — Runner Context Bugs（10 项）。
- **溯源风险**: RISK-USE-02
- **优先级**: P0
- **dimensions**: [usability]

---

### INTENT-USE-005 — `vars` 上下文文档声明与平台实际不支持的落差

- **场景**：文档 `context.md` 中声明 `vars` 上下文在 workflow/job/step/if/action 全部可用，但 case-base-detail.md 中 TC-005~007、TC-115~119 全部因 "vars context unsupported" 被标为 DEPRECATE/D 测不动。
- **用户视角**：开发者按文档使用 `${{ vars.DEPLOY_ENV }}` 却得到空字符串，无法判断是变量未配置还是平台根本不支持。
- **可理解性判据**：
  - 下列至少满足其一：
    1. 当 workflow 引用 `vars.*` 但平台不支持时，解析报错信息明确说 `vars context is not supported in this platform version`；
    2. 或官方文档移除/标注 `vars` 为「暂不支持」，并与实现保持一致。
  - 若引用 `vars.*` 时静默为空且无文档说明，记为缺陷。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: Parity Matrix 中 `vars` 能力项标记与实际平台行为矛盾。
- **溯源风险**: RISK-USE-02
- **优先级**: P0
- **dimensions**: [usability]

---

### INTENT-USE-006 — YAML 静态校验报错应给出精确字段路径与有效值

- **场景**：迁移过来的 workflow 使用了 GitHub 风格字段（如 `permissions: contents: read`、`runs-on: ubuntu-latest` 单字符串无效场景、或非法 `permissions` 值）。
- **用户视角**：泛化的 "YAML parse error" 让开发者逐行猜哪里不兼容。
- **可理解性判据**：
  - 错误信息（API 返回体或 UI 提示）必须包含：
    1. 精确字段路径，如 `jobs.build.permissions.contents` 或 `jobs.deploy.runs-on`；
    2. 用户提供的值（如 `contents`）；
    3. 该平台允许的值列表或格式说明（如 `"有效权限项: project, pr, issue, note, repository, hook"` 或 `"runs-on 应为三段式 {os,arch,flavor} 或 default"`）。
- **是否需 llm_assisted**: 否（结构化响应可断言）。
- **关联的兼容性差异**: COMPAT-NOTES §6（permissions 命名）、§7（runner 标签）。
- **溯源风险**: RISK-USE-03
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-007 — `workflow_dispatch` 缺少必填参数时 API 报错应指明参数名与来源

- **场景**：通过 API 触发 workflow_dispatch 时漏传了 required input，或在 UI 手动触发时未填写。
- **用户视角**：只收到 "Bad Request" 或 "触发失败"，不知道缺了哪个字段。
- **可理解性判据**：
  - HTTP 400 响应体（或 UI 弹窗）必须包含：
    1. 缺失的参数名（如 `environment`）；
    2. 该参数是 `required`；
    3. 触发方式说明（如 "请在弹窗中填写" 或 "请在请求体中提供 `inputs.environment`"）。
- **是否需 llm_assisted**: 否（结构化响应可断言）。
- **关联的兼容性差异**: COMPAT-NOTES §9 — inputs 仅支持 string 类型（若报错同时提及类型限制则更佳）。
- **溯源风险**: RISK-USE-03
- **优先级**: P2
- **dimensions**: [usability]

---

### INTENT-USE-008 — MR 触发 CI 失败后通知的时效性与信息完整性

- **场景**：开发者提交 MR 后 CI 构建失败，等待通知以便及时修复。
- **用户视角**：通知延迟或内容不完整（缺少仓库名、MR 标题、失败状态）会导致漏看或点进去找不到对应 MR。
- **可理解性判据**：
  - 通知 API 响应或邮件/站内信必须同时满足：
    1. `subject.type` 为 `PullRequest`；
    2. `reason` 为 `state_change`（或 `mention` 若用户被指派）；
    3. `subject.title` 非空且与 MR 标题一致；
    4. `updated_at` 与 CI 终态时间差 <= 5 分钟；
    5. 通知正文/摘要中包含 CI 状态关键词（如 "失败" / "failed" / "未通过"）。
- **是否需 llm_assisted**: 否（API 字段+时间阈值可判定）。
- **关联的兼容性差异**: 无。
- **溯源风险**: RISK-USE-04
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-009 — 制品库版本冲突报错应包含包名、版本号与操作指引

- **场景**：开发者发布包时版本号已存在，收到 409 或类似错误。
- **用户视角**：泛化的 "conflict" 或 "already exists" 让人不确定是自己版本号写错还是网络重试导致。
- **可理解性判据**：
  - 错误响应体必须包含：
    1. 包名称（如 `@scope/pkg-name`）；
    2. 冲突的版本号（如 `1.2.3`）；
    3. 原因短语（如 "version already exists" / "版本已存在"）；
    4. 可操作提示（如 "请升级版本号后重试" 或 "如需覆盖请先删除旧版本"）。
- **是否需 llm_assisted**: 否（结构化响应可断言）。
- **关联的兼容性差异**: 无。
- **溯源风险**: RISK-USE-05
- **优先级**: P2
- **dimensions**: [usability]

---

### INTENT-USE-010 — 废弃 workflow 命令（`::set-output`/`::set-env`/`::add-path`）日志应给出带行号的替换指引

- **场景**：迁移的老项目 workflow 中仍使用 GitHub 旧版命令格式，Runner 执行时仅静默忽略或输出不明所以的 warn。
- **用户视角**：用户不知道这些命令已被废弃，看到 "set-output" 没生效以为是权限问题。
- **可理解性判据**：
  - 日志中对应行必须同时包含：
    1. 关键词 "deprecated" / "已废弃" / "不再支持"；
    2. 发生该命令的源文件行号或 step 名（如 `step "Set output"`）；
    3. 替换命令的完整写法（如 `echo "name=value" >> "$ATOMGIT_OUTPUT"`）。
- **是否需 llm_assisted**: 否（日志文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §11 — 废弃命令与替代方案。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-011 — Secret 掩码被绕过时日志应发出暴露预警

- **场景**：文档 `using-secrets.md` 自承 `echo "${{ secrets.X }}"` 可能绕过脱敏。开发者在不知情下写出此类脚本。
- **用户视角**：用户以为 secrets 一定被星号掩盖，实际上可能完整出现在日志里，且自己不会主动检查每一行日志。
- **可理解性判据**：
  - 当平台检测到 secret 值以明文形式出现在日志中时，必须在运行结果页生成一条 **warning 注解（annotation）**，包含：
    1. "secret value may be exposed" / "密钥可能已暴露"；
    2. 暴露发生的 step 名称；
    3. 建议操作（如 "避免在 run 脚本中直接 echo secret"）。
  - 仅依赖日志中的 `***` 替换不算通过；必须有主动预警。
- **是否需 llm_assisted**: 是（需要判断 annotation 的语义是否构成「预警」而非普通信息）。
- **关联的兼容性差异**: Parity Matrix `secrets` 日志脱敏项标记为 🟡（文档自承可绕过）。
- **溯源风险**: RISK-USE-01（迁移安全习惯差异）
- **优先级**: P1
- **dimensions**: [usability, security]

---

### INTENT-USE-012 — `stages` 与 `jobs` 混用报错应解释 GitCode 特有的阶段机制

- **场景**：GitHub 迁移者习惯顶层写 `jobs:`，看到 GitCode 文档有 `stages` 但不理解两者关系，写出 `jobs` 与 `stages` 嵌套错误的 YAML。
- **用户视角**：报错如果只写 "invalid structure"，用户不知道 GitCode 的阶段概念与 GitHub 不同。
- **可理解性判据**：
  - 错误信息必须包含：
    1. 指出 `stages` 是 AtomGit 特有的编排机制；
    2. 说明 `jobs` 在含 `stages` 时应嵌套在 stage 内；
    3. 给出一个最小正确示例（或指向 `workflow-file-location-structure.md` 的链接）。
- **是否需 llm_assisted**: 是（需要判断错误解释是否足够让 GitHub 用户理解差异）。
- **关联的兼容性差异**: COMPAT-NOTES §4 — stages / post 为 GitCode 特有。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-013 — `workflow_dispatch` / `workflow_call` 非 string 输入类型迁移报错应说明平台限制

- **场景**：GitHub workflow 定义了 `boolean`、`choice`、`number` 类型输入，直接迁移到 GitCode。
- **用户视角**：GitHub 支持多类型输入，GitCode 仅支持 string。若报错只说 "invalid type"，用户不知道是平台缩减了能力。
- **可理解性判据**：
  - 校验错误必须同时包含：
    1. 受影响的 input 名称（如 `perform_deploy`）；
    2. 用户声明的不支持的类型（如 `boolean`）；
    3. 明确说明 "GitCode 当前仅支持 `string` 类型"（或 "AtomGit only supports string type for inputs"）；
    4. 建议的改写方式（如 "请将 boolean 改为 string，并在步骤内自行转换"）。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §9 — inputs 类型限制。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-014 — `permissions` 使用 GitHub 命名时报错应列出 GitCode 权限域映射

- **场景**：迁移 workflow 中写 `permissions: contents: read`、`pull-requests: write` 等 GitHub 风格权限。
- **用户视角**：用户不知道 GitCode 权限域完全不同，若报错只写 "unknown permission" 则需要翻文档猜映射。
- **可理解性判据**：
  - 错误信息必须同时包含：
    1. 不被识别的 GitHub 权限名（如 `contents`、`pull-requests`）；
    2. GitCode 对应的有效权限名列表（`project`、`pr`、`issue`、`note`、`repository`、`hook`）；
    3. 常用映射速查（如 `contents → repository`、`pull-requests → pr`、`issues → issue`）。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §6 — permissions 权限域命名差异。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-015 — `runs-on` 标签不匹配时报错应给出三段式格式示例

- **场景**：用户写 `runs-on: ubuntu-latest`（单字符串）或 `runs-on: [self-hosted, linux, gpu]`（含不存在标签），Job 无法调度。
- **用户视角**：GitHub 用单标签即可，GitCode 需要三段式。报错如果只写 "no runner available"，用户不知道是写法问题还是资源池问题。
- **可理解性判据**：
  - 错误信息（或 job 卡片上的提示）必须包含：
    1. 无法匹配的标签值（如 `gpu` 或 `ubuntu-latest` 单字符串）；
    2. 有效的标签格式示例（如 `{ubuntu-24,x64,small}` 或 `default`）；
    3. 指向 runner 标签文档的链接或可用标签查询方式。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §7 — Runner 标签体系差异。
- **溯源风险**: RISK-USE-01
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-016 — 工作流命令 `::error::` / `::warning::` 注解在 UI 中的可读性与定位能力

- **场景**：Step 脚本输出 `::error file=src/app.py,line=42,col=5::Missing type annotation`，开发者需要在运行结果页快速定位到代码问题。
- **用户视角**：如果注解只显示纯文本消息而没有文件/行号链接，开发者需要手动在仓库里搜索，调试效率低。
- **可理解性判据**：
  - 运行结果页的 annotation 列表必须同时包含：
    1. 消息正文（`Missing type annotation`）；
    2. 文件路径（`src/app.py`）；
    3. 行号（`42`）；
    4. severity 级别（`error` 或 `warning`）。
  - 额外加分项（非硬性）：文件路径可点击跳转对应仓库文件行号（若 UI 已实现）。
- **是否需 llm_assisted**: 是（需要判断 UI 呈现的 annotation 是否「足够 readable」以及链接是否可点，需视觉/语义评判）。
- **关联的兼容性差异**: 无。
- **溯源风险**: RISK-USE-01（调试体验）
- **优先级**: P1
- **dimensions**: [usability]

---

### INTENT-USE-017 — 官方文档中残留 GitHub 措辞的自洽性

- **场景**：`runtime-environment-variables.md` 在描述 Action 路径时使用了 `GITHUB_ACTION_PATH`，而 GitCode 实际应使用 `ATOMGIT_ACTION_PATH`（COMPAT-NOTES §2 已标注）。
- **用户视角**：开发者读文档配置环境变量时，若文档混用两套命名，会产生困惑并写错 workflow。
- **可理解性判据**：
  - 在 `runtime-environment-variables.md` 及所有 `gitcode-spec/` 下的官方文档中：
    1. 凡描述 GitCode 平台特有变量时，不得出现 `GITHUB_` 前缀（`GITHUB_ACTION_PATH`、`GITHUB_ACTIONS` 等）作为「当前平台变量名」；
    2. 若必须提及 GitHub 作对照，应明确标注「GitHub 侧为 GITHUB_*，GitCode 侧为 ATOMGIT_*」；
    3. 出现 `GITHUB_*` 作为「当前平台变量」的每一处均记为缺陷。
- **是否需 llm_assisted**: 否（文本搜索可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §2 — 系统环境变量前缀差异。
- **溯源风险**: RISK-USE-02
- **优先级**: P0
- **dimensions**: [usability]

---

### INTENT-USE-018 — `workflow_call` 嵌套超过 2 层时的报错应给出深度与调用链

- **场景**：复用工作流嵌套过深（A calls B calls C calls D），超过 GitCode 最大 2 层限制。
- **用户视角**：复杂的 GitHub 企业级 workflow 常有深层嵌套；报错若只说 "nested too deep"，用户不知道当前是第几层、哪个文件触发了限制。
- **可理解性判据**：
  - 错误信息必须包含：
    1. 当前嵌套深度（如 `current depth: 3`）；
    2. 最大允许深度（`max depth: 2`）；
    3. 触发超限的 workflow 文件路径（如 `.gitcode/workflows/deploy.yml`）；
    4. 调用链简图（如 `ci.yml → build.yml → deploy.yml`）或文字描述。
- **是否需 llm_assisted**: 否（文本匹配可判定）。
- **关联的兼容性差异**: COMPAT-NOTES §5 — workflow_call 嵌套最多 2 层。
- **溯源风险**: RISK-USE-01
- **优先级**: P2
- **dimensions**: [usability]

---

## 覆盖度速查

| 风险项 | 覆盖 Intent |
|---|---|
| RISK-USE-01 迁移报错不指明 GitCode 差异 | USE-001, USE-002, USE-003, USE-010, USE-012, USE-013, USE-014, USE-015, USE-018 |
| RISK-USE-02 官方文档承诺与实现不一致 | USE-004, USE-005, USE-017 |
| RISK-USE-03 API 错误信息不返回具体字段或业务语义 | USE-006, USE-007 |
| RISK-USE-04 MR/Issue 缺少通知或延迟 | USE-008 |
| RISK-USE-05 Package 版本冲突提示不清晰 | USE-009 |

- **总 intent 数**: 18
- **需 llm_assisted**: USE-011, USE-012, USE-016（3 条）
- **跨维度**: USE-011 [usability, security]
- **P0**: USE-004, USE-005, USE-017（3 条）
- **P1**: USE-001~003, USE-006, USE-008, USE-010~016（13 条）
- **P2**: USE-007, USE-009, USE-018（3 条）
