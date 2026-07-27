# 安全维度测试意图（Security Intents）

> 产出：安全 Agent（security）
> Run：2026-07-27-01（增量模式 / 基底加速）
> 基底：Run 2026-07-23-01（delivered，36 条 security intent 全准入、51 条用例全覆盖）
> 覆盖：fork PR 隔离 / pull_request_target 滥用 / secret 日志脱敏 / 表达式注入 / 供应链 / cache&artifact 投毒 / runner 隔离 / 权限最小化 / 评论触发 / 环境审批 / 网络边界 / 侧信道 / **token 生命周期 / secret 管理面 / 组织级边界 / 日志访问控制 / 命名遮蔽 / GitCode 特有评论正则 / 评论编辑 TOCTOU / workflow_run 缺失补偿 / 敏感文件打包 / 安全审计**
> 总量：46 条（沿用 36 + 新增 10）

---

## 0. 本轮增量说明（与 Run 2026-07-23-01 的关系）

本轮为增量发散。上一轮 36 条 intent（INTENT-SEC-001~036）经门禁全准入且均有用例覆盖，攻击面判断仍然成立，**全部沿用，不重复展开**。本轮在此基础上做两类增量：

1. **实证刷新**：`inputs/history/issues-encountered.md` 确认两条真实安全事件，已回注到对应沿用 intent 的备注（不改历史文件，仅在本文件标注）：
   - **#51**：「fork 仓提 PR 能够获取到主仓的密钥」——已确认的真实漏洞，无修复日期记录 → 直接坐实 INTENT-SEC-001/003 为**回归命脉**，执行时必须通过。
   - **#66**：「pull_request_target 访问 secrets 的 fork PR 场景目前还未实现（开发中，715）」→ INTENT-SEC-002/035 对应的 pull_request_target×fork 路径在输入快照时点刚上线或仍缺失；执行时若路径尚不存在，应判「机制缺失=待验证」，不得以「跑不通」为由跳过 negative 断言。
2. **新增 10 条 intent（INTENT-SEC-037~046）**：覆盖上轮未触及的攻击面——token 生命周期、secret 管理面（回读/鉴权/审计）、组织级 secret 可见性边界、日志访问控制与保留、系统变量命名遮蔽、GitCode 特有 `comments` 正则过滤、评论 `edited` 事件 TOCTOU、`workflow_run` 缺失的补偿控制、敏感文件打包、安全审计日志。ID 从 037 起编，与上轮无冲突。

### 输入退化标注

- `inputs/business-context/`：**⚠️ 仍仅 README.md 空模板**，无部署模型、历史安全问题台账、Runner 拓扑。SEC-022/023/028 及新增 SEC-040 的判定证据基于规格片段与通用关注点，若 business-context 后续补充内网拓扑，需重审。
- `inputs/gitcode-spec/`：token-permissions.md / pr-mr-pipeline-security.md / using-secrets.md / syntax-reference/trigger-events.md（fetched 2026-07-20）。关键新事实：
  - spec 明确 secret「**创建后无法在界面查看原值，只能更新覆盖**」（using-secrets.md）→ SEC-038 获得规格 oracle。
  - spec 明确 secret 命名规则：仅大写字母/数字/下划线、**不得以 `ATOMGIT_` 开头**、不得以数字开头 → SEC-041 获得规格 oracle。
  - `pull_request_comment` 为 **GitCode 特有事件**，带 `comments` **正则**过滤与 `edited`/`deleted` 类型（trigger-events.md §1.4/1.5）→ SEC-042/043 的攻击面来源。
  - **全规格无 `workflow_run`**（grep 0 命中）→ GitHub 推荐的「非特权 pull_request + 特权 workflow_run」分离模式在 GitCode 无等价物 → SEC-044。
- `inputs/security-knowledge/`：3 份文件（github-actions-security-series.md / issues.md / README.md 含 OWASP CICD Top10 映射），版本 2026-07-21，与上轮一致；issues.md §2/§3 中「token 过期轮换」「日志扫描/保留期/导出权限」两条上轮未落地，本轮由 SEC-037/040/046 补齐。

---

## 1. 信任边界图（文字描述）

