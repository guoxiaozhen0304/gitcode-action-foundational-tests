# Security Intents — 防御性验收目标

> 维度：`security`  
> 产出日期：2026-08-18  
> Agent：security agent（攻击面测绘师 / 防御性安全评审）

---

## 缺失输入清单及退化影响

| 缺失输入 | 预期路径 | 退化影响 |
|---------|---------|---------|
| `security-knowledge/`（GitHub Actions 安全加固手册、公开 CVE 模式分析） | `phase01/inputs/security-knowledge/` | 无法直接引用已知 CVE 编号与加固对照表；威胁类别描述退化为 STRIDE + 通用 CI/CD 攻击面标签，缺少具体 CVE 溯源。 |
| `business-context/`（部署模型、历史安全问题） | `phase01/inputs/business-context/` | 无法评估自托管 Runner 是否部署于内网、无法基于历史安全事故调整概率；Runner 内网逃逸攻击面仅做通用假设，未针对特定网络拓扑加固。 |

> 本产出中所有密钥、token、内网地址均以占位符表示（如 `DEPLOY_TOKEN`、`ATOMGIT_TOKEN`、`prod-server.example.com`）。

---

## 一、Secrets 与 Fork 隔离

### INTENT-SEC-001
```
意图 ID:    INTENT-SEC-001
维度标签:   [security]
标题:       fork PR 触发 pull_request 事件时严禁读取目标仓库 secrets

风险点:     RISK-SEC-01（fork PR 读到仓库 secrets）——外部贡献者通过 fork 提 PR，若平台 secret 隔离失效，可直接窃取项目级/组织级密钥。
预期系统行为: fork 来源的 workflow 在 pull_request 事件下执行时，secrets 上下文为空或不可解析，任何读取尝试均返回空值/失败。
Oracle 来源: GitCode规格（pr-mr-pipeline-security.md、using-secrets.md）

攻击面:     目标仓库 secrets（项目级/组织级 Secret）
不可信主体: 外部 fork 贡献者（无仓库写权限的第三方账号）
敏感资产:   secrets.PROD_DEPLOY_KEY、secrets.REGISTRY_PASSWORD 等项目级/组织级密钥
应防住的行为: 外部 fork PR 在 pull_request 事件触发的工作流中通过 ${{ secrets.X }} 或环境变量注入读取到真实 secret 值。
负向断言目标: 工作流日志中不得出现 secret 明文；通过 API 查询工作流运行详情不得返回 secret 值；fork PR 运行状态中 secrets 相关步骤不得标记为成功获取非空值。
判定证据:   1) 工作流运行日志中 `echo "${{ secrets.XXX }}"` 输出为空或 `***`；2) 环境变量注入后打印验证值为空；3) 运行结果 API 返回的 `secrets` 上下文字段为空对象。
威胁类别:   Info Disclosure（信息泄露）/ STRIDE-I

验证要点:
  - [负向] 外部 fork PR 的 workflow 中 `${{ secrets.TEST_SECRET }}` 不得解析出真实值
  - [负向] 将 secret 注入 env 后打印，日志中不得出现真实值
  - [非功能] 判定需在运行完成后的日志与 API 响应中双重确认

优先级线索: RISK-SEC-01（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/pr-mr-pipeline-security.md`（fetched 2026-07-20）; `gitcode-spec/security-permissions/using-secrets.md`
```

### INTENT-SEC-002
```
意图 ID:    INTENT-SEC-002
维度标签:   [security]
标题:       secret 表达式脱敏机制不得被基础绕过手段穿透

风险点:     GitCode 文档自承 `${{ secrets.X }}` 可能绕过脱敏（using-secrets.md）。攻击者可能通过拼接、base64 编码、多行输出等方式让 secret 值逃离 `***` 替换。
预期系统行为: 无论 secret 经过何种转换（拼接、编码、分割、多行），只要最终输出包含 secret 原始子串，日志中对应部分均应被替换为 `***`。
Oracle 来源: GitCode规格（using-secrets.md）

攻击面:     工作流运行日志脱敏引擎
不可信主体: 任何可在 workflow 中执行命令的账号（含外部 fork PR 在自有代码中执行的步骤）
敏感资产:   secrets.XXX 的原始字节序列
应防住的行为: 通过 `echo "${{ secrets.XXX }}" | base64`、`echo "prefix${{ secrets.XXX }}suffix"`、`printf '%s' '${{ secrets.XXX }}'` 等方式在日志中还原 secret 明文。
负向断言目标: 运行日志全文扫描不得匹配 secret 原始值或其常见变形（base64、urlencode、单字符分割拼接后的重组串）。
判定证据:   1) 抓取完整运行日志文本，用 secret 原始值及其 base64 编码串做子串搜索，命中数为 0；2) 对多行 secret 的每一行均执行子串搜索，命中数为 0。
威胁类别:   Info Disclosure / 日志脱敏绕过

验证要点:
  - [负向] base64 编码后的 secret 不得出现在日志中
  - [负向] 前缀+secret+后缀的拼接输出中，secret 部分应被 `***` 替换
  - [负向] 多行 secret 的任意单行不得泄露

优先级线索: RISK-SEC-05（P0 blocker）+ RISK-SEC-01 关联
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/using-secrets.md`（文档自承可能绕过）
```

