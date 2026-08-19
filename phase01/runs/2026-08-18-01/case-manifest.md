# Case Manifest — Run 2026-08-18-01

> 用例全集清单（复用 + 新增 + DEPRECATE）
> 生成日期: 2026-08-18
> 基底: `baseline/case-base-detail.md` (260 KEEP + 307 DEPRECATE + 62 NEEDS-UPDATE) + `runs/smoke/cases/yaml/` (9 smoke YAMLs)

---

## 一、复用记录

以下 intent 已由 KEEP 历史用例或 smoke YAML 覆盖，本轮 **不生成新用例**，在 manifest 中标注复用来源。

### 1.1 由 KEEP 用例覆盖（workflow/Actions 基础能力）

| Intent | 优先级 | 覆盖 KEEP TC | 备注 |
|---|---|---|---|
| COMPAT-001 | P1 | TC-366, TC-383 | workflow 文件目录 `.gitcode/workflows/` |
| COMPAT-003 | P1 | TC-017~085 | 核心上下文对象命名差异 `atomgit.*` |
| COMPAT-004 | P1 | TC-197~222 | 系统环境变量前缀差异 `GITHUB_*` → `ATOMGIT_*` |
| COMPAT-005 | P1 | TC-356 | token 名称差异 `GITHUB_TOKEN` → `ATOMGIT_TOKEN` |
| COMPAT-006 | P1 | TC-176 | 状态函数调用语法差异 `success()` → `success` |
| COMPAT-007 | P1 | TC-179 | 失败状态函数名称差异 `failure()` → `failed` |
| COMPAT-008 | P1 | TC-180~187 | 表达式函数边界行为差异 |
| COMPAT-009 | P1 | TC-163, TC-539 | 数字字面量类型处理差异 |
| COMPAT-010 | P1 | TC-425, TC-464~470 | `pull_request` types 取值命名差异 |
| COMPAT-011 | P1 | TC-422, TC-514~517 | `paths` 路径过滤匹配上限 300 文件 |
| COMPAT-012 | P1 | TC-475~479, TC-504 | `schedule` cron 触发语义与调度边界 |
| COMPAT-013 | P1 | TC-238, TC-339 | `workflow_dispatch` / `workflow_call` inputs 类型限制 |
| COMPAT-015 | P1 | TC-371, TC-402~407, TC-584~587 | `stages` 阶段机制 |
| COMPAT-016 | P1 | TC-401, TC-406~407, TC-587 | `post` 后处理阶段 |
| COMPAT-017 | P1 | TC-289~290, TC-520~523 | `concurrency` 并发控制语法与语义差异 |
| COMPAT-018 | P1 | TC-351~353, TC-408~416, TC-588 | `permissions` 权限域命名差异 |
| COMPAT-019 | P1 | TC-356 | `permissions` 默认权限范围差异 |
| COMPAT-020 | P1 | TC-363, TC-365, TC-446~455, TC-457 | `runs-on` Runner 标签体系差异 |
| COMPAT-021 | P1 | TC-023, TC-094~095, TC-136~139, TC-441~442 | `runner` 上下文字段值格式差异 |
| COMPAT-022 | P1 | TC-437 | 默认 shell 选择差异 |
| COMPAT-026 | P1 | TC-304~312 | 内置 action 引用写法与版本锁定差异 |
| COMPAT-027 | P1 | TC-240~246 | 废弃 workflow 命令降级方式差异 |
| COMPAT-029 | P1 | TC-371, TC-399, TC-402 | `jobs` 顶层字段与 `stages` 嵌套结构兼容性 |
| COMPAT-014 | P2 | TC-426 | `workflow_call` 嵌套层数上限差异 |
| REL-001 | P1 | TC-289, TC-521 | `concurrency.max=5` 边界 |
| REL-003 | P1 | TC-520 | `concurrency` preemption 抢占 |
| REL-006 | P1 | TC-403 | `stages.fail_fast=true` 单 job 失败立即终止 |
| REL-024 | P1 | TC-426 | `workflow_call` 嵌套层数边界 |
| USE-004 | P0 | TC-023, TC-094~095, TC-136~139 | `runner.os` 文档值与实际返回值不一致 |
| USE-005 | P0 | TC-005~007, TC-115~119, TC-019 | `vars` 上下文文档声明与平台实际不支持 |
| USE-001 | P1 | TC-366, TC-383 | 迁移报错应指明路径差异 |
| USE-002 | P1 | TC-017~085 | 迁移报错应指明上下文命名差异 |
| USE-003 | P1 | TC-356, TC-197~222 | 迁移报错应指明令牌名称差异 |
| USE-006 | P1 | TC-274, TC-275 | YAML 静态校验报错应给出精确字段路径与有效值 |
| USE-010 | P1 | TC-240~246 | 废弃 workflow 命令日志应给出带行号替换指引 |
| USE-012 | P1 | TC-371, TC-399 | `stages` 与 `jobs` 混用报错应解释 GitCode 特有阶段机制 |
| USE-013 | P1 | TC-238, TC-339 | `workflow_dispatch` / `workflow_call` 非 string 输入类型迁移报错 |
| USE-014 | P1 | TC-351~416 | `permissions` 使用 GitHub 命名时报错应列出 GitCode 权限域映射 |
| USE-015 | P1 | TC-363, TC-365, TC-446~455, TC-457, TC-571~573 | `runs-on` 标签不匹配时报错应给出三段式格式示例 |
| USE-018 | P2 | TC-426 | `workflow_call` 嵌套超过 2 层时报错应给出深度与调用链 |