### 1.1 不可信主体（攻击发起点）
- **外部 fork 贡献者**：任何人可 fork 后提 PR，触发 `pull_request` / `pull_request_target` / `pull_request_comment` 流水线——开源社区最大攻击面（实证：history #51 曾真实泄露主仓密钥）。
- **PR/Issue 评论者**：`issue_comment` / `pull_request_comment` 触发面，不受 PR 审批保护；评论可**编辑**（`edited` 类型），触发后内容可变。
- **不可信事件负载字段**（攻击者可控）：PR 标题/正文、分支名（`head_ref`)、commit message、commit author name/email、评论正文。
- **第三方 action 作者**：`uses:` 引用的外部代码，在流水线上下文内运行，可隐式获取 token。
- **相邻项目/仓库**：多项目共享 runner 资源池时，项目 A 的 workflow 对项目 B 构成横向不可信主体。
- **（新增）同组织内其他仓库**：组织级 secret 若可见性边界失效，组织内任一仓库的 workflow 均可读取。

### 1.2 敏感资产（应被保护的对象）
- 项目级 / 组织级 / 环境级 **Secret**（`${{ secrets.* }}`）及其**管理面**（创建/更新/删除/回读权限与审计）。
- **ATOMGIT_TOKEN**（自动令牌）及其**生命周期**（签发-使用-失效全链路）。
- **Runner**（宿主/容器文件系统、`/tmp`、workspace、内网网络位置、进程空间、环境变量）。
- **Cache / Artifact**（跨 job/run 共享数据，投毒载体与信息泄露通道；内容可能意外夹带 `.env`/`.git-credentials` 等敏感文件）。
- **workflow 执行逻辑**（不应被不可信 PR 改写后以高权限运行）。
- **运行日志**（含历史日志的访问权限与保留期——脱敏只在写入时做，读取面失控同样致命）。

### 1.3 可触发的特权路径（重点监视）
- **`pull_request_target`**：base 上下文运行、有 secret + 写 token——最易被滥用（Pwn Request）。
- **`pull_request` from fork**：应强制 token 只读 + secret 隔离（实证 #51 曾失效）。
- **显式 `checkout head.sha` + 高权限上下文**：文档自承的注入点。
- **Cache 写 / Artifact 传递**：fork PR 污染主分支；不可信运行产物被特权运行消费。
- **评论触发**：`issue_comment` / `pull_request_comment`（含 GitCode 特有 `comments` 正则过滤）可绕过 PR 审批；`edited` 事件引入 TOCTOU 面。
- **（新增）Secret/token 管理面**：回读接口、权限配置、审计缺失本身就是攻击面。

---

## 2. 按 STRIDE 分类的攻击面扫描结果

| STRIDE 类别 | 攻击面 | 对应 intent | 覆盖数 |
|---|---|---|---|
| **S 伪装 (Spoofing)** | Action typosquatting、TOCTOU 伪装、系统变量命名遮蔽 | SEC-015, SEC-023, SEC-031, SEC-041 | 4 |
| **T 篡改 (Tampering)** | Workflow 文件篡改、Cache/Artifact 投毒、供应链重写、写协议注入、表达式注入、正则过滤绕过、评论编辑 | SEC-003, SEC-009~014, SEC-018~021, SEC-024, SEC-029, SEC-030, SEC-042, SEC-043 | 17 |
| **R 抵赖 (Repudiation)** | 环境审批绕过、评论触发审计缺失、TOCTOU 无代码固定、敏感操作无审计日志 | SEC-026, SEC-027, SEC-030, SEC-031, SEC-046 | 5 |
| **I 信息泄露 (Info Disclosure)** | Fork PR secret 泄露、日志脱敏绕过、Runner 残留、侧信道、网络外泄、跨项目/跨仓库 secret 访问、token 复活、日志读取面、敏感文件打包 | SEC-001, SEC-002, SEC-004~008, SEC-020~022, SEC-025, SEC-028, SEC-032, SEC-033, SEC-037~040, SEC-045 | 20 |
| **D 拒绝服务 (DoS)** | 大 artifact/cache 资源耗尽、恶意 workflow 资源滥用 | SEC-019, SEC-033 | 2 |
| **E 权限提升 (Elevation)** | pull_request_target 滥用、token 权限过大、permissions 失效、环境 secret 绕过、评论触发提权、特权分离机制缺失 | SEC-001~003, SEC-016, SEC-017, SEC-030, SEC-036, SEC-044 | 8 |

