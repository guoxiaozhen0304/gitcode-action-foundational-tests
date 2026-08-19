# 全平台测试意图（Test Intents）— Spec Analyst 产出

> Run ID: `2026-08-18-01`  
> 产出 Agent: spec-analyst  
> 覆盖范围: Actions + API + Git Repository + MR + Issues + Packages + 用户与权限 + Webhooks & 集成  
> 依据输入: `phase01/inputs/gitcode-spec/*.md`、`phase01/inputs/gitcode-api/*`、`phase01/baseline/parity-matrix.md`、`phase01/baseline/risk-register.md`

---

## 缺失输入清单

| 缺失目录/文件 | 影响范围 | 处理方式 |
|---|---|---|
| `phase01/inputs/platform-config/` | 配额/容量/边界值参数（runner 资源上限、artifact 大小上限、cache 容量、并发上限、请求速率限制阈值） | 涉及此类参数的 intent 标注「缺 platform-config，参数待补」 |
| `phase01/inputs/github-reference/` | GitHub 官方语义对照 | 兼容性 intent 的 oracle 以 `COMPAT-NOTES.md` 与 Parity Matrix 为准，不做额外 GitHub 对照假设 |

---

## 一、CI/CD — Actions（9 条）

### INTENT-COMP-001
- **维度标签**: `[completeness, compatibility]`
- **能力项**: 工作流文件目录 `.gitcode/workflows/`
- **预期系统行为**: 系统仅识别 `.gitcode/workflows/` 目录下的 `.yml`/`.yaml` 工作流文件；`.github/workflows/` 不被识别。文档明确此差异，迁移场景需验证报错或静默忽略行为。
- **风险/验证理由**: 迁移摩擦高发区（RISK-USE-01 / RISK-COMPAT-01）。若 `.github/workflows/` 被静默忽略，用户从 GitHub 迁移后 workflow 不触发且无明确提示，导致开箱失败。
- **优先级**: P1
- **出处**: `workflow-file-location-structure.md`、Parity Matrix

### INTENT-SEC-001
- **维度标签**: `[security]`
- **能力项**: fork PR 的 secret 隔离（`pull_request` 事件）
- **预期系统行为**: 来自 fork 的 PR 触发 `pull_request` 事件时，job 运行上下文中 `secrets.*` 不可访问（值为空或访问报错），`ATOMGIT_TOKEN` 权限为只读；job 日志中不得出现任何 secret 值。
- **风险/验证理由**: RISK-SEC-01（blocker）。fork PR 读到仓库 secrets 是 Actions 最高频攻击面，必须逐条实测隔离强度。
- **优先级**: P0
- **出处**: `pr-mr-pipeline-security.md`、`using-secrets.md`

### INTENT-SEC-003
- **维度标签**: `[security]`
- **能力项**: `pull_request_target` checkout 不可信代码风险
- **预期系统行为**: `pull_request_target` 事件下 workflow 使用目标分支版本，ATOMGIT_TOKEN 拥有声明权限且可访问 secrets；若 checkout 了 `atomgit.event.pull_request.head.sha` 并执行其中脚本，系统应不自动阻断，但文档需明确警示此模式风险。
- **风险/验证理由**: RISK-SEC-03（blocker）。高权限上下文运行不可信代码是典型注入面，需验证系统是否提供额外防护（如环境审批、敏感操作二次确认）。
- **优先级**: P0
- **出处**: `pr-mr-pipeline-security.md`

### INTENT-SEC-002
- **维度标签**: `[security]`
- **能力项**: 不可信输入导致的脚本注入
- **预期系统行为**: PR 标题、分支名、issue 评论等不可信输入被直接拼接进 `run:` 脚本时，系统不应自动转义或阻断；但 secret 值出现在日志输出时应被 `***` 遮蔽（含 `${{ secrets.X }}` 展开值）。
- **风险/验证理由**: RISK-SEC-02（blocker）。业界最常见 Actions 漏洞类；同时 `using-secrets.md` 自承 `echo "${{ secrets.X }}"` 可能绕过脱敏，需实测验证。
- **优先级**: P0
- **出处**: `using-secrets.md`、`variables-secrets-context-expressions.md`

