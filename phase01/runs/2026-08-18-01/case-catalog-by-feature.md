# 用例功能项分类索引 — Run 2026-08-18-01

> 将本轮交付的 **92 条新增用例** 按「产品功能模块」重新聚类，便于审视各功能域的覆盖密度与维度分布。
> 生成日期: 2026-08-19

---

## 分类总览

| 功能项 | 用例数 | 占比 | 覆盖维度 | test_type 分布 |
|---|---|---|---|---|
| 1. Workflow / Actions (CI/CD) | 46 | 50.0% | compat / rel / sec / use | workflow 为主，少量 api |
| 2. Git Repository (代码托管) | 9 | 9.8% | completeness / rel | git + api |
| 3. Merge Request (PR) | 7 | 7.6% | completeness | api |
| 4. Issues & Board (Kanban) | 9 | 9.8% | completeness | api |
| 5. Packages (制品库) | 5 | 5.4% | completeness / rel / sec / use | api |
| 6. User & Organization / Auth | 8 | 8.7% | completeness / sec | api + git |
| 7. Webhooks & Notifications | 6 | 6.5% | completeness / rel / sec / use | api |
| 8. System / Cross-cutting | 2 | 2.2% | completeness / use | api |
| **合计** | **92** | **100%** | **5 个维度全覆盖** | **workflow / api / git** |

---

## 1. Workflow / Actions (CI/CD) — 46 条

> 覆盖 Actions 引擎的兼容性、稳定性、安全性与易用性。对应 Parity Matrix 模块「CI/CD — Actions」。

### 1.1 兼容性 (compat)
| 用例 ID | 优先级 | 标题 | test_type |
|---|---|---|---|
| COMPAT-MASK-01-001 | P0 | secret 经过 base64 拼接变形后仍应在日志中被掩码 | workflow |
| COMPAT-PRTARGET-01-001 | P0 | pull_request_target 默认 checkout 目标仓库 base 分支代码 | workflow |
| COMPAT-PRTARGET-01-002 | P0 | pull_request_target 中显式 checkout PR 头分支后执行不可信脚本应被隔离 | workflow |
| COMPAT-MIGR-01-001 | P0 | 使用 GitHub Actions 语法时校验器报错应指明 GitCode 差异 | workflow |
| COMPAT-UNKN-01-001 | P1 | 含未知顶层字段的 YAML 应给出精确字段路径与有效值提示 | workflow |
| COMPAT-CACHE-01-001 | P1 | fork PR 写入的 cache 不得被目标仓库主分支读取 | workflow |

### 1.2 稳定性 (reliability)
| 用例 ID | 优先级 | 标题 | test_type |
|---|---|---|---|
| REL-NEEDS-01-001 | P0 | needs 依赖的 matrix job 全成功但上游初始化 job 失败时下游不应执行 | workflow |
| REL-CONC-01-001 | P1 | 短时间内高频触发同仓库 workflow 的排队与公平性 | workflow |
| REL-MATX-01-001 | P1 | matrix max-parallel=2 时矩阵展开实例并发度被限制 | workflow |
| REL-MATX-01-002 | P1 | matrix fail-fast=true 时单实例失败取消其余实例 | workflow |
| REL-MATX-01-003 | P1 | 矩阵组合数超过平台上限时应报错或拒绝 | workflow |
| REL-LOGS-01-001 | P1 | 单 step 输出 50MB 文本日志的实时性与完整性 | workflow |
| REL-TIME-01-001 | P1 | job 运行 350 分钟观察正常终止 vs 超时 kill | workflow |
| REL-STEPS-01-001 | P1 | 单 job 16 个 step 的调度与状态回写完整性 | workflow |
| REL-FAULT-01-001 | P1 | runner 磁盘写满后 job 行为与报错清晰度 | workflow |
| REL-FAULT-01-002 | P1 | stress CPU 时 step 超时与心跳保活 | workflow |
| REL-FAULT-01-003 | P1 | 模拟 runner 崩溃后 job 状态迁移与重调度 | workflow |
| REL-FAULT-01-004 | P1 | 断开 runner 外网后观察依赖下载失败与重试 | workflow |
| REL-ACTN-01-001 | P1 | 依赖 action 不可用时 workflow 失败与报错清晰度 | workflow |
| REL-ARTF-01-001 | P1 | 上传 500MB artifact 观察上限与报错 | workflow |
| REL-CACH-01-001 | P1 | 写入 500MB cache 观察上限与 LRU 淘汰 | workflow |
| REL-MEM-01-001 | P1 | small runner 上申请 12GB 内存观察 OOM kill 行为 | workflow |
| REL-RERUN-01-001 | P1 | 连续请求第 4 次 rerun 观察拒绝行为 | api |