### INTENT-SEC-003
```
意图 ID:    INTENT-SEC-003
维度标签:   [security]
标题:       secret 值不得通过制品（artifact）或缓存元数据外泄

风险点:     即使日志脱敏正常，若 workflow 将含 secret 的文件上传为 artifact 或写入 cache，后续运行或外部下载仍可读取。
预期系统行为: artifact 与 cache 内容不参与 secret 脱敏；系统应阻止将 secret 明文写入持久化存储，或通过扫描机制在上传前拦截。
Oracle 来源: GitCode规格（using-secrets.md 提示“不要把 secret 写入制品或缓存”）+ 通用 CI/CD 安全最佳实践

攻击面:     Artifact 上传接口 / Cache 存储后端
不可信主体: 拥有仓库读权限的账号（含外部 fork PR 在允许写 artifact 的场景）
敏感资产:   secrets.XXX 原始值、ATOMGIT_TOKEN 明文
应防住的行为: 工作流将 `$SECRET` 或 `${{ secrets.XXX }}` 写入文件后通过 upload-artifact 上传，或被 cache 插件打包进缓存包。
负向断言目标: 下载该 artifact 或恢复该 cache 后，内部文件中不得出现 secret 原始值或 ATOMGIT_TOKEN 明文。
判定证据:   1) 下载 artifact 压缩包并全文扫描 secret 原始值，命中数为 0；2) 恢复 cache 后遍历缓存目录，扫描 secret 原始值，命中数为 0。
威胁类别:   Info Disclosure / 持久化存储泄露

验证要点:
  - [负向] artifact 文件内容不得包含 secret 明文
  - [负向] cache 包解压后不得包含 secret 明文

优先级线索: RISK-SEC-05（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/using-secrets.md`; `gitcode-spec/core-concepts/artifacts-and-cache.md`
```

---

## 二、表达式注入与不可信输入

### INTENT-SEC-004
```
意图 ID:    INTENT-SEC-004
维度标签:   [security]
标题:       不可信 PR 元数据（标题/分支名/提交信息）不得注入 run 脚本导致命令执行

风险点:     RISK-SEC-02（脚本注入）——PR 标题、分支名、commit message 等来自不可信输入，若直接拼接到 `run:` 命令中，可导致任意命令执行。
预期系统行为: 平台将不可信输入视为纯字符串字面量，在注入 shell 前完成转义或禁止内联求值；或 runner 在解析 `${{ }}` 时对其中的上下文值做安全转义。
Oracle 来源: GitHub行为（业界公认高危漏洞类）+ GitCode规格（expressions.md、using-script-commands.md）

攻击面:     `run:` 脚本步骤的 shell 命令解析器
不可信主体: 外部 fork 贡献者（可控制 PR 标题、分支名、commit message）
敏感资产:   Runner 执行环境、ATOMGIT_TOKEN、仓库代码、后续步骤的权限上下文
应防住的行为: 在 `run: echo "${{ atomgit.event.pull_request.title }}"` 中，若标题包含 `"; cat /etc/passwd; #` 之类的载荷，不得触发额外命令执行。
负向断言目标: 工作流运行日志中不得出现注入命令的执行痕迹（如 `/etc/passwd` 内容输出、非预期网络请求、非预期进程创建）；运行状态不得因注入命令而改变为预期外的 success/failure。
判定证据:   1) 运行日志中仅出现预期的 echo 输出，无注入命令的副作用痕迹；2) 若平台采用防御性求值（如拒绝执行含可疑字符的表达式），日志中应出现明确的解析/拒绝错误；3) 运行结束后的文件系统快照不得出现注入命令创建的新文件。
威胁类别:   Elevation（权限提升）/ CWE-74（Injection）

验证要点:
  - [负向] 含反引号、分号、管道符的 PR 标题不得触发命令执行
  - [负向] 含 `${{ }}` 嵌套或 Unicode 同形字符的分支名不得逃逸表达式边界
  - [正向] 正常无害标题应能正常打印

优先级线索: RISK-SEC-02（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/syntax-reference/expressions.md`; `gitcode-spec/core-concepts/variables-secrets-context-expressions.md`
```

### INTENT-SEC-005
```
意图 ID:    INTENT-SEC-005
维度标签:   [security]
标题:       issue_comment / workflow_dispatch 等事件中的不可信输入不得注入脚本

风险点:     除 PR 元数据外，issue 评论、手动触发输入、commit message 等同样属于不可信输入，存在同类注入面。
预期系统行为: 所有来自外部用户输入的上下文字段（`atomgit.event.comment.body`、`inputs.*`、`atomgit.event.head_commit.message`）在嵌入 `run:` 前均经过安全处理。
Oracle 来源: GitHub行为 + GitCode规格

攻击面:     `run:` 脚本步骤 / `env:` 环境变量赋值
不可信主体: 任何可发表评论、可推送代码、可手动触发 workflow 的外部/内部用户
敏感资产:   Runner 环境、Token、内网可达服务
应防住的行为: 通过 issue 评论正文嵌入 shell 元字符，workflow 被触发后不得执行非预期命令。
负向断言目标: 运行日志中不得出现注入命令的输出或副作用；workflow 不得因输入中的 shell 特殊字符而异常终止或跳过安全步骤。
判定证据:   1) 日志中仅显示输入的纯文本表示，无命令执行副作用；2) 环境变量注入后，子 shell 中 `echo $VAR` 输出为纯文本而非被二次解析执行；3) 网络出口监控（如有）不得记录运行期间的非预期出站连接。
威胁类别:   Elevation / CWE-74（Injection）

验证要点:
  - [负向] issue 评论含 shell 元字符时不得触发命令执行
  - [负向] workflow_dispatch inputs 含控制字符时不得注入

优先级线索: RISK-SEC-02（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/core-concepts/trigger-events.md`; `gitcode-spec/syntax-reference/expressions.md`
```

### INTENT-SEC-006
```
意图 ID:    INTENT-SEC-006
维度标签:   [security]
标题:       通过 ATOMGIT_ENV / ATOMGIT_OUTPUT 文件写入的污染数据不得破坏后续步骤执行上下文