### INTENT-SEC-004
- **维度标签**: `[security]`
- **能力项**: cache 跨 fork/跨分支隔离
- **预期系统行为**: fork PR 运行产生的 cache 不得污染主仓库的 cache key 命名空间；主仓库 cache 在 fork PR 上下文中不可读（或按文档策略隔离）。
- **风险/验证理由**: RISK-SEC-04。cache 投毒是供应链攻击模式，文档未明确 cache 隔离策略（Parity Matrix 标记 ❓），必须实测。
- **优先级**: P1
- **出处**: `core-concepts/artifacts-and-cache.md`、Parity Matrix

### INTENT-COMPAT-001
- **维度标签**: `[compatibility, usability]`
- **能力项**: 上下文对象与变量命名差异（`atomgit.*` / `ATOMGIT_*`）
- **预期系统行为**: `atomgit.ref`、`atomgit.sha`、`atomgit.event_name` 等上下文对象可用；`GITHUB_*` 系列环境变量不可用；系统报错不指明「这是 GitCode 与 GitHub 的差异」。
- **风险/验证理由**: RISK-COMPAT-01 / RISK-USE-01。直接迁移的 GitHub workflow 因上下文对象不兼容会全线失效，报错质量决定迁移摩擦大小。
- **优先级**: P1
- **出处**: `COMPAT-NOTES.md`、`syntax-reference/context.md`

### INTENT-COMP-002
- **维度标签**: `[completeness]`
- **能力项**: 未知/不支持字段的处理方式
- **预期系统行为**: workflow YAML 中包含文档未声明的字段时，系统行为应为「报错并指明不支持的字段」或「静默忽略」；文档需明确降级策略。
- **风险/验证理由**: RISK-COMP-02。Parity Matrix 标记 ❓，默认值/降级方式是兼容性差异高发区，不明确会导致迁移后行为静默不同。
- **优先级**: P1
- **出处**: Parity Matrix、多处缺失

### INTENT-REL-001
- **维度标签**: `[reliability]`
- **能力项**: 并发控制 `concurrency.max`（1–5）+ QUEUE/IGNORE 策略
- **预期系统行为**: 同一 concurrency group 内同时运行的 run 数不超过声明上限；超限时按策略排队或忽略；并发洪泛时系统不崩溃、不丢事件。
- **风险/验证理由**: RISK-REL-01。缺 platform-config，参数待补（具体 max 上限、队列深度、公平性策略未公开）。
- **优先级**: P1
- **出处**: `workflow-file-location-structure.md`、Parity Matrix

### INTENT-COMP-003
- **维度标签**: `[completeness, compatibility]`
- **能力项**: `workflow_dispatch`/`workflow_call` 的 `inputs` 类型限制
- **预期系统行为**: `inputs` 仅支持 `string` 类型；传入非 string 类型（如 boolean/choice/number）时解析应报错或按字符串降级处理。
- **风险/验证理由**: RISK-COMPAT-01 / RISK-USE-01。GitHub 支持 boolean/choice/number/environment，迁移时类型不兼容会导致参数语义变更。
- **优先级**: P1
- **出处**: `COMPAT-NOTES.md`、`trigger-events.md`

---

## 二、代码托管 — Git Repository（5 条）

### INTENT-GIT-001
- **维度标签**: `[completeness, security]`
- **能力项**: Git Clone（HTTPS/SSH）与 PAT 鉴权
- **预期系统行为**: 公开仓库支持匿名 clone；私有仓库支持 HTTPS PAT 鉴权（`oauth2:<token>` 格式）与 SSH 密钥鉴权；非法凭据返回 401/403，不泄露仓库存在性信息。
- **风险/验证理由**: RISK-COMP-01。核心 API/协议可用性是平台根基；PAT 泄露风险（RISK-SEC-05）与鉴权失败信息泄露需一并验证。
- **优先级**: P0
- **出处**: `repository-spec.md`、`user-org-spec.md`