> 注：一条 intent 可跨多个 STRIDE 类别，上表按主要类别归类。

---

## 3. 沿用 Intent 清单（36 条，全文见 `runs/2026-07-23-01/intents/security.md` §3）

> 关系标注：**沿用** = 意图不变，复用旧 ID 与已有用例基底；备注列仅登记本轮新增实证/输入变化，不修改历史文件。

| 意图 ID | 标题（摘要） | 优先级 | 风险对齐 | 关系 | 本轮备注 |
|---|---|---|---|---|---|
| INTENT-SEC-001 | fork PR 触发 pull_request 不可读 secrets | P0 | RISK-SEC-01 | 沿用 | **实证强化**：history #51 为已确认真实泄露事件，本 intent 为回归命脉，negative 断言必须通过（门禁零容忍） |
| INTENT-SEC-002 | pull_request_target checkout 不可信代码时 secrets/写权限受控 | P0 | RISK-SEC-01 | 沿用 | **实证刷新**：history #66 表明 fork 场景 7.15 前后才实现；若路径缺失按「机制缺失」记录而非跳过 |
| INTENT-SEC-003 | fork PR 的 ATOMGIT_TOKEN 仅 read | P0 | RISK-SEC-01 | 沿用 | 同 SEC-001，#51 实证 |
| INTENT-SEC-004 | secret 日志/summary/堆栈脱敏 `***` | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-005 | 脱敏不可被 base64 绕过 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-006 | 脱敏不可被拼接/插值绕过 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-007 | 脱敏不可被多行值绕过 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-008 | 脱敏不可被分片输出绕过 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-009 | PR 标题/正文不可注入 run 脚本 | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-010 | 分支名/标签名不可注入 run 脚本 | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-011 | 评论内容不可注入 run 脚本 | P0 | RISK-SEC-02 | 沿用 | 关联新增 SEC-042/043（GitCode 特有评论面） |
| INTENT-SEC-012 | commit message/author email 不可注入 | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-013 | 防双重模板渲染（二次求值） | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-014 | 第三方 action 支持完整 commit SHA 固定 | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-015 | 第三方 action 来源信任边界（typosquatting） | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-016 | 显式 permissions 在 job 级实际生效 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-017 | 未声明 permissions 默认最小化 | P0 | RISK-SEC-01 | 沿用 | spec 补充：`permissions: {}` 空声明 → 仅 repository:read（token-permissions.md），可作 oracle |
| INTENT-SEC-018 | fork PR 写 cache 不可被主仓读取 | P0 | RISK-SEC-01 | 沿用 | parity-matrix cache fork 隔离仍为 ❓，实测确认 |
| INTENT-SEC-019 | fork PR artifact 不可被主仓下载/执行 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-020 | job 结束 workspace/临时文件彻底清理 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-021 | runner 环境变量与 /tmp 跨 job 隔离 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-022 | 自托管 runner 跨项目残留隔离 | P0 | RISK-SEC-01 | 沿用 | 输入退化：business-context 空，拓扑证据待补 |
| INTENT-SEC-023 | runner 网络出站受控（SSRF/内网跳板） | P0 | RISK-SEC-02 | 沿用 | 同上 |
| INTENT-SEC-024 | 变量名特殊字符（中划线）不导致意外求值/泄露 | P0 | RISK-SEC-02 | 沿用 | 关联新增 SEC-041（命名遮蔽面） |
| INTENT-SEC-025 | printenv/进程枚举输出仍保持脱敏 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-026 | 评论触发关键字过滤不可被绕过 | P0 | RISK-SEC-02 | 沿用 | GitCode 特有 `comments` 正则过滤由新增 SEC-042 细化 |
| INTENT-SEC-027 | 环境级 secret 审批前不可访问 | P0 | RISK-SEC-01 | 沿用 | 关联 COMPAT-NEW-002（环境级 secrets 降级行为，compat 维度回填） |
| INTENT-SEC-028 | workflow 命令（add-mask）响应不泄露原值 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-029 | 跨运行 artifact 视为不可信数据 | P0 | RISK-SEC-02 | 沿用 | GitCode 无 workflow_run 等价物，关联新增 SEC-044 |
| INTENT-SEC-030 | ATOMGIT_ENV/OUTPUT/PATH 写协议防污染 | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-031 | TOCTOU：审批后推新 commit 不被特权运行采用 | P0 | RISK-SEC-02 | 沿用 | 评论 `edited` 变体由新增 SEC-043 细化 |
| INTENT-SEC-032 | secret 不经 output/artifact/summary 侧信道外泄 | P0 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-033 | 大 artifact/cache 配额与边界限制 | P0 | RISK-SEC-02 | 沿用 | — |
| INTENT-SEC-034 | OIDC/短时凭据缺失需明示并提供替代 | P1 | RISK-SEC-01 | 沿用 | — |
| INTENT-SEC-035 | pull_request_target 使用 base 分支 workflow 版本 | P0 | RISK-SEC-01 | 沿用 | 同 SEC-002 备注（#66） |
| INTENT-SEC-036 | token 默认权限范围与 job 级覆盖正确生效 | P0 | RISK-SEC-01 | 沿用 | — |

