# Case Manifest — Run 2026-08-25-01

> 用例全集清单（上轮复用 + 本轮新增 UI 用例）
> 生成日期: 2026-08-25

---

## 统计摘要

- **总用例数**: 159 条
  - 上轮复用: 135 条
  - 本轮新增 UI: 24 条

### 按 test_type 统计

| test_type | 条数 |
|---|---|
| api | 86 |
| git | 5 |
| workflow | 44 |
| ui | 24 |

### 按维度统计

| 维度 | 条数 |
|---|---|
| completeness | 98 |
| usability | 16 |
| reliability | 18 |
| compatibility | 6 |
| security | 21 |

### 按优先级统计

| 优先级 | 条数 |
|---|---|
| P0 | 41 |
| P1 | 108 |
| P2 | 10 |

---

## 一、已有用例复用记录（上轮基底）

本轮 `cases/` 目录已完整复制上轮用例，不重复生成。

### 1.1 已有 UI 用例参考（不在本轮 cases/ 目录，仅作覆盖参考）

| 已有用例 | 覆盖 Intent | 说明 |
|---|---|---|
| UI-ISSUE-01-002 | USE-001（部分） | 已覆盖创建 Issue 正向路径 |
| UI-MR-01-002 | USE-003（部分） | 已覆盖 MR 创建正向路径 |
| UI-MR-01-003 | USE-004（部分） | 已覆盖合并成功路径 |

### 1.2 本轮已复制用例按维度清单（135 条）

#### completeness