### INTENT-GIT-002
- **维度标签**: `[completeness, security]`
- **能力项**: 保护分支规则强制生效
- **预期系统行为**: 配置 `force_push: false`、`require_ci_pass: true`、`require_review_count: 1` 后，低权限角色（Developer）向受保护分支强制推送应被拒绝；CI 未通过或评审不足时合并应被阻止。
- **风险/验证理由**: RISK-SEC-06。权限越界是 blocker 级风险；保护分支是防止代码污染的最后防线。
- **优先级**: P0
- **出处**: `repository-spec.md` §1.2、§2.3

### INTENT-GIT-003
- **维度标签**: `[completeness, reliability]`
- **能力项**: 大文件存储（LFS）协议支持
- **预期系统行为**: Git LFS 追踪文件可通过标准 Git LFS 客户端上传/下载；API 端点 `/api/v5/repos/{owner}/{repo}/lfs/objects` 可创建/获取 LFS 对象；大文件（缺 platform-config，参数待补：具体上限未知）上传不中断、不内存溢出。
- **风险/验证理由**: RISK-REL-05。大文件克隆/推送超时或内存溢出是稳定性风险；LFS 协议支持缺失会导致特定仓库无法迁移。
- **优先级**: P1
- **出处**: `repository-spec.md` §2.6

### INTENT-GIT-004
- **维度标签**: `[completeness, compatibility]`
- **能力项**: 分支/标签创建与删除
- **预期系统行为**: 通过 API 可创建分支（基于 ref）、删除分支；可创建/删除 Release 与标签；删除已保护分支应被拒绝。
- **风险/验证理由**: RISK-COMP-01。核心 API 缺失会导致自动化工具链断裂；Parity Matrix 标记 ❓，需验证可用性。
- **优先级**: P1
- **出处**: `repository-spec.md` §2.2、§2.5

### INTENT-GIT-005
- **维度标签**: `[completeness]`
- **能力项**: 空仓库/空数据场景 API 行为
- **预期系统行为**: 无分支、无提交、无 issue、无 MR 的仓库，调用列表类 API 应返回空数组（`[]`）而非 500/404；状态码与响应体结构应与有数据场景一致。
- **风险/验证理由**: RISK-COMP-03。空数据场景 API 行为异常是常见边界缺陷，影响 CI 模板与自动化工具的健壮性。
- **优先级**: P1
- **出处**: `repository-spec.md`、`api-reference.md`

---

## 三、Merge Request（5 条）

### INTENT-MR-001
- **维度标签**: `[completeness]`
- **能力项**: MR 创建、状态机与合并策略
- **预期系统行为**: 基于分支创建 MR 后，状态为 `open`；支持 `merge`/`squash`/`rebase` 合并策略；执行合并后状态转为 `merged`；`[WIP]` 标题前缀使 MR 处于 draft 状态且不可合并。
- **风险/验证理由**: RISK-COMP-01。MR 是代码协作核心机制，核心流程不可用则平台不可工作。
- **优先级**: P0
- **出处**: `merge-request-spec.md` §1.1、§1.2、§2.1

### INTENT-MR-002
- **维度标签**: `[completeness, usability]`
- **能力项**: 冲突检测与可合并状态
- **预期系统行为**: 调用 `/api/v5/repos/{owner}/{repo}/pulls/{number}/merge` 返回 `mergeable`（boolean）与 `mergeable_state`（`clean`/`conflict`/`blocked`/`unknown`）；存在冲突时 `mergeable=false`，合并操作被拒绝并返回明确错误信息。
- **风险/验证理由**: RISK-USE-03。API 错误信息若不返回具体业务语义（如「存在冲突」vs 泛化 400），开发者无法自动处理。
- **优先级**: P1
- **出处**: `merge-request-spec.md` §2.3