---

## 4. 新增 Intent（10 条，本轮增量）

### 攻击面组 M：Token 生命周期（新增）

```
意图 ID:    INTENT-SEC-037
维度标签:   [security]
标题:       ATOMGIT_TOKEN 生命周期与 run 绑定，结束后失效且不可经残留复活

风险点:     issues.md §2 与 security-series 总结均点名「token 过期/轮换——过期 token 是否仍能通过缓存访问」。若 ATOMGIT_TOKEN 在 run 结束/取消后仍有效，或 token 值经 cache/artifact/日志残留被后续运行复活使用，则一次泄露即成持久化后门。
预期系统行为: ATOMGIT_TOKEN 与单次 run（或更短窗口）绑定，run 完成/取消/超时后失效；过期 token 调用任何 API 返回 401/403；token 值不得经 cache/artifact 残留被下一 run 当作有效凭据使用。
Oracle 来源: GitCode规格（token 自动生成的语义）/ GitHub行为（GITHUB_TOKEN run 结束失效）

验证要点:
  - [正向] run 进行中 token 可完成其 permissions 内的操作
  - [负向] run 结束后旧 token 调用 API 绝不应成功；残留于 cache/artifact 的 token 在新 run 中绝不应可用
  - [非功能] rerun 场景应签发新 token 或明确复用未过期 token，行为可判定

负向断言目标: 系统绝不应允许已结束/已取消 run 的 ATOMGIT_TOKEN 继续通过鉴权；判定证据：run 完成后持旧 token 调用只读 API 返回 401/403，且新 run 使用残留 token 的调用同样被拒。
威胁类别: STRIDE-Info Disclosure / Elevation；OWASP CICD-05；CVE 类：凭据生命周期失效
优先级线索: RISK-SEC-01（P1——非直接 blocker，但属 secret/token 管理实证关注点，issues.md §2）
破坏级别:   fixture
来源输入:   security-knowledge/issues.md §2；security-knowledge/github-actions-security-series.md 总结#6；gitcode-spec/security-permissions/token-permissions.md
```

### 攻击面组 N：Secret 管理面与组织级边界（新增）

```
意图 ID:    INTENT-SEC-038
维度标签:   [security]
标题:       Secret 写后不可回读，管理操作需鉴权并留审计

风险点:     spec 承诺「创建后无法在界面查看原值，只能更新覆盖」。若存在任何 UI/API 路径可回读 secret 明文，或低权限成员可创建/更新/删除 secret 而无审计记录，则管理面本身即泄露通道。
预期系统行为: secret 值一经写入不可经任何 UI/API 回读明文（仅能更新覆盖）；创建/更新/删除操作要求相应权限并留下可追溯记录。
Oracle 来源: GitCode规格（using-secrets.md「不可查看」安全机制）

验证要点:
  - [正向] 授权管理员可创建/更新 secret，workflow 正常引用
  - [负向] 任何读取接口/UI 绝不应返回 secret 明文；无权限角色的管理操作绝不应成功
  - [非功能] 管理操作应有审计记录可查

负向断言目标: 系统绝不应提供可回读 secret 明文的接口或界面；判定证据：枚举 secret 相关 API/UI 响应，均不含明文 value 字段；越权管理操作返回 403。
威胁类别: STRIDE-Info Disclosure / Repudiation；OWASP CICD-05 / CICD-08
优先级线索: RISK-SEC-01（P1——管理面实证关注点，issues.md §2）
破坏级别:   fixture
来源输入:   gitcode-spec/security-permissions/using-secrets.md；security-knowledge/issues.md §2
```

