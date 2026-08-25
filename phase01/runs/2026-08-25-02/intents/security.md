# Security Intents — 防御性验收目标

> 维度：`security`  
> 产出日期：2026-08-25  
> Agent：security agent（攻击面测绘师 / 防御性安全评审）  
> Run：`2026-08-25-02`  
> 增量说明：本轮在上轮（2026-08-18-01，20 条基底 intent）基础上，**补充 `ui_candidate` 标注**并**新增 8 条 UI 专项安全 intent**（INTENT-SEC-021 ~ 028），重点覆盖可通过 Web UI 验证的安全防御场景。

---

## 基底 intent（复用自 2026-08-18-01，格式已更新）

### INTENT-SEC-001
```
id: INTENT-SEC-001
dimensions: [security]
attack_surface: 目标仓库 secrets（项目级/组织级 Secret）
untrusted_actor: 外部 fork 贡献者（无仓库写权限的第三方账号）
sensitive_asset: secrets.PROD_DEPLOY_KEY、secrets.REGISTRY_PASSWORD 等项目级/组织级密钥
negative_goal: 外部 fork PR 在 pull_request 事件触发的工作流中通过 ${{ secrets.X }} 或环境变量注入读取到真实 secret 值。
priority: P0
ui_candidate: true
threat_category: Info Disclosure（STRIDE-I）
rationale: fork PR secret 隔离是 CI/CD 平台安全命脉。一旦失效，外部贡献者可瞬间窃取部署密钥、容器 registry 密码等核心凭证，导致供应链灾难。
expected_behavior: fork 来源的 workflow 在 pull_request 事件下执行时，secrets 上下文为空或不可解析，任何读取尝试均返回空值/失败。日志中不得出现 secret 明文。
evidence: 1) Web UI 运行日志中 `echo "${{ secrets.XXX }}"` 输出为空或 `***`；2) 环境变量注入后打印验证值为空；3) 运行结果 API 返回的 secrets 上下文字段为空对象。
```

### INTENT-SEC-002
```
id: INTENT-SEC-002
dimensions: [security]
attack_surface: 工作流运行日志脱敏引擎
untrusted_actor: 任何可在 workflow 中执行命令的账号（含外部 fork PR 在自有代码中执行的步骤）
sensitive_asset: secrets.XXX 的原始字节序列
negative_goal: 通过 echo "${{ secrets.XXX }}" | base64、前缀+secret+后缀拼接、printf 单字符输出等方式在日志中还原 secret 明文。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / 日志脱敏绕过
rationale: GitCode 文档自承 `${{ secrets.X }}` 可能绕过脱敏。base64 编码、拼接、多行分割是业界最常见的 masking 绕过手段，必须在引擎层防御。
expected_behavior: 无论 secret 经过何种转换（拼接、编码、分割、多行），只要最终输出包含 secret 原始子串，日志中对应部分均应被替换为 `***`。
evidence: 1) Web UI 中打开完整运行日志，用 secret 原始值及其 base64 编码串做子串搜索，命中数为 0；2) 对多行 secret 的每一行均执行子串搜索，命中数为 0。
```

### INTENT-SEC-003
```
id: INTENT-SEC-003
dimensions: [security]
attack_surface: Artifact 上传接口 / Cache 存储后端
untrusted_actor: 拥有仓库读权限的账号（含外部 fork PR 在允许写 artifact 的场景）
sensitive_asset: secrets.XXX 原始值、ATOMGIT_TOKEN 明文
negative_goal: 工作流将 $SECRET 或 ${{ secrets.XXX }} 写入文件后通过 upload-artifact 上传，或被 cache 插件打包进缓存包。
priority: P0
ui_candidate: false
threat_category: Info Disclosure / 持久化存储泄露
rationale: 即使日志脱敏正常，若 workflow 将含 secret 的文件上传为 artifact 或写入 cache，后续运行或外部下载仍可读取。这是 secret 泄露的第二条路径。
expected_behavior: artifact 与 cache 内容不参与 secret 脱敏；系统应阻止将 secret 明文写入持久化存储，或通过扫描机制在上传前拦截。
evidence: 1) 下载 artifact 压缩包并全文扫描 secret 原始值，命中数为 0；2) 恢复 cache 后遍历缓存目录，扫描 secret 原始值，命中数为 0。
```

