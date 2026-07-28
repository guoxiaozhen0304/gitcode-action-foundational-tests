## 失败分诊 · COMP-PR-01-004 · pre-merge ref 在 PR 存续期可解析且语义裁定

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'PRE_MERGE_MARKER'，实际 absent
- assertions[1] (positive, run_logs) — 期望 log contains 'REF_CONTENT_DUMPED'，实际 absent

**根因初判**: 产品缺陷 / 环境问题

**责任人**: 平台方 — merge request ref `refs/merge-requests/1/merge` 在 GitCode 平台上不可解析（fatal: couldn't find remote ref）

**证据**:

- **Job 日志关键行**（共 49 行）:
  ```
  行 30: git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --progress --depth=1 origin +refs/merge-requests/1/merge:refs/remotes/merge-requests/1/merge
  行 31: fatal: couldn't find remote ref refs/merge-requests/1/merge
  行 33-36: ERROR ID: CHECKOUT.00010010 — Git命令执行失败
  行 47: ::error::git进行拉取动作失败, 执行git命令失败
  ```
  checkout action 尝试 fetch `refs/merge-requests/1/merge`（MR #1 的合并预览 ref），远程仓库**不存在该 ref**，导致 checkout 失败，workflow FAILED。

- **预期行为**（用例 YAML COMP-PR-01-004，P1，维度 completeness）:
  - 在某 PR #1 存续期内，该 `ref` 应可解析
  - checkout 成功后，仓库工作区应包含文件 `pre_merge_marker.txt`
  - 日志应包含 `PRE_MERGE_MARKER` 和 `REF_CONTENT_DUMPED`

- **实际行为**:
  - Merge request ref 在远程仓库中不存在 → 整个 checkout 步骤失败
  - 被阻断的功能：pre-merge ref 的可解析性、语义裁定、合并内容验证均未进行

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 46 行：`atomgit.head_ref` 说明为 "PR 源分支（仅 PR 事件）"
  - `phase01/inputs/gitcode-spec/security-permissions/pr-mr-pipeline-security.md`（如存在）可能描述 merge request ref 的行为
  - 未在文档中找到对 `refs/merge-requests/*/merge` 格式的明确承诺，这本身可能是一个**文档缺口**

- **Fixture 分析**:
  - 用例 YAML 第 8 行声明 `repo_fixture: pr-merge-ref`，此 fixture 需预设一个活跃的 PR #1
  - 如果 `pr-merge-ref` fixture 未正确创建 PR #1，或 PR #1 已关闭/合并，则 ref 自然不存在
  - 然而，GitCode 平台是否**支持** `refs/merge-requests/*/merge` 这种 ref 格式是关键问题——若不支持，即便有活跃 PR，ref 也不存在

**置信度**: 中 — ref 不存在是确定的，但不清楚是**平台不支持此 ref 格式**还是**fixture 未创建活跃 PR**

**影响**:
- **阻塞性**: 🔴阻塞 — checkout 失败，整个 workflow 无法继续
- **静默性**: 🟡可察觉 — 平台明确报错 `fatal: couldn't find remote ref`
- **影响面**: 🟡同维度 — 若平台不支持此 ref 格式，影响所有依赖 pre-merge ref 的 CI 流程
- **综合**: 阻塞但可察觉，pre-merge ref 不可解析
- **是否有规避手段**: 否 — 无替代机制获取 MR 的合并预览内容

**建议**:
- Phase 02 确认 `pr-merge-ref` fixture 是否创建了活跃的 PR #1
- 平台方确认 GitCode Actions 是否支持 `refs/merge-requests/N/merge` ref 格式（GitHub 在 PR 场景下提供 `refs/pull/N/merge`）
- 若不支持，文档应明确标注，且此用例应归为"平台能力边界（不支持 pre-merge ref）"
- 相关用例: COMP-PR-01-005（同一 ref 格式，同一根因）