| ID | test_type | priority | title | intent_ref |
|---|---|---|---|---|
| API-BOARD-01-001 | api | P2 | 探测仓库 Projects/看板 API 可用性 | INTENT-ISSUE-006 |
| API-BOARD-01-002 | api | P2 | 探测 Issues 列表 API 是否返回项目/看板字段 | INTENT-ISSUE-006 |
| API-BRANCH-01-004 | api | P1 | 通过 API 创建分支 | INTENT-GIT-004 |
| API-HOOK-01-001 | api | P1 | 创建 Webhook 并验证事件投递 | INTENT-HOOK-001 |
| API-HOOK-01-002 | api | P1 | Webhook 签名验证失败时拒绝请求 | INTENT-HOOK-001 |
| API-ISSUE-01-002 | api | P0 | 创建 Issue 并关闭 | INTENT-ISSUE-001 |
| API-ISSUE-01-003 | api | P1 | 创建标签并关联到 Issue | INTENT-ISSUE-002 |
| API-ISSUE-01-004 | api | P1 | 创建里程碑并关联到 Issue | INTENT-ISSUE-002 |
| API-ISSUE-01-005 | api | P1 | 创建 Issue 评论并包含 @提及 | INTENT-ISSUE-003 |
| API-ISSUE-01-007 | api | P2 | 探测仓库 Issue 模板目录存在性 | INTENT-ISSUE-005 |
| API-ISSUE-01-008 | api | P2 | 探测 Issue 创建 API 是否支持模板参数 | INTENT-ISSUE-005 |
| API-MR-01-002 | api | P0 | 创建 MR 并验证状态机流转 | INTENT-MR-001 |
| API-MR-01-003 | api | P0 | MR 使用 Squash 合并策略 | INTENT-MR-001 |
| API-MR-01-004 | api | P0 | 提交 MR 行级评论 | INTENT-MR-003 |
| API-MR-01-005 | api | P0 | 提交 MR 评审并标记 APPROVE | INTENT-MR-003 |
| API-MR-01-006 | api | P0 | MR 必须过 CI 才能合并 | INTENT-MR-004 |
| API-MR-01-007 | api | P1 | MR 冲突检测返回 conflict 状态 | INTENT-MR-002 |
| API-REPO-01-002 | api | P1 | 空仓库的分支列表返回空数组 | INTENT-GIT-005 |
| API-SMOKE-01-001 | api | P1 | 探测 设置项目模块 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-002 | api | P1 | 探测 修改项目代码审查设置 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-003 | api | P1 | 探测 更新仓库的权限模式 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-004 | api | P1 | 探测 设置项目推送规则 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-005 | api | P1 | 探测 Fork一个仓库 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-006 | api | P1 | 探测 上传图片 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-007 | api | P1 | 探测 上传文件 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-008 | api | P1 | 探测 更新仓库设置 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-009 | api | P1 | 探测 更新 Pull Request设置 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-010 | api | P1 | 探测 更新项目成员角色 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-011 | api | P1 | 探测 仓库转移 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-012 | api | P1 | 探测 标记一个仓库里的通知为已读 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-013 | api | P1 | 探测 新建保护分支规则 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-014 | api | P1 | 探测 删除分支 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-015 | api | P1 | 探测 创建commit评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-016 | api | P1 | 探测 删除commit评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-017 | api | P1 | 探测 更新Commit评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-018 | api | P1 | 探测 创建一个仓库的Tag 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-019 | api | P1 | 探测 创建项目保护 tag 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-020 | api | P1 | 探测 修改项目保护 tag 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-021 | api | P1 | 探测 删除项目保护 tag 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-022 | api | P1 | 探测 删除仓库的一个Tag 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-023 | api | P1 | 探测 创建Issue标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-024 | api | P1 | 探测 删除Issue所有标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-025 | api | P1 | 探测 替换Issue所有标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-026 | api | P1 | 探测 删除Issue标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-027 | api | P1 | 探测 更新Issue某条评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-028 | api | P1 | 探测 删除Issue某条评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-029 | api | P1 | 探测 设置Issue关联的分支 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-030 | api | P1 | 探测 删除一个仓库任务标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-031 | api | P1 | 探测 更新一个仓库的任务标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-032 | api | P1 | 探测 替换所有仓库标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-033 | api | P1 | 探测 取消用户测试Pull Request 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-034 | api | P1 | 探测 重置 Pull Request测试 的状态 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-035 | api | P1 | 探测 指派用户测试 Pull Request 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-036 | api | P1 | 探测 Pull Request关联issue 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-037 | api | P1 | 探测 Pull Request删除关联的issue 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-038 | api | P1 | 探测 更新Pull Request信息 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-039 | api | P1 | 探测 创建 Pull Request标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-040 | api | P1 | 探测 替换 Pull Request所有标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-041 | api | P1 | 探测 回复Pull Request评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-042 | api | P1 | 探测 删除 Pull Request标签 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-043 | api | P1 | 探测 修改检视意见解决状态 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-044 | api | P1 | 探测 处理 Pull Request测试 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-045 | api | P1 | 探测 指派用户评审Pull Request 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-046 | api | P1 | 探测 取消用户评审Pull Request 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-047 | api | P1 | 探测 重置 Pull Request审查 的状态 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-048 | api | P1 | 探测 指派用户审查 Pull Request 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-049 | api | P1 | 探测 取消用户审查 Pull Request 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-050 | api | P1 | 探测 编辑评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-051 | api | P1 | 探测 删除评论 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-052 | api | P1 | 探测 删除仓库单个里程碑 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-053 | api | P1 | 探测 更新仓库里程碑 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-054 | api | P1 | 探测 添加项目成员或更新项目成员权限 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-055 | api | P1 | 探测 移除项目成员 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-056 | api | P1 | 探测 更新一个仓库WebHook 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-057 | api | P1 | 探测 删除一个仓库WebHook 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-058 | api | P1 | 探测 更新仓库Release 端点可用性 | INTENT-COMP-106 |
| API-SMOKE-01-059 | api | P1 | 探测 删除指定 Artifact 端点可用性 | INTENT-COMP-106 |
| API-TAG-01-001 | api | P1 | 通过 API 创建 Release 与 Tag | INTENT-GIT-004 |
| API-USER-01-002 | api | P0 | PAT 带正确 scope 可访问仓库 API | INTENT-AUTH-001 |
| API-USER-01-003 | api | P0 | PAT 无 repo scope 时访问仓库 API 返回 403 | INTENT-AUTH-001 |
| API-USER-01-004 | api | P0 | Developer 角色不可修改保护分支规则 | INTENT-AUTH-002 |
| API-USER-01-005 | git | P0 | Reporter 角色不可推送代码 | INTENT-AUTH-002 |
| GIT-CLONE-01-002 | git | P0 | Git Clone 使用 PAT 进行 HTTPS 鉴权 | INTENT-GIT-001 |
| GIT-CLONE-01-003 | git | P0 | Git Clone 使用 SSH 密钥鉴权 | INTENT-GIT-001 |
| GIT-LFS-01-001 | git | P1 | Git LFS 跟踪并推送大文件 | INTENT-GIT-003 |

