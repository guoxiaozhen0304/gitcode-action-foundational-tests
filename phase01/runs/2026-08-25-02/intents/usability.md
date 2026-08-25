# Usability Intents — Phase 01 Run 2026-08-25-02（增量）

> **Agent**: usability（易用性）  
> **输入版本**: `gitcode-spec/` 2026-08-18 · `gitcode-api/` 2026-08-19 · `testing-focus.md` 当前版本 · `risk-register.md` 当前版本  
> **缺失输入标注**: `phase01/inputs/business-context/` 目录不存在，本轮 intent 未基于具体业务迁移场景/改造点/历史摩擦记录生成；如有此类输入，建议补充后通过 `/phase01-update dim:usability` 重审。  
> **增量说明**: 本轮为 Run 2026-08-25-02 的增量 intent。上轮 Run 2026-08-25-01 已产出 INTENT-USE-001~012（12 条）及对应 24 条 UI 用例。本轮重点补充 **Actions 流水线 Web UI 场景**、**迁移摩擦的 UI 反馈**、**调试体验与可观测性 UI**，避免与上轮完全重复，但对上轮未深入的可理解性判据进行细化。

---

## INTENT-USE-013
- **id**: INTENT-USE-013
- **dimensions**: [usability]
- **scenario**: 流水线（Actions）列表页的状态筛选、运行记录展示与空状态
- **user_perspective**: 从 GitHub 迁移过来的开发者，习惯在 Actions 标签页查看所有 workflow 运行记录
- **pain_point**: 列表页无运行记录时缺乏引导文案；状态筛选（成功/失败/运行中）响应慢或筛选后无明确空状态提示；运行编号、触发事件、耗时等字段排版混乱，开发者难以快速定位目标运行。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 导航到仓库 Actions 标签页 → 观察左侧 workflow 名称列表 → 点击某个 workflow → 观察右侧运行记录列表 → 点击状态筛选器（成功/失败/运行中）→ 观察筛选结果与空状态 → 浏览器刷新后观察筛选条件是否保持
- **understandability_criterion**: 空状态时页面应展示「当前无运行记录」文案，并给出「如何创建 workflow 文件」或「前往文档」链接；状态筛选器应带有明确的图标/颜色对应关系（如绿色勾=成功、红色叉=失败、黄色圆=运行中）；运行记录卡片应至少包含：运行编号（如 #42）、触发事件名称、触发分支、触发人头像/名称、耗时、状态徽标。
- **llm_assisted**: false
- **rationale**: Actions 列表是开发者调试 CI 的第一入口；列表信息密度低或空状态缺失会直接增加定位问题运行的时间成本，影响从 GitHub 迁移后的操作习惯连续性。
- **expected_behavior**: 列表即时加载（<3s）；筛选后 URL 应同步查询参数；空状态提供创建指引；运行记录按时间倒序排列。
- **related_compat_diff**: 无直接差异，但 GitHub Actions 列表的筛选交互是迁移用户的习惯基准。

---

## INTENT-USE-014
- **id**: INTENT-USE-014
- **dimensions**: [usability, completeness]
- **scenario**: 流水线运行详情页的 stage/job/step 层级展开与状态可视化
- **user_perspective**: 迁移开发者首次在 GitCode 上排查流水线失败原因，需要像 GitHub 一样逐层展开查看执行详情
- **pain_point**: stage/job/step 的层级关系不清晰；失败 step 未在视觉上高亮；展开/折叠交互无动画或状态丢失；Post 阶段与普通 job 的区分不明显；无耗时分布图或甘特图辅助定位瓶颈。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 从 Actions 列表点击某次运行进入详情页 → 观察左侧 stage 侧栏与右侧 job 卡片 → 点击展开失败的 job 卡片 → 逐一点击 step 行查看日志 → 观察 Post 阶段的展示位置 → 尝试折叠/展开全部
- **understandability_criterion**: 失败 step 必须在视觉上以红色边框、红色文字或红色图标明确标记；stage 侧栏应显示每个 stage 的完成状态图标；job 卡片应展示 Runner 标签（如 `{ubuntu-24,x64,small}`）、开始时间、结束时间、总耗时；Post 阶段应以独立区块展示，并标注「后处理」或「Post」字样；展开失败 job 后，失败的 step 应自动滚动到可视区域。
- **llm_assisted**: false
- **rationale**: 运行详情页是调试体验的核心战场；层级混乱或失败点不突出会让开发者在长流水线中「找错」成本倍增。
- **expected_behavior**: 失败 job/step 自动高亮；stage 侧栏支持点击跳转；job 卡片内 step 按时间线排列；Post 阶段在主线流程结束后展示。
- **related_compat_diff**: GitCode 特有 `stages` 阶段机制与 `post` 后处理阶段，与 GitHub 的纯 job DAG 不同；UI 需帮助迁移用户理解此差异。