风险点:     攻击者若能在某 step 中控制写入 `$ATOMGIT_ENV` 或 `$ATOMGIT_OUTPUT` 的内容，可污染后续步骤的环境变量或输出，形成间接注入。
预期系统行为: Runner 在读取 ATOMGIT_ENV / ATOMGIT_OUTPUT 文件时，对键名和值做格式校验，拒绝包含换行注入、路径遍历、空字节的内容。
Oracle 来源: GitHub行为 + GitCode规格（workflow-commands.md）

攻击面:     Step 间环境变量/输出传递机制
不可信主体: 任何可在当前 job 的前序 step 中执行代码的账号
敏感资产:   后续 step 的执行环境、PATH 变量、步骤输出值
应防住的行为: 向 `$ATOMGIT_ENV` 写入 `EVIL_VAR=1\nLD_PRELOAD=/tmp/mal.so` 或利用多行语法污染后续环境；向 `$ATOMGIT_OUTPUT` 写入伪造的 step 输出键值对。
负向断言目标: 后续 step 的环境变量中不得出现攻击者注入的额外键；`PATH` 变量不得被篡改指向攻击者可控目录；步骤输出不得被覆盖为伪造值。
判定证据:   1) 后续 step 中执行 `env | grep EVIL_` 结果为空；2) `echo $PATH` 与初始 PATH 相比仅含预期追加目录；3) 读取 steps.<id>.outputs.<name> 得到预期值而非伪造值。
威胁类别:   Tampering（篡改）/ CWE-74（Injection）

验证要点:
  - [负向] ATOMGIT_ENV 写入含换行注入的内容不得污染后续环境变量
  - [负向] ATOMGIT_OUTPUT 不得被伪造为其他 step 的输出

优先级线索: RISK-SEC-02（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/syntax-reference/workflow-commands.md`
```

---

## 三、pull_request_target 高权限上下文

### INTENT-SEC-007
```
意图 ID:    INTENT-SEC-007
维度标签:   [security]
标题:       pull_request_target 事件中 checkout PR 头分支代码后不得直接执行不可信构建脚本

风险点:     RISK-SEC-03（pull_request_target checkout 不可信代码）——`pull_request_target` 使用目标仓库 workflow + 拥有写权限 + 可访问 secret，若显式 checkout `head.sha` 并运行其中脚本，等于高权限运行不可信代码。
预期系统行为: 平台不对用户 checkout 行为做强制限制，但测试需验证：若用户确实执行了此类危险模式，secret 和 token 的泄露面是否被最小化（即其他防御层是否仍然生效）。
Oracle 来源: GitCode规格（pr-mr-pipeline-security.md 明确提示风险）

攻击面:     pull_request_target 事件下的高权限 Runner 环境
不可信主体: 外部 fork 贡献者（其代码被 checkout 到本地运行）
敏感资产:   ATOMGIT_TOKEN（写权限）、项目 secrets、内网可达接口
应防住的行为: 在 `pull_request_target` workflow 中 checkout `atomgit.event.pull_request.head.sha` 后，不可信代码试图读取 `$ATOMGIT_TOKEN` 或 `${{ secrets.XXX }}` 并外发。
负向断言目标: 即使处于 pull_request_target 上下文，若 workflow 显式运行了不可信代码，日志中 secrets 仍应被 `***` 遮蔽；artifact/cache 中不得出现 token 明文；运行日志中不得出现非预期的外发网络请求痕迹。
判定证据:   1) 日志中 ATOMGIT_TOKEN 值为 `***` 或被掩码；2) secrets 相关输出被遮蔽；3) 网络层（如有监控）未观测到向公网地址的异常 HTTP 请求。
威胁类别:   Elevation / STRIDE-E（权限提升）/ 高权限上下文执行不可信代码

验证要点:
  - [负向] pull_request_target 下 checkout 不可信代码后，secret 脱敏机制仍应生效
  - [负向] 不可信代码试图通过环境变量读取 ATOMGIT_TOKEN 时，实际获得值应为空或被掩码
  - [非功能] 该 intent 重点验证“其他防御层在危险模式下是否仍然生效”，而非禁止 checkout 本身

优先级线索: RISK-SEC-03（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/pr-mr-pipeline-security.md`
```

### INTENT-SEC-008
```
意图 ID:    INTENT-SEC-008
维度标签:   [security]
标题:       pull_request_target 的 workflow 文件必须来自目标仓库 base 分支，不得被 fork 篡改

风险点:     `pull_request_target` 的安全基石之一是“执行目标仓库的 workflow 版本”。若平台实现缺陷导致实际执行了 fork 中的 workflow 版本，攻击者可直接在高权限上下文中植入恶意步骤。
预期系统行为: pull_request_target 触发时，Runner 拉取的 `.gitcode/workflows/*.yml` 始终来自目标仓库的默认分支（或 base 分支）版本，与 PR 中的 workflow 修改无关。
Oracle 来源: GitCode规格（pr-mr-pipeline-security.md）