### INTENT-MR-003
- **维度标签**: `[completeness, security]`
- **能力项**: MR 代码评审与行级评论
- **预期系统行为**: 支持提交评审（APPROVE/REQUEST_CHANGES/COMMENT）与行级评论（指定 commit_id、path、position）；未满足 `require_review_count` 时合并被阻止；评审人权限不足时操作应被拒绝。
- **风险/验证理由**: RISK-SEC-06。权限越界风险：低权限用户不应能 approve 并绕过合并门禁。
- **优先级**: P0
- **出处**: `merge-request-spec.md` §2.2

### INTENT-MR-004
- **维度标签**: `[completeness, reliability]`
- **能力项**: CI 门禁（MR 必须过 CI）
- **预期系统行为**: 保护分支开启 `require_ci_pass: true` 后，MR 在 CI 未完成或失败时不可合并；CI 状态变更后自动更新 MR 可合并状态。
- **风险/验证理由**: RISK-REL-02。needs 依赖的 matrix job 全成功但上游 job 初始化失败时无声失败，可能导致 CI 状态误判为通过。
- **优先级**: P0
- **出处**: `repository-spec.md` §1.2、`merge-request-spec.md` §3.4

### INTENT-MR-005
- **维度标签**: `[usability, compatibility]`
- **能力项**: MR 模板（Description Template）与 Draft 状态
- **预期系统行为**: 支持预置 MR 描述模板；Draft/WIP MR 禁止直接合并；从 GitHub 迁移的 PR 模板在 GitCode 中可复用或给出明确不兼容提示。
- **风险/验证理由**: RISK-USE-01 / RISK-COMPAT-01。协作流程依赖模板，迁移时静默不生效会降低团队效率。
- **优先级**: P1
- **出处**: `merge-request-spec.md` §1.1、Parity Matrix

---

## 四、Issues（4 条）

### INTENT-ISSUE-001
- **维度标签**: `[completeness]`
- **能力项**: Issue CRUD 与状态流转
- **预期系统行为**: 支持创建、更新、关闭、重新打开 Issue；状态字段取值 `open`/`closed`；关闭后可重新打开。
- **风险/验证理由**: RISK-COMP-01。Issue 是项目管理核心，核心端点缺失不可接受。
- **优先级**: P0
- **出处**: `issue-spec.md` §1.2、§2.1

### INTENT-ISSUE-002
- **维度标签**: `[completeness, compatibility]`
- **能力项**: 标签与里程碑管理
- **预期系统行为**: 标签支持自定义名称、颜色（hex 不含 `#`）、描述；里程碑支持标题、描述、截止日期、状态（open/closed）；标签名称唯一，重复创建应报错。
- **风险/验证理由**: RISK-COMP-02。颜色格式 hex 不含 `#` 与部分平台习惯不同，是默认值/格式差异高发区。
- **优先级**: P1
- **出处**: `issue-spec.md` §1.1、§2.3、§2.4

### INTENT-ISSUE-003
- **维度标签**: `[completeness, usability]`
- **能力项**: Issue 评论与 @提及通知
- **预期系统行为**: Issue/MR 评论支持 Markdown；`@username` 提及触发站内通知/邮件通知；评论中引用其他 Issue/MR 可正确解析为链接。
- **风险/验证理由**: RISK-USE-04。MR/Issue 缺少通知或通知延迟直接影响协作体验。
- **优先级**: P1
- **出处**: `issue-spec.md` §1.1、`discussion-notification-spec.md` §1.1、§1.2