### 1.3 安全性 (security)
| 用例 ID | 优先级 | 标题 | test_type |
|---|---|---|---|
| SEC-FORK-01-001 | P0 | fork PR 触发 pull_request 时严禁读取目标仓库 secrets | workflow |
| SEC-FORK-01-002 | P0 | fork PR 通过 secrets 对象枚举不得获取 secret 名列表 | workflow |
| SEC-MASK-01-001 | P0 | secret 经过 JSON 转义与 URL 编码后仍应在日志中被掩码 | workflow |
| SEC-LEAK-01-001 | P0 | secret 值不得通过 artifact 文件外泄 | workflow |
| SEC-INJ-01-001 | P0 | PR 标题含命令注入 payload 时不应执行 | workflow |
| SEC-INJ-01-002 | P0 | 分支名含 shell 元字符时不应破坏 run 脚本 | workflow |
| SEC-INJ-01-003 | P0 | issue_comment 正文含脚本注入 payload 时不应执行 | workflow |
| SEC-ENV-01-001 | P0 | 通过 ATOMGIT_ENV 写入污染数据不得破坏后续步骤执行上下文 | workflow |
| SEC-PRTARGET-01-001 | P0 | pull_request_target 中 checkout PR 头分支后运行 build.sh 应被隔离 | workflow |
| SEC-PRTARGET-01-002 | P0 | pull_request_target 中恶意 PR 修改 workflow 文件不被执行 | workflow |
| SEC-PRTARGET-01-003 | P0 | pull_request_target 的 workflow 文件来源校验 | workflow |
| SEC-PERM-01-001 | P0 | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限应只读 | workflow |
| SEC-PERM-01-002 | P0 | job 级 permissions 声明应正确限制 ATOMGIT_TOKEN 权限 | workflow |
| SEC-CACHE-01-001 | P1 | fork PR 保存的 cache 不得被主分支 workflow 命中 | workflow |
| SEC-CACHE-01-002 | P1 | 不同仓库使用相同 cache key 时数据隔离 | workflow |
| SEC-ACTION-01-001 | P1 | 浮动 tag 被篡改后使用 commit SHA 固定可防供应链攻击 | workflow |
| SEC-ACTION-01-002 | P1 | 本地 action 使用路径遍历引用仓库外路径应被拒绝 | workflow |
| SEC-RUNNER-01-001 | P1 | 复用型 Runner 不得跨 job 残留敏感文件或环境变量 | workflow |
| SEC-RUNNER-01-002 | P1 | 自托管 Runner 注册令牌不得在工作流日志或环境变量中泄露 | workflow |

### 1.4 易用性 (usability)
| 用例 ID | 优先级 | 标题 | test_type |
|---|---|---|---|
| USE-NOTIF-01-001 | P1 | MR 触发 CI 失败后通知的时效性与信息完整性 | workflow |
| USE-MASK-01-001 | P1 | Secret 掩码被绕过时日志应发出暴露预警 | workflow |
| USE-ANNO-01-001 | P1 | workflow 命令注解在 UI 中的可读性与定位能力 | workflow |
| USE-INPUT-01-001 | P2 | workflow_dispatch 缺少必填参数时 API 报错应指明参数名 | api |

---

## 2. Git Repository (代码托管) — 9 条

> 覆盖 Git 克隆、LFS、分支、Tag、Release、空仓库等基础代码托管能力。对应 Parity Matrix 模块「代码托管 — Git Repository」。