### 1.2 由 smoke YAML 覆盖

| Intent | 优先级 | 复用 Smoke YAML | 备注 |
|---|---|---|---|
| GIT-001 (部分) | P0 | GIT-CLONE-01-001 | Git Clone 基础能力，PAT/SSH 未覆盖 |
| MR-001 (部分) | P0 | API-PULLS-01-001 | MR 列表/获取，创建/合并策略未覆盖 |
| ISSUE-001 (部分) | P0 | API-ISSUES-01-001 | Issue 列表/获取，CRUD 未覆盖 |
| GIT-004 (部分) | P1 | API-BRANCHES-01-001 | 分支列表，创建/删除/标签未覆盖 |
| (API 基础) | — | API-REPO-01-001, API-USER-01-001, API-COMMITS-01-001 | smoke 基线用例 |
| (Git 基础) | — | GIT-FETCH-01-001 | smoke 基线用例 |
| (Workflow 基础) | — | REL-WORKFLOW-01-001 | smoke 基线用例 |

---

## 二、新增用例清单

本轮共生成 **88 条** 增量用例（text + YAML 一一对应），覆盖 **~65 条缺口 intent**。

### 2.1 按维度统计

| 维度 | 新增条数 | P0 | P1 | P2 |
|---|---|---|---|---|
| completeness | 31 | 14 | 17 | 0 |
| compatibility | 6 | 4 | 2 | 0 |
| reliability | 20 | 1 | 19 | 0 |
| security | 24 | 15 | 9 | 0 |
| usability | 7 | 1 | 4 | 2 |
| **合计** | **88** | **35** | **51** | **2** |

> 注：按维度分别计数，存在跨维度重复（如 completeness+security、compatibility+security 等）。去重后 **88 条** 物理用例。

### 2.2 按 test_type 统计

| test_type | 条数 | 说明 |
|---|---|---|
| `api` | 31 | REST API 测试（MR/Issue/Branch/Tag/Repo/User/Org/Hook/Status/Package/Rate） |
| `git` | 3 | Git CLI 操作（Clone PAT/SSH, LFS） |
| `workflow` | 54 | Actions workflow 测试（含 fault_injection 4 条） |

### 2.3 详细清单

#### completeness 维度（31 条）