攻击面:     pull_request_target 事件的 workflow 解析与加载路径
不可信主体: 外部 fork 贡献者（尝试通过 PR 修改 workflow 文件以影响执行逻辑）
敏感资产:   高权限 workflow 执行逻辑、ATOMGIT_TOKEN、secrets
应防住的行为: fork PR 中修改 `.gitcode/workflows/pr-target.yml` 加入恶意 step，该修改不得在 `pull_request_target` 触发时被加载执行。
负向断言目标: pull_request_target 运行日志中不得出现 fork PR 中新增的恶意 step 名称或命令；workflow 文件哈希应与 base 分支一致。
判定证据:   1) 运行日志中的步骤列表与 base 分支 workflow 定义一致；2) 在恶意 PR 中新增 step 后，pull_request_target 运行未执行该 step；3) Runner 工作区中的 `.gitcode/workflows/` 文件内容与 base 分支一致。
威胁类别:   Tampering / Spoofing（欺骗）

验证要点:
  - [负向] fork PR 修改 workflow 文件后，pull_request_target 运行不得加载修改后的版本
  - [正向] pull_request 事件（对比组）应加载 fork 中的 workflow 版本

优先级线索: RISK-SEC-03（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/pr-mr-pipeline-security.md`
```

---

## 四、Cache 投毒与隔离

### INTENT-SEC-009
```
意图 ID:    INTENT-SEC-009
维度标签:   [security]
标题:       fork PR 不得污染目标仓库主分支的 cache 内容

风险点:     RISK-SEC-04（cache 投毒）——若 fork PR 写入了与主分支相同 key 的 cache，后续主分支运行恢复该 cache 时将引入不可信数据（如篡改的依赖包、预编译恶意二进制）。
预期系统行为: fork PR 产生的 cache 与目标仓库主分支 cache 在存储层完全隔离，或至少 key 命名空间隔离，主分支运行永远不会命中 fork PR 写入的 cache。
Oracle 来源: GitCode规格未明确声明隔离策略（using-dependency-cache.md、artifacts-and-cache.md 均缺失 fork 隔离说明），属未知行为，需实测确认。

攻击面:     Cache 存储后端 key 作用域与隔离策略
不可信主体: 外部 fork 贡献者
敏感资产:   主分支构建产物完整性、依赖包完整性、后续运行时的 Runner 环境
应防住的行为: fork PR 的 workflow 使用与主分支相同的 cache key（如 `npm-Linux-package-lock.json-hash`）写入被污染的缓存包，主分支后续运行恢复该 cache。
负向断言目标: 主分支运行恢复 cache 后，缓存目录中的文件哈希与原始预期一致，不得出现 fork PR 中植入的额外文件或篡改内容。
判定证据:   1) fork PR 运行后向 cache 写入标记文件（如 `.FORK_POISONED`）；2) 主分支新触发运行恢复相同 key 的 cache；3) 恢复后检查缓存目录，标记文件不得存在；4) 对关键依赖文件做哈希比对，应与主分支原始值一致。
威胁类别:   Tampering / 供应链投毒

验证要点:
  - [负向] 主分支运行恢复的 cache 中不得出现 fork PR 植入的标记文件
  - [负向] 主分支运行恢复的 cache 中关键依赖文件哈希不得被篡改

优先级线索: RISK-SEC-04（P1）
破坏级别:   fixture
来源输入:   `gitcode-spec/writing-pipelines/using-dependency-cache.md`; `gitcode-spec/core-concepts/artifacts-and-cache.md`（文档未明确 fork 隔离策略，属 ❓ 未知项）
```

### INTENT-SEC-010
```
意图 ID:    INTENT-SEC-010
维度标签:   [security]
标题:       跨仓库 cache key 不得发生碰撞导致数据泄露或投毒

风险点:     若不同仓库使用相同 cache key（如通用语言 + OS 前缀），平台后端若未做仓库级隔离，A 仓库可读取/覆盖 B 仓库的 cache，造成信息泄露或投毒。
预期系统行为: cache key 在后端自动附加仓库级命名空间前缀，即使两个仓库声明完全相同的 key，实际存储路径也不相同。
Oracle 来源: 通用 CI/CD 安全最佳实践（GitHub Actions 的 cache 是仓库隔离的）

攻击面:     Cache 存储后端全局 key 空间
不可信主体: 仓库 A 的维护者（尝试读取/覆盖仓库 B 的 cache）
敏感资产:   其他仓库的缓存内容（可能含编译产物、内部路径信息、配置片段）
应防住的行为: 仓库 A 的 workflow 声明与仓库 B 相同的 cache key，并成功恢复出仓库 B 的缓存内容。
负向断言目标: 仓库 A 恢复 cache 后，缓存目录中不得出现仅属于仓库 B 的特征文件或路径。
判定证据:   1) 仓库 B 向 cache 写入含唯一标记的文件；2) 仓库 A 使用相同 key 触发 cache restore；3) 仓库 A 恢复后的缓存目录中不得出现该唯一标记文件。
威胁类别:   Info Disclosure / Tampering

验证要点:
  - [负向] 仓库 A 不得恢复出仓库 B 的 cache 内容
  - [正向] 同一仓库内使用相同 key 应能正常命中

优先级线索: RISK-SEC-04（P1）
破坏级别:   fixture
来源输入:   `gitcode-spec/core-concepts/artifacts-and-cache.md`
```