---

## INTENT-USE-015
- **id**: INTENT-USE-015
- **dimensions**: [usability]
- **scenario**: 手动触发 workflow_dispatch 的表单填写与参数校验反馈
- **user_perspective**: 迁移开发者需要在 UI 上手动触发部署流水线，并填写输入参数
- **pain_point**: 表单未按 workflow 中 `inputs` 定义的顺序渲染；必填项未标记星号；参数 `description` 未展示为字段提示；提交时必填项为空仅给出泛化「请填写完整」而非定位到具体字段；布尔/数字类型在 GitCode 中只能输入 string，但 UI 未提示此限制。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 导航到 Actions 标签页 → 选择包含 workflow_dispatch 的 workflow → 点击「Run workflow」按钮 → 观察弹出的参数表单 → 留空必填项并提交 → 观察校验提示 → 填写参数后提交 → 观察运行是否按参数值启动
- **understandability_criterion**: 每个输入字段旁必须展示 `description` 文案；必填字段以红色星号（*）标记；留空提交时，具体空字段应以红色边框高亮并展示内联错误文案（如「部署目标环境为必填项」）；表单顶部或底部应有提示「所有输入参数均为字符串类型，如需布尔/数字语义请在 workflow 中自行转换」。
- **llm_assisted**: false
- **rationale**: workflow_dispatch 是调试和发布的高频入口；表单校验不清会导致参数误填、部署到错误环境等严重事故。
- **expected_behavior**: 表单字段顺序与 YAML 定义一致；必填校验即时反馈；提交后弹窗关闭并刷新运行列表。
- **related_compat_diff**: GitCode `inputs` 仅支持 `string` 类型，GitHub 支持 `boolean`/`choice`/`number`/`environment`；UI 需明示此限制以减少迁移摩擦。

---

## INTENT-USE-016
- **id**: INTENT-USE-016
- **dimensions**: [usability]
- **scenario**: 流水线失败时日志中的错误信息可读性与定位体验
- **user_perspective**: 迁移开发者需要像阅读 GitHub Actions 日志一样，快速定位 GitCode 流水线失败的根本原因
- **pain_point**: 错误日志缺少 step 编号前缀，难以区分哪个 step 失败；错误堆栈未折叠，长日志中关键错误行被淹没；没有「跳转到第一个错误」按钮；YAML 语法错误未指明具体文件路径和行号；GitCode 特有语法（如 `stages`、`atomgit` 上下文）的错误提示未给出修复示例链接。
- **priority**: P0
- **ui_candidate**: true
- **ui_interaction**: 触发一个故意包含语法错误的 workflow → 等待运行失败 → 进入运行详情页 → 展开失败的 job → 观察日志面板中的错误展示 → 点击「下载日志」按钮 → 搜索关键字如 "Error" 或 "fatal" → 观察高亮效果 → 检查是否有行号/文件路径提示
- **understandability_criterion**: 失败 step 的日志面板顶部应展示一个红色错误摘要栏，包含：失败 step 名称、退出码（如 exit code 1）、失败原因简述（如 "YAML parse error"）；若失败原因为 YAML 语法错误，摘要栏必须包含文件路径（如 `.gitcode/workflows/ci.yml`）和具体行号（如 `line 12`）；日志中每个 step 的输出必须以 `Step X: <step_name>` 为前缀；错误关键字（如 `Error`、`fatal`、`FAIL`）必须以红色高亮显示；日志面板顶部必须提供「下载日志」按钮和「跳转到第一个错误」链接。
- **llm_assisted**: false
- **rationale**: 日志是 CI 调试的唯一信息源；错误定位效率直接决定开发者修复问题的速度。RISK-USE-02（文档承诺与实现不一致）的高优先级要求错误提示必须具体、可执行。
- **expected_behavior**: 错误摘要栏常驻于日志面板顶部；点击行号可复制该行；下载日志为 UTF-8 纯文本。
- **related_compat_diff**: GitCode 的 `atomgit` 上下文、`stages`、`post` 等为特有语法；相关错误提示需帮助迁移开发者理解差异。

---

