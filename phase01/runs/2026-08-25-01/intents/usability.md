# Usability Intents — Web UI Automation (Phase 01 Run 2026-08-25-01)

## INTENT-USE-001
- **dimensions**: [usability]
- **priority**: P0
- **title**: Issue 创建流程的表单可用性与异常提示验证
- **risk**: Issue 创建是高频核心操作；表单校验缺失或提示不清会导致用户重复提交或创建无效 Issue，直接影响协作效率。
- **expected_behavior**: 必填项为空、标题过长或标签非法时，系统应在对应字段附近即时显示明确错误提示，且提交按钮置灰或拦截提交；创建成功后自动跳转至新 Issue 详情页。
- **test_approach**: Playwright UI 自动化，覆盖空标题、超长标题、非法字符、快速重复点击提交等场景。

## INTENT-USE-002
- **dimensions**: [usability]
- **priority**: P0
- **title**: Issue 列表筛选与排序的交互响应及状态保持
- **risk**: 筛选/排序状态丢失或响应延迟会降低大规模项目管理效率，用户可能误以为数据未同步。
- **expected_behavior**: 按状态、标签、负责人筛选及多字段排序后，列表即时刷新；浏览器刷新或返回后筛选条件应通过 URL Query 保持；无结果时展示友好空状态引导。
- **test_approach**: Playwright UI 自动化，验证筛选组合、排序切换、URL 同步、空状态渲染。

## INTENT-USE-003
- **dimensions**: [usability]
- **priority**: P0
- **title**: Merge Request 创建时源/目标分支选择与差异预览可用性
- **risk**: 分支选错会导致代码误合并，差异加载失败会让用户在无上下文的情况下提交 MR，存在严重质量风险。
- **expected_behavior**: 分支选择器应支持搜索且禁止选择相同分支；差异预览需在合理时间内加载完成；若无可合并差异则明确提示并禁用提交。
- **test_approach**: Playwright UI 自动化，验证分支搜索、同分支拦截、大 diff 加载、无 diff 提示。

## INTENT-USE-004
- **dimensions**: [usability, completeness]
- **priority**: P0
- **title**: Merge 按钮的权限控制与冲突状态交互反馈
- **risk**: 无权限用户若能点击 Merge 或冲突时仍显示可合并，将直接威胁主干稳定性。
- **expected_behavior**: 存在冲突或 CI 未通过时 Merge 按钮置灰并说明原因；无权限用户不展示 Merge 按钮或提示权限不足；点击后显示进度直至完成或失败。
- **test_approach**: Playwright UI 自动化，结合不同角色账号验证按钮状态与提示文案。

## INTENT-USE-005
- **dimensions**: [usability]
- **priority**: P1
- **title**: 仓库文件树在大目录下的加载与浏览体验
- **risk**: 深层目录或大量文件时渲染卡顿、路径面包屑丢失会导致开发者定位文件困难。
- **expected_behavior**: 文件树支持懒加载或分页，展开/折叠流畅；面包屑始终可见且可点击回退；点击文件后代码高亮正确渲染。
- **test_approach**: Playwright UI 自动化，测试深层目录导航、大目录展开、面包屑回退、代码高亮。

## INTENT-USE-006
- **dimensions**: [usability]
- **priority**: P1
- **title**: 分支切换器在仓库浏览场景的搜索与切换体验
- **risk**: 分支数量庞大时无法快速定位目标分支，会显著降低多分支开发效率。
- **expected_behavior**: 分支切换器支持键盘搜索、最近使用分支置顶；切换后页面内容（文件树、README）无刷新闪烁或 404；非法分支名输入给出即时反馈。
- **test_approach**: Playwright UI 自动化，验证搜索过滤、最近分支、切换后内容一致性、异常分支名处理。

## INTENT-USE-007
- **dimensions**: [usability, completeness]
- **priority**: P1
- **title**: 全局搜索的输入响应与结果分类展示
- **risk**: 搜索是跨仓库/跨项目信息检索的核心入口；结果分类混乱或高延迟会使用户转向外部工具。
- **expected_behavior**: 输入时即时展示建议（debounce 合理）；结果页按仓库/Issue/MR/代码等分类展示；无结果时提供模糊搜索建议；分页或无限滚动稳定。
- **test_approach**: Playwright UI 自动化，测试搜索建议、分类标签切换、无结果状态、长列表滚动。

## INTENT-USE-008
- **dimensions**: [usability]
- **priority**: P1
- **title**: 用户工作台通知中心的读取与批量操作体验
- **risk**: 通知堆积或已读状态不同步会导致用户错过关键协作事件（如 MR 被合并、Issue 被指派）。
- **expected_behavior**: 通知列表按时间倒序，未读有显式标记；支持单条/全部已读；点击通知应跳转至对应业务页面并标记为已读；空状态时引导用户关注仓库。
- **test_approach**: Playwright UI 自动化，验证未读标记、批量已读、跳转行为、空状态。

## INTENT-USE-009
- **dimensions**: [usability]
- **priority**: P2
- **title**: 登录流程的多因子与错误提示可用性
- **risk**: 登录失败原因不明（如密码错误 vs 账号锁定）会增加用户挫败感，甚至导致支持工单上升。
- **expected_behavior**: 账号/密码错误时给出模糊但明确的提示（不暴露账号是否存在）；验证码过期或错误可刷新重试；登录成功后正确重定向至原目标页；会话过期后交互应引导重新登录而非白屏。
- **test_approach**: Playwright UI 自动化，覆盖错误凭证、验证码刷新、登录后重定向、会话过期场景。

## INTENT-USE-010
- **dimensions**: [usability, completeness]
- **priority**: P2
- **title**: 个人设置页表单保存与即时反馈
- **risk**: 设置项（如邮箱、SSH Key、通知偏好）保存失败无提示，会导致用户配置静默丢失。
- **expected_behavior**: 修改设置后保存按钮即时响应；成功/失败均展示 Toast 或内联提示；邮箱等敏感变更需二次确认；表单离开前若有未保存改动应提示确认。
- **test_approach**: Playwright UI 自动化，验证保存成功/失败提示、二次确认弹窗、未保存离开拦截。

## INTENT-USE-011
- **dimensions**: [usability]
- **priority**: P2
- **title**: 代码查看页的行内评论与锚点分享体验
- **risk**: 代码评审是质量门禁的核心环节；行评论无法定位或锚点链接失效会严重影响异步评审效率。
- **expected_behavior**: 点击行号可高亮并生成锚点链接；复制链接后在新标签页打开应自动滚动至对应行并高亮；行内评论展开/收起不导致页面跳动；长代码文件支持惰性加载或虚拟滚动。
- **test_approach**: Playwright UI 自动化，验证行高亮、锚点链接持久化、评论展开、大文件滚动。

## INTENT-USE-012
- **dimensions**: [usability]
- **priority**: P2
- **title**: 无权限/404 页面的友好提示与返回引导
- **risk**: 直接暴露 404/403 技术堆栈或缺乏返回引导，会降低安全感知并增加用户流失。
- **expected_behavior**: 访问不存在仓库或无权限页面时，展示品牌一致的友好插图与文案；提供返回首页、搜索或联系管理员的明确按钮；不暴露内部路径或技术细节。
- **test_approach**: Playwright UI 自动化，验证 404/403 页面渲染、按钮跳转、信息泄露检查。