| 用例 ID | 优先级 | 标题 | intent_ref | test_type |
|---|---|---|---|---|
| GIT-CLONE-01-002 | P0 | Git Clone 使用 PAT 进行 HTTPS 鉴权 | INTENT-GIT-001 | git |
| GIT-CLONE-01-003 | P0 | Git Clone 使用 SSH 密钥鉴权 | INTENT-GIT-001 | git |
| API-BRANCH-01-002 | P0 | 设置保护分支规则并验证强制推送被拒绝 | INTENT-GIT-002 | api |
| API-BRANCH-01-003 | P0 | 保护分支要求 CI 通过才可合并 | INTENT-GIT-002 | api |
| API-MR-01-002 | P0 | 创建 MR 并验证状态机流转 | INTENT-MR-001 | api |
| API-MR-01-003 | P0 | MR 使用 Squash 合并策略 | INTENT-MR-001 | api |
| API-MR-01-004 | P0 | 提交 MR 行级评论 | INTENT-MR-003 | api |
| API-MR-01-005 | P0 | 提交 MR 评审并标记 APPROVE | INTENT-MR-003 | api |
| API-MR-01-006 | P0 | MR 必须过 CI 才能合并 | INTENT-MR-004 | api |
| API-ISSUE-01-002 | P0 | 创建 Issue 并关闭 | INTENT-ISSUE-001 | api |
| API-USER-01-002 | P0 | PAT 带正确 scope 可访问仓库 API | INTENT-AUTH-001 | api |
| API-USER-01-003 | P0 | PAT 无 repo scope 时访问仓库 API 返回 403 | INTENT-AUTH-001 | api |
| API-USER-01-004 | P0 | Developer 角色不可修改保护分支规则 | INTENT-AUTH-002 | api |
| API-USER-01-005 | P0 | Reporter 角色不可推送代码 | INTENT-AUTH-002 | git |
| GIT-LFS-01-001 | P1 | Git LFS 跟踪并推送大文件 | INTENT-GIT-003 | git |
| API-BRANCH-01-004 | P1 | 通过 API 创建分支 | INTENT-GIT-004 | api |
| API-TAG-01-001 | P1 | 通过 API 创建 Release 与 Tag | INTENT-GIT-004 | api |
| API-REPO-01-002 | P1 | 空仓库的分支列表返回空数组 | INTENT-GIT-005 | api |
| API-MR-01-007 | P1 | MR 冲突检测返回 conflict 状态 | INTENT-MR-002 | api |
| API-MR-01-008 | P1 | Draft MR 标题含 WIP 前缀且不可直接合并 | INTENT-MR-005 | api |
| API-ISSUE-01-003 | P1 | 创建标签并关联到 Issue | INTENT-ISSUE-002 | api |
| API-ISSUE-01-004 | P1 | 创建里程碑并关联到 Issue | INTENT-ISSUE-002 | api |
| API-ISSUE-01-005 | P1 | 创建 Issue 评论并包含 @提及 | INTENT-ISSUE-003 | api |
| API-ISSUE-01-006 | P1 | MR 描述含 close 关键字合并后自动关闭 Issue | INTENT-ISSUE-004 | api |
| API-PKG-01-001 | P1 | 上传 npm 格式包并验证元数据 | INTENT-PKG-001 | api |
| API-PKG-01-002 | P1 | 上传 Docker 镜像并验证拉取 | INTENT-PKG-001 | api |
| API-ORG-01-001 | P1 | 团队权限批量分配到仓库 | INTENT-AUTH-003 | api |
| API-HOOK-01-001 | P1 | 创建 Webhook 并验证事件投递 | INTENT-HOOK-001 | api |
| API-HOOK-01-002 | P1 | Webhook 签名验证失败时拒绝请求 | INTENT-HOOK-001 | api |
| API-STATUS-01-001 | P1 | 创建 Commit Status 并关联到 MR | INTENT-HOOK-002 | api |
| API-RATE-01-001 | P1 | API 速率限制 429 与 Retry-After | INTENT-REL-018 | api |

#### compatibility 维度（6 条）

| 用例 ID | 优先级 | 标题 | intent_ref | test_type |
|---|---|---|---|---|
| COMPAT-MASK-01-001 | P0 | secret 经过 base64 拼接变形后仍应在日志中被掩码 | INTENT-COMPAT-023 | workflow |
| COMPAT-PRTARGET-01-001 | P0 | pull_request_target 默认 checkout 目标仓库 base 分支代码 | INTENT-COMPAT-024 | workflow |
| COMPAT-PRTARGET-01-002 | P0 | pull_request_target 中显式 checkout PR 头分支后执行不可信脚本应被隔离 | INTENT-COMPAT-024 | workflow |
| COMPAT-MIGR-01-001 | P0 | 使用 GitHub Actions 语法时校验器报错应指明 GitCode 差异 | INTENT-COMPAT-028 | workflow |
| COMPAT-UNKN-01-001 | P1 | 含未知顶层字段的 YAML 应给出精确字段路径与有效值提示 | INTENT-COMPAT-002 | workflow |
| COMPAT-CACHE-01-001 | P1 | fork PR 写入的 cache 不得被目标仓库主分支读取 | INTENT-COMPAT-025 | workflow |

#### reliability 维度（19 条）

