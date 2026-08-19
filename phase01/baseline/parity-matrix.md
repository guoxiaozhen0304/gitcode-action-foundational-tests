# GitCode 平台能力清单（功能冒烟覆盖坐标系）

> L0 基线之一。左列能力项来自 spec-analyst 的能力清单；支持状态需人+agent 共同确认。
> 本文件是**纯功能清单**，仅作为「GitCode 自身功能是否被用例覆盖」的坐标系。
> **每个「部分/不支持/未知」项都应能反查到覆盖它的用例。**

## 支持状态图例
- ✅ 完全支持（已验证可用）
- 🟡 部分支持（有限制或子集）
- ❌ 不支持
- ❓ 未知（规格未明，需验证）

---

## 一、CI/CD — Actions

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| 工作流文件目录 `.gitcode/workflows/` | 语法 | 🟡 | 使用 `.gitcode/workflows/` 而非 `.github/workflows/` | workflow-file-location-structure.md | INTENT-COMP-001 |
| 未知/不支持字段处理 | 语法 | ❓ | 文档未明确降级方式 | 多处缺失 | INTENT-COMP-002 |
| `push` 触发 + branches/paths 过滤 | 触发器 | ✅ | 通配与取反支持，paths 上限 300 | trigger-events.md | INTENT-COMP-003 |
| `pull_request` vs `pull_request_target` 隔离 | 触发器/安全 | ✅ | fork PR 严格隔离 secret，需实测确认强度 | pr-mr-pipeline-security.md | INTENT-COMP-004 |
| `schedule` cron 最短间隔 | 触发器 | 🟡 | 最短 5 分钟，UTC，仅默认分支 | trigger-events.md | INTENT-COMP-005 |
| `workflow_call` 嵌套层数 | 执行模型 | 🟡 | 最多 2 层 | trigger-events.md | INTENT-COMP-006 |
| `stages` 阶段机制 | 执行模型 | ❌ | GitCode 特有，阶段间串行+阶段内并行 | core-concepts/workflow-job-step-action.md | INTENT-COMP-007 |
| `post` 后处理阶段 | 执行模型 | ❌ | GitCode 特有，默认 run_always: true | workflow-file-location-structure.md | INTENT-COMP-007 |
| `timeout-minutes` 默认 360 分钟 | 执行模型 | ✅ | 与 GitHub 一致 | configure-jobs.md | INTENT-COMP-008 |
| `rerun` 次数限制 | 执行模型 | 🟡 | 最多 3 次，超 6h 不可 rerun | rerun-failed-jobs.md | INTENT-COMP-009 |
| `runs-on` 标签体系 | Runner | 🟡 | 三段式 `{os,arch,flavor}` | using-hosted-runners.md | INTENT-COMP-010 |
| Runner 环境隔离 / 一次性 | Runner | ❓ | 文档未明确 Runner 是否复用 | 未明确 | INTENT-COMP-011 |
| `secrets` 日志脱敏 `***` | 安全 | 🟡 | 文档自承 `${{ secrets.X }}` 可能绕过 | using-secrets.md | INTENT-COMP-012 |
| `permissions` 默认权限 | 安全 | ❓ | 称"使用仓库设置"，默认值未明确 | token-permissions.md | INTENT-COMP-013 |
| `permissions` 权限域命名 | 安全 | ❌ | 用 `repository`/`pr`/`issue`/`hook` 等 | token-permissions.md | INTENT-COMP-022 |
| `pull_request_target` checkout 风险 | 安全 | ✅ | 高权限运行不可信代码风险，需实测 | pr-mr-pipeline-security.md | INTENT-COMP-014 |
| `upload-artifact` / `download-artifact` | Artifact | 🟡 | 保留期默认 90 天；大小上限未公开 | upload-download-artifacts.md | INTENT-COMP-015 |
| `cache` fork 场景隔离 | Artifact | ❓ | 文档未明确 cache 隔离策略 | using-dependency-cache.md | INTENT-COMP-016 |
| 运行状态机 + 日志完整性 | 可观测性 | ✅ | queued→in_progress→completed | view-run-results.md | INTENT-COMP-017 |
| `ATOMGIT_STEP_SUMMARY` Markdown | 可观测性 | 🟡 | 前缀差异，功能语义一致 | runtime-environment-variables.md | INTENT-COMP-018 |
| 上下文对象命名 `atomgit.*` | 兼容性 | ❌ | 用 `atomgit.*` 替代 `github.*` | syntax-reference/context.md | INTENT-COMP-019 |
| 状态函数无括号 `success`/`failed` | 兼容性 | ❌ | 无括号语法 | expressions.md | INTENT-COMP-020 |
| 表达式函数 `contains`/`hashFiles`/`toJson` | 兼容性 | ❓ | 边界行为待验证 | expressions.md | INTENT-COMP-021 |
| `workflow_dispatch.inputs` 类型 | 兼容性 | 🟡 | 仅支持 `string` | trigger-events.md | INTENT-COMP-023 |
| 迁移报错质量 | 易用性 | ❓ | 文档未系统说明报错差异指引 | COMPAT-NOTES.md | INTENT-COMP-024 |
| `concurrency.max` 1-5 + QUEUE/IGNORE | 稳定性 | 🟡 | 实现细节待实测 | workflow-file-location-structure.md | INTENT-COMP-025 |
| `strategy.matrix` 组合数上限 | 稳定性 | ❓ | 未公开上限 | configure-matrix-builds.md | INTENT-COMP-026 |