| 用例 ID | 优先级 | 标题 | test_type | 维度 |
|---|---|---|---|---|
| GIT-CLONE-01-002 | P0 | Git Clone 使用 PAT 进行 HTTPS 鉴权 | git | completeness |
| GIT-CLONE-01-003 | P0 | Git Clone 使用 SSH 密钥鉴权 | git | completeness |
| GIT-LFS-01-001 | P1 | Git LFS 跟踪并推送大文件 | git | completeness |
| API-BRANCH-01-002 | P0 | 设置保护分支规则并验证强制推送被拒绝 | api | completeness |
| API-BRANCH-01-003 | P0 | 保护分支要求 CI 通过才可合并 | api | completeness |
| API-BRANCH-01-004 | P1 | 通过 API 创建分支 | api | completeness |
| API-TAG-01-001 | P1 | 通过 API 创建 Release 与 Tag | api | completeness |
| API-REPO-01-002 | P1 | 空仓库的分支列表返回空数组 | api | completeness |
| REL-GIT-01-001 | P1 | 1GB+ 仓库克隆的耗时与资源稳定性 | git | reliability |

---

## 3. Merge Request (PR / 合并请求) — 7 条

> 覆盖 MR 创建、状态机、合并策略、评审、草稿、冲突检测。对应 Parity Matrix 模块「Merge Request」。

| 用例 ID | 优先级 | 标题 | test_type | 维度 |
|---|---|---|---|---|
| API-MR-01-002 | P0 | 创建 MR 并验证状态机流转 | api | completeness |
| API-MR-01-003 | P0 | MR 使用 Squash 合并策略 | api | completeness |
| API-MR-01-004 | P0 | 提交 MR 行级评论 | api | completeness |
| API-MR-01-005 | P0 | 提交 MR 评审并标记 APPROVE | api | completeness |
| API-MR-01-006 | P0 | MR 必须过 CI 才能合并 | api | completeness |
| API-MR-01-007 | P1 | MR 冲突检测返回 conflict 状态 | api | completeness |
| API-MR-01-008 | P1 | Draft MR 标题含 WIP 前缀且不可直接合并 | api | completeness |

---

## 4. Issues & Board (Kanban / 看板) — 9 条

> 覆盖 Issue 创建/关闭、标签、里程碑、评论、@提及、自动关闭、Issue 模板、看板。对应 Parity Matrix 模块「Issues」。

| 用例 ID | 优先级 | 标题 | test_type | 维度 |
|---|---|---|---|---|
| API-ISSUE-01-002 | P0 | 创建 Issue 并关闭 | api | completeness |
| API-ISSUE-01-003 | P1 | 创建标签并关联到 Issue | api | completeness |
| API-ISSUE-01-004 | P1 | 创建里程碑并关联到 Issue | api | completeness |
| API-ISSUE-01-005 | P1 | 创建 Issue 评论并包含 @提及 | api | completeness |
| API-ISSUE-01-006 | P1 | MR 描述含 close 关键字合并后自动关闭 Issue | api | completeness |
| API-ISSUE-01-007 | P2 | 探测仓库 Issue 模板目录存在性 | api | completeness |
| API-ISSUE-01-008 | P2 | 探测 Issue 创建 API 是否支持模板参数 | api | completeness |
| API-BOARD-01-001 | P2 | 探测仓库 Projects/看板 API 可用性 | api | completeness |
| API-BOARD-01-002 | P2 | 探测 Issues 列表 API 是否返回项目/看板字段 | api | completeness |

---

## 5. Packages (制品库) — 5 条

> 覆盖 npm/Docker 包上传、元数据验证、大文件断点续传、权限防覆盖、版本冲突报错。对应 Parity Matrix 模块「Packages」。

| 用例 ID | 优先级 | 标题 | test_type | 维度 |
|---|---|---|---|---|
| API-PKG-01-001 | P1 | 上传 npm 格式包并验证元数据 | api | completeness |
| API-PKG-01-002 | P1 | 上传 Docker 镜像并验证拉取 | api | completeness |
| REL-PKG-01-001 | P1 | 500MB 包中途断网观察断点续传或重试 | api | reliability |
| SEC-PKG-01-001 | P1 | 低权限用户不得覆盖或删除已有包版本 | api | security |
| USE-PKG-01-001 | P2 | 制品库版本冲突报错应包含包名、版本号与操作指引 | api | usability |

---

## 6. User & Organization / Auth (用户与权限) — 8 条

> 覆盖 PAT scope、角色权限（Developer/Reporter）、团队批量授权、审计日志。对应 Parity Matrix 模块「用户与权限」。