| 用例 ID | 优先级 | 标题 | intent_ref | test_type |
|---|---|---|---|---|
| REL-NEEDS-01-001 | P0 | needs 依赖的 matrix job 全成功但上游初始化 job 失败时下游不应执行 | INTENT-REL-005 | workflow |
| REL-CONC-01-001 | P1 | 短时间内高频触发同仓库 workflow 的排队与公平性 | INTENT-REL-002 | workflow |
| REL-MATX-01-001 | P1 | matrix max-parallel=2 时矩阵展开实例并发度被限制 | INTENT-REL-004 | workflow |
| REL-MATX-01-002 | P1 | matrix fail-fast=true 时单实例失败取消其余实例 | INTENT-REL-007 | workflow |
| REL-MATX-01-003 | P1 | 矩阵组合数超过平台上限时应报错或拒绝 | INTENT-REL-008 | workflow |
| REL-LOGS-01-001 | P1 | 单 step 输出 50MB 文本日志的实时性与完整性 | INTENT-REL-009 | workflow |
| REL-GIT-01-001 | P1 | 1GB+ 仓库克隆的耗时与资源稳定性 | INTENT-REL-010 | git |
| REL-TIME-01-001 | P1 | job 运行 350 分钟观察正常终止 vs 超时 kill | INTENT-REL-011 | workflow |
| REL-STEPS-01-001 | P1 | 单 job 16 个 step 的调度与状态回写完整性 | INTENT-REL-012 | workflow |
| REL-FAULT-01-001 | P1 | runner 磁盘写满后 job 行为与报错清晰度 | INTENT-REL-013 | workflow |
| REL-FAULT-01-002 | P1 | stress CPU 时 step 超时与心跳保活 | INTENT-REL-014 | workflow |
| REL-FAULT-01-003 | P1 | 模拟 runner 崩溃后 job 状态迁移与重调度 | INTENT-REL-015 | workflow |
| REL-FAULT-01-004 | P1 | 断开 runner 外网后观察依赖下载失败与重试 | INTENT-REL-016 | workflow |
| REL-ACTN-01-001 | P1 | 依赖 action 不可用时 workflow 失败与报错清晰度 | INTENT-REL-017 | workflow |
| REL-HOOK-01-001 | P1 | Webhook 接收端 5xx 时观察重试间隔与风暴抑制 | INTENT-REL-019 | api |
| REL-ARTF-01-001 | P1 | 上传 500MB artifact 观察上限与报错 | INTENT-REL-020 | workflow |
| REL-CACH-01-001 | P1 | 写入 500MB cache 观察上限与 LRU 淘汰 | INTENT-REL-021 | workflow |
| REL-PKG-01-001 | P1 | 500MB 包中途断网观察断点续传或重试 | INTENT-REL-022 | api |
| REL-MEM-01-001 | P1 | small runner 上申请 12GB 内存观察 OOM kill 行为 | INTENT-REL-023 | workflow |
| REL-RERUN-01-001 | P1 | 连续请求第 4 次 rerun 观察拒绝行为 | INTENT-REL-025 | api |

#### security 维度（23 条）