## INTENT-USE-017
- **id**: INTENT-USE-017
- **dimensions**: [usability]
- **scenario**: Job 日志的搜索、折叠与下载功能可用性
- **user_perspective**: 迁移开发者在长日志中查找特定关键字（如 secret 脱敏标记、特定命令输出）
- **pain_point**: 搜索框不支持正则或大小写不敏感；搜索结果无高亮或跳转；长 step 输出未自动折叠，导致页面卡顿；下载的日志文件名无意义（如 `log.txt` 而非 `{owner}-{repo}-job-{id}.log`）；下载后本地打开编码异常但 UI 无 UTF-8 提示。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 进入运行详情页 → 展开某 job 日志 → 在日志面板顶部搜索框输入关键词 → 观察匹配结果高亮与跳转 → 尝试点击 step 标题折叠/展开长输出 → 点击「下载日志」→ 观察下载文件名与内容格式
- **understandability_criterion**: 搜索框必须至少支持普通文本匹配，并在匹配行以黄色背景高亮；若存在多个匹配结果，必须展示匹配计数（如 "3/15"）并提供上一个/下一个跳转按钮；每个 step 的输出超过 50 行时必须默认折叠，并展示「展开 X 行」按钮；下载的日志文件名必须包含仓库名、job 名或 job ID；下载按钮旁应有 tooltip 或提示文案「日志为 UTF-8 编码」。
- **llm_assisted**: false
- **rationale**: 长日志的可检索性是调试体验的硬指标；GitHub Actions 的日志折叠和搜索是迁移用户的高频对比基准。
- **expected_behavior**: 搜索即时响应（debounce <300ms）；折叠/展开动画流畅；下载文件可直接用文本编辑器打开。
- **related_compat_diff**: 无。

---

## INTENT-USE-018
- **id**: INTENT-USE-018
- **dimensions**: [usability]
- **scenario**: 重新运行失败 job 的入口可见性与状态刷新
- **user_perspective**: 迁移开发者发现流水线因偶发问题（如网络超时）失败，希望重新运行以确认问题可恢复
- **pain_point**: 「Re-run」按钮位置不明显或与「删除运行」过于接近；点击重新运行后无即时反馈（如 Toast 提示「正在创建新运行」）；新运行记录未自动出现在列表顶部，需手动刷新；重新运行限制（如最多 3 次）未在按钮旁提示，点击后仅给出后端报错。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 进入一个失败的运行详情页 → 观察右上角操作按钮区 → 点击「重新运行」或「Re-run failed jobs」→ 观察即时反馈 → 返回 Actions 列表 → 观察新运行记录是否出现 → 连续重新运行 4 次观察限制提示
- **understandability_criterion**: 「重新运行」按钮必须在页面右上角或顶部操作栏中以主按钮样式（如蓝色背景）展示，且与危险操作（删除）保持足够间距；点击后必须展示 Toast 或弹窗提示「新运行 #43 已创建，正在排队」；新运行必须在 5 秒内出现在 Actions 列表顶部，且列表应自动刷新或提供「刷新」按钮；当运行已达到最大重试次数（3 次）时，按钮应置灰并展示 tooltip「已达到最大重新运行次数（3/3）」；若运行超过 6 小时不可重新运行，按钮应置灰并提示「超过 6 小时的运行不可重新运行」。
- **llm_assisted**: false
- **rationale**: 重新运行是 CI 故障排查的标准动作；入口隐蔽或限制不明会增加开发者的挫败感。
- **expected_behavior**: 按钮可见、限制前置提示、新运行自动刷新出现。
- **related_compat_diff**: 无直接差异，但重新运行时的上下文变量保持与 GitHub 行为是否一致属于 compat-diff 范畴。

---

## INTENT-USE-019
- **id**: INTENT-USE-019
- **dimensions**: [usability, compatibility]
- **scenario**: workflow 文件放在错误目录（`.github/workflows/` 而非 `.gitcode/workflows/`）时的 UI 提示
- **user_perspective**: 迁移开发者直接将 GitHub 仓库的 `.github/workflows/` 目录 push 到 GitCode，期望流水线自动触发
- **pain_point**: 文件放到 `.github/workflows/` 后，GitCode 静默忽略，UI 上没有任何提示告知「 workflow 文件位置错误」；开发者误以为平台未启用 Actions 或存在 bug，反复检查设置页；文档虽说明了正确路径，但 UI 未在错误场景下主动引导。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 在仓库中创建 `.github/workflows/ci.yml`（非 `.gitcode/workflows/`）→ push 到仓库 → 导航到 Actions 标签页 → 观察是否检测到 workflow → 观察是否有引导横幅或提示 → 检查仓库首页或设置页是否有「检测到 GitHub 风格 workflow 路径」提示
- **understandability_criterion**: 当仓库存在 `.github/workflows/` 目录但不存在 `.gitcode/workflows/` 目录时，Actions 标签页必须展示一个黄色/橙色警告横幅，文案包含：「检测到 `.github/workflows/` 目录，但 GitCode Action 的 workflow 文件应存放在 `.gitcode/workflows/` 目录下」；横幅必须提供一个「查看迁移文档」链接或「一键迁移」按钮（若支持）；该提示不得被用户误认为是「Actions 功能未开启」的通用提示。
- **llm_assisted**: true
- **rationale**: 目录路径差异是 GitCode↔GitHub 最显眼的迁移摩擦点（见 COMPAT-NOTES.md §1）；UI 若不在此场景主动干预，迁移开发者将大量流失在第一步。对应风险登记册 RISK-USE-01（迁移报错不指明 GitCode 差异）。
- **expected_behavior**: 警告横幅常驻于 Actions 空状态页；点击链接跳转至官方迁移文档。
- **related_compat_diff**: `.github/workflows/` vs `.gitcode/workflows/` — GitCode 官方已声明差异，但 UI 需在错误场景下主动提示。