### INTENT-SEC-004
```
id: INTENT-SEC-004
dimensions: [security]
attack_surface: `run:` 脚本步骤的 shell 命令解析器
untrusted_actor: 外部 fork 贡献者（可控制 PR 标题、分支名、commit message）
sensitive_asset: Runner 执行环境、ATOMGIT_TOKEN、仓库代码、后续步骤的权限上下文
negative_goal: 在 `run: echo "${{ atomgit.event.pull_request.title }}"` 中，若标题包含 shell 元字符，不得触发额外命令执行。
priority: P0
ui_candidate: true
threat_category: Elevation（权限提升）/ CWE-74（Injection）
rationale: 脚本注入是 Actions 平台历史上最高频的漏洞类。PR 标题、分支名、commit message 等不可信输入直接拼接到 shell 命令中，可导致任意命令执行。
expected_behavior: 平台将不可信输入视为纯字符串字面量，在注入 shell 前完成转义或禁止内联求值；或 runner 在解析 `${{ }}` 时对其中的上下文值做安全转义。
evidence: 1) Web UI 运行日志中仅出现预期的 echo 输出，无注入命令的副作用痕迹；2) 若平台采用防御性求值，日志中应出现明确的解析/拒绝错误；3) 运行结束后的文件系统快照不得出现注入命令创建的新文件。
```

### INTENT-SEC-005
```
id: INTENT-SEC-005
dimensions: [security]
attack_surface: `run:` 脚本步骤 / `env:` 环境变量赋值
untrusted_actor: 任何可发表评论、可推送代码、可手动触发 workflow 的外部/内部用户
sensitive_asset: Runner 环境、Token、内网可达服务
negative_goal: 通过 issue 评论正文嵌入 shell 元字符，workflow 被触发后不得执行非预期命令。
priority: P0
ui_candidate: true
threat_category: Elevation / CWE-74（Injection）
rationale: 除 PR 元数据外，issue 评论、手动触发输入、commit message 等同样属于不可信输入，存在同类注入面。攻击面不可遗漏。
expected_behavior: 所有来自外部用户输入的上下文字段（`atomgit.event.comment.body`、`inputs.*`、`atomgit.event.head_commit.message`）在嵌入 `run:` 前均经过安全处理。
evidence: 1) Web UI 日志中仅显示输入的纯文本表示，无命令执行副作用；2) 环境变量注入后，子 shell 中 `echo $VAR` 输出为纯文本而非被二次解析执行；3) 网络出口监控（如有）不得记录运行期间的非预期出站连接。
```

### INTENT-SEC-006
```
id: INTENT-SEC-006
dimensions: [security]
attack_surface: Step 间环境变量/输出传递机制
untrusted_actor: 任何可在当前 job 的前序 step 中执行代码的账号
sensitive_asset: 后续 step 的执行环境、PATH 变量、步骤输出值
negative_goal: 向 `$ATOMGIT_ENV` 写入换行注入内容污染后续环境变量；向 `$ATOMGIT_OUTPUT` 写入伪造的 step 输出键值对。
priority: P0
ui_candidate: false
threat_category: Tampering（篡改）/ CWE-74（Injection）
rationale: ATOMGIT_ENV / ATOMGIT_OUTPUT 文件协议是 step 间通信的桥梁。若缺乏格式校验，攻击者可通过换行注入、路径遍历污染整个 job 的执行上下文。
expected_behavior: Runner 在读取 ATOMGIT_ENV / ATOMGIT_OUTPUT 文件时，对键名和值做格式校验，拒绝包含换行注入、路径遍历、空字节的内容。
evidence: 1) 后续 step 中执行 `env | grep EVIL_` 结果为空；2) `echo $PATH` 与初始 PATH 相比仅含预期追加目录；3) 读取 steps.<id>.outputs.<name> 得到预期值而非伪造值。
```

### INTENT-SEC-007
```
id: INTENT-SEC-007
dimensions: [security]
attack_surface: pull_request_target 事件下的高权限 Runner 环境
untrusted_actor: 外部 fork 贡献者（其代码被 checkout 到本地运行）
sensitive_asset: ATOMGIT_TOKEN（写权限）、项目 secrets、内网可达接口
negative_goal: 在 pull_request_target workflow 中 checkout `atomgit.event.pull_request.head.sha` 后，不可信代码试图读取 `$ATOMGIT_TOKEN` 或 `${{ secrets.XXX }}` 并外发。
priority: P0
ui_candidate: true
threat_category: Elevation / 高权限上下文执行不可信代码
rationale: `pull_request_target` 使用目标仓库 workflow + 拥有写权限 + 可访问 secret，若显式 checkout head.sha 并运行其中脚本，等于高权限运行不可信代码。这是 GitHub Actions 历史上最臭名昭著的安全陷阱。
expected_behavior: 即使处于 pull_request_target 上下文，若 workflow 显式运行了不可信代码，secret 和 token 的泄露面仍被最小化（其他防御层仍然生效）。
evidence: 1) Web UI 日志中 ATOMGIT_TOKEN 值为 `***` 或被掩码；2) secrets 相关输出被遮蔽；3) artifact/cache 中不得出现 token 明文；4) 网络层未观测到向公网地址的异常 HTTP 请求。
```

