# Completeness Intents — Web UI Automation (Phase 01 Run 2026-08-25-01)

## INTENT-COMP-001
- **dimensions**: [completeness]
- **priority**: P0
- **title**: Issue 详情页核心信息渲染与评论操作覆盖
- **risk**: Issue 详情是协作闭环的核心页面；若评论区无法加载、状态按钮缺失或关联 MR 不显示，会导致用户无法跟进问题，现有用例仅覆盖列表页，存在重大场景遗漏。
- **expected_behavior**: Issue 详情页应正确展示标题、状态、标签、负责人、描述及评论列表；支持添加/删除评论；状态流转按钮（关闭/重新打开）可见且可交互。
- **test_approach**: Playwright UI 自动化，访问具体 Issue 详情页，验证元素存在、评论提交与状态切换。

## INTENT-COMP-002
- **dimensions**: [completeness]
- **priority**: P0
- **title**: Issue 标签与里程碑管理页面的存在性与绑定功能
- **risk**: 标签和里程碑是项目管理的分类与进度基础；若管理页面缺失或绑定后未生效，将直接导致项目治理手段失效，当前无任何 UI 用例覆盖。
- **expected_behavior**: 仓库应提供标签列表/新建页、里程碑列表/新建页；在 Issue 详情或列表可将标签/里程碑绑定至 Issue，保存后即时生效并在列表筛选中可用。
- **test_approach**: Playwright UI 自动化，验证标签/里程碑页面可达、新建/编辑/删除流程、Issue 绑定与筛选联动。

## INTENT-COMP-003
- **dimensions**: [completeness]
- **priority**: P0
- **title**: Merge Request 差异对比页与代码评审评论的完整渲染
- **risk**: 代码评审是质量门禁的核心环节；若 diff 区域无法渲染、大文件被截断无提示或行内评论无法添加，则评审流于形式，现有用例未覆盖 diff 查看与评审交互。
- **expected_behavior**: MR 详情页应展示源/目标分支差异，支持文件级展开/折叠；支持点击行号添加行内评论；评论应持久化并在刷新后可见。
- **test_approach**: Playwright UI 自动化，打开具体 MR diff 页，验证文件树、diff 渲染、行评论提交与回显。

## INTENT-COMP-004
- **dimensions**: [completeness]
- **priority**: P0
- **title**: MR 生命周期状态流转（关闭、重新打开、合并后锁定）
- **risk**: MR 状态管理混乱会导致已关闭请求被误合并或已合并请求仍可重复操作，威胁主干稳定性；当前仅有合按钮用例，缺少关闭与重新打开覆盖。
- **expected_behavior**: MR 作者或管理员可执行关闭和重新打开；已关闭 MR 应禁用合并按钮并提示状态；已合并 MR 不允许再次合并或关闭，页面展示锁定态。
- **test_approach**: Playwright UI 自动化，对不同状态 MR 验证按钮可用性、状态文案及操作后 URL/页面一致性。

## INTENT-COMP-005
- **dimensions**: [completeness]
- **priority**: P1
- **title**: 仓库文件在线编辑、预览与提交记录查看
- **risk**: 轻量编辑和提交追溯是日常高频操作；若编辑入口缺失或提交历史无法加载，将迫使用户切换至本地 Git，降低平台粘性；当前仅覆盖仓库首页文件树可见性。
- **expected_behavior**: 文件浏览页支持点击编辑进入 Web IDE/编辑器，修改后可填写提交信息并直接提交；提交历史页按时间倒序列出 commit，支持点击查看具体 diff。
- **test_approach**: Playwright UI 自动化，验证文件编辑入口、编辑-提交流程、提交历史列表及单条 commit 详情页可达。

## INTENT-COMP-006
- **dimensions**: [completeness]
- **priority**: P1
- **title**: 分支列表管理、保护规则与分支对比功能覆盖
- **risk**: 分支是版本控制的核心；若分支列表无法展示、保护规则设置页缺失或分支对比无结果，会导致发布管理失控；现有用例未覆盖分支管理场景。
- **expected_behavior**: 仓库应提供分支列表页，支持搜索与删除；分支保护规则页支持设置推送/合并权限；分支对比页可任选两分支展示差异。
- **test_approach**: Playwright UI 自动化，验证分支列表页可达、保护规则表单提交、对比页差异渲染。