---

## 五、Token 与权限越界

### INTENT-SEC-011
```
意图 ID:    INTENT-SEC-011
维度标签:   [security]
标题:       未声明 permissions 时 ATOMGIT_TOKEN 默认权限不得过大

风险点:     RISK-SEC-06（权限越界）——GitCode 文档称“未声明 permissions 时使用仓库设置中定义的权限”，但默认值未明确；若默认包含 write 权限，低风险触发事件（如 fork PR）可能获得过高权限。
预期系统行为: 默认权限应遵循最小权限原则，至少对 fork PR 等外部触发场景默认为 read-only。
Oracle 来源: GitCode规格（token-permissions.md 声明“未声明时使用仓库设置中定义的权限”，但默认值未公开）

攻击面:     ATOMGIT_TOKEN 默认权限范围
不可信主体: 外部 fork 贡献者 / 低权限仓库成员
敏感资产:   仓库代码、PR/Issue 数据、Webhook 配置
应防住的行为: 在 workflow 中不声明 permissions 时，fork PR 触发的工作流中的 ATOMGIT_TOKEN 获得 repository:write、pr:write 等写权限。
负向断言目标: 不声明 permissions 的 workflow 中，fork PR 触发后使用 ATOMGIT_TOKEN 调用写接口（如推送代码、修改 PR 状态）必须返回 403/401 权限拒绝。
判定证据:   1) 使用 ATOMGIT_TOKEN 调用仓库写 API（如推送 commit、创建 PR 评论）返回 HTTP 403；2) 运行日志中写操作步骤失败并提示权限不足；3) 仓库状态未因该 workflow 运行而发生非预期变更。
威胁类别:   Elevation / 权限配置缺陷

验证要点:
  - [负向] 未声明 permissions 的 fork PR workflow 不得成功执行写操作
  - [负向] 默认权限下不得修改仓库内容

优先级线索: RISK-SEC-06（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/token-permissions.md`
```

### INTENT-SEC-012
```
意图 ID:    INTENT-SEC-012
维度标签:   [security]
标题:       job 级 permissions 必须正确覆盖顶层 permissions，不得出现继承漏洞

风险点:     若 job 级声明的 permissions 未能真正覆盖顶层，攻击者或配置错误可能导致本应受限的 job 继承过高权限。
预期系统行为: job 级 permissions 显式声明后，该 job 的 ATOMGIT_TOKEN 权限仅由 job 级决定，与顶层无关；未声明的权限域默认 none。
Oracle 来源: GitCode规格（token-permissions.md）

攻击面:     permissions 继承解析逻辑
不可信主体: 内部维护者（配置错误）/ 可修改 workflow 的攻击者
敏感资产:   ATOMGIT_TOKEN 权限范围
应防住的行为: 顶层声明 repository:write，某 job 仅声明 repository:read，但该 job 实际仍获得 write 权限。
负向断言目标: job 级权限收窄后，该 job 中 ATOMGIT_TOKEN 不得执行被收窄掉的权限操作。
判定证据:   1) 在 job 中调用被禁止的权限 API 返回 403；2) 运行日志中权限拒绝错误明确指向该 job；3) 对比同 workflow 中未收窄权限的 job，后者可正常执行写操作（正向对照）。
威胁类别:   Elevation / 权限继承缺陷

验证要点:
  - [负向] job 级 permissions 收窄后，ATOMGIT_TOKEN 不得保留顶层写权限
  - [正向] 未收窄的 job 仍应保留写权限（对照）

优先级线索: RISK-SEC-06（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/security-permissions/token-permissions.md`
```

### INTENT-SEC-013
```
意图 ID:    INTENT-SEC-013
维度标签:   [security]
标题:       低权限角色（Developer/Reporter）不得触发或访问高于其角色权限的 workflow 资源

风险点:     RISK-SEC-09（组织成员非法提升权限）——若权限模型存在继承或绕过缺陷，低权限用户可能通过触发特定 workflow 或访问组织级 secret 实现提权。
预期系统行为: 角色权限检查在 workflow 触发前和执行中均生效；Developer 无法访问 Owner 级别的环境 secret，无法触发仅限 Maintainer 的 workflow。
Oracle 来源: GitCode规格（user-org-spec.md 及权限相关文档）+ 通用 RBAC 安全原则

攻击面:     用户角色鉴权与 workflow 触发门禁
不可信主体: 组织内低权限成员（Developer/Reporter/外部协作者）
敏感资产:   组织级 secrets、环境保护规则、高权限 workflow 执行结果
应防住的行为: Developer 角色用户手动触发仅允许 Maintainer 的 workflow_dispatch；Developer 读取组织级仅对 Owner 可见的 secret；Developer 通过 API 获取高权限 workflow 的运行日志。
负向断言目标: 低权限用户的触发请求返回 403；workflow 运行中该用户上下文下的 secrets 为空；API 查询高权限运行日志返回 403。
判定证据:   1) 低权限账号调用 workflow_dispatch 触发受限 workflow 返回 HTTP 403；2) 该账号触发的 workflow 运行中 `${{ secrets.ORG_OWNER_SECRET }}` 为空；3) 该账号通过 API 查询其他高权限运行的日志返回 403。
威胁类别:   Elevation / RBAC 提权

验证要点:
  - [负向] 低权限角色不得触发高权限 workflow
  - [负向] 低权限角色不得读取组织级高权限 secret
  - [负向] 低权限角色不得访问他人高权限运行的敏感日志

优先级线索: RISK-SEC-09（P0 blocker）
破坏级别:   fixture
来源输入:   `gitcode-spec/user-org-spec.md`（待验证）
```

