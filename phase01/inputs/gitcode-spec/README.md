# inputs/gitcode-spec/ （**必需**）— 已补充 ✅

GitCode 平台技术规格文档总入口。包含两部分：
1. **Actions 流水线文档**（官方镜像）
2. **产品功能技术规格**（从 `gitcode-docs/` 整理 + API 补充）

---

## 一、产品功能技术规格（新增）

> 整理日期：2026-08-18
> 来源：`gitcode-docs/`（用户手册风格）+ 补充 Agent 需要的 API 端点、请求参数、枚举值、配置示例。

| 文件 | 模块 | 覆盖范围 | 来源 |
|---|---|---|---|
| [repository-spec.md](repository-spec.md) | 代码托管 / Repository | 项目创建、分支管理、保护分支、成员权限、Tags & Releases、LFS | `gitcode-docs/项目/*` |
| [merge-request-spec.md](merge-request-spec.md) | 合并请求 / Merge Request | MR 创建、代码评审、草稿 MR、冲突解决、快进合并、合并策略 | `gitcode-docs/合并请求/*` |
| [issue-spec.md](issue-spec.md) | Issues | Issue 创建/关闭、标签、里程碑、评论、指派、筛选 | `gitcode-docs/Issue.md` |
| [user-org-spec.md](user-org-spec.md) | 用户与组织 / User & Organization | 用户认证、PAT 令牌、组织管理、成员角色、权限继承、SSH 密钥 | `gitcode-docs/用户/*` + `组织.md` |
| [discussion-notification-spec.md](discussion-notification-spec.md) | 讨论与通知 / Discussion & Notification | 评论系统、@提及、通知机制、Webhooks、签名验证 | 分散于各模块文档 |

### 使用方式

**Phase 01 — Agent 设计用例时：**
1. **spec-analyst agent**：阅读对应模块的 spec 文件，提取可验证的功能点
2. **case-writer agent**：依据 spec 中的「API 端点」和「枚举值」填写 YAML 用例
3. **review-gate agent**：对照 spec 检查用例覆盖度

**Phase 02 — 执行时：**
- 本目录**不直接参与**执行；执行依据是 `phase02/scripts/api_runner.py` 和 `phase02/scripts/git_runner.py`
- spec 中的「配置示例」可供调试时参考（curl 命令可直接复制粘贴测试）

### 与 gitcode-docs/ 的关系

| 维度 | `gitcode-docs/` | `gitcode-spec/` |
|---|---|---|
| 目标读者 | 终端用户 | AI Agent / 测试工程师 |
| 内容风格 | 操作指南、截图说明 | 技术规格、API 参数、枚举值 |
| 用途 | 产品使用手册 | 测试用例设计输入 |

> **结论**：`gitcode-docs/` 不能替代 `gitcode-spec/`，但可互补。docs 提供「功能有什么」，spec 补充「怎么测、调什么 API」。
> 
> **归档说明**：原始产品文档已归档至 [`../archive/gitcode-docs-20260818/`](../archive/gitcode-docs-20260818/)，如需回查用户手册级细节（截图、操作步骤、界面文案）可前往查阅。

### 待补充项（已知缺口）

- [ ] **Packages / 制品库** — npm、Maven、PyPI、Docker 等包管理协议
- [ ] **Actions / CI-CD** — 工作流语法、触发器、Runner、Artifact、Cache（已有官方镜像，见下文）
- [ ] **Pages / 静态站点托管**
- [ ] **Wiki / 项目文档**
- [ ] **Security / 安全扫描**

---

## 二、Actions 流水线文档（官方镜像）

GitCode Action（AtomGit Action）官方流水线文档的**离线镜像**，抓取自
https://docs.gitcode.com/docs/help/home/org_project/pipeline/ （2026-07-20，共 50 页）。

### 导航
- **[INDEX.md](INDEX.md)** — 全部 50 页索引 + 来源 URL + 勘误清单
- **[COMPAT-NOTES.md](COMPAT-NOTES.md)** — 抓取中发现的 GitCode↔GitHub 差异速记（喂 compat-diff agent）

### 结构（镜像官方目录）
```
00-overview.md / 01-quick-start.md
core-concepts/        (5)   核心概念
writing-pipelines/    (13)  编写流水线
running-pipelines/    (4)   运行流水线
runner-management/    (4)   Runner 管理
security-permissions/ (3)   安全与权限
syntax-reference/     (6)   语法与配置参考
examples/             (6)   示例教程
action-development/   (7)   Action 插件开发
```

### 消费方
spec-analyst · case-writer（编译 YAML 语法依据）· security（权限/隔离）· reliability（配额/runner）· usability（错误/文档）· compat-diff（对照 COMPAT-NOTES + github-reference）

### 持续勘误
- 每个文件头 `<!-- source | fetched -->` 记录来源与抓取日期。
- 文档更新后重抓对应页覆盖即可；两处已知待优化项见 INDEX.md 勘误清单。
- 抓取方式：WebFetch 逐页转 Markdown（要求保留中文原文与完整代码块/表格）。

**已补充 / 50 页 / 2026-07-20**