### INTENT-ISSUE-004
- **维度标签**: `[completeness]`
- **能力项**: Issue 关联 MR/Commit（关键字自动关闭）
- **预期系统行为**: MR 描述或 commit message 中包含 `close`/`fix`/`resolve #N` 时，合并后自动关闭对应 Issue；不支持关键字时不应误关闭无关 Issue。
- **风险/验证理由**: RISK-COMP-01。追溯关联是 DevOps 工作流关键能力，缺失会导致工单管理脱节。
- **优先级**: P1
- **出处**: `issue-spec.md` §1.1、Parity Matrix

---

## 五、Packages（3 条）

### INTENT-PKG-001
- **维度标签**: `[completeness, compatibility]`
- **能力项**: 包格式协议支持（npm/Maven/PyPI/Docker）
- **预期系统行为**: 支持 `npm publish`/`npm install`、`mvn deploy`、`twine upload`/`pip install`、`docker push`/`docker pull` 等标准协议；包仓库协议与标准 registry 兼容（如 npmrc 配置无需大幅修改）。
- **风险/验证理由**: RISK-COMP-05 / RISK-COMPAT-04。Package 格式支持缺失或协议不兼容会导致工具链集成失败，直接影响开发者使用。
- **优先级**: P1
- **出处**: `parity-matrix.md` §五

### INTENT-SEC-007
- **维度标签**: `[security]`
- **能力项**: 包访问权限控制与防恶意覆盖
- **预期系统行为**: 私有包仅对授权用户/组织可见；同一版本号不可被不同内容覆盖（不可变版本约束）；无写权限用户执行 `npm publish` 等操作应被拒绝。
- **风险/验证理由**: RISK-SEC-07。Package 仓库被恶意覆盖/投毒是供应链安全风险；权限控制缺失会导致内部包被外部替换。
- **优先级**: P1
- **出处**: `parity-matrix.md` §五

### INTENT-REL-006
- **维度标签**: `[reliability, usability]`
- **能力项**: 大文件包上传中断与恢复
- **预期系统行为**: 大文件（缺 platform-config，参数待补：具体包大小上限未知）上传中断后，客户端可重试或断点续传；上传失败后返回明确错误信息（如大小超限、认证失败），不返回泛化 500。
- **风险/验证理由**: RISK-REL-06 / RISK-USE-05。上传中断无法恢复且提示不清晰会严重影响开发者体验。
- **优先级**: P2
- **出处**: `parity-matrix.md` §五

---

## 六、用户与权限（5 条）

### INTENT-AUTH-001
- **维度标签**: `[completeness, security]`
- **能力项**: PAT 认证与权限范围（Scopes）生效
- **预期系统行为**: PAT 带 `repo` scope 可读写仓库；带 `read:user` 仅可读取用户信息；带 `public_repo` 仅可访问公开仓库；scope 不足时 API 返回 403 并指明缺少的 scope。
- **风险/验证理由**: RISK-SEC-05 / RISK-SEC-06。Token 泄露后若权限未正确限制，影响面扩大；PAT 日志脱敏绕过问题需一并验证。
- **优先级**: P0
- **出处**: `user-org-spec.md` §1.1、§3.4

### INTENT-SEC-009
- **维度标签**: `[security]`
- **能力项**: 组织成员权限继承与防提权
- **预期系统行为**: 组织成员角色（`admin`/`member`）正确继承到组织下所有项目；Developer 不可通过 API 调用手动提升自身或他人为 Maintainer/Owner；角色变更操作需由更高权限角色执行。
- **风险/验证理由**: RISK-SEC-09（blocker）。组织成员非法提升权限是权限继承缺陷，可能导致整个组织失控。
- **优先级**: P0
- **出处**: `user-org-spec.md` §1.2、§2.3

### INTENT-AUTH-002
- **维度标签**: `[completeness]`
- **能力项**: 仓库成员角色（Owner/Maintainer/Developer/Reporter）权限边界
- **预期系统行为**: Reporter 只读、不可提交；Developer 可 push/创建 MR，不可删除项目/修改保护分支规则；Maintainer 可管理设置、合并请求、保护分支；Owner 拥有一切权限。
- **风险/验证理由**: RISK-SEC-06。权限越界（低权限用户访问高权限资源）是 blocker 级风险，每个角色的否定权限都需验证。
- **优先级**: P0
- **出处**: `repository-spec.md` §1.1、`user-org-spec.md` §1.3