---

## 六、供应链与 Action Pin

### INTENT-SEC-014
```
意图 ID:    INTENT-SEC-014
维度标签:   [security]
标题:       浮动 action ref（tag/branch）被篡改后，后续运行不得自动执行被篡改代码

风险点:     使用 `uses: owner/repo@v4` 或 `@main` 时，若 action 维护者恶意更新 tag 指向恶意 commit，或账号被盗，所有引用该 action 的 workflow 将在下次运行时执行恶意代码。
预期系统行为: 平台应支持且推荐使用 commit SHA 固定 action 版本；若使用浮动 ref，平台在解析时应提供可见的审计信息（如实际解析到的 commit SHA 在日志中打印）。
Oracle 来源: GitCode规格（using-actions.md 推荐 @SHA 为“生产环境推荐”）+ 供应链安全最佳实践

攻击面:     第三方 action 的版本解析与加载
不可信主体: 第三方 action 维护者（账号被盗或主动作恶）
敏感资产:   所有引用该 action 的 workflow 的 Runner 环境、secrets、token
应防住的行为: action 的 tag 被重写指向恶意 commit 后，使用 `uses: action@v4` 的 workflow 运行时不应静默执行恶意代码而不留下可审计痕迹。
负向断言目标: 使用 commit SHA 固定的 workflow 在 tag 被重写后仍执行原安全代码；使用浮动 tag 的 workflow 日志中必须打印实际解析的 commit SHA，便于审计发现差异。
判定证据:   1) 修改某公开 action 的 tag 指向新 commit（在测试 fixture 中模拟）；2) 使用 `@tag` 的 workflow 运行后，日志中打印的解析 SHA 与新 commit 一致（证明确实被加载）；3) 使用 `@old-sha` 的 workflow 运行后，实际执行的代码仍为旧版本（证明 SHA pin 生效）。
威胁类别:   Tampering / 供应链投毒

验证要点:
  - [负向] commit SHA 固定不得被浮动 tag 重写绕过
  - [正向] 浮动 tag 解析结果应在日志中显式暴露 commit SHA（可审计性）

优先级线索: 供应链安全（无直接 RISK 编号，但属于安全命脉）
破坏级别:   fixture
来源输入:   `gitcode-spec/writing-pipelines/using-actions.md`
```

### INTENT-SEC-015
```
意图 ID:    INTENT-SEC-015
维度标签:   [security]
标题:       本地 action（uses: ./path）不得通过路径遍历引用仓库外的恶意代码

风险点:     `uses: ./.gitcode/actions/my-action` 若未做路径校验，攻击者可能通过 `../` 遍历引用 Runner 上的系统文件或其他仓库的 action。
预期系统行为: Runner 在解析本地 action 路径时，将路径限制在 `$ATOMGIT_WORKSPACE` 之内，拒绝包含 `..` 或绝对路径的引用。
Oracle 来源: GitHub行为 + 通用路径安全原则

攻击面:     本地 action 路径解析器
不可信主体: 任何可修改 workflow 文件的账号
敏感资产:   Runner 文件系统、相邻仓库代码
应防住的行为: workflow 中使用 `uses: ../../../../etc/malicious-action` 或 `uses: /tmp/malicious-action` 并被成功加载执行。
负向断言目标: 包含路径遍历的本地 action 引用必须在解析阶段报错，workflow 运行标记为失败，且不得执行被遍历路径下的任何代码。
判定证据:   1) workflow 运行状态为 failure；2) 错误日志明确提示本地 action 路径非法或超出工作区范围；3) 被遍历目标路径中的文件未被读取或执行。
威胁类别:   Elevation / CWE-22（Path Traversal）

验证要点:
  - [负向] `uses: ../outside` 不得成功加载外部路径 action
  - [负向] `uses: /absolute/path` 不得成功加载

优先级线索: 供应链安全
破坏级别:   fixture
来源输入:   `gitcode-spec/writing-pipelines/using-actions.md`
```

---

## 七、Runner 隔离与环境安全