```
意图 ID:    INTENT-SEC-039
维度标签:   [security]
标题:       组织级 Secret 的仓库可见性边界必须生效

风险点:     组织级 secret 面向组织内多仓库共享，若可见性边界失效（组织内任意仓库的 workflow 均可读取全部组织级 secret），则一个被入侵的边缘仓库可拖库整个组织的机密；fork PR 场景下边界更关键。
预期系统行为: 组织级 secret 仅对可见范围内的仓库/项目生效；范围外仓库 workflow 引用时返回空或报错；fork PR 路径下组织级 secret 与项目级同等隔离。
Oracle 来源: GitCode规格（using-secrets.md 组织级 Secret 章节；可见范围粒度规格未明，需实测确认）

验证要点:
  - [正向] 范围内仓库可正常引用组织级 secret
  - [负向] 范围外仓库、fork PR 触发的 workflow 绝不应读到组织级 secret 原值
  - [非功能] 可见性配置变更即时生效（无缓存残留窗口）

负向断言目标: 系统绝不应让可见范围外的仓库或 fork PR 运行获取组织级 secret 值；判定证据：范围外运行中引用返回空值，日志全文搜索原值命中数为 0。
威胁类别: STRIDE-Info Disclosure / Elevation；OWASP CICD-05 / CICD-06
优先级线索: RISK-SEC-01（P1——issues.md §2「组织级 vs 仓库级可见性边界」实证关注点）
破坏级别:   fixture
来源输入:   gitcode-spec/security-permissions/using-secrets.md；security-knowledge/issues.md §1/§2
```

### 攻击面组 O：日志读取面（新增）

```
意图 ID:    INTENT-SEC-040
维度标签:   [security]
标题:       运行日志的访问控制、保留期与历史日志脱敏一致性

风险点:     issues.md §3 点名：日志扫描、保留期、下载/导出权限。脱敏只在写入时生效，若日志对无关人员开放下载、过期后仍可恢复、或历史日志（secret 轮换前产生）仍可访问，则 secret 轮换与脱敏均失去意义。rerun 旧运行时新日志不应复活已失效信息。
预期系统行为: 日志查看/下载/导出需对应权限；日志有明确保留期，过期后不可恢复；历史日志中的 secret 遮蔽状态不随后续操作回退。
Oracle 来源: GitCode规格 / 差异声明（保留期规格未明，需实测确认）

验证要点:
  - [正向] 有权限成员可查看/下载日志
  - [负向] 无权限角色绝不应读取或下载日志；过期日志绝不应可恢复；任何日志副本（含导出件）中 secret 原值命中数为 0
  - [非功能] 日志访问行为本身可审计（关联 SEC-046）

负向断言目标: 系统绝不应让未授权主体读取运行日志，也不应让过期日志可恢复；判定证据：越权访问返回 403/404，过期日志访问返回不存在，导出日志全文搜索 secret 原值命中数为 0。
威胁类别: STRIDE-Info Disclosure / Repudiation；OWASP CICD-05 / CICD-08
优先级线索: RISK-SEC-01（P1——issues.md §3 实证关注点）
破坏级别:   fixture
来源输入:   security-knowledge/issues.md §3；gitcode-spec/running-pipelines/view-job-logs.md
```

### 攻击面组 P：命名与系统变量遮蔽（新增）