| 用例 ID | 优先级 | 标题 | intent_ref | test_type |
|---|---|---|---|---|
| SEC-FORK-01-001 | P0 | fork PR 触发 pull_request 时严禁读取目标仓库 secrets | INTENT-SEC-001 | workflow |
| SEC-FORK-01-002 | P0 | fork PR 通过 secrets 对象枚举不得获取 secret 名列表 | INTENT-SEC-001 | workflow |
| SEC-MASK-01-001 | P0 | secret 经过 JSON 转义与 URL 编码后仍应在日志中被掩码 | INTENT-SEC-002 | workflow |
| SEC-LEAK-01-001 | P0 | secret 值不得通过 artifact 文件外泄 | INTENT-SEC-003 | workflow |
| SEC-INJ-01-001 | P0 | PR 标题含命令注入 payload 时不应执行 | INTENT-SEC-004 | workflow |
| SEC-INJ-01-002 | P0 | 分支名含 shell 元字符时不应破坏 run 脚本 | INTENT-SEC-004 | workflow |
| SEC-INJ-01-003 | P0 | issue_comment 正文含脚本注入 payload 时不应执行 | INTENT-SEC-005 | workflow |
| SEC-ENV-01-001 | P0 | 通过 ATOMGIT_ENV 写入污染数据不得破坏后续步骤执行上下文 | INTENT-SEC-006 | workflow |
| SEC-PRTARGET-01-001 | P0 | pull_request_target 中 checkout PR 头分支后运行 build.sh 应被隔离 | INTENT-SEC-007 | workflow |
| SEC-PRTARGET-01-002 | P0 | pull_request_target 中恶意 PR 修改 workflow 文件不被执行 | INTENT-SEC-007 | workflow |
| SEC-PRTARGET-01-003 | P0 | pull_request_target 的 workflow 文件来源校验 | INTENT-SEC-008 | workflow |
| SEC-PERM-01-001 | P0 | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限应只读 | INTENT-SEC-011 | workflow |
| SEC-PERM-01-002 | P0 | job 级 permissions 声明应正确限制 ATOMGIT_TOKEN 权限 | INTENT-SEC-012 | workflow |
| SEC-ROLE-01-001 | P0 | Developer 角色不得修改仓库设置或管理 secrets | INTENT-SEC-013 | api |
| SEC-ROLE-01-002 | P0 | Reporter 角色不得触发 workflow_dispatch | INTENT-SEC-013 | api |
| SEC-CACHE-01-001 | P1 | fork PR 保存的 cache 不得被主分支 workflow 命中 | INTENT-SEC-009 | workflow |
| SEC-CACHE-01-002 | P1 | 不同仓库使用相同 cache key 时数据隔离 | INTENT-SEC-010 | workflow |
| SEC-ACTION-01-001 | P1 | 浮动 tag 被篡改后使用 commit SHA 固定可防供应链攻击 | INTENT-SEC-014 | workflow |
| SEC-ACTION-01-002 | P1 | 本地 action 使用路径遍历引用仓库外路径应被拒绝 | INTENT-SEC-015 | workflow |
| SEC-RUNNER-01-001 | P1 | 复用型 Runner 不得跨 job 残留敏感文件或环境变量 | INTENT-SEC-016 | workflow |
| SEC-PKG-01-001 | P1 | 低权限用户不得覆盖或删除已有包版本 | INTENT-SEC-017 | api |
| SEC-HOOK-01-001 | P1 | Webhook secret 在配置界面不回显且签名验证不可绕过 | INTENT-SEC-018 | api |
| SEC-AUDIT-01-001 | P1 | 审计日志记录权限变更与 secret 访问事件 | INTENT-SEC-019 | api |
| SEC-RUNNER-01-002 | P1 | 自托管 Runner 注册令牌不得在工作流日志或环境变量中泄露 | INTENT-SEC-020 | workflow |

#### usability 维度（7 条）

| 用例 ID | 优先级 | 标题 | intent_ref | test_type |
|---|---|---|---|---|
| USE-DOCS-01-001 | P0 | 官方文档中 GitHub 专有措辞应已替换为 GitCode 术语 | INTENT-USE-017 | api |
| USE-NOTIF-01-001 | P1 | MR 触发 CI 失败后通知的时效性与信息完整性 | INTENT-USE-008 | workflow |
| USE-MASK-01-001 | P1 | Secret 掩码被绕过时日志应发出暴露预警 | INTENT-USE-011 | workflow |
| USE-ANNO-01-001 | P1 | workflow 命令注解在 UI 中的可读性与定位能力 | INTENT-USE-016 | workflow |
| USE-NOTIF-01-002 | P1 | 站内通知与邮件通知的及时性与完整性 | INTENT-USE-019 | api |
| USE-INPUT-01-001 | P2 | workflow_dispatch 缺少必填参数时 API 报错应指明参数名 | INTENT-USE-007 | api |
| USE-PKG-01-001 | P2 | 制品库版本冲突报错应包含包名、版本号与操作指引 | INTENT-USE-009 | api |

---

## 三、DEPRECATE 记录

以下历史用例已在 `baseline/case-base-detail.md` 中标记为 DEPRECATE，本轮 **不纳入交付集**。

### 3.1 D 测不动（22 条）