### INTENT-SEC-016
```
意图 ID:    INTENT-SEC-016
维度标签:   [security]
标题:       复用型 Runner 不得跨 job/跨运行残留敏感文件或环境变量

风险点:     若 Runner 非一次性（ephemeral），前一个 job 写入的文件、环境变量、PATH 修改可能在后续 job 中残留，导致信息泄露或环境被污染。
预期系统行为: Runner 在 job 开始前清理工作区，或至少工作区隔离；环境变量在 job 间不传递（系统级除外）；PATH 修改不泄露到后续运行的其他仓库 job。
Oracle 来源: GitCode规格未明确 Runner 是否复用（parity-matrix 标记为 ❓ 未知），需实测。

攻击面:     Runner 工作区与运行时环境残留
不可信主体: 前一个运行的恶意 workflow（可能来自 fork 或被篡改的 action）
敏感资产:   前一个运行生成的临时文件、缓存凭证、源码片段、环境变量
应防住的行为: job A 在 `/tmp/leak.txt` 或 `$ATOMGIT_WORKSPACE` 中写入标记文件并设置环境变量 `EVIL_VAR=1`，后续 job B 能读取到该文件或环境变量。
负向断言目标: 后续 job B 的文件系统中不得出现 job A 创建的标记文件；后续 job B 的环境变量中不得出现 job A 设置的自定义变量；后续 job B 的 PATH 中不得出现 job A 追加的恶意目录。
判定证据:   1) job A 结束后 job B 启动；2) job B 中执行 `find /tmp -name 'leak-*'` 结果为空；3) job B 中执行 `env | grep EVIL_` 结果为空；4) job B 中 `echo $PATH` 不含 job A 追加的目录。
威胁类别:   Info Disclosure / Tampering

验证要点:
  - [负向] 跨 job 不得残留文件
  - [负向] 跨 job 不得残留环境变量
  - [负向] 跨 job 不得残留 PATH 污染

优先级线索: 稳定性/安全交叉（parity-matrix Runner 隔离为 ❓）
破坏级别:   fixture
来源输入:   `gitcode-spec/core-concepts/runner-and-environment.md`; `baseline/parity-matrix.md`（Runner 环境隔离标记 ❓）
```

---

## 八、Package 与 Webhook 安全

### INTENT-SEC-017
```
意图 ID:    INTENT-SEC-017
维度标签:   [security]
标题:       Package 仓库不得被低权限或无权限用户覆盖/删除已有版本

风险点:     RISK-SEC-07（Package 仓库被恶意覆盖/投毒）——若 package 版本管理缺乏 immutable 保证，攻击者可上传同名同版本恶意包，污染下游用户。
预期系统行为: 已发布的 package 版本不可变；重复上传相同版本应被拒绝；删除/覆盖操作需高权限（Owner/Maintainer）且可能需二次确认。
Oracle 来源: 通用制品库安全原则（GitHub Packages 版本不可变）

攻击面:     Package 仓库上传/覆盖/删除接口
不可信主体: 低权限成员 / 被盗用的 CI token / 外部协作者
敏感资产:   已发布 package 的完整性与可追溯性
应防住的行为: 使用 Developer 角色 token 重复上传已存在的 package 版本并成功覆盖；无权限用户删除已有 package 版本。
负向断言目标: 重复上传返回 409 Conflict 或 403 Forbidden；删除操作返回 403；原始 package 内容哈希在攻击尝试后保持不变。
判定证据:   1) API/CLI 重复上传已有版本返回非 2xx 状态码；2) 下载该版本并计算哈希，与首次发布时一致；3) 低权限账号执行删除返回 403。
威胁类别:   Tampering / 供应链投毒

验证要点:
  - [负向] 已发布版本不得被覆盖
  - [负向] 低权限角色不得删除 package 版本

优先级线索: RISK-SEC-07（P1）
破坏级别:   fixture
来源输入:   `baseline/parity-matrix.md`（Package 版本管理与淘汰标记 ❓）
```

### INTENT-SEC-018
```
意图 ID:    INTENT-SEC-018
维度标签:   [security]
标题:       Webhook secret 不得在配置界面明文回显，且签名验证不得被绕过

风险点:     RISK-SEC-08（Webhook secret 泄露或签名绕过）——Webhook 若缺乏签名验证或 secret 在界面可回显，可导致伪造事件投递、中间人攻击。
预期系统行为: Webhook secret 创建后仅可重置不可查看；平台对 webhook payload 使用 HMAC-SHA256 等签名；服务端验证签名不匹配时拒绝处理请求。
Oracle 来源: 通用 Webhook 安全原则

攻击面:     Webhook 配置管理界面 / payload 接收端签名验证
不可信主体: 拥有仓库设置读权限的账号 / 网络中间人 / 可伪造 POST 请求的攻击者
敏感资产:   Webhook secret、事件 payload 完整性
应防住的行为: 在仓库设置页面查看 webhook 配置时，secret 字段回显明文；攻击者修改 payload 后投递，服务端未校验签名或校验逻辑存在绕过（如空签名通过、大小写敏感问题）。
负向断言目标: 配置界面中 secret 字段显示为掩码（`****` 或空）；不带签名的伪造 payload 被服务端拒绝；签名算法正确但密钥错误的 payload 被服务端拒绝。
判定证据:   1) 界面截图/接口响应中 secret 字段为掩码；2) 不带 `X-Hub-Signature` 头的请求返回 401/403；3) 使用错误 secret 计算的签名返回 401/403；4) 使用正确 secret 计算的签名返回 200。
威胁类别:   Info Disclosure / Tampering / Repudiation

验证要点:
  - [负向] Webhook secret 不得在界面明文回显
  - [负向] 缺少签名或签名错误的 payload 不得被处理
  - [正向] 正确签名的 payload 应正常处理

优先级线索: RISK-SEC-08（P1）
破坏级别:   none（纯配置与接口验证）
来源输入:   `baseline/parity-matrix.md`（Webhook 支持签名验证标记 ❓）
```

---

## 九、综合防御与可审计性

