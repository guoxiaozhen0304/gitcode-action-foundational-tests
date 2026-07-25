# 失败分诊 — 2026-07-24-02 COMPAT Cases

**数据源**: `failure/2026-07-24-02/`
**对照文档**: `phase01/inputs/gitcode-spec/`

---

## 失败分诊 · COMPAT-CACHE-01-001 · cache 行为等价性——缓存命中场景

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_logs) — 期望日志含 `CACHE_HIT`，实际 absent（日志显示 `CACHE_MISS`）

**根因初判**: 产品 bug（文档缺口）

**责任人**: 平台方

**证据**:

- **Job 日志全量（关键行）**:
  ```
  ::warning::[cache eventValidation] normalized=manual allowlistMatch=false
  allowlist=[push|pull_request|merge_request]
  ATOMGIT_EVENT_NAME=Manual
  hint: event not in allowlist [push|pull_request|merge_request]
  CACHE_MISS
  ```
  cache 插件在 `workflow_dispatch`（Manual 事件）下**明确拒绝工作**，
  日志显式打印了事件不在 allowlist 中的警告，导致缓存命中失败，输出 `CACHE_MISS`。

- **预期行为**（Phase 01 文本用例，P1，compatibility）:
  该用例测试 GitCode cache 行为等价性——缓存命中场景。在 `workflow_dispatch` 触发下，
  期望缓存正常命中，日志输出 `CACHE_HIT`。

- **实际行为**:
  cache 插件在 `workflow_dispatch` 事件下静默退化——不报 YAML 校验错误，
  但运行时拒绝提供缓存服务，输出 `CACHE_MISS`。用例的 `workflow_dispatch` 触发方式
  是按 `VALIDATION-RULES.md` 规则 8a（非 trigger 测试默认用 `workflow_dispatch`）生成的。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/using-dependency-cache.md`:
  文档描述了 cache 的用法，但**未提及** cache 仅在 `push|pull_request|merge_request`
  事件下可用。`workflow_dispatch` 触发时 cache 静默失败，用户按文档配置 cache 后看不到
  预期加速效果，且无清晰错误提示。

- **失败传导链**: 无上游依赖，单 job 执行。

**置信度**: 高（日志错误信息明确：`event not in allowlist [push|pull_request|merge_request]`）

**影响**:
- **阻塞性**: 🟡 非阻塞 — workflow 本身 COMPLETED，cache miss 只是回退到全量构建
- **静默性**: 🔴 静默错误 — 平台不报 YAML 校验错，运行时仅 warning，cache 静默退化
- **影响面**: 🔴 跨维度 — 所有使用 `workflow_dispatch` 触发的 pipeline 的 cache 都不可用
- **综合**: 静默+跨维度——`workflow_dispatch` 下 cache 静默失效，影响所有手动触发 pipeline 的构建速度
- **是否有规避手段**: 是 — 改用 `push` 触发事件

**建议**:
- 文档补充：`using-dependency-cache.md` 应注明 cache 仅在 `push|pull_request|merge_request` 事件下生效
- 平台侧：可考虑在 `workflow_dispatch` 场景下给 error 而非 warning，或支持此场景的 cache

---

## 失败分诊 · COMPAT-DIR-01-002 · 工作流目录差异——.github/workflows/ 不应被识别

**判定结果**: FAIL
**失败断言**: assertions[1] (negative, run_logs) — 期望日志**不出现** `GITHUB_DIR_WORKFLOW_RAN`，实际 FOUND

**根因初判**: 产品 bug（平台行为与文档不一致）

**责任人**: 平台方

**证据**:

- **Job 日志全量（关键行）**:
  ```
  ::debug::Executing: bash -e /home/slave1/runner/workers/...
  GITHUB_DIR_WORKFLOW_RAN
  ```
  `.github/workflows/` 目录下的 workflow 被平台发现并执行，输出了 `GITHUB_DIR_WORKFLOW_RAN`。

- **预期行为**（Phase 01 文本用例，P1，compatibility）:
  用例期望 GitCode **不应**识别 `.github/workflows/` 目录下的 workflow——
  GitCode 使用 `.gitcode/workflows/` 而非 GitHub 的 `.github/workflows/`。

- **实际行为**:
  平台**同时**识别了 `.github/workflows/` 目录，与 GitCode 文档声明的目录规范矛盾。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/workflow-file-location-structure.md`:
  文档明确声明 workflow 文件应放在 `.gitcode/workflows/` 下（"在仓库的 `.gitcode/workflows/` 目录下"）。
  **未提及** `.github/workflows/` 是否也被识别。平台行为与文档承诺的目录规范不一致——
  若 `.github/workflows/` 也被识别，文档应明确说明兼容性行为。