```
意图 ID:    INTENT-SEC-041
维度标签:   [security]
标题:       Secret/变量命名约束必须实际生效，防止遮蔽系统变量

风险点:     spec 规定 secret 名仅允许大写字母/数字/下划线、不得以 ATOMGIT_ 开头、不得以数字开头。若校验不生效，攻击者可创建与系统环境变量同名的 secret（如遮蔽 ATOMGIT_TOKEN、ATOMGIT_ENV），在 job 环境中覆盖系统值，劫持写协议路径或凭据。与 SEC-024（中划线解析错误）互补——本条针对「遮蔽系统变量」的主动攻击面。
预期系统行为: 违反命名规则的 secret/变量在创建时被拒绝并给出明确报错；任何用户自定义值不得覆盖平台注入的系统环境变量。
Oracle 来源: GitCode规格（using-secrets.md 命名规则）

验证要点:
  - [正向] 合法命名创建成功
  - [负向] 以 ATOMGIT_ 开头、含非法字符、数字开头的 secret 创建绝不应成功；job 环境中系统变量值绝不应被同名用户变量替换
  - [非功能] 拒绝时报错应指明命名规则（关联 USE-028）

负向断言目标: 系统绝不应接受可遮蔽系统变量的 secret/变量命名，也绝不应让同名用户值覆盖系统环境变量；判定证据：违规创建返回明确校验错误，job 内系统变量取值与平台注入值一致。
威胁类别: STRIDE-Spoofing / Tampering / Elevation；OWASP CICD-05
优先级线索: RISK-SEC-02（P1——规格明确承诺的防护，验证其实际生效）
破坏级别:   fixture
来源输入:   gitcode-spec/security-permissions/using-secrets.md；inputs/history/issues-encountered.md #38（中划线实证）
```

### 攻击面组 Q：GitCode 特有评论触发面（新增）

```
意图 ID:    INTENT-SEC-042
维度标签:   [security, compatibility]
标题:       pull_request_comment 的 comments 正则过滤语义必须安全（GitCode 特有）

风险点:     pull_request_comment 为 GitCode 特有事件，`comments` 字段按正则过滤评论内容。正则默认子串匹配：配置 `/deploy` 时，「请不要 /deploy」这类反讽/引用文本同样命中，造成误触发特权 workflow；反之攻击者也可能利用正则语义差异绕过预期的精确匹配。GitHub 无此机制，属 GitCode 独有攻击面，无 GitHub oracle 可对照。
预期系统行为: comments 过滤的匹配语义（子串/全串/锚定）明确且文档化；过滤不可被 markdown 格式、大小写、嵌入文本等手段造成预期外触发或预期内漏触发；误触发面应有文档警示。
Oracle 来源: GitCode规格（trigger-events.md §1.5「基于正则表达式的评论内容过滤」）/ 差异声明

验证要点:
  - [正向] 精确指令评论正常触发
  - [负向] 引用/反讽/代码块内嵌指令文本绝不应造成预期外触发；绕过过滤语义的伪装评论绝不应触发
  - [非功能] 触发记录可回溯到匹配的具体评论内容（关联 SEC-046 审计）

负向断言目标: 系统绝不应让不符合配置意图的评论文本触发 pull_request_comment workflow；判定证据：构造语义边界评论（引用、代码块、变形空白），触发结果与配置意图一致，非预期触发次数为 0。
威胁类别: STRIDE-Tampering / Elevation / Repudiation；OWASP CICD-03 / CICD-08
优先级线索: RISK-SEC-02（P1——GitCode 特有机制，无对标 oracle，误触发面实测确认）
破坏级别:   fixture
来源输入:   gitcode-spec/syntax-reference/trigger-events.md §1.5；gitcode-spec/COMPAT-NOTES.md；security-knowledge/github-actions-security-series.md Part 4
关系:       变体自 INTENT-SEC-026（关键字过滤），细化为 GitCode 特有正则机制
```