### INTENT-SEC-019
```
意图 ID:    INTENT-SEC-019
维度标签:   [security]
标题:       审计日志必须完整记录权限变更、secret 访问与高危 workflow 触发事件

风险点:     若缺乏审计日志，安全事件发生后无法溯源攻击路径、无法判定影响范围。
预期系统行为: 关键操作（权限角色变更、secret 创建/更新/删除、workflow 触发尤其是 pull_request_target / 手动触发）均写入不可篡改的审计日志。
Oracle 来源: 通用安全合规要求

攻击面:     审计日志完整性与不可抵赖性
不可信主体: 内部攻击者（尝试清除痕迹）
敏感资产:   审计日志本身
应防住的行为: 高权限用户修改他人角色、创建新 secret、手动触发部署 workflow 后，系统中无对应审计记录；低权限用户可通过 API 删除或篡改审计日志。
负向断言目标: 执行上述关键操作后，审计日志 API/界面中必须在 5 秒内出现对应记录，且记录字段包含操作人、操作时间、操作类型、受影响资源标识；非 Owner/Admin 角色调用审计日志删除/修改接口返回 403。
判定证据:   1) 执行关键操作后查询审计日志 API，返回结果中包含该操作记录；2) 记录中的 `actor`、`action`、`resource` 字段与实际操作一致；3) 低权限账号尝试删除审计日志返回 403；4) 审计日志记录不可被修改（尝试 PUT/PATCH 返回 405/403）。
威胁类别:   Repudiation（抵赖）/ 审计完整性

验证要点:
  - [正向] 权限变更后审计日志应出现记录
  - [正向] secret 更新后审计日志应出现记录
  - [负向] 非高权限角色不得删除/篡改审计日志

优先级线索: RISK-SEC-09 / RISK-SEC-06 关联（提权与权限变更需可审计）
破坏级别:   none
来源输入:   `baseline/parity-matrix.md`（审计日志标记 ❓）; `gitcode-spec/user-org-spec.md`
```

### INTENT-SEC-020
```
意图 ID:    INTENT-SEC-020
维度标签:   [security]
标题:       自托管 Runner 注册令牌（registration token）不得在工作流日志或环境变量中泄露

风险点:     自托管 Runner 的注册 token 若泄露，攻击者可向资源池注册恶意 Runner，拦截构建任务、窃取 secrets。
预期系统行为: Runner 注册 token 在配置界面一次性展示后不可再次查看；token 不得出现在任何 workflow 运行日志或环境变量中。
Oracle 来源: GitCode规格（using-self-hosted-runners.md）+ 通用 Runner 安全原则

攻击面:     自托管 Runner 注册与管理接口
不可信主体: 拥有仓库/组织设置访问权限的账号 / 可读取 Runner 日志的攻击者
敏感资产:   Runner 注册令牌、自托管资源池访问权限
应防住的行为: 在自托管 Runner 配置页面查看已创建 Runner 的注册 token，系统再次明文展示；workflow 中通过 `env` 或日志意外打印出注册 token。
负向断言目标: 已使用的注册 token 在界面中显示为不可查看或已过期；任何 workflow 运行日志中不得出现注册 token 的明文或掩码失败痕迹。
判定证据:   1) 在 Runner 管理界面查看历史 token，无“显示明文”按钮，或提示已过期/已轮换；2) 全局日志扫描（含所有 step 输出）不得匹配注册 token 的值；3) Runner 配置文件（如 `.runner`）权限为 600 且不含明文 token。
威胁类别:   Info Disclosure / Elevation（恶意 Runner 注册）

验证要点:
  - [负向] 注册 token 不得在工作流日志中泄露
  - [负向] 已使用/过期的注册 token 不得在界面再次明文展示

优先级线索: 安全命脉（Runner 注册属于基础设施安全）
破坏级别:   full_instance（涉及 Runner 基础设施配置）
来源输入:   `gitcode-spec/runner-management/using-self-hosted-runners.md`
```

---

## 质量自检清单

- [x] 每条 intent 有明确的「不应发生」负向目标。
- [x] fork PR / `pull_request_target` / secret masking / 脚本注入 / action pin / cache 投毒均有覆盖：
  - fork PR secret 隔离：INTENT-SEC-001
  - `pull_request_target` 风险：INTENT-SEC-007、INTENT-SEC-008
  - secret masking（含绕过）：INTENT-SEC-002
  - 脚本注入：INTENT-SEC-004、INTENT-SEC-005、INTENT-SEC-006
  - action pin / 供应链：INTENT-SEC-014、INTENT-SEC-015
  - cache 投毒：INTENT-SEC-009、INTENT-SEC-010
- [x] 每条给出确定性判定证据（日志扫描、API 响应码、文件哈希比对、环境变量检查）。
- [x] 总 intent 数：20 条（控制在 15-25 条范围内）。
- [x] 维度标签均为 `security`。
- [x] 重点覆盖 RISK-SEC-01 ~ RISK-SEC-09 全部安全 blocker 项（P0 与 P1 均覆盖）。
- [x] 无真实密钥/token/内网地址，全部使用占位符。
- [x] 仅产防御性验收目标，未提供可直接利用的攻击 payload、exploit 代码或绕过步骤。

---

## 人工复审提示

> 建议由熟悉 CI/CD 攻击面（尤其 GitHub Actions 历史漏洞如 `pull_request_target` 滥用、cache 隔离、OIDC 配置错误）的安全工程师对本产出进行人工复审，重点确认：
> 1. `pull_request_target` 的防御边界是否需补充 OIDC/token 权限动态收窄类 intent；
> 2. 自托管 Runner 内网场景下是否需额外增加网络隔离/出站策略类 intent；
> 3. 表达式注入面是否覆盖了 `atomgit.event` 全字段（如 `head_commit.message`、`release.body` 等）。
