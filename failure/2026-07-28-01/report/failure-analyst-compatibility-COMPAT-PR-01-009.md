## 失败分诊 · COMPAT-PR-01-009 · pull_request 触发时 atomgit.sha/ref 的代码版本语义（对齐 GitHub merge commit 模型）

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'PROBE_DONE'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方 — 平台在 pull_request 事件下上报的 `atomgit.ref = refs/merge-requests/41/merge` 指向一个不存在的 git ref，导致 checkout action 检出失败；此反映出平台 context 上报与底层 git 基础设施之间的断裂

**证据**:

- **Job 日志关键段落**（56 行；Step 1 执行成功，Step 2 检出失败，Step 3 从未执行）:
  ```
  === STEP 1 "Record context sha and ref" ===
  ::debug::Executing: bash -e .../5765526b.sh
  CTX_SHA=9943fa681663653d6f14d3b6e930ec40271b33b0
  CTX_REF=refs/merge-requests/41/merge
  ENV_SHA=9943fa681663653d6f14d3b6e930ec40271b33b0
  ```
  **Step 1 结论**：平台能正确输出 `atomgit.sha` 和 `ATOMGIT_SHA` 的值（均为 `9943fa...`）；`atomgit.ref` 被上报为 `refs/merge-requests/41/merge`——这是 GitLab 风格的 merge request ref 路径

  ```
  === STEP 2 "(TC) checkout source" ===
  ::debug::git fetch origin +refs/merge-requests/41/merge:refs/remotes/merge-requests/41/merge
  fatal: couldn't find remote ref refs/merge-requests/41/merge
  [ERROR] ID: CHECKOUT.00010010 — Git命令执行失败，根因: git进行拉取动作失败
  ::error::git进行拉取动作失败, 执行git命令失败
  ```
  **Step 2 结论**：checkout action 使用 `refs/merge-requests/41/merge` 作为 fetch target，但远程 git 服务器上不存在此 ref → fetch 失败 → checkout 步骤失败 → 步骤退出码 1

  **失败传导链**：Step 1 (Record context) OK → Step 2 (checkout) FAILED → Step 3 (Record checked out commit, verify PROBE_DONE) IGNORED。下游代码版本验证和语义比对的全部逻辑未被测试到。

- **预期行为**（Phase 01 文本用例 COMPAT-PR-01-009，P1，兼容性）:
  - 操作步骤 1: 输出 atomgit.sha、atomgit.ref 及环境变量
  - 操作步骤 2: 检出代码后记录实际检出的提交 SHA
  - 操作步骤 3: 将观测值与已知 PR head/base/试合并 sha 比对定位语义
  - 预期结果: atomgit.sha/ref 的确切语义得到确定结论；checkout 检出的代码版本与 atomgit.sha 一致
  - 验证点: [负向] 不应出现 checkout 检出版本与 atomgit.sha 指向版本不一致

- **实际行为**:
  - `atomgit.sha` 能够正确输出（`9943fa...`）
  - `atomgit.ref` 上报为 `refs/merge-requests/41/merge`——此 ref 在远程 git 服务器上不存在
  - checkout action 因 ref 不存在而失败，无法验证 checkout 检出代码与 atomgit.sha 的一致性
  - **核心断裂**：平台 context 层告知 Runner "ref 是 refs/merge-requests/41/merge"，但底层 git 服务器不提供此 ref 的访问

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 31 行：`atomgit.ref` 定义为 "触发引用（分支或标签全名，如 `refs/heads/main`）"——文档仅给出分支和标签示例，未明确 `pull_request` 事件下的 ref 格式
  - `phase01/inputs/gitcode-spec/security-permissions/pr-mr-pipeline-security.md` 第 14-16 行：提到 pull_request 事件下 "checkout默认代码来源 = PR预合并分支"——说明平台**预期**提供 PR 的预合并分支引用
  - `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 45-47 行：Pull Request 事件上下文字段包括 `atomgit.event.pull_request.head.ref`（源分支名）和 `atomgit.event.pull_request.head.sha`（源分支最新 SHA）——说明平台具备感知 PR head 信息的能力
  - 测试 YAML 的 Step 1 已验证 `atomgit.event` 能传输 PR 信息（CTX_REF 存在），但 `refs/merge-requests/41/merge` 格式的 ref 在 git 层面不可达——这是 context 值与 git 基础设施的不一致

**置信度**: 高（日志第一段 Step 1 明确输出 ref 值，第二段 checkout fetch 明确报 ref 不存在；交叉验证确认 git 服务器不提供 `refs/merge-requests/*` 路径的访问）

**影响**:
- **阻塞性**: 🔴 阻塞 — 任何使用 `checkout` action 的 `pull_request` 触发 workflow 均会因 ref 不存在而检出失败，CI pipeline 无法运行到代码检查/构建步骤
- **静默性**: 🟡 可察觉 — git fetch 错误信息可见，用户能发现 checkout 失败，但错误诊断信息（"couldn't find remote ref"）直接暴露了平台 ref 构造与 git 基础层的不一致
- **影响面**: 🔴 跨维度 — 所有 `pull_request` 触发的 workflow 若使用 checkout（默认行为），均无法成功检出代码；这影响所有 PR CI pipeline 的执行基线
- **综合**: 阻塞+跨维度——`atomgit.ref` 在 pull_request 事件下指向不存在的 git ref，checkout 必然失败，PR CI 流水线全线断裂；这是 context 层与 git 基础设施之间的一次级联断裂
- **是否有规避手段**: 否——用户无法改变平台上报的 `atomgit.ref` 值，也无法让 checkout action 跳过 fetch 目标 ref 的步骤

**建议**:
- 平台需统一 `atomgit.ref` 在 pull_request 事件下的语义：若要以 merge ref 形式提供，git 服务器必须实际创建并暴露该 ref；否则应回退为 PR head sha/branch ref 形式
- Context 文档应补全 pull_request 事件下 `atomgit.ref` 和 `atomgit.sha` 的确切含义和取值规则
- 相关用例: COMPAT-PR 系列所有依赖 checkout 的 pull_request 触发用例