### INTENT-AUTH-003
- **维度标签**: `[completeness, compatibility]`
- **能力项**: 团队（Team）权限批量分配与仓库继承
- **预期系统行为**: 组织下可创建团队；团队成员批量获得对指定仓库的访问权限；团队权限变更后，成员对仓库的访问权限同步更新；通过 API 可查询团队有权访问的仓库列表。
- **风险/验证理由**: RISK-COMP-01。团队权限是组织治理核心能力，API 缺失或行为不兼容会导致权限管理工具链断裂。
- **优先级**: P1
- **出处**: `user-org-spec.md` §1.2、§2.3

### INTENT-REL-003
- **维度标签**: `[reliability]`
- **能力项**: API 速率限制与 429/Retry-After 返回
- **预期系统行为**: 高频请求触发速率限制时，API 返回 429 状态码；响应头包含 `Retry-After` 或等效字段，指示客户端等待秒数；速率限制阈值（缺 platform-config，参数待补：具体 QPS/每小时上限未知）需可验证。
- **风险/验证理由**: RISK-REL-03。速率限制未正确返回 429/Retry-After 会导致客户端无法自适应退避，引发重试风暴。
- **优先级**: P1
- **出处**: `api-reference.md`、Parity Matrix

---

## 七、Webhooks & 集成（4 条）

### INTENT-HOOK-001
- **维度标签**: `[completeness, security]`
- **能力项**: Webhook 创建、事件投递与签名验证
- **预期系统行为**: 支持创建 Webhook 监听 `push`/`pull_request`/`issues`/`issue_comment`/`release` 等事件；Payload 使用 `secret` 进行 HMAC-SHA256 签名；签名错误/被篡改时接收方可验证失败；支持 SSL 验证与 `insecure_ssl` 跳过选项。
- **风险/验证理由**: RISK-SEC-08。Webhook secret 泄露或签名绕过可导致中间人攻击、伪造事件触发外部系统。
- **优先级**: P1
- **出处**: `discussion-notification-spec.md` §1.3、§2.3

### INTENT-REL-004
- **维度标签**: `[reliability]`
- **能力项**: Webhook 投递失败的重试与超时控制
- **预期系统行为**: 接收端返回非 2xx 或超时时，系统应自动重试（重试次数与退避策略待确认：缺 platform-config，参数待补）；连续失败后 Webhook 自动禁用或标记为异常；不产生重试风暴。
- **风险/验证理由**: RISK-REL-04。Webhook 投递失败无重试或重试风暴会导致集成不可靠或对接收端造成 DDoS。
- **优先级**: P1
- **出处**: `discussion-notification-spec.md` §1.3

### INTENT-HOOK-002
- **维度标签**: `[completeness]`
- **能力项**: CI 状态回写（Commit Status / MR 状态关联）
- **预期系统行为**: Actions 运行完成后，运行状态（success/failure/cancelled）应回写到对应 commit 或 MR；MR 列表页可查看关联 CI 状态；保护分支的 `require_ci_pass` 可读取此状态进行门禁判断。
- **风险/验证理由**: RISK-COMP-01。CI 状态不回写会导致合并门禁失效，破坏代码质量防护体系。
- **优先级**: P1
- **出处**: `discussion-notification-spec.md` §1.2、`repository-spec.md` §1.2