#### usability

| ID | test_type | priority | title | intent_ref |
|---|---|---|---|---|
| API-MR-01-008 | api | P1 | Draft MR 标题含 WIP 前缀且不可直接合并 | INTENT-MR-005 |
| USE-ANNO-01-001 | workflow | P1 | workflow 命令 ::error:: / ::warning:: 注解在 UI 中的可读性与定位能力 | INTENT-USE-016 |
| USE-DOCS-01-001 | api | P0 | 官方文档中 GitHub 专有措辞应已替换为 GitCode 术语 | INTENT-USE-017 |
| USE-MASK-01-001 | workflow | P1 | Secret 掩码被绕过时日志应发出暴露预警 | INTENT-USE-011 |
| USE-NOTIF-01-001 | workflow | P1 | MR 触发 CI 失败后通知的时效性与信息完整性 | INTENT-USE-008 |

#### reliability

| ID | test_type | priority | title | intent_ref |
|---|---|---|---|---|
| API-RATE-01-001 | api | P1 | 高频触发下 API 正确返回 429 与 Retry-After | INTENT-REL-018 |
| REL-ACTN-01-001 | workflow | P1 | 依赖 action 不可用时 workflow 失败与报错清晰度 | INTENT-REL-017 |
| REL-ARTF-01-001 | workflow | P1 | 上传 500MB artifact 观察上限与报错 | INTENT-REL-020 |
| REL-CACH-01-001 | workflow | P1 | 写入 500MB cache 观察上限与 LRU 淘汰 | INTENT-REL-021 |
| REL-CONC-01-001 | workflow | P1 | 短时间内高频触发同仓库 workflow 的排队与公平性 | INTENT-REL-002 |
| REL-FAULT-01-001 | workflow | P1 | runner 磁盘写满后 job 行为与报错清晰度 | INTENT-REL-013 |
| REL-FAULT-01-002 | workflow | P1 | stress CPU 时 step 超时与心跳保活 | INTENT-REL-014 |
| REL-FAULT-01-003 | workflow | P1 | 模拟 runner 崩溃后 job 状态迁移与重调度 | INTENT-REL-015 |
| REL-FAULT-01-004 | workflow | P1 | 断开 runner 外网后观察依赖下载失败与重试 | INTENT-REL-016 |
| REL-GIT-01-001 | git | P1 | 1GB+ 仓库克隆的耗时与资源稳定性 | INTENT-REL-010 |
| REL-LOGS-01-001 | workflow | P1 | 单 step 输出 50MB 文本日志的实时性与完整性 | INTENT-REL-009 |
| REL-MATX-01-001 | workflow | P1 | matrix max-parallel=2 时矩阵展开实例并发度被限制 | INTENT-REL-004 |
| REL-MATX-01-002 | workflow | P1 | matrix fail-fast=true 时单实例失败取消其余实例 | INTENT-REL-007 |
| REL-MATX-01-003 | workflow | P1 | 矩阵组合数超过平台上限时应报错或拒绝 | INTENT-REL-008 |
| REL-MEM-01-001 | workflow | P1 | small runner 上申请 12GB 内存观察 OOM kill 行为 | INTENT-REL-023 |
| REL-NEEDS-01-001 | workflow | P0 | needs 依赖的 matrix job 全成功但上游初始化 job 失败时下游不应执行 | INTENT-REL-005 |
| REL-STEPS-01-001 | workflow | P1 | 单 job 16 个 step 的调度与状态回写完整性 | INTENT-REL-012 |
| REL-TIME-01-001 | workflow | P1 | job 运行 350 分钟观察正常终止 vs 超时 kill | INTENT-REL-011 |