```
意图 ID:    INTENT-SEC-043
维度标签:   [security]
标题:       评论 edited/deleted 事件的 TOCTOU 面：触发后内容变更不应改变已授权语义

风险点:     issue_comment / pull_request_comment 支持 edited/deleted 类型。TOCTOU 变体：攻击者先发合规评论触发 workflow，运行排队期间将评论编辑为恶意内容（若 workflow 运行时再读评论体，则读到篡改后内容）；或管理员基于评论内容审批后，评论被编辑使审计记录与执行依据不一致。
预期系统行为: workflow 触发时事件负载应快照触发时刻的评论内容；edited 再触发应视为新事件重新评估；审计记录中的评论内容与执行依据一致。
Oracle 来源: GitCode规格（trigger-events.md §1.4/1.5）/ GitHub行为（同类 TOCTOU 模式）

验证要点:
  - [正向] created 触发读取到触发时刻内容
  - [负向] 触发后编辑评论绝不应改变已排队/运行中 workflow 读到的事件负载；edited 触发的运行绝不应沿用旧快照冒充原审批
  - [非功能] 审计中评论内容哈希与触发时刻一致

负向断言目标: 系统绝不应让运行中的 workflow 读取到触发后被编辑的评论内容并据此改变行为；判定证据：运行内读取的评论体与触发时刻快照一致，编辑后内容未出现在执行依据中。
威胁类别: STRIDE-Tampering / Repudiation / Elevation；OWASP CICD-03；CVE 类：TOCTOU
优先级线索: RISK-SEC-02（P1——SEC-031 的评论侧变体，GitCode 显式支持 edited 类型，面真实存在）
破坏级别:   fixture
来源输入:   gitcode-spec/syntax-reference/trigger-events.md §1.4/1.5；security-knowledge/github-actions-security-series.md Part 4
关系:       变体自 INTENT-SEC-031（TOCTOU），扩展至评论编辑维度
```

### 攻击面组 R：特权分离机制缺失的补偿（新增）

```
意图 ID:    INTENT-SEC-044
维度标签:   [security, compatibility]
标题:       缺少 workflow_run 等价特权分离机制时，平台应提供等价防护或明确指引

风险点:     GitHub 防 Pwn Request 的标准模式是「非特权 pull_request + 特权 workflow_run」两段式。GitCode 全规格无 workflow_run（grep 0 命中），意味着用户只能在 pull_request_target 单事件内做特权操作，防护全部压在 SEC-002/035 两点上，纵深缺失。若无文档指引，迁移用户会按 GitHub 模式书写而静默失效或误用。
预期系统行为: 平台应提供某种等价特权链机制（或明确声明不支持），并对「特权 workflow 消费不可信运行产物」的场景给出官方安全写法指引；不可信运行绝不应存在隐式触发特权运行的路径。
Oracle 来源: 差异声明（GitCode 未声明 workflow_run 支持）

验证要点:
  - [负向] 系统绝不应存在不可信（fork PR）运行隐式拉起高权限后续运行的路径
  - [非功能] 文档应明示 workflow_run 不支持及替代安全模式（如 pull_request_target + 审批/label gate）

负向断言目标: 不可信运行绝不应能通过任何链式触发机制获得特权上下文；判定证据：枚举可用触发器清单确认无 workflow_run 等价物，且 fork PR 运行结束后无任何自动拉起的特权运行记录。
威胁类别: STRIDE-Elevation；OWASP CICD-03；CVE 类：Pwn Request / workflow_run 链式攻击
优先级线索: RISK-SEC-01/02（P1——机制缺失型缺口，定位同 SEC-034 OIDC）
破坏级别:   none
来源输入:   gitcode-spec（全库 grep 无 workflow_run）；security-knowledge/github-actions-security-series.md Part 1/4
```

### 攻击面组 S：共享数据内容卫生（新增）

```
意图 ID:    INTENT-SEC-045
维度标签:   [security]
标题:       Artifact/Cache 打包不应意外夹带敏感文件（.env / .git-credentials 等）

风险点:     issues.md §4 点名：宽通配上传（如整个 workspace）可能把 .env、.git-credentials、私钥等敏感文件打进 artifact/cache，随后被有下载权限的任何角色取走——泄露面不经过 secrets 体系，脱敏机制管不到。
预期系统行为: 平台应对明显敏感文件名/路径的打包给出警示或防护（如默认排除、显式确认）；下载方应被告知 artifact/cache 属不可信内容；至少文档明确该风险与推荐写法。
Oracle 来源: 差异声明 / GitHub行为（社区最佳实践）

验证要点:
  - [负向] 含常见敏感文件名的打包绝不应在无警示的情况下静默成功；若平台无防护，文档必须明示风险
  - [非功能] 若提供扫描/排除机制，命中清单可判定

负向断言目标: 系统绝不应在不给出任何警示的情况下，让含敏感文件的 artifact/cache 被打包并可被跨角色下载而无痕；判定证据：打包含敏感文件名时日志/结果中存在可识别的警示记录，或文档中检索到该风险说明。
威胁类别: STRIDE-Info Disclosure；OWASP CICD-05 / CICD-10
优先级线索: RISK-SEC-01（P2——用户卫生与平台护栏结合部，非直接 blocker）
破坏级别:   fixture
来源输入:   security-knowledge/issues.md §4；testing-focus.md §8
```