---

## INTENT-USE-020
- **id**: INTENT-USE-020
- **dimensions**: [usability, compatibility]
- **scenario**: 使用 GitHub 专有语法（`github.ref`、`GITHUB_TOKEN`、`success()`）时的报错信息质量
- **user_perspective**: 迁移开发者直接复制 GitHub Actions workflow 到 GitCode，未修改上下文变量和函数名
- **pain_point**: 运行失败时日志仅给出「表达式解析失败」或「变量未定义」的泛化错误，未指明「`github.ref` 在 GitCode 中应改为 `atomgit.ref`」；`GITHUB_TOKEN` 未替换为 `ATOMGIT_TOKEN` 时，错误提示未说明环境变量命名差异；`success()` 带括号时解析失败，但错误信息未提示「GitCode 状态函数不带括号」。
- **priority**: P0
- **ui_candidate**: true
- **ui_interaction**: 在 `.gitcode/workflows/` 中提交包含 `github.ref`、`GITHUB_TOKEN`、`success()` 的 YAML → 触发运行 → 等待失败 → 进入运行详情页查看日志 → 观察错误提示内容 → 检查错误摘要是否包含迁移建议
- **understandability_criterion**: 当日志中包含对未定义上下文 `github` 的引用时，错误摘要必须明确写出：「上下文 `github` 未定义。在 GitCode Action 中，请使用 `atomgit` 上下文（如 `atomgit.ref`）替代 `github`。」；当使用 `secrets.GITHUB_TOKEN` 或环境变量 `GITHUB_TOKEN` 时，错误提示必须包含：「GitCode 使用 `ATOMGIT_TOKEN` 作为自动令牌，请将 `GITHUB_TOKEN` 替换为 `ATOMGIT_TOKEN`。」；当状态函数使用带括号语法（如 `success()`）时，错误提示必须包含：「GitCode 状态函数不带括号，请改为 `success`（无括号）。」；每条提示必须附带官方差异文档链接。
- **llm_assisted**: true
- **rationale**: 上下文变量和函数语法差异是迁移摩擦的最高发区（见 COMPAT-NOTES.md §2、§3）；若报错不指明「这是 GitCode 差异」，开发者只能盲猜。对应风险登记册 RISK-USE-02（P0）。
- **expected_behavior**: 错误信息将「未定义变量」与「GitCode 差异」绑定，给出可直接替换的代码示例。
- **related_compat_diff**: `github.*` → `atomgit.*`；`GITHUB_*` → `ATOMGIT_*`；`success()` → `success`；`failure()` → `failed`。

---

## INTENT-USE-021
- **id**: INTENT-USE-021
- **dimensions**: [usability]
- **scenario**: PR 页面 Checks 标签中流水线状态的汇总展示与可理解性
- **user_perspective**: 迁移开发者在提交 MR/PR 后，习惯在 PR 详情页的 Checks/流水线标签中查看 CI 结果
- **pain_point**: Checks 标签加载缓慢（>5s）；流水线运行记录未按 workflow 名称分组；失败运行的错误摘要未在 Checks 列表中展示，必须点击进入运行详情才能看到；成功的运行与失败的运行未按颜色/图标明显区分；缺少「重新运行」快捷入口。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 创建一个 MR → 等待流水线触发 → 进入 MR 详情页 → 切换到 Checks/流水线标签 → 观察运行列表的加载速度与布局 → 观察失败运行的摘要信息 → 尝试点击「重新运行」按钮
- **understandability_criterion**: Checks 标签必须在 3 秒内完成加载；每个 workflow 运行记录卡片必须展示：workflow 名称、状态徽标（绿/红/黄）、失败时的简要原因（如 "build step failed"）、耗时、触发时间；失败记录必须以红色边框或红色背景高亮；每个记录卡片必须提供「查看详情」和「重新运行」两个可操作按钮；若所有运行均成功，页面顶部应展示绿色通过横幅「所有检查已通过」。
- **llm_assisted**: false
- **rationale**: PR 页面的 Checks 标签是代码评审人判断代码质量的第一视窗；信息密度低或加载慢会直接影响评审效率。
- **expected_behavior**: 列表即时加载；失败记录高亮；支持快捷重新运行；状态变更后自动刷新。
- **related_compat_diff**: 无直接差异，但 GitHub 的 Checks 展示是迁移用户的体验基准。