#### compatibility

| ID | test_type | priority | title | intent_ref |
|---|---|---|---|---|
| COMPAT-CACHE-01-001 | workflow | P1 | fork PR 写入的 cache 不得被目标仓库主分支读取 | INTENT-COMPAT-025 |
| COMPAT-MASK-01-001 | workflow | P0 | secret 经过 base64 拼接变形后仍应在日志中被掩码 | INTENT-COMPAT-023 |
| COMPAT-MIGR-01-001 | workflow | P0 | 使用 GitHub Actions 语法时校验器报错应指明 GitCode 差异 | INTENT-COMPAT-028 |
| COMPAT-PRTARGET-01-001 | workflow | P0 | pull_request_target 默认 checkout 目标仓库 base 分支代码 | INTENT-COMPAT-024 |
| COMPAT-PRTARGET-01-002 | workflow | P0 | pull_request_target 中显式 checkout PR 头分支后执行不可信脚本应被隔离 | INTENT-COMPAT-024 |
| COMPAT-UNKN-01-001 | workflow | P1 | 含未知顶层字段的 YAML 应给出精确字段路径与有效值提示 | INTENT-COMPAT-002 |

#### security

| ID | test_type | priority | title | intent_ref |
|---|---|---|---|---|
| SEC-ACTION-01-001 | workflow | P1 | 浮动 tag 被篡改后使用 commit SHA 固定可防供应链攻击 | INTENT-SEC-014 |
| SEC-ACTION-01-002 | workflow | P1 | 本地 action 使用路径遍历引用仓库外路径应被拒绝 | INTENT-SEC-015 |
| SEC-CACHE-01-001 | workflow | P1 | fork PR 保存的 cache 不得被主分支 workflow 命中 | INTENT-SEC-009 |
| SEC-CACHE-01-002 | workflow | P1 | 不同仓库使用相同 cache key 时数据隔离 | INTENT-SEC-010 |
| SEC-ENV-01-001 | workflow | P0 | 通过 ATOMGIT_ENV 写入污染数据不得破坏后续步骤执行上下文 | INTENT-SEC-006 |
| SEC-FORK-01-001 | workflow | P0 | fork PR 触发 pull_request 时严禁读取目标仓库 secrets | INTENT-SEC-001 |
| SEC-FORK-01-002 | workflow | P0 | fork PR 通过 ${{ secrets }} 对象枚举不得获取 secret 名列表 | INTENT-SEC-001 |
| SEC-HOOK-01-001 | api | P1 | Webhook secret 在配置界面不回显且签名验证不可绕过 | INTENT-SEC-018 |
| SEC-INJ-01-001 | workflow | P0 | PR 标题含命令注入 payload 时不应执行 | INTENT-SEC-004 |
| SEC-INJ-01-002 | workflow | P0 | 分支名含 shell 元字符时不应破坏 run 脚本 | INTENT-SEC-004 |
| SEC-INJ-01-003 | workflow | P0 | issue_comment 正文含脚本注入 payload 时不应执行 | INTENT-SEC-005 |
| SEC-LEAK-01-001 | workflow | P0 | secret 值不得通过 artifact 文件外泄 | INTENT-SEC-003 |
| SEC-MASK-01-001 | workflow | P0 | secret 经过 JSON 转义与 URL 编码后仍应在日志中被掩码 | INTENT-SEC-002 |
| SEC-PERM-01-001 | workflow | P0 | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限应只读 | INTENT-SEC-011 |
| SEC-PERM-01-002 | workflow | P0 | job 级 permissions 声明应正确限制 ATOMGIT_TOKEN 权限 | INTENT-SEC-012 |
| SEC-PRTARGET-01-001 | workflow | P0 | pull_request_target 中 checkout PR 头分支后运行 build.sh 应被隔离 | INTENT-SEC-007 |
| SEC-PRTARGET-01-002 | workflow | P0 | pull_request_target 中恶意 PR 修改 workflow 文件不被执行 | INTENT-SEC-007 |
| SEC-PRTARGET-01-003 | workflow | P0 | pull_request_target 的 workflow 文件来源校验 | INTENT-SEC-008 |
| SEC-ROLE-01-002 | api | P0 | Reporter 角色不得触发 workflow_dispatch | INTENT-SEC-013 |
| SEC-RUNNER-01-001 | workflow | P1 | 复用型 Runner 不得跨 job 残留敏感文件或环境变量 | INTENT-SEC-016 |
| SEC-RUNNER-01-002 | workflow | P1 | 自托管 Runner 注册令牌不得在工作流日志或环境变量中泄露 | INTENT-SEC-020 |