---

## 二、代码托管 — Git Repository

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| Git Clone（HTTPS/SSH） | 核心 | ✅ | 支持匿名/鉴权 clone，oauth2:token 格式有效 | — | INTENT-GIT-001 |
| Git Push（HTTPS/SSH） | 核心 | 🟡 | 需 token 鉴权，格式待确认 | — | INTENT-GIT-003 |
| 分支创建与删除 | 核心 | ✅ | 待验证 | — | INTENT-GIT-004 |
| 标签创建与删除 | 核心 | ✅ | 待验证 | — | INTENT-GIT-005 |
| 分支保护规则 | 治理 | ❓ | 推送前检查、强制 review、status check | — | INTENT-GIT-006 |
| 强制推送（force push）控制 | 治理 | ❓ | 可禁止 force push 到受保护分支 | — | INTENT-GIT-007 |
| 代码审查（Code Review） | 治理 | ❓ | 行级评论、建议修改、批量解决 | — | INTENT-GIT-008 |
| 大文件存储（LFS） | 扩展 | ❓ | Git LFS 协议支持 | — | INTENT-GIT-009 |
| 仓库镜像/同步 | 扩展 | ❓ | 自动同步到外部仓库 | — | INTENT-GIT-010 |
| 子模块（Submodule）支持 | 扩展 | ❓ | `.gitmodules` 解析与克隆 | — | INTENT-GIT-011 |

---

## 三、Merge Request / Pull Request

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| MR 创建与关闭 | 核心 | ✅ | 基于分支创建 MR，支持标题/描述/草稿 | — | INTENT-MR-001 |
| MR 列表与筛选 | 核心 | ✅ | 按状态（open/closed/merged）筛选 | — | INTENT-MR-002 |
| MR 详情查看 | 核心 | ✅ | 查看 diff、commit 列表、冲突状态 | — | INTENT-MR-003 |
| 合并策略（Merge/Squash/Rebase） | 核心 | ✅ | 支持多种合并方式 | — | INTENT-MR-004 |
| 代码审查与行级评论 | 协作 | ❓ | Reviewer 指派、Approve/Request changes | — | INTENT-MR-005 |
| CI 门禁（MR 必须过 CI） | 质量 | ❓ | 可配置 status check 通过才能合并 | — | INTENT-MR-006 |
| 冲突检测与解决提示 | 质量 | ❓ | 自动检测分支冲突 | — | INTENT-MR-007 |
| MR 模板（Description Template） | 协作 | ❓ | 预置 MR 描述模板 | — | INTENT-MR-008 |
| Draft/WIP MR | 协作 | ❓ | 草稿 MR 禁止直接合并 | — | INTENT-MR-009 |

---