---

## INTENT-USE-022
- **id**: INTENT-USE-022
- **dimensions**: [usability, security]
- **scenario**: 无权限用户尝试手动触发流水线或查看 Secrets 配置页时的 UI 反馈
- **user_perspective**: 仓库 Reporter 角色或外部协作者，误触了「Run workflow」按钮或尝试查看设置页
- **pain_point**: 无权限用户点击「Run workflow」后，系统静默无反应或仅给出「403 Forbidden」技术错误码；访问 Secrets 页时直接 403 白屏，无返回引导；权限不足时的错误页面文案生硬（如「你没有权限」），未说明需要什么角色（如 Maintainer 及以上）。
- **priority**: P0
- **ui_candidate**: true
- **ui_interaction**: 以 Reporter 角色账号登录 → 进入仓库 Actions 标签页 → 尝试点击某 workflow 的「Run workflow」→ 观察反馈 → 尝试直接访问仓库设置页的 Secrets 配置 → 观察页面反馈 → 检查错误提示是否说明所需角色
- **understandability_criterion**: 当无权限用户点击「Run workflow」时，必须弹出模态框或 Toast，文案包含：「当前账号无权限手动触发流水线。请联系仓库 Maintainer 或 Owner。」；当无权限用户访问 Secrets 页时，页面必须展示友好的权限不足提示（非白屏），文案包含：「你需要 Maintainer 或 Owner 角色才能查看和配置 Secrets。」；提示中必须提供「返回仓库首页」和「联系管理员」按钮；不得暴露内部 API 路径或技术堆栈信息（如 403 nginx 页面）。
- **llm_assisted**: true
- **rationale**: 权限边界不清晰是安全与易用性的交叉点；粗暴的 403 页面会降低平台专业度，并可能导致用户向支持团队提交无效工单。对应风险登记册 RISK-SEC-06（权限越界）与 RISK-USE-02（P0）。
- **expected_behavior**: 操作被拦截，UI 给出角色要求和返回路径，不暴露技术细节。
- **related_compat_diff**: 无。

---

## INTENT-USE-023
- **id**: INTENT-USE-023
- **dimensions**: [usability]
- **scenario**: Runner 标签不存在或格式错误时的 UI 错误提示
- **user_perspective**: 迁移开发者在 `runs-on` 中使用了 GitHub 风格的单标签（如 `ubuntu-latest`）或错误的三段式格式
- **pain_point**: 运行排队后长时间无响应，UI 仅显示「等待 Runner」而不说明「当前标签无匹配的 Runner」；`runs-on: ubuntu-latest` 在 GitCode 中可能需要映射为 `{ubuntu-24,x64,small}`，但 UI 未提示标签格式要求；自托管 Runner 离线时，运行卡在 queued 状态，无「Runner 离线」提示。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 提交一个包含 `runs-on: [nonexistent-label]` 的 workflow → 触发运行 → 进入运行详情页 → 观察 job 卡片的排队状态与提示文案 → 将标签改为 `ubuntu-latest`（GitHub 风格单标签）→ 观察是否正确匹配或给出提示 → 停止自托管 Runner 后触发运行 → 观察 queued 状态的提示
- **understandability_criterion**: 当 `runs-on` 标签无匹配 Runner 时，job 卡片必须展示黄色警告状态，文案包含：「未找到匹配标签 `[标签名]` 的 Runner。请检查 Runner 标签配置或联系管理员添加 Runner。」；当使用单标签（如 `ubuntu-latest`）而系统期望三段式时，提示文案必须包含：「GitCode Runner 标签使用三段式格式 `{os,arch,flavor}`，如 `{ubuntu-24,x64,small}`。详见文档。」；当自托管 Runner 离线导致排队超时时，提示必须包含：「目标 Runner 当前离线，上次在线时间为 X 分钟前。」
- **llm_assisted**: true
- **rationale**: Runner 标签体系是 GitCode 与 GitHub 的重要差异（见 COMPAT-NOTES.md §7）；迁移开发者极易因标签不匹配而遭遇「运行卡住」的谜团。
- **expected_behavior**: 排队状态给出具体原因；提供前往 Runner 管理页的链接；超时后自动标记为失败并给出最终原因。
- **related_compat_diff**: GitCode 三段式标签 `{os,arch,flavor}` vs GitHub 单标签 `ubuntu-latest`。

---