### INTENT-USE-004
- **维度标签**: `[usability]`
- **能力项**: 站内通知与邮件通知的及时性与完整性
- **预期系统行为**: Issue/MR 创建、关闭、合并、被指派、被 @提及 时，相关用户应在合理时延内（缺 platform-config，参数待补：具体 SLA 未知）收到站内通知；邮件通知（若配置）与站内通知内容一致；通知列表 API `/api/v5/notifications` 可按 `all`/`participating`/`since`/`before` 筛选分页。
- **风险/验证理由**: RISK-USE-04。MR/Issue 缺少通知或通知延迟直接破坏协作体验，是高频客诉点。
- **优先级**: P1
- **出处**: `discussion-notification-spec.md` §1.2、§2.2

---

## 汇总

| 模块 | 意图数 | P0 数 | P1 数 | P2 数 |
|---|---|---|---|---|
| CI/CD — Actions | 9 | 3 | 6 | 0 |
| 代码托管 — Git Repository | 5 | 2 | 3 | 0 |
| Merge Request | 5 | 2 | 3 | 0 |
| Issues | 4 | 1 | 3 | 0 |
| Packages | 3 | 0 | 2 | 1 |
| 用户与权限 | 5 | 3 | 2 | 0 |
| Webhooks & 集成 | 4 | 0 | 4 | 0 |
| **合计** | **35** | **11** | **23** | **1** |

### 按维度统计

| 维度 | 意图数 |
|---|---|
| completeness | 22 |
| security | 10 |
| compatibility | 8 |
| reliability | 7 |
| usability | 7 |

（注：跨维度 intent 被重复计数）

### 溯源链闭合检查

| 风险项 | 覆盖意图 |
|---|---|
| RISK-SEC-01 | INTENT-SEC-001 |
| RISK-SEC-02 | INTENT-SEC-002 |
| RISK-SEC-03 | INTENT-SEC-003 |
| RISK-SEC-04 | INTENT-SEC-004 |
| RISK-SEC-05 | INTENT-SEC-002 / INTENT-AUTH-001 |
| RISK-SEC-06 | INTENT-GIT-002 / INTENT-MR-003 / INTENT-AUTH-002 |
| RISK-SEC-07 | INTENT-SEC-007 |
| RISK-SEC-08 | INTENT-HOOK-001 |
| RISK-SEC-09 | INTENT-SEC-009 |
| RISK-COMP-01 | INTENT-GIT-001 / INTENT-MR-001 / INTENT-ISSUE-001 / INTENT-AUTH-003 / INTENT-HOOK-002 |
| RISK-COMP-02 | INTENT-COMP-002 / INTENT-ISSUE-002 |
| RISK-COMP-03 | INTENT-GIT-005 |
| RISK-COMP-04 | INTENT-REL-003 |
| RISK-COMP-05 | INTENT-PKG-001 |
| RISK-REL-01 | INTENT-REL-001 |
| RISK-REL-02 | INTENT-MR-004 |
| RISK-REL-03 | INTENT-REL-003 |
| RISK-REL-04 | INTENT-REL-004 |
| RISK-REL-05 | INTENT-GIT-003 |
| RISK-REL-06 | INTENT-REL-006 |
| RISK-COMPAT-01 | INTENT-COMPAT-001 / INTENT-COMP-003 / INTENT-MR-005 |
| RISK-COMPAT-02 | INTENT-COMPAT-001 |
| RISK-COMPAT-03 | （本次未单独覆盖，属 P2 边角） |
| RISK-COMPAT-04 | INTENT-PKG-001 |
| RISK-USE-01 | INTENT-COMP-001 / INTENT-COMPAT-001 / INTENT-MR-005 |
| RISK-USE-02 | （已在 INTENT-USE-004 中部分覆盖，需文档一致性专项） |
| RISK-USE-03 | INTENT-MR-002 |
| RISK-USE-04 | INTENT-ISSUE-003 / INTENT-USE-004 |
| RISK-USE-05 | INTENT-REL-006 |

> 所有 P0 blocker 风险项均已覆盖；RISK-COMPAT-03（Git 客户端 sparse-checkout 兼容性）为 P2 边角，本次未单独出 intent，留待后续 run 补全。