### 攻击面组 T：安全审计（新增）

```
意图 ID:    INTENT-SEC-046
维度标签:   [security]
标题:       敏感操作必须留有可审计记录（secret 变更 / 权限变更 / rerun / 环境审批 / 评论触发）

风险点:     OWASP CICD-08（审计与日志不足）与 issues.md §3 均点名。secret 被改、permissions 放宽、运行被 rerun、环境审批通过、评论触发特权 workflow——若无审计轨迹，泄露发生后无法溯源，STRIDE-R 维度整体失守。
预期系统行为: 上述敏感操作均产生含操作者、时间、对象、变更摘要的审计记录，且普通项目成员不可擦除。
Oracle 来源: GitCode规格 / 差异声明（审计能力规格未明，需实测确认）

验证要点:
  - [正向] 执行各类敏感操作后审计记录可查
  - [负向] 敏感操作绝不应无痕发生；审计记录绝不应可被操作者本人删除或篡改
  - [非功能] 审计记录保留期与导出能力可判定

负向断言目标: 系统绝不应允许敏感操作（secret/权限/rerun/审批/特权触发）无痕发生；判定证据：逐类执行操作后检索审计记录，覆盖率 100%，且尝试以操作者身份删除审计记录被拒。
威胁类别: STRIDE-Repudiation；OWASP CICD-08
优先级线索: RISK-SEC-01/02（P1——抵赖类防护，规格未明需实测）
破坏级别:   fixture
来源输入:   security-knowledge/README.md OWASP CICD-08 映射；security-knowledge/issues.md §3
```

---

## 5. 覆盖自检与质量清单

- [x] 每条 intent 有明确的「不应发生」负向目标。
- [x] fork PR / pull_request_target / secret masking（base64/拼接/多行/分片）/ 脚本注入 / action pin / cache 投毒 / artifact 投毒 / runner 残留 / 网络隔离 / 权限最小化 / 评论触发（含 GitCode 特有正则）/ 环境审批 / 侧信道 / OIDC 缺口 / TOCTOU（commit + 评论编辑双变体）/ token 生命周期 / secret 管理面 / 组织级边界 / 日志访问控制 / 命名遮蔽 / 特权分离缺失 / 敏感文件打包 / 安全审计 均有覆盖。
- [x] 每条给出确定性判定证据（日志命中数 0、401/403/404、cache miss、快照一致性、审计覆盖率 100% 等）。
- [x] 未出现真实密钥/token/内网地址，均使用占位符或描述性语言。
- [x] 未包含可直接利用的攻击 payload、exploit 代码或绕过步骤——所有攻击面以意图层语言描述。
- [x] 已标注输入退化（business-context 空模板）。
- [x] 新 intent ID（037~046）与 Run 2026-07-23-01 无冲突；变体关系（042→026、043→031）已显式注明。
- [x] 风险登记册两个 blocker（RISK-SEC-01 / RISK-SEC-02）均有 P0 intent 覆盖，且 #51 实证已回注。

> **人工复审建议**：请具备 CI/CD 攻击面经验的工程师重点复审——
> 1. INTENT-SEC-001/003（#51 实证的回归命脉，negative 断言必须在真实环境可观测）；
> 2. INTENT-SEC-002/035（#66 表明 fork×pull_request_target 路径刚实现，需确认判定证据与实现现状对齐）；
> 3. INTENT-SEC-037（token 生命周期，规格未明示失效语义，判定证据需与平台实际行为校准）；
> 4. INTENT-SEC-042（GitCode 特有正则过滤，无 GitHub oracle，需确认「配置意图」如何形式化为可判定断言）。