## INTENT-USE-024
- **id**: INTENT-USE-024
- **dimensions**: [usability]
- **scenario**: 流水线配置语法错误（如 YAML 缩进错误、非法字段）时的静态校验 UI 提示
- **user_perspective**: 迁移开发者提交了一个格式错误的 workflow YAML，期望在运行前或在日志中得到可理解的错误信息
- **pain_point**: YAML 缩进错误导致 workflow 完全无法解析，但 UI 上仅显示「解析失败」而无具体行号和列号；使用了 GitHub 支持但 GitCode 不支持的字段（如 `services` 容器服务）时，错误提示未说明「该字段在 GitCode 中不支持」；非法字段被静默忽略，导致开发者以为配置生效。
- **priority**: P0
- **ui_candidate**: true
- **ui_interaction**: 提交一个包含缩进错误的 YAML（如 `jobs:` 后少两个空格）→ push 后观察 Actions 标签页 → 进入运行详情页观察错误提示 → 再提交一个包含 GitCode 不支持字段（如假设 `services:`）的 YAML → 观察运行时的错误信息或静默行为
- **understandability_criterion**: YAML 解析失败时，错误摘要必须包含：具体文件路径、错误行号、错误列号、错误类型（如 "YAML syntax error: incorrect indentation"）；若错误为使用了不支持的字段，提示必须包含：「字段 `xxx` 在当前版本的 GitCode Action 中不受支持。支持的字段列表参见文档。」；若非法字段被静默忽略，则此行为必须在文档中明确声明，且 UI 上的 workflow 编辑器（如有）应以黄色下划线或警告图标标注该字段。
- **llm_assisted**: true
- **rationale**: 静态校验的报错质量直接决定开发者修复配置错误的效率；对应风险登记册 RISK-USE-02（P0：文档承诺与实现不一致）。
- **expected_behavior**: 错误信息精确定位到文件、行、列；不支持字段明确报错而非静默忽略（除非文档已声明忽略策略）。
- **related_compat_diff**: GitCode 不支持字段的降级方式（报错 vs 静默忽略）是兼容性差异高发区。

---

## INTENT-USE-025
- **id**: INTENT-USE-025
- **dimensions**: [usability]
- **scenario**: Commit 列表/详情页流水线状态徽标的展示与点击跳转
- **user_perspective**: 迁移开发者希望在 Commits 页面像 GitHub 一样，通过状态徽标快速判断某次提交是否通过了 CI
- **pain_point**: Commit 列表页的状态徽标缺失或加载延迟；徽标颜色与流水线状态不对应（如失败显示灰色而非红色）；点击徽标后未跳转至对应运行详情页，而是跳转至通用的 Actions 列表；无状态徽标的 commit 与正在运行的 commit 区分不明显。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 进入仓库 Commits 页面 → 观察每条 commit 右侧的状态徽标 → 点击某个成功的徽标 → 观察跳转目标 → 点击某个失败的徽标 → 观察跳转目标 → 观察正在运行中的 commit 徽标是否为旋转动画
- **understandability_criterion**: 每条 commit 右侧必须展示一个与流水线最终状态对应的状态徽标：成功=绿色勾、失败=红色叉、运行中=黄色旋转圆、未触发/无 workflow=无徽标或灰色横线；状态徽标必须支持 hover tooltip，展示 workflow 名称和状态文字；点击徽标必须直接跳转至该 commit 触发的最新运行详情页（而非通用列表）；若一次 commit 触发了多个 workflow，徽标应展示聚合状态（任一失败则整体失败，全部成功则整体成功）。
- **llm_assisted**: false
- **rationale**: Commit 状态徽标是开发者快速浏览代码健康度的核心视觉线索；缺失或跳转错误会打断日常代码审查节奏。
- **expected_behavior**: 徽标即时渲染；点击直达运行详情；多 workflow 聚合逻辑正确。
- **related_compat_diff**: 无。

---

## INTENT-USE-026
- **id**: INTENT-USE-026
- **dimensions**: [usability]
- **scenario**: Step summary Markdown 在运行详情页的渲染质量
- **user_perspective**: 迁移开发者使用 `ATOMGIT_STEP_SUMMARY` 输出构建报告、测试统计等 Markdown 内容，期望在 UI 上正确渲染
- **pain_point**: Step summary 中的表格未渲染，显示为原始 Markdown 管道符；代码块无语法高亮；图片无法加载；Emoji 显示为方框或乱码；summary 内容过长时未截断或折叠，导致运行详情页纵向无限拉长。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 运行一个输出复杂 Markdown（含表格、代码块、图片链接、emoji）到 `ATOMGIT_STEP_SUMMARY` 的 workflow → 进入运行详情页 → 观察 Step summary 区域的渲染效果 → 检查表格边框、代码高亮、图片加载 → 检查长内容是否有折叠
- **understandability_criterion**: Step summary 区域必须正确渲染标准 Markdown 表格（含表头、行、边框线）；代码块必须支持语法高亮（至少支持 `bash`、`yaml`、`json`、`python`）；图片链接必须以 `<img>` 形式展示，若加载失败则展示占位图和 alt 文本；常用 Emoji（如 :white_check_mark: :x: :warning:）必须正确渲染为对应 Unicode 字符或平台图标；当 summary 内容超过 500 字符或 20 行时，必须默认折叠并展示「展开全部」按钮。
- **llm_assisted**: true
- **rationale**: Step summary 是 CI 结果的可视化摘要；渲染质量差会让自动化报告失去价值。
- **expected_behavior**: Markdown 正确渲染；长内容折叠；图片有降级处理。
- **related_compat_diff**: `ATOMGIT_STEP_SUMMARY` 对应 GitHub 的 `GITHUB_STEP_SUMMARY`；渲染行为应与 GitHub 对齐。