## 四、Issues

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| Issue 创建与关闭 | 核心 | ✅ | 标题/描述/标签/指派/里程碑 | — | INTENT-ISSUE-001 |
| Issue 列表与筛选 | 核心 | ✅ | 按状态/标签/指派人筛选 | — | INTENT-ISSUE-002 |
| Issue 评论 | 协作 | ✅ | 支持 Markdown 评论与引用 | — | INTENT-ISSUE-003 |
| 标签（Label）管理 | 治理 | ✅ | 自定义颜色/名称/描述 | — | INTENT-ISSUE-004 |
| 里程碑（Milestone）管理 | 治理 | ✅ | 按截止日期聚合 Issue/PR | — | INTENT-ISSUE-005 |
| Issue 模板 | 协作 | ✅ | 预置 Issue 描述模板 | — | INTENT-ISSUE-006 |
| Issue 关联 MR/Commit | 追溯 | ✅ | 通过关键字（close/fix）自动关联 | — | INTENT-ISSUE-007 |
| 看板（Board/Kanban） | 协作 | ✅ | 拖拽式状态流转 | — | INTENT-ISSUE-008 |

---

## 五、Packages（制品库）

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| npm 包上传与下载 | 核心 | ❓ | `npm publish`/`npm install` | — | INTENT-PKG-001 |
| Maven 包上传与下载 | 核心 | ❓ | `mvn deploy`/`mvn dependency` | — | INTENT-PKG-002 |
| PyPI 包上传与下载 | 核心 | ❓ | `twine upload`/`pip install` | — | INTENT-PKG-003 |
| Docker 镜像上传与下载 | 核心 | ❓ | `docker push`/`docker pull` | — | INTENT-PKG-004 |
| NuGet/Gradle/Go 模块支持 | 扩展 | ❓ | 其他包管理器协议 | — | INTENT-PKG-005 |
| 包版本管理与淘汰 | 治理 | ❓ | 删除旧版本、保留策略 | — | INTENT-PKG-006 |
| 包访问权限控制 | 安全 | ❓ | 公开/私有/组织内可见 | — | INTENT-PKG-007 |
| 包与仓库关联 | 追溯 | ❓ | 包页面显示来源仓库/CI 构建 | — | INTENT-PKG-008 |

---

## 六、用户与权限

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| 用户认证（OAuth2/Token） | 核心 | ✅ | Personal Access Token + OAuth App，实测有效 | — | INTENT-AUTH-001 |
| 仓库成员角色（Owner/Maintainer/Developer） | 核心 | ❓ | 细粒度角色控制 | — | INTENT-AUTH-002 |
| 组织（Organization）管理 | 治理 | ❓ | 组织级仓库/成员/权限 | — | INTENT-AUTH-003 |
| 团队（Team）与权限继承 | 治理 | ❓ | 团队级权限，仓库继承 | — | INTENT-AUTH-004 |
| 外部协作者（Collaborator） | 治理 | ❓ | 非组织成员访问仓库 | — | INTENT-AUTH-005 |
| SSO / LDAP 集成 | 企业 | ❓ | 企业级统一身份认证 | — | INTENT-AUTH-006 |
| 审计日志（Audit Log） | 安全 | ❓ | 关键操作记录与查询 | — | INTENT-AUTH-007 |
| 两步验证（2FA） | 安全 | ❓ | TOTP/SMS 二次验证 | — | INTENT-AUTH-008 |

---

## 七、Webhooks & 集成

| 能力项 | 分类 | GitCode 支持状态 | 备注 | 出处 | 关联意图 |
|---|---|---|---|---|---|
| 仓库 Webhook（Push/MR/Issue） | 核心 | ❓ | HTTP POST 回调，支持签名验证 | — | INTENT-HOOK-001 |
| Webhook 投递可靠性 | 稳定性 | ❓ | 失败重试、超时控制、IP 白名单 | — | INTENT-HOOK-002 |
| CI 状态回写（Commit Status） | 集成 | ❓ | Actions 结果回写到 MR/Commit | — | INTENT-HOOK-003 |

---

> **填写建议**：阿蓁确认每项后，把 ❓ 改为 ✅/🟡/❌，补充「备注」。每确认一项，回写「关联意图」ID（Agent 产用例时填充）。