- **失败传导链**: 无

**置信度**: 高（日志明确显示 `.github` 目录 workflow 被执行）

**影响**:
- **阻塞性**: 🟡 非阻塞 — workflow 仍可正常运行
- **静默性**: 🔴 静默错误 — 用户可能以为只在 `.gitcode/` 放的 workflow 就是唯一版本，实际 `.github/` 也会被执行
- **影响面**: 🟡 同维度 — 影响所有仓库的 workflow 组织策略
- **综合**: 静默+同维度——平台同时识别两种目录但文档只声明一种，用户可能意外触发未预期的 workflow
- **是否有规避手段**: 否 — 平台级行为，用户无法关闭

**建议**:
- 文档补充：明确声明 `.github/workflows/` 是否也被识别及其优先级

---

## 失败分诊 · COMPAT-INPUTS-01-001 · workflow_dispatch inputs 类型限制 - boolean 应报错

**判定结果**: FAIL
**失败断言**: assertions[0] (negative, run_status) — 期望 conclusion != COMPLETED（平台应拒绝），实际 COMPLETED

**根因初判**: 产品 bug（能力边界——平台静默接受了不支持的输入类型）

**责任人**: 平台方

**证据**:

- **Job 日志全量（关键行）**:
  ```
  ::debug::Executing: bash -e /home/slave1/runner/workers/...
  INPUT_OK
  ```
  workflow 以 `COMPLETED` 状态结束，日志输出 `INPUT_OK`——说明
  即便 inputs 使用了 GitHub 的 `type: boolean`，GitCode 也没有拒绝，
  workflow 正常执行完成。

- **预期行为**（Phase 01 文本用例，P1，compatibility）:
  用例期望 GitCode 对不支持的 `type: boolean` input 报错。
  GitCode 的 `workflow_dispatch` inputs 不支持 `type: boolean`（仅支持 `string`/`choice`）。

- **实际行为**:
  平台静默接受了 `type: boolean`，workflow 正常触发并执行完成——
  既不报错也不警告，用户无法知道自己的配置是否有行为偏差。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/running-pipelines/manually-trigger-pipeline.md`:
  文档列出 `inputs` 参数包括 `description`、`required`、`default`、`type`，
  `type` 允许值为 `string`、`choice`、`number`。**未提及** `boolean` 是否被拒绝或静默降级。

- **失败传导链**: 无

**置信度**: 高

**影响**:
- **阻塞性**: ⚪ 无影响 — workflow 正常运行
- **静默性**: 🔴 静默错误 — 平台不报错也不警告，用户以为 `boolean` 有效
- **影响面**: 🟢 单用例 — 仅影响使用 `boolean` input type 的场景
- **综合**: 静默+单用例——平台静默接受不支持的输入类型，用户无从知晓
- **是否有规避手段**: 是 — 用户改用 `type: string` + `default: "true"`

**建议**:
- 平台应校验 `inputs.*.type` 并拒绝不支持的 `boolean` 类型

---

## 失败分诊 · COMPAT-RUNSON-01-002 · runs-on 标签体系——单标签字符串应报错

**判定结果**: FAIL
**失败断言**: assertions[2] (negative, run_logs) — 期望日志**不出现** `RUNSON_STRING_ACCEPTED`，实际 FOUND

**根因初判**: 用例问题（断言逻辑翻转——实际行为与文档一致，平台正确接受单字符串格式）

**责任人**: Phase 01

**证据**:

- **Job 日志全量（关键行）**:
  ```
  ::debug::Executing: bash -e /home/slave1/runner/workers/...
  RUNSON_STRING_ACCEPTED
  ```
  workflow 以 `COMPLETED` 结束，日志输出 `RUNSON_STRING_ACCEPTED`——
  平台**接受**了单字符串 `runs-on: "ubuntu-latest"` 格式。

- **预期行为**（Phase 01 文本用例，P1，compatibility）:
  用例期望 GitCode 拒绝单字符串标签（认为 GitCode 要求三段式数组格式 `['codearts-hosted','os','arch','flavor']`）。

- **实际行为**:
  平台接受单字符串 `runs-on`，workflow 正常执行。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/configure-jobs.md`:
  文档示例 `runs-on: default` 明确展示了单字符串格式是**合法**的。
  `default` 是 GitCode 指定的保留标签名，等价于默认托管 runner。
  测试用例使用的 `"ubuntu-latest"` 可能被平台映射到默认 runner 而非报错。