---

## INTENT-USE-027
- **id**: INTENT-USE-027
- **dimensions**: [usability]
- **scenario**: 流水线取消/暂停/挂起状态的 UI 反馈与恢复引导
- **user_perspective**: 迁移开发者手动取消了一个运行，或运行因并发限制被挂起，需要理解当前状态并知道如何恢复
- **pain_point**: 取消后页面状态未即时更新，仍显示「运行中」数秒；挂起/暂停状态的图标与「排队中」相同，开发者无法区分；被挂起的运行未说明挂起原因（如「并发限制：当前队列位置 3/5」）；取消后无「重新运行」快捷入口。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 手动触发一个 workflow → 在运行中点击「取消」→ 观察页面状态变化 → 观察取消后的操作按钮 → 再触发多个 workflow 使超出并发限制 → 观察被挂起运行的状态展示
- **understandability_criterion**: 取消操作后，运行状态必须在 3 秒内从「运行中」变为「已取消」，且状态徽标变为灰色或带有取消图标；取消状态的运行卡片必须展示取消人名称和取消时间；被挂起/暂停的运行必须展示独立的状态图标（如暂停符号 ⏸）而非与「排队中」共用同一图标；挂起原因必须以内联文案展示，如「当前并发数已满（3/3），排队位置：第 2 位」；取消状态的运行详情页必须保留「重新运行」按钮。
- **llm_assisted**: false
- **rationale**: 状态机可视化是 workflow 可观测性的基础；状态反馈延迟或原因不明会让开发者误以为系统卡死。
- **expected_behavior**: 状态即时刷新；挂起原因明确；取消后可重新运行。
- **related_compat_diff**: GitCode 的 `concurrency` 机制与 GitHub 类似，但 UI 需清晰展示 QUEUE/IGNORE 策略的差异。

---

## INTENT-USE-028
- **id**: INTENT-USE-028
- **dimensions**: [usability]
- **scenario**: Issue/MR 评论中 @提及 的自动补全与选中体验
- **user_perspective**: 迁移开发者在 Issue 或 MR 评论中需要 @提及 团队成员，期望获得自动补全和正确的通知触发
- **pain_point**: 输入 `@` 后无自动补全下拉框；补全列表不包含组织成员或外部协作者；选中用户后用户名未高亮显示；@提及后对方未收到通知，但 UI 上无任何发送失败的提示；在 Markdown 预览模式下 @提及 未渲染为可点击链接。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 进入某 Issue 详情页 → 在评论框中输入 `@` → 观察是否出现用户补全列表 → 输入用户名过滤 → 点击选中 → 观察文本高亮 → 提交评论 → 切换到 Markdown 预览模式 → 观察 @提及 是否渲染为链接
- **understandability_criterion**: 输入 `@` 后必须在 300ms 内弹出用户补全下拉框，列表至少包含仓库成员和组织成员；补全列表必须支持键盘上下键选择和回车确认；选中后用户名必须以蓝色高亮或下划线样式展示；提交评论后，@提及的用户名必须渲染为指向该用户主页的超链接；若 @提及 的用户不存在或无权限查看该 Issue/MR，系统应在提交后给出内联警告「用户 @xxx 可能无法收到此通知」。
- **llm_assisted**: false
- **rationale**: @提及 是协作场景的高频交互；补全缺失或通知失败会直接影响异步沟通效率。对应风险登记册 RISK-USE-04（MR/Issue 通知可靠性）。
- **expected_behavior**: 自动补全即时响应；键盘可选；渲染为链接；通知失败有降级提示。
- **related_compat_diff**: 无。

---