### INTENT-SEC-008
```
id: INTENT-SEC-008
dimensions: [security]
attack_surface: pull_request_target 事件的 workflow 解析与加载路径
untrusted_actor: 外部 fork 贡献者（尝试通过 PR 修改 workflow 文件以影响执行逻辑）
sensitive_asset: 高权限 workflow 执行逻辑、ATOMGIT_TOKEN、secrets
negative_goal: fork PR 中修改 `.gitcode/workflows/pr-target.yml` 加入恶意 step，该修改不得在 `pull_request_target` 触发时被加载执行。
priority: P0
ui_candidate: false
threat_category: Tampering / Spoofing（欺骗）
rationale: `pull_request_target` 的安全基石之一是"执行目标仓库的 workflow 版本"。若平台实现缺陷导致实际执行了 fork 中的 workflow 版本，攻击者可直接在高权限上下文中植入恶意步骤。
expected_behavior: pull_request_target 触发时，Runner 拉取的 `.gitcode/workflows/*.yml` 始终来自目标仓库的默认分支（或 base 分支）版本，与 PR 中的 workflow 修改无关。
evidence: 1) 运行日志中的步骤列表与 base 分支 workflow 定义一致；2) 在恶意 PR 中新增 step 后，pull_request_target 运行未执行该 step；3) Runner 工作区中的 `.gitcode/workflows/` 文件内容与 base 分支一致。
```

### INTENT-SEC-009
```
id: INTENT-SEC-009
dimensions: [security]
attack_surface: Cache 存储后端 key 作用域与隔离策略
untrusted_actor: 外部 fork 贡献者
sensitive_asset: 主分支构建产物完整性、依赖包完整性、后续运行时的 Runner 环境
negative_goal: fork PR 的 workflow 使用与主分支相同的 cache key 写入被污染的缓存包，主分支后续运行恢复该 cache。
priority: P1
ui_candidate: false
threat_category: Tampering / 供应链投毒
rationale: 若 fork PR 写入了与主分支相同 key 的 cache，后续主分支运行恢复该 cache 时将引入不可信数据（如篡改的依赖包、预编译恶意二进制）。这是供应链投毒的经典路径。
expected_behavior: fork PR 产生的 cache 与目标仓库主分支 cache 在存储层完全隔离，或至少 key 命名空间隔离，主分支运行永远不会命中 fork PR 写入的 cache。
evidence: 1) fork PR 运行后向 cache 写入标记文件（如 `.FORK_POISONED`）；2) 主分支新触发运行恢复相同 key 的 cache；3) 恢复后检查缓存目录，标记文件不得存在；4) 对关键依赖文件做哈希比对，应与主分支原始值一致。
```

### INTENT-SEC-010
```
id: INTENT-SEC-010
dimensions: [security]
attack_surface: Cache 存储后端全局 key 空间
untrusted_actor: 仓库 A 的维护者（尝试读取/覆盖仓库 B 的 cache）
sensitive_asset: 其他仓库的缓存内容（可能含编译产物、内部路径信息、配置片段）
negative_goal: 仓库 A 的 workflow 声明与仓库 B 相同的 cache key，并成功恢复出仓库 B 的缓存内容。
priority: P1
ui_candidate: false
threat_category: Info Disclosure / Tampering
rationale: 若不同仓库使用相同 cache key，平台后端若未做仓库级隔离，A 仓库可读取/覆盖 B 仓库的 cache，造成信息泄露或投毒。
expected_behavior: cache key 在后端自动附加仓库级命名空间前缀，即使两个仓库声明完全相同的 key，实际存储路径也不相同。
evidence: 1) 仓库 B 向 cache 写入含唯一标记的文件；2) 仓库 A 使用相同 key 触发 cache restore；3) 仓库 A 恢复后的缓存目录中不得出现该唯一标记文件。
```

### INTENT-SEC-011
```
id: INTENT-SEC-011
dimensions: [security]
attack_surface: ATOMGIT_TOKEN 默认权限范围
untrusted_actor: 外部 fork 贡献者 / 低权限仓库成员
sensitive_asset: 仓库代码、PR/Issue 数据、Webhook 配置
negative_goal: 在 workflow 中不声明 permissions 时，fork PR 触发的工作流中的 ATOMGIT_TOKEN 获得 repository:write、pr:write 等写权限。
priority: P0
ui_candidate: false
threat_category: Elevation / 权限配置缺陷
rationale: GitCode 文档称"未声明 permissions 时使用仓库设置中定义的权限"，但默认值未明确；若默认包含 write 权限，低风险触发事件（如 fork PR）可能获得过高权限。
expected_behavior: 默认权限应遵循最小权限原则，至少对 fork PR 等外部触发场景默认为 read-only。
evidence: 1) 使用 ATOMGIT_TOKEN 调用仓库写 API（如推送 commit、创建 PR 评论）返回 HTTP 403；2) 运行日志中写操作步骤失败并提示权限不足；3) 仓库状态未因该 workflow 运行而发生非预期变更。
```

### INTENT-SEC-012
```
id: INTENT-SEC-012
dimensions: [security]
attack_surface: permissions 继承解析逻辑
untrusted_actor: 内部维护者（配置错误）/ 可修改 workflow 的攻击者
sensitive_asset: ATOMGIT_TOKEN 权限范围
negative_goal: 顶层声明 repository:write，某 job 仅声明 repository:read，但该 job 实际仍获得 write 权限。
priority: P0
ui_candidate: false
threat_category: Elevation / 权限继承缺陷
rationale: 若 job 级声明的 permissions 未能真正覆盖顶层，攻击者或配置错误可能导致本应受限的 job 继承过高权限。权限继承漏洞是 RBAC 系统的经典缺陷。
expected_behavior: job 级 permissions 显式声明后，该 job 的 ATOMGIT_TOKEN 权限仅由 job 级决定，与顶层无关；未声明的权限域默认 none。
evidence: 1) 在 job 中调用被禁止的权限 API 返回 403；2) 运行日志中权限拒绝错误明确指向该 job；3) 对比同 workflow 中未收窄权限的 job，后者可正常执行写操作（正向对照）。
```

### INTENT-SEC-013
```
id: INTENT-SEC-013
dimensions: [security]
attack_surface: 用户角色鉴权与 workflow 触发门禁
untrusted_actor: 组织内低权限成员（Developer/Reporter/外部协作者）
sensitive_asset: 组织级 secrets、环境保护规则、高权限 workflow 执行结果
negative_goal: Developer 角色用户手动触发仅允许 Maintainer 的 workflow_dispatch；Developer 读取组织级仅对 Owner 可见的 secret；Developer 通过 API 获取高权限 workflow 的运行日志。
priority: P0
ui_candidate: true
threat_category: Elevation / RBAC 提权
rationale: 若权限模型存在继承或绕过缺陷，低权限用户可能通过触发特定 workflow 或访问组织级 secret 实现提权。这是内部威胁的核心场景。
expected_behavior: 角色权限检查在 workflow 触发前和执行中均生效；Developer 无法访问 Owner 级别的环境 secret，无法触发仅限 Maintainer 的 workflow。
evidence: 1) 低权限账号调用 workflow_dispatch 触发受限 workflow 返回 HTTP 403；2) 该账号触发的 workflow 运行中 `${{ secrets.ORG_OWNER_SECRET }}` 为空；3) 该账号通过 API 查询其他高权限运行的日志返回 403；4) Web UI 中低权限用户看不到高权限 workflow 的"Run workflow"按钮或运行日志入口。
```

### INTENT-SEC-014
```
id: INTENT-SEC-014
dimensions: [security]
attack_surface: 第三方 action 的版本解析与加载
untrusted_actor: 第三方 action 维护者（账号被盗或主动作恶）
sensitive_asset: 所有引用该 action 的 workflow 的 Runner 环境、secrets、token
negative_goal: action 的 tag 被重写指向恶意 commit 后，使用 `uses: action@v4` 的 workflow 运行时不应静默执行恶意代码而不留下可审计痕迹。
priority: P1
ui_candidate: false
threat_category: Tampering / 供应链投毒
rationale: 使用浮动 ref（tag/branch）时，若 action 维护者恶意更新 tag 指向恶意 commit，或账号被盗，所有引用该 action 的 workflow 将在下次运行时执行恶意代码。这是供应链攻击的标杆场景。
expected_behavior: 平台应支持且推荐使用 commit SHA 固定 action 版本；若使用浮动 ref，平台在解析时应提供可见的审计信息（如实际解析到的 commit SHA 在日志中打印）。
evidence: 1) 修改某公开 action 的 tag 指向新 commit（在测试 fixture 中模拟）；2) 使用 `@tag` 的 workflow 运行后，日志中打印的解析 SHA 与新 commit 一致（证明确实被加载）；3) 使用 `@old-sha` 的 workflow 运行后，实际执行的代码仍为旧版本（证明 SHA pin 生效）。
```

### INTENT-SEC-015
```
id: INTENT-SEC-015
dimensions: [security]
attack_surface: 本地 action 路径解析器
untrusted_actor: 任何可修改 workflow 文件的账号
sensitive_asset: Runner 文件系统、相邻仓库代码
negative_goal: workflow 中使用 `uses: ../../../../etc/malicious-action` 或 `uses: /tmp/malicious-action` 并被成功加载执行。
priority: P1
ui_candidate: false
threat_category: Elevation / CWE-22（Path Traversal）
rationale: `uses: ./path` 若未做路径校验，攻击者可能通过 `../` 遍历引用 Runner 上的系统文件或其他仓库的 action，导致任意代码执行。
expected_behavior: Runner 在解析本地 action 路径时，将路径限制在 `$ATOMGIT_WORKSPACE` 之内，拒绝包含 `..` 或绝对路径的引用。
evidence: 1) workflow 运行状态为 failure；2) 错误日志明确提示本地 action 路径非法或超出工作区范围；3) 被遍历目标路径中的文件未被读取或执行。
```

### INTENT-SEC-016
```
id: INTENT-SEC-016
dimensions: [security]
attack_surface: Runner 工作区与运行时环境残留
untrusted_actor: 前一个运行的恶意 workflow（可能来自 fork 或被篡改的 action）
sensitive_asset: 前一个运行生成的临时文件、缓存凭证、源码片段、环境变量
negative_goal: job A 在 `/tmp/leak.txt` 或 `$ATOMGIT_WORKSPACE` 中写入标记文件并设置环境变量 `EVIL_VAR=1`，后续 job B 能读取到该文件或环境变量。
priority: P1
ui_candidate: false
threat_category: Info Disclosure / Tampering
rationale: 若 Runner 非一次性（ephemeral），前一个 job 写入的文件、环境变量、PATH 修改可能在后续 job 中残留，导致信息泄露或环境被污染。这对自托管 Runner 尤其危险。
expected_behavior: Runner 在 job 开始前清理工作区，或至少工作区隔离；环境变量在 job 间不传递（系统级除外）；PATH 修改不泄露到后续运行的其他仓库 job。
evidence: 1) job A 结束后 job B 启动；2) job B 中执行 `find /tmp -name 'leak-*'` 结果为空；3) job B 中执行 `env | grep EVIL_` 结果为空；4) job B 中 `echo $PATH` 不含 job A 追加的恶意目录。
```

### INTENT-SEC-017
```
id: INTENT-SEC-017
dimensions: [security]
attack_surface: Package 仓库上传/覆盖/删除接口
untrusted_actor: 低权限成员 / 被盗用的 CI token / 外部协作者
sensitive_asset: 已发布 package 的完整性与可追溯性
negative_goal: 使用 Developer 角色 token 重复上传已存在的 package 版本并成功覆盖；无权限用户删除已有 package 版本。
priority: P1
ui_candidate: true
threat_category: Tampering / 供应链投毒
rationale: 若 package 版本管理缺乏 immutable 保证，攻击者可上传同名同版本恶意包，污染下游用户。Package 不可变是制品库安全的基本原则。
expected_behavior: 已发布的 package 版本不可变；重复上传相同版本应被拒绝；删除/覆盖操作需高权限（Owner/Maintainer）且可能需二次确认。
evidence: 1) API/CLI 重复上传已有版本返回非 2xx 状态码；2) Web UI 中 Package 版本列表页显示"不可删除"或"不可覆盖"提示；3) 下载该版本并计算哈希，与首次发布时一致；4) 低权限账号在 UI 中看不到删除按钮或点击后返回 403。
```

### INTENT-SEC-018
```
id: INTENT-SEC-018
dimensions: [security]
attack_surface: Webhook 配置管理界面 / payload 接收端签名验证
untrusted_actor: 拥有仓库设置读权限的账号 / 网络中间人 / 可伪造 POST 请求的攻击者
sensitive_asset: Webhook secret、事件 payload 完整性
negative_goal: 在仓库设置页面查看 webhook 配置时，secret 字段回显明文；攻击者修改 payload 后投递，服务端未校验签名或校验逻辑存在绕过（如空签名通过）。
priority: P1
ui_candidate: true
threat_category: Info Disclosure / Tampering / Repudiation
rationale: Webhook 若缺乏签名验证或 secret 在界面可回显，可导致伪造事件投递、中间人攻击。这是 Webhook 安全的双重防线。
expected_behavior: Webhook secret 创建后仅可重置不可查看；平台对 webhook payload 使用 HMAC-SHA256 等签名；服务端验证签名不匹配时拒绝处理请求。
evidence: 1) Web UI 截图/接口响应中 secret 字段为掩码；2) 不带 `X-Hub-Signature` 头的请求返回 401/403；3) 使用错误 secret 计算的签名返回 401/403；4) 使用正确 secret 计算的签名返回 200。
```

### INTENT-SEC-019
```
id: INTENT-SEC-019
dimensions: [security]
attack_surface: 审计日志完整性与不可抵赖性
untrusted_actor: 内部攻击者（尝试清除痕迹）
sensitive_asset: 审计日志本身
negative_goal: 高权限用户修改他人角色、创建新 secret、手动触发部署 workflow 后，系统中无对应审计记录；低权限用户可通过 API 删除或篡改审计日志。
priority: P1
ui_candidate: true
threat_category: Repudiation（抵赖）/ 审计完整性
rationale: 若缺乏审计日志，安全事件发生后无法溯源攻击路径、无法判定影响范围。审计是事后取证与合规的根基。
expected_behavior: 关键操作（权限角色变更、secret 创建/更新/删除、workflow 触发尤其是 pull_request_target / 手动触发）均写入不可篡改的审计日志。
evidence: 1) 执行关键操作后，Web UI 审计日志页面中必须在 5 秒内出现对应记录；2) 记录中的 `actor`、`action`、`resource` 字段与实际操作一致；3) 低权限账号尝试删除审计日志返回 403；4) 审计日志记录不可被修改（尝试 PUT/PATCH 返回 405/403）。
```

### INTENT-SEC-020
```
id: INTENT-SEC-020
dimensions: [security]
attack_surface: 自托管 Runner 注册与管理接口
untrusted_actor: 拥有仓库/组织设置访问权限的账号 / 可读取 Runner 日志的攻击者
sensitive_asset: Runner 注册令牌、自托管资源池访问权限
negative_goal: 在自托管 Runner 配置页面查看已创建 Runner 的注册 token，系统再次明文展示；workflow 中通过 `env` 或日志意外打印出注册 token。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / Elevation（恶意 Runner 注册）
rationale: 自托管 Runner 的注册 token 若泄露，攻击者可向资源池注册恶意 Runner，拦截构建任务、窃取 secrets。这是基础设施安全的命脉。
expected_behavior: Runner 注册 token 在配置界面一次性展示后不可再次查看；token 不得出现在任何 workflow 运行日志或环境变量中。
evidence: 1) Web UI 中 Runner 管理界面查看历史 token，无"显示明文"按钮，或提示已过期/已轮换；2) 全局日志扫描（含所有 step 输出）不得匹配注册 token 的值；3) Runner 配置文件（如 `.runner`）权限为 600 且不含明文 token。
```

---

## 增量 intent（UI 专项，本轮新增）

### INTENT-SEC-021
```
id: INTENT-SEC-021
dimensions: [security]
attack_surface: Secret 管理 Web UI（项目设置 → Action 密钥与变量）
untrusted_actor: 任何拥有项目设置读权限的账号（含共享设备/屏幕共享场景下的合法用户）
sensitive_asset: Secret 原始值（如 DEPLOY_TOKEN、REGISTRY_PASSWORD）
negative_goal: 已创建的 secret 在 Web UI 的编辑/查看页面中以明文形式展示其原始值，或提供"显示明文"按钮/切换开关。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / STRIDE-I
rationale: Secret 一旦在 UI 中可回显，即失去了"仅对 workflow 运行时可见"的安全边界。共享屏幕、录屏、 shoulder surfing 均可导致泄露。这是 secret 管理的第一道 UI 防线。
expected_behavior: 创建 secret 后，在"Action 密钥与变量"页面中，secret 的值字段始终显示为掩码（如 `****` 或空值），不提供任何查看明文的功能。用户只能通过"更新"操作覆盖为新值。
evidence: 1) 登录仓库设置页面，进入"Action 密钥与变量"；2) 在已创建的 secret 行中，Value 字段为掩码状态，无"眼睛"图标或"显示"链接；3) 点击"编辑"进入更新弹窗，原值字段为空或显示占位符，不回显真实值；4) 检查浏览器 DevTools Network 中加载 secret 列表的 API 响应，value 字段为空或已被服务端掩码。
```

### INTENT-SEC-022
```
id: INTENT-SEC-022
dimensions: [security]
attack_surface: 仓库设置页面的 secrets 可见性控制
untrusted_actor: 外部 fork 贡献者（无目标仓库写权限的第三方账号）
sensitive_asset: Secret 名称列表及存在性信息（攻击者可据此推断系统架构与攻击面）
negative_goal: 外部 fork 贡献者通过 Web UI 导航到目标仓库的"Action 密钥与变量"页面，并成功看到 secrets 列表（即使值为空，名称也不应暴露）。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / STRIDE-I
rationale: Secret 名称本身也是敏感信息（如 `PROD_DEPLOY_KEY` 泄露了部署目标）。fork 贡献者不应通过 UI 得知目标仓库使用了哪些 secret，这是信息泄露的纵深防御。
expected_behavior: 外部 fork 贡献者在目标仓库的 Web UI 中，"项目设置"菜单下不显示"Action 密钥与变量"入口；或直接访问该页面 URL 时返回 403/404。
evidence: 1) 以 fork 贡献者身份登录 Web UI，进入目标仓库；2) 点击"项目设置"，侧边栏/菜单中不存在"Action 密钥与变量"选项；3) 直接浏览器地址栏输入该设置页的 URL，服务端返回 403 Forbidden 或重定向到仓库首页；4) API 调用获取 secrets 列表返回 403。
```

### INTENT-SEC-023
```
id: INTENT-SEC-023
dimensions: [security]
attack_surface: Workflow 运行日志 Web UI（运行详情 → Step 日志）
untrusted_actor: 任何可查看运行日志的账号（包括外部协作者、Reporter 角色）
sensitive_asset: Secret 值、ATOMGIT_TOKEN 明文、环境变量中的敏感信息
negative_goal: 在 Web UI 的运行日志详情页中，包含 secret 值的输出行以原始明文展示，未被替换为 `***`。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / 日志脱敏绕过
rationale: 运行日志是协作调试的核心界面，访问面远大于 API。若 UI 中的日志未做 masking，低权限协作者即可直接截图窃取 secret。这是 masking 机制的 UI 层验证。
expected_behavior: 无论 secret 以何种方式输出（直接 echo、环境变量打印、命令参数暴露），Web UI 的日志渲染层均应将匹配的 secret 子串替换为 `***`。
evidence: 1) 在 Web UI 中打开某 workflow 运行详情页；2) 展开包含 `echo "${{ secrets.XXX }}"` 的 step 日志；3) 目视检查日志中 secret 值显示为 `***`；4) 使用浏览器查找功能（Ctrl+F）搜索 secret 原始值的子串，命中数为 0；5) 对 base64 编码后的 secret 同样执行 UI 层查找，命中数为 0。
```

### INTENT-SEC-024
```
id: INTENT-SEC-024
dimensions: [security]
attack_surface: 环境级 Secret 的审批规则 UI 与执行门禁
untrusted_actor: 无审批权限的仓库成员（Developer/Reporter）
sensitive_asset: 环境级 secret（如生产环境部署密钥）
negative_goal: 未经审批的 workflow 运行成功获取到环境级 secret，或 UI 中非审批人可点击"跳过审批""强制继续"等按钮。
priority: P1
ui_candidate: true
threat_category: Elevation / 审批绕过
rationale: 环境级 secret 通常对应生产环境凭证，是最后一道人工审核防线。若审批规则在 UI 层被绕过，攻击者可直接触发生产部署而无需任何人知情。
expected_behavior: 配置环境审批人（reviewers）后，需要该环境 secret 的 workflow 在运行到对应 job 时进入"等待审批"状态；Web UI 中仅审批人可见"批准"按钮，非审批人仅能看到"等待中"状态且无法干预。
evidence: 1) 以 Maintainer 身份在 UI 中配置环境"production"的审批人为 Owner A；2) 以 Developer 身份触发需要 `environment: production` 的 workflow；3) Web UI 运行详情页显示该 job 状态为 "waiting for approval"；4) Developer 视角的 UI 中不存在"批准"或"拒绝"按钮；5) Owner A 登录后可在同一页面看到审批操作入口；6) 未经审批前，workflow 无法继续执行，且 secrets 上下文中不包含该环境 secret。
```

### INTENT-SEC-025
```
id: INTENT-SEC-025
dimensions: [security]
attack_surface: Workflow 触发与日志访问的 UI 权限控制
untrusted_actor: 组织内低权限成员（Developer/Reporter）
sensitive_asset: 高权限 workflow 的运行结果、日志中的敏感信息、secrets 引用痕迹
negative_goal: 低权限角色通过 Web UI 查看或触发仅限 Maintainer/Owner 的高权限 workflow（如部署 workflow、secret 清理 workflow）。
priority: P0
ui_candidate: true
threat_category: Elevation / RBAC 提权
rationale: UI 是权限控制的最直接表现。若后端已做权限限制但 UI 未同步（如按钮未禁用、页面未隐藏），用户可能通过前端按钮触发后端 403，但更大的风险是 UI 泄露了 workflow 存在性、运行历史或日志中的敏感上下文。
expected_behavior: 低权限角色在仓库的"Actions"或"流水线"页面中，看不到无权限访问的 workflow 卡片/列表；运行历史中无权限的运行日志条目被隐藏或置灰；直接访问运行日志 URL 返回 403。
evidence: 1) 以 Developer 身份登录 Web UI，进入仓库 Actions 页面；2) 仅对 Maintainer 可见的 workflow（如 `deploy-prod.yml`）不在左侧 workflow 列表中出现；3) 该 workflow 的历史运行记录不在运行列表中展示；4) 直接浏览器访问某高权限运行日志的 URL，返回 403 Forbidden；5) 以 Maintainer 身份登录同一页面，可正常查看该 workflow 与日志（对照）。
```

### INTENT-SEC-026
```
id: INTENT-SEC-026
dimensions: [security]
attack_surface: Personal Access Token（PAT）管理 Web UI
untrusted_actor: 可访问用户设置的账号（含共享设备、临时借用账号场景）
sensitive_asset: PAT 明文（具备 repo、admin:org 等 scope 的完整访问凭证）
negative_goal: 已创建的 PAT 在 Web UI 的详情/列表页面中可再次查看完整明文，或提供"显示 token"按钮。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / STRIDE-I
rationale: PAT 等同于用户密码，一旦泄露可长期冒用用户身份。业界标准（GitHub/GitLab）均只在创建时展示一次 token，之后永久掩码。GitCode 必须遵循同等安全水位。
expected_behavior: PAT 创建时仅在弹窗/页面中展示一次完整 token；此后在 PAT 列表页和详情页中，token 字段显示为掩码（如 `ghp_****xxxx` 仅展示后 4 位）或完全隐藏，无查看明文入口。
evidence: 1) 登录用户设置 → PAT 管理；2) 创建新 PAT，记录弹窗中展示的完整 token；3) 关闭弹窗后，在 PAT 列表页中该 token 显示为掩码；4) 点击"编辑/详情"进入 PAT 详情页，token 字段不回显明文；5) 检查浏览器 DevTools Network 中加载 PAT 列表的 API 响应，token 字段为空或已被服务端掩码。
```

### INTENT-SEC-027
```
id: INTENT-SEC-027
dimensions: [security]
attack_surface: 组织级 Secret 的仓库范围隔离 UI
untrusted_actor: 组织内未被授权的仓库成员
sensitive_asset: 组织级 secret 的值与存在性
negative_goal: 组织级 secret 被错误地展示给未在白名单中的仓库；或在未授权仓库的 workflow 运行中通过 secrets 上下文成功读取。
priority: P1
ui_candidate: true
threat_category: Info Disclosure / 权限配置缺陷
rationale: 组织级 secret 通常跨多个仓库共享（如统一容器 registry 凭证）。若范围控制失效， secret 可能泄露给组织内不应访问的仓库成员，扩大攻击面。
expected_behavior: 在 UI 中创建组织级 secret 并指定仅对仓库 A、B 可见后，仓库 C 的"Action 密钥与变量"页面中不出现该 secret；仓库 C 的 workflow 中 `${{ secrets.ORG_SECRET }}` 解析为空。
evidence: 1) 以 Owner 身份在组织设置中创建 secret `ORG_DEPLOY_KEY`，并设置仅对仓库 A 可见；2) 以仓库 B 的 Maintainer 身份登录 UI，进入仓库 B 的"Action 密钥与变量"页面；3) 该页面中不存在 `ORG_DEPLOY_KEY`；4) 在仓库 B 触发 workflow，步骤中打印 `${{ secrets.ORG_DEPLOY_KEY }}`，日志中输出为空或 `***`（若为空值则不应被 mask，需确认实际为空）；5) 以仓库 A 的 Maintainer 身份登录，确认该 secret 正常可见且 workflow 中可正常读取（对照）。
```

### INTENT-SEC-028
```
id: INTENT-SEC-028
dimensions: [security]
attack_surface: Workflow 运行详情页的 secrets/环境变量展示面板
untrusted_actor: 任何可查看运行详情页的低权限账号
sensitive_asset: Secret 名称列表、环境变量键值对
negative_goal: 来自 fork PR 的 workflow 运行在 Web UI 详情页中，仍向查看者展示 secrets 名称列表或环境变量中的敏感键值对。
priority: P0
ui_candidate: true
threat_category: Info Disclosure / 上下文泄露
rationale: fork PR 的运行天然处于低信任上下文。即使 secret 值为空，展示 secrets 名称列表也会向外部贡献者泄露目标仓库的安全架构（如使用了哪些第三方服务、部署目标等）。
expected_behavior: fork PR 触发的 workflow 运行详情页中，"Secrets"或"环境变量"面板应显示为"不可用""无权限"或完全隐藏；即使查看者是仓库 Owner，该运行实例的 secrets 上下文也因事件类型限制而空。
evidence: 1) 以外部 fork 贡献者身份触发 pull_request 事件 workflow；2) 以仓库 Maintainer 身份登录 Web UI，打开该运行详情页；3) 查看"环境变量"或"Secrets"标签页，确认不展示任何 secret 名称或值；4) 页面提示"fork PR 运行无法访问 secrets"或类似说明；5) 以 push 事件触发的运行详情页作为对照，确认正常展示 secrets 名称（值为掩码）。
```

---

## 质量自检清单

- [x] 每条 intent 有明确的「不应发生」负向目标。
- [x] 基底 intent（001~020）覆盖 fork PR / `pull_request_target` / secret masking / 脚本注入 / action pin / cache 投毒 / RBAC / 审计 / Runner 注册 token。
- [x] 增量 intent（021~028）全部标注 `ui_candidate: true`，专注 Web UI 可验证的安全防御场景。
- [x] 全部 28 条 intent 均给出确定性判定证据（UI 元素检查、API 响应码、日志扫描、权限对照）。
- [x] 优先级取自风险登记册，P0 覆盖全部安全 blocker 项。
- [x] 无真实密钥/token/内网地址，全部使用占位符。
- [x] 仅产防御性验收目标，未提供可直接利用的攻击 payload、exploit 代码或绕过步骤。
- [x] 总 intent 数：28 条（基底 20 + 增量 8）。

---

## 人工复审提示

> 建议由熟悉 CI/CD 攻击面（尤其 GitHub Actions 历史漏洞）的安全工程师对本产出进行人工复审，重点确认：
> 1. UI 专项 intent（021~028）是否覆盖了 GitCode Web 界面中所有可独立验证的安全控制点；
> 2. `ui_candidate: true` 的标注是否准确——是否存在需要混合 API + UI 才能判定、纯 UI 无法闭环的场景；
> 3. 自托管 Runner 内网场景下，是否需额外增加网络隔离/出站策略的 UI 验证 intent（如 Runner 管理页面中的网络策略配置）。