- **失败传导链**: 无

**置信度**: 中（需确认平台对 `"ubuntu-latest"` 单字符串的实际语义——是映射到默认 runner 还是等同于三段式标签）

**影响**:
- **阻塞性**: ⚪ 无影响 — 平台行为与文档一致，单字符串是合法格式
- **静默性**: ⚪ 无影响 — 文档已确认单字符串合法
- **影响面**: ⚪ 无影响
- **综合**: 用例断言与平台文档承诺相反——文档明确支持单字符串格式，用例期望拒绝
- **是否有规避手段**: — 用例应修正断言逻辑

**建议**:
- 用例断言改为 positive（期望接受单字符串），或删除此用例

---

## 失败分诊 · COMPAT-VARS-01-006 · vars 在 Action 中的可用性差异

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED

**根因初判**: 产品缺陷（能力边界——平台不支持 `vars.*` 上下文）

**责任人**: 平台方

**证据**:

- **Job 日志全量（关键行）**:
  ```
  [ERROR] 描述: 插件执行异常.
  [ERROR] 根因: Input required and not supplied: COMMIT_REF_NAME
  ::error::Input required and not supplied: COMMIT_REF_NAME
  ```
  checkout 步骤失败——`vars.ACTION_VAR` 在 `with:` 中求值为空，
  导致 checkout action 缺少必需的 `COMMIT_REF_NAME` 输入。

- **预期行为**（Phase 01 文本用例，P1，compatibility）:
  用例期望 `vars.*` 上下文在 Action 的 `with:` 中可用，
  与 GitHub Actions 的 `vars` 行为一致。

- **实际行为**:
  `vars.ACTION_VAR` 求值为空，导致 action 执行失败。
  GitCode 平台不支持 `vars.*` 上下文（`VALIDATION-RULES.md` §7 已记录）。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/core-concepts/variables-secrets-context-expressions.md`:
  文档列出了支持的上下文，**未提及** `vars.*`。
  `COMPAT-NOTES.md` 也未记录此差异。

- **失败传导链**: 无（单 job）

**置信度**: 高（`vars.*` 不支持已在 §7 确认，日志验证了求值为空）

**影响**:
- **阻塞性**: 🔴 阻塞 — workflow 无法执行到预期结束
- **静默性**: 🟡 可察觉 — 平台报错但错误信息只提示"Input required"，未说明 `vars.*` 不可用
- **影响面**: 🟡 同维度 — 所有引用 `vars.*` 上下文的 Action `with:` 调用均受影响
- **综合**: 阻塞+可察觉——`vars.*` 不支持导致 workflow 失败，错误归因误导用户
- **是否有规避手段**: 否 — 平台不支持 `vars.*`，无法绕过

**建议**:
- 文档补充 `COMPAT-NOTES.md`：注明 `vars.*` 上下文不支持，与 GitHub Actions 的差异

---

## 汇总

| Case | 根因 | 责任人 | 类型 |
|------|------|--------|------|
| COMPAT-CACHE-01-001 | cache 不允许 workflow_dispatch 事件 | 平台方 | 文档缺口 |
| COMPAT-DIR-01-002 | 平台额外识别 .github/ 目录 | 平台方 | 行为差异 |
| COMPAT-INPUTS-01-001 | 平台静默接受 boolean input | 平台方 | 能力边界 |
| COMPAT-RUNSON-01-002 | 单字符串 runs-on 实际合法 | Phase 01 | 用例问题 |
| COMPAT-VARS-01-006 | vars.* 上下文不支持 | 平台方 | 能力边界 |

---

*分析依据: `phase02/agents/failure-analyst/CLAUDE.md` · 2026-07-24*