## INTENT-USE-029
- **id**: INTENT-USE-029
- **dimensions**: [usability, security]
- **scenario**: 仓库设置页 Secrets 配置表单的可用性与错误提示
- **user_perspective**: 迁移开发者需要在 UI 上配置 Secrets，用于替代 GitHub 上配置的同名 secret
- **pain_point**: Secret 名称输入框未实时校验命名规则（大写字母/数字/下划线，不能以 ATOMGIT_ 开头）；重复添加同名 Secret 时给出「保存失败」而非「名称已存在，请更新而非新建」；Secret 值输入框不支持多行文本或显示字数；保存成功后无 Toast 确认；删除 Secret 前无二次确认，误操作导致流水线中断。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 进入仓库设置 → Secrets 配置页 → 点击「新建 Secret」→ 输入非法名称（如小写字母或以 ATOMGIT_ 开头）→ 观察实时校验反馈 → 输入已存在的名称 → 观察提示 → 填写值并保存 → 观察保存反馈 → 尝试删除某 Secret → 观察是否有二次确认
- **understandability_criterion**: Secret 名称输入框必须在失焦或输入时实时校验，并在不符合规则时给出红色边框和内联文案：「Secret 名称只能包含大写字母、数字和下划线，且不能以 ATOMGIT_ 开头。」；当输入已存在的 Secret 名称时，表单应切换为「更新」模式，或给出提示：「Secret 名称已存在，保存将覆盖原值。」；Secret 值输入框必须支持多行文本（textarea），并在右下角展示字符计数；保存成功后必须展示绿色 Toast「Secret 保存成功」；删除 Secret 前必须弹出模态框确认，文案包含 Secret 名称和警告「删除后引用该 Secret 的流水线将失败」。
- **llm_assisted**: false
- **rationale**: Secrets 是 CI/CD 的敏感配置入口；表单校验缺失或误删除会导致生产流水线中断。对应风险登记册 RISK-SEC-05（PAT/Secret 泄露与配置）。
- **expected_behavior**: 实时校验、覆盖提示、保存确认、删除二次确认。
- **related_compat_diff**: `secrets.ATOMGIT_TOKEN` 对应 GitHub 的 `secrets.GITHUB_TOKEN`；Secrets 命名规则应保持一致以降低迁移成本。

---

## INTENT-USE-030
- **id**: INTENT-USE-030
- **dimensions**: [usability]
- **scenario**: 大 diff 文件在 MR 评审页的懒加载/分页与性能提示
- **user_perspective**: 迁移开发者在评审包含大量文件变更的 MR 时，期望页面流畅加载并了解加载进度
- **pain_point**: 大 MR（如 >100 个文件变更）打开后页面白屏或卡死数秒；diff 区域无加载骨架屏或进度提示；大文件（如 >1MB 的生成文件）未自动折叠，导致滚动极长；超出显示限制的文件未给出「还有 X 个文件未加载，点击加载更多」的提示；二进制文件未明确标注「二进制差异不可查看」。
- **priority**: P1
- **ui_candidate**: true
- **ui_interaction**: 打开一个包含大量文件变更的 MR → 观察 diff 区域的加载过程 → 检查是否有骨架屏或进度条 → 滚动到底部观察是否有「加载更多」按钮 → 检查大生成文件是否默认折叠 → 检查二进制文件的展示方式
- **understandability_criterion**: 当 MR 包含超过 20 个文件变更时，页面必须展示加载骨架屏或进度提示（如「正在加载差异，已加载 15/120 个文件」）；单文件 diff 超过 500 行时必须默认折叠超出部分，并展示「展开剩余 X 行」按钮；文件列表顶部必须展示统计信息「共 X 个文件变更，+Y 行，-Z 行」；二进制文件必须以独立卡片展示，文案为「二进制文件，无法显示差异」；若存在被隐藏的大文件（如 >1MB），必须以灰色折叠条展示，并标注文件大小和「此文件过大，已自动折叠」。
- **llm_assisted**: false
- **rationale**: 大 MR 评审是日常协作的高频场景；页面卡顿或无加载反馈会让评审人放弃在线评审，转向本地工具。
- **expected_behavior**: 懒加载或分页；大文件自动折叠；二进制明确标注；文件统计常驻顶部。
- **related_compat_diff**: 无直接差异，但 diff 渲染性能与 GitHub 的对比是迁移用户的隐性期望。

---

## 质量自检

- [x] 错误信息类 intent（016、019、020、022、023、024、029）给出了「应包含什么」的具体判据，不是「报错要友好」。
- [x] 覆盖了从 GitHub 迁移的主要摩擦路径：workflow 目录路径差异（019）、上下文变量差异（020）、Runner 标签差异（023）、手动触发表单差异（015）。
- [x] 需主观评判的项（019、020、022、023、024、026）显式标了 `llm_assisted`；其余客观可判定的标 `false`。
- [x] 不与 compat-diff 重复：易用性关注「体验/可理解」，兼容性关注「行为对不对」。
- [x] intent 只描述意图层，未写执行细节、未写 GitCode 具体语法。
- [x] 优先级取自风险登记册：P0 对应 RISK-USE-02（文档承诺与实现不一致），P1 对应 RISK-USE-01（迁移报错不指明差异）和 RISK-USE-04（通知延迟）。