---

## 二、本轮新增 UI 用例清单（24 条）

针对准入 intent 的缺口生成新 UI 用例，覆盖 Issue/MR/Repo/Search/User/Nav/Board/Code/Org 等主题。

| ID | dimension | priority | title | intent_ref |
|---|---|---|---|---|
| UI-BOARD-25-001 | completeness | P2 | 全局看板列表与卡片交互覆盖 | INTENT-COMP-010 |
| UI-CODE-25-001 | usability | P2 | 代码查看页行内评论与锚点分享体验 | INTENT-USE-011 |
| UI-CODE-25-002 | completeness | P2 | 代码 Blame 视图与 Raw 文件查看可达性 | INTENT-COMP-011 |
| UI-ISSUE-25-001 | usability | P0 | Issue 创建时空标题异常提示验证 | INTENT-USE-001 |
| UI-ISSUE-25-002 | usability | P0 | Issue 列表筛选与排序交互响应验证 | INTENT-USE-002 |
| UI-ISSUE-25-003 | completeness | P0 | Issue 详情页评论操作与核心信息渲染 | INTENT-COMP-001 |
| UI-ISSUE-25-004 | completeness | P0 | Issue 标签与里程碑绑定功能 | INTENT-COMP-002 |
| UI-MR-25-001 | usability | P0 | Merge Request 创建时分支选择与差异预览可用性 | INTENT-USE-003 |
| UI-MR-25-002 | usability | P0 | Merge Request 冲突状态交互反馈 | INTENT-USE-004 |
| UI-MR-25-003 | completeness | P0 | Merge Request 关闭与重新打开状态流转 | INTENT-COMP-004 |
| UI-MR-25-004 | completeness | P0 | Merge Request 差异对比页代码评审评论完整渲染 | INTENT-COMP-003 |
| UI-MR-25-005 | completeness | P0 | Merge Request 合并后页面锁定与状态展示 | INTENT-COMP-004 |
| UI-MR-25-006 | completeness | P2 | 合并冲突时 Web 冲突解决入口与状态提示覆盖 | INTENT-COMP-012 |
| UI-NAV-25-001 | usability | P2 | 无权限与 404 页面友好提示及返回引导 | INTENT-USE-012 |
| UI-ORG-25-001 | completeness | P1 | 组织设置与仓库级集成配置页面核心功能可达性 | INTENT-COMP-008 |
| UI-REPO-25-001 | usability | P1 | 仓库文件树大目录下加载与浏览体验 | INTENT-USE-005 |
| UI-REPO-25-002 | usability | P1 | 分支切换器搜索与切换体验 | INTENT-USE-006 |
| UI-REPO-25-003 | completeness | P1 | 仓库文件在线编辑与预览 | INTENT-COMP-005 |
| UI-REPO-25-004 | completeness | P1 | 分支列表管理与保护规则功能覆盖 | INTENT-COMP-006 |
| UI-REPO-25-005 | completeness | P1 | 仓库成员管理页面邀请与列表 | INTENT-COMP-007 |
| UI-REPO-25-006 | completeness | P1 | 仓库 Fork 流程与 Fork 后独立导航 | INTENT-COMP-009 |
| UI-SEARCH-25-001 | usability | P1 | 全局搜索输入响应与结果分类展示 | INTENT-USE-007 |
| UI-USER-25-001 | usability | P1 | 用户工作台通知中心读取与批量操作 | INTENT-USE-008 |
| UI-USER-25-002 | usability | P2 | 个人设置页表单保存与即时反馈 | INTENT-USE-010 |