## INTENT-COMP-007
- **dimensions**: [completeness]
- **priority**: P1
- **title**: 仓库成员管理页面的邀请、列表与角色变更
- **risk**: 权限管理是安全合规的基础；若成员管理页缺失或角色变更后未即时生效，会导致越权访问或协作受阻；当前无用户与权限相关 UI 用例。
- **expected_behavior**: 仓库设置中应存在成员管理页，展示当前成员列表；支持通过用户名/邮箱邀请新成员；可修改成员角色（Owner/Maintainer/Developer 等）；变更后成员权限即时生效。
- **test_approach**: Playwright UI 自动化，验证成员页可达、邀请流程、角色下拉切换及保存提示。

## INTENT-COMP-008
- **dimensions**: [completeness]
- **priority**: P1
- **title**: 组织设置与仓库级集成配置页面的核心功能可达性
- **risk**: 组织和仓库设置（如 Webhook、部署密钥、合并策略）是 DevOps 流程的枢纽；若页面缺失或表单无法提交，将导致自动化链路断裂。
- **expected_behavior**: 组织/仓库设置页应包含基本信息、成员、Webhooks、部署密钥、合并策略等模块；各模块表单可正常加载、保存并给出反馈。
- **test_approach**: Playwright UI 自动化，遍历设置页各 Tab，验证表单渲染、保存成功/失败状态及数据持久化。

## INTENT-COMP-009
- **dimensions**: [completeness]
- **priority**: P1
- **title**: 仓库 Fork 流程与 Fork 后仓库的独立导航
- **risk**: Fork 是开源协作的核心路径；若 Fork 入口缺失、流程中断或 Fork 后页面仍指向原仓库，会阻碍外部贡献者参与；当前无任何 Fork 相关 UI 覆盖。
- **expected_behavior**: 公开仓库应展示 Fork 按钮；点击后支持选择目标命名空间并确认创建；Fork 完成后自动跳转至新仓库首页，且后续导航（代码、Issues、MR）均指向 Fork 仓库。
- **test_approach**: Playwright UI 自动化，验证 Fork 入口存在、Fork 向导表单提交、跳转后 URL 与内容独立性。

## INTENT-COMP-010
- **dimensions**: [completeness]
- **priority**: P2
- **title**: 全局看板/Projects 页面的列表与卡片交互覆盖
- **risk**: 看板是敏捷项目管理的重要视图；若看板页面无法加载、Issue 卡片无法拖拽或状态列缺失，将直接影响团队迭代管理效率。
- **expected_behavior**: 项目看板页应展示多列状态（如待处理/进行中/已完成）；Issue 以卡片形式存在；支持拖拽卡片变更状态，且变更后 Issue 状态同步更新。
- **test_approach**: Playwright UI 自动化，验证看板页可达、列与卡片渲染、拖拽交互及状态同步。

## INTENT-COMP-011
- **dimensions**: [completeness]
- **priority**: P2
- **title**: 代码 Blame 视图与 Raw 文件查看的页面可达性
- **risk**: 代码追溯与原始文件查看是排查问题和集成外部工具的高频需求；若入口缺失或页面 500，会降低开发者对平台专业度的信任。
- **expected_behavior**: 文件浏览页应提供 Blame/Raw 切换入口；Blame 视图按行展示最近提交作者与时间；Raw 视图返回纯文本内容，无 HTML 框架干扰。
- **test_approach**: Playwright UI 自动化，验证 Blame/Raw 按钮存在、Blame 信息渲染、Raw 页内容与类型正确。

## INTENT-COMP-012
- **dimensions**: [completeness, usability]
- **priority**: P2
- **title**: 合并冲突时的 Web 冲突解决入口与状态提示覆盖
- **risk**: 冲突是合并流程的常见阻塞点；若冲突时缺少 Web 解决入口或提示文案不明确，会导致用户无法自助处理，增加支持成本；当前用例未覆盖冲突场景。
- **expected_behavior**: 存在冲突的 MR 应在详情页顶部明确提示冲突文件列表；提供“在线解决冲突”或“命令行指引”入口；冲突解决后页面状态自动刷新为可合并。
- **test_approach**: Playwright UI 自动化，构造冲突 MR，验证冲突提示、解决入口存在及状态刷新。