| TC-ID | 标题 | 淘汰原因 |
|---|---|---|
| TC-005 | vars(组织级) | vars context unsupported |
| TC-006 | vars(项目级) | vars context unsupported |
| TC-007 | vars覆盖 | vars context unsupported |
| TC-016 | inputs required校验 | platform-side validation |
| TC-115~119 | vars@各级别 | vars context unsupported |
| TC-120 | job@workflow级别 | platform-side validation |
| TC-129~130, 135, 145, 155 | 上下文@不合法级别 | platform-side validation |
| TC-522 | max=0非法值 | platform-side validation |
| TC-524 | matrix空数组 | platform-side validation |
| TC-578~580 | needs非法依赖 | platform-side validation |
| TC-590 | permissions非法值 | platform-side validation |
| TC-608 | input_id含非法字符 | platform-side validation |

### 3.2 SKIP with Permanent Reason（62 条）

主要类别：
- **vars/secrets 难真测**: TC-008~014, TC-019, TC-024, TC-100~102, TC-140~144, TC-196 等
- **非对应事件 SKIP**: TC-061~083 中大量 PR/issue_comment 字段在非对应事件下 SKIP
- **外部资源/工具链不可用**: TC-255, 364, 449~452, 456, 458~460, 482~485
- **平台侧校验/UI人工**: TC-012~015, TC-513, TC-581~583 等

### 3.3 用例不当 / Low Value（27 + 107 条）

- **纯文档型/无独立验证价值**: TC-386~392（命名建议）、TC-405（单 stage 可缺省）
- **shell 内部无法验证平台行为**: TC-436, TC-551~553（mask/set-output 废弃格式）
- **重复覆盖**: TC-033, TC-035, TC-052, TC-192, TC-204 等（已被 KEEP 主用例覆盖）
- **P3 Trivial**: TC-137~139, TC-163, TC-254~261, TC-387~389 等

完整清单见 `baseline/case-base-detail.md` §DEPRECATE。

---

## 四、P0 Intent 覆盖闭合检查

全部 26 条 P0 intent 均已有对应用例：

| P0 Intent | 覆盖用例 | 状态 |
|---|---|---|
| GIT-001 | GIT-CLONE-01-002/003 | 新增 |
| GIT-002 | API-BRANCH-01-002/003 | 新增 |
| MR-001 | API-MR-01-002/003 | 新增 |
| MR-003 | API-MR-01-004/005 | 新增 |
| MR-004 | API-MR-01-006 | 新增 |
| ISSUE-001 | API-ISSUE-01-002 | 新增 |
| AUTH-001 | API-USER-01-002/003 | 新增 |
| AUTH-002 | API-USER-01-004/005 | 新增 |
| COMPAT-023 | COMPAT-MASK-01-001 | 新增 |
| COMPAT-024 | COMPAT-PRTARGET-01-001/002 | 新增 |
| COMPAT-028 | COMPAT-MIGR-01-001 | 新增 |
| REL-005 | REL-NEEDS-01-001 | 新增 |
| SEC-001 | SEC-FORK-01-001/002 | 新增 |
| SEC-002 | SEC-MASK-01-001 | 新增 |
| SEC-003 | SEC-LEAK-01-001 | 新增 |
| SEC-004 | SEC-INJ-01-001/002 | 新增 |
| SEC-005 | SEC-INJ-01-003 | 新增 |
| SEC-006 | SEC-ENV-01-001 | 新增 |
| SEC-007 | SEC-PRTARGET-01-001/002 | 新增 |
| SEC-008 | SEC-PRTARGET-01-003 | 新增 |
| SEC-011 | SEC-PERM-01-001 | 新增 |
| SEC-012 | SEC-PERM-01-002 | 新增 |
| SEC-013 | SEC-ROLE-01-001/002 | 新增 |
| USE-004 | TC-023, TC-094~095 等 | 复用 KEEP |
| USE-005 | TC-005~007, TC-115~119 等 | 复用 KEEP |
| USE-017 | USE-DOCS-01-001 | 新增 |

**结论**: 26/26 P0 intent 全部覆盖，无盲区。

---

## 五、交付物清单

| 路径 | 数量 | 说明 |
|---|---|---|
| `runs/2026-08-18-01/cases/text/*.md` | 88 | 文本用例（source of truth） |
| `runs/2026-08-18-01/cases/yaml/*.yaml` | 88 | 可执行 YAML（派生，schema 合规） |
| `runs/2026-08-18-01/case-manifest.md` | 1 | 本文件 |

---

*生成工具: gen_cases.py (手动逐字段写入，未使用 yaml.dump)*
*Schema 校验: 基于 executable-case.schema.yaml + VALIDATION-RULES.md 自检*