| 用例 ID | 优先级 | 标题 | test_type | 维度 |
|---|---|---|---|---|
| API-USER-01-002 | P0 | PAT 带正确 scope 可访问仓库 API | api | completeness |
| API-USER-01-003 | P0 | PAT 无 repo scope 时访问仓库 API 返回 403 | api | completeness |
| API-USER-01-004 | P0 | Developer 角色不可修改保护分支规则 | api | completeness |
| API-USER-01-005 | P0 | Reporter 角色不可推送代码 | git | completeness |
| API-ORG-01-001 | P1 | 团队权限批量分配到仓库 | api | completeness |
| SEC-ROLE-01-001 | P0 | Developer 角色不得修改仓库设置或管理 secrets | api | security |
| SEC-ROLE-01-002 | P0 | Reporter 角色不得触发 workflow_dispatch | api | security |
| SEC-AUDIT-01-001 | P1 | 审计日志记录权限变更与 secret 访问事件 | api | security |

---

## 7. Webhooks & Notifications (Webhooks 与通知) — 6 条

> 覆盖 Webhook 创建/签名/重试、Commit Status 回写、站内/邮件通知。对应 Parity Matrix 模块「Webhooks & 集成」。

| 用例 ID | 优先级 | 标题 | test_type | 维度 |
|---|---|---|---|---|
| API-HOOK-01-001 | P1 | 创建 Webhook 并验证事件投递 | api | completeness |
| API-HOOK-01-002 | P1 | Webhook 签名验证失败时拒绝请求 | api | completeness |
| API-STATUS-01-001 | P1 | 创建 Commit Status 并关联到 MR | api | completeness |
| REL-HOOK-01-001 | P1 | Webhook 接收端 5xx 时观察重试间隔与风暴抑制 | api | reliability |
| SEC-HOOK-01-001 | P1 | Webhook secret 在配置界面不回显且签名验证不可绕过 | api | security |
| USE-NOTIF-01-002 | P1 | 站内通知与邮件通知的及时性与完整性 | api | usability |

---

## 8. System / Cross-cutting (系统级 / 跨功能) — 2 条

> 不归属于单一产品模块，属于平台级基础设施或跨功能体验。

| 用例 ID | 优先级 | 标题 | test_type | 维度 | 说明 |
|---|---|---|---|---|---|
| API-RATE-01-001 | P1 | API 速率限制 429 与 Retry-After | api | completeness | 全局 API 网关能力 |
| USE-DOCS-01-001 | P0 | 官方文档中 GitHub 专有措辞应已替换为 GitCode 术语 | api | usability | 跨模块文档一致性 |

---

## 附录：P0 用例在功能项中的分布

| 功能项 | P0 用例数 | 具体用例 |
|---|---|---|
| Workflow / Actions | 19 | COMPAT-MASK/PRTARGET×2/MIGR, SEC-FORK×2/MASK/LEAK/INJ×3/ENV/PRTARGET×3/PERM×2, REL-NEEDS |
| Git Repository | 4 | GIT-CLONE-01-002/003, API-BRANCH-01-002/003 |
| Merge Request | 5 | API-MR-01-002~006 |
| Issues & Board | 1 | API-ISSUE-01-002 |
| Packages | 0 | — |
| User & Auth | 5 | API-USER-01-002~005, SEC-ROLE-01-001 |
| Webhooks & Notifications | 0 | — |
| System / Cross-cutting | 1 | USE-DOCS-01-001 |
| **合计** | **35** | — |

> 全部 26 条 P0 intent 展开为 35 条 P0 用例，无一遗漏。

---

## 附录：功能项 × test_type 双轴矩阵

| 功能项 | workflow | api | git | 小计 |
|---|---|---|---|---|
| Workflow / Actions | 45 | 1 | 0 | 46 |
| Git Repository | 0 | 5 | 4 | 9 |
| Merge Request | 0 | 7 | 0 | 7 |
| Issues & Board | 0 | 9 | 0 | 9 |
| Packages | 0 | 5 | 0 | 5 |
| User & Auth | 0 | 7 | 1 | 8 |
| Webhooks & Notifications | 0 | 6 | 0 | 6 |
| System / Cross-cutting | 0 | 2 | 0 | 2 |
| **合计** | **45** | **42** | **5** | **92** |

> 与 `coverage.md` §三 的维度分布一致（workflow 45 = 40 原 + 5 被重新归类到 Workflow 的 api 用例如 REL-RERUN/USE-INPUT；此处按功能项重新切分后更直观）。

---

*索引生成: 基于 `case-manifest.md` 详细清单，按 Parity Matrix 7 大模块 + 系统级切分。*