### 新增用例与 Intent 覆盖映射

| Intent ID | 覆盖用例 | 覆盖场景 |
|---|---|---|
| INTENT-USE-001 | UI-ISSUE-25-001 | Issue 创建空标题异常提示 |
| INTENT-USE-002 | UI-ISSUE-25-002 | Issue 列表筛选与排序 |
| INTENT-USE-003 | UI-MR-25-001 | MR 创建分支选择与 diff 预览 |
| INTENT-USE-004 | UI-MR-25-002 | MR 冲突状态交互反馈 |
| INTENT-USE-005 | UI-REPO-25-001 | 仓库文件树大目录浏览 |
| INTENT-USE-006 | UI-REPO-25-002 | 分支切换器搜索与切换 |
| INTENT-USE-007 | UI-SEARCH-25-001 | 全局搜索输入响应与分类展示 |
| INTENT-USE-008 | UI-USER-25-001 | 工作台通知中心读取与批量操作 |
| INTENT-USE-010 | UI-USER-25-002 | 个人设置页表单保存与即时反馈 |
| INTENT-USE-011 | UI-CODE-25-001 | 代码查看页行内评论与锚点分享 |
| INTENT-USE-012 | UI-NAV-25-001 | 无权限/404 页面友好提示与返回引导 |
| INTENT-COMP-001 | UI-ISSUE-25-003 | Issue 详情页核心信息渲染与评论操作 |
| INTENT-COMP-002 | UI-ISSUE-25-004 | Issue 标签与里程碑管理绑定功能 |
| INTENT-COMP-003 | UI-MR-25-004 | MR diff 页与代码评审评论完整渲染 |
| INTENT-COMP-004 | UI-MR-25-003, UI-MR-25-005 | MR 关闭/重开/合并后锁定状态流转 |
| INTENT-COMP-005 | UI-REPO-25-003 | 仓库文件在线编辑、预览与提交记录查看 |
| INTENT-COMP-006 | UI-REPO-25-004 | 分支列表管理、保护规则与分支对比 |
| INTENT-COMP-007 | UI-REPO-25-005 | 仓库成员管理页面邀请、列表与角色变更 |
| INTENT-COMP-008 | UI-ORG-25-001 | 组织设置与仓库级集成配置核心功能可达性 |
| INTENT-COMP-009 | UI-REPO-25-006 | 仓库 Fork 流程与 Fork 后独立导航 |
| INTENT-COMP-010 | UI-BOARD-25-001 | 全局看板/Projects 页面列表与卡片交互 |
| INTENT-COMP-011 | UI-CODE-25-002 | 代码 Blame 视图与 Raw 文件查看可达性 |
| INTENT-COMP-012 | UI-MR-25-006 | 合并冲突时 Web 冲突解决入口与状态提示 |

---

## 三、Schema 与校验状态

- Schema: `phase01/schema/executable-case.schema.yaml`（已扩展 `test_type: ui`）
- 校验脚本: `phase02/scripts/schema_check.py`（已同步支持 `ui` test_type）
- 本轮校验结果: **159 条通过 / 0 条拒收**

---

## 状态

`completed`（用例设计 + 编译 + 校验全部完成）
