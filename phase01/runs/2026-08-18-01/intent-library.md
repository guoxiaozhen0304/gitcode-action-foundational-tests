# Intent Library — Run 2026-08-18-01

> Orchestrator 汇总产出  
> 原始输入: spec.md (35) + compat.md (29) + security.md (20) + reliability.md (25) + usability.md (18) = 127 条  
> 去重后准入: 113 条 | 被合并/淘汰: 14 条（含 13 条未准入记录 + 5 条合并/拆分后无独立记录）  
> 优先级来源: `baseline/risk-register.md`（不自造）  

---

## 一、completeness 维度（20 条准入 + 3 条未准入）

### INTENT-GIT-001
- **状态**: 准入
- **维度标签**: `[completeness, security]`
- **优先级**: P0
- **标题**: Git Clone（HTTPS/SSH）与 PAT 鉴权
- **覆盖的风险项**: RISK-COMP-01, RISK-SEC-05, RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — Git Clone（HTTPS/SSH）✅
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-GIT-002
- **状态**: 准入
- **维度标签**: `[completeness, security]`
- **优先级**: P0
- **标题**: 保护分支规则强制生效
- **覆盖的风险项**: RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — 分支保护规则 ❓, 强制推送控制 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-MR-001
- **状态**: 准入
- **维度标签**: `[completeness]`
- **优先级**: P0
- **标题**: MR 创建、状态机与合并策略
- **覆盖的风险项**: RISK-COMP-01
- **覆盖的能力项**: Parity Matrix — MR 创建与关闭 ✅, 合并策略 ❓, Draft/WIP MR ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-MR-003
- **状态**: 准入
- **维度标签**: `[completeness, security]`
- **优先级**: P0
- **标题**: MR 代码评审与行级评论
- **覆盖的风险项**: RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — 代码审查与行级评论 ❓, CI 门禁 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-MR-004
- **状态**: 准入
- **维度标签**: `[completeness, reliability]`
- **优先级**: P0
- **标题**: CI 门禁（MR 必须过 CI）
- **覆盖的风险项**: RISK-REL-02
- **覆盖的能力项**: Parity Matrix — CI 门禁 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-ISSUE-001
- **状态**: 准入
- **维度标签**: `[completeness]`
- **优先级**: P0
- **标题**: Issue CRUD 与状态流转
- **覆盖的风险项**: RISK-COMP-01
- **覆盖的能力项**: Parity Matrix — Issue 创建与关闭 ✅
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-AUTH-001
- **状态**: 准入
- **维度标签**: `[completeness, security]`
- **优先级**: P0
- **标题**: PAT 认证与权限范围（Scopes）生效
- **覆盖的风险项**: RISK-SEC-05, RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — 用户认证（OAuth2/Token）✅
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-AUTH-002
- **状态**: 准入
- **维度标签**: `[completeness]`
- **优先级**: P0
- **标题**: 仓库成员角色（Owner/Maintainer/Developer/Reporter）权限边界
- **覆盖的风险项**: RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — 仓库成员角色 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-GIT-003
- **状态**: 准入
- **维度标签**: `[completeness, reliability]`
- **优先级**: P1
- **标题**: 大文件存储（LFS）协议支持
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — 大文件存储（LFS）❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-GIT-004
- **状态**: 准入
- **维度标签**: `[completeness, compatibility]`
- **优先级**: P1
- **标题**: 分支/标签创建与删除
- **覆盖的风险项**: RISK-COMP-01
- **覆盖的能力项**: Parity Matrix — 分支创建与删除 ❓, 标签创建与删除 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-GIT-005
- **状态**: 准入
- **维度标签**: `[completeness]`
- **优先级**: P1
- **标题**: 空仓库/空数据场景 API 行为
- **覆盖的风险项**: RISK-COMP-03
- **覆盖的能力项**: Parity Matrix — 空数据边界
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-MR-002
- **状态**: 准入
- **维度标签**: `[completeness, usability]`
- **优先级**: P1
- **标题**: 冲突检测与可合并状态
- **覆盖的风险项**: RISK-USE-03
- **覆盖的能力项**: Parity Matrix — 冲突检测与解决提示 ❓, MR 详情查看 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-MR-005
- **状态**: 准入
- **维度标签**: `[usability, compatibility]`
- **优先级**: P1
- **标题**: MR 模板（Description Template）与 Draft 状态
- **覆盖的风险项**: RISK-USE-01, RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — MR 模板 ❓, Draft/WIP MR ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-ISSUE-002
- **状态**: 准入
- **维度标签**: `[completeness, compatibility]`
- **优先级**: P1
- **标题**: 标签与里程碑管理
- **覆盖的风险项**: RISK-COMP-02
- **覆盖的能力项**: Parity Matrix — 标签管理 ❓, 里程碑管理 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-ISSUE-003
- **状态**: 准入
- **维度标签**: `[completeness, usability]`
- **优先级**: P1
- **标题**: Issue 评论与 @提及通知
- **覆盖的风险项**: RISK-USE-04
- **覆盖的能力项**: Parity Matrix — Issue 评论 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-ISSUE-004
- **状态**: 准入
- **维度标签**: `[completeness]`
- **优先级**: P1
- **标题**: Issue 关联 MR/Commit（关键字自动关闭）
- **覆盖的风险项**: RISK-COMP-01
- **覆盖的能力项**: Parity Matrix — Issue 关联 MR/Commit ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-PKG-001
- **状态**: 准入
- **维度标签**: `[completeness, compatibility]`
- **优先级**: P1
- **标题**: 包格式协议支持（npm/Maven/PyPI/Docker）
- **覆盖的风险项**: RISK-COMP-05, RISK-COMPAT-04
- **覆盖的能力项**: Parity Matrix — Packages 全部 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-AUTH-003
- **状态**: 准入
- **维度标签**: `[completeness, compatibility]`
- **优先级**: P1
- **标题**: 团队（Team）权限批量分配与仓库继承
- **覆盖的风险项**: RISK-COMP-01
- **覆盖的能力项**: Parity Matrix — 团队与权限继承 ❓, 组织管理 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-HOOK-001
- **状态**: 准入
- **维度标签**: `[completeness, security]`
- **优先级**: P1
- **标题**: Webhook 创建、事件投递与签名验证
- **覆盖的风险项**: RISK-SEC-08
- **覆盖的能力项**: Parity Matrix — 仓库 Webhook ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-HOOK-002
- **状态**: 准入
- **维度标签**: `[completeness]`
- **优先级**: P1
- **标题**: CI 状态回写（Commit Status / MR 状态关联）
- **覆盖的风险项**: RISK-COMP-01
- **覆盖的能力项**: Parity Matrix — CI 状态回写 ❓
- **去重关系**: 无
- **来源 Agent**: spec-analyst

### INTENT-COMP-001（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[completeness, compatibility]`
- **优先级**: P1
- **标题**: 工作流文件目录 `.gitcode/workflows/`
- **覆盖的风险项**: RISK-USE-01, RISK-COMPAT-01
- **去重关系**: **被 COMPAT-001 覆盖**（compat-diff 拆分更细）
- **来源 Agent**: spec-analyst
- **未准入原因**: 与 compat.md INTENT-COMPAT-001 同义，compat-diff 版本描述更完整

### INTENT-COMP-002（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[completeness]`
- **优先级**: P1
- **标题**: 未知/不支持字段的处理方式
- **覆盖的风险项**: RISK-COMP-02
- **去重关系**: **被 COMPAT-002 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: compat.md INTENT-COMPAT-002 对降级方式差异描述更完整

### INTENT-COMP-003（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[completeness, compatibility]`
- **优先级**: P1
- **标题**: `workflow_dispatch`/`workflow_call` 的 `inputs` 类型限制
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-01
- **去重关系**: **被 COMPAT-013 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: compat.md INTENT-COMPAT-013 对 GitHub/GitCode 差异对比更完整

---

## 二、compatibility 维度（29 条准入 + 1 条未准入）

### INTENT-COMPAT-023
- **状态**: 准入
- **维度标签**: `[compatibility, security]`
- **优先级**: P0
- **标题**: `secrets` 日志脱敏（masking）强度与绕过检测
- **覆盖的风险项**: RISK-SEC-05
- **覆盖的能力项**: Parity Matrix — `secrets` 日志脱敏 🟡
- **去重关系**: 关联 INTENT-SEC-002（安全维度专项脱敏绕过）
- **来源 Agent**: compat-diff

### INTENT-COMPAT-024
- **状态**: 准入
- **维度标签**: `[compatibility, security]`
- **优先级**: P0
- **标题**: `pull_request_target` 事件下 `checkout` action 的默认代码来源与隔离强度
- **覆盖的风险项**: RISK-SEC-01, RISK-SEC-03
- **覆盖的能力项**: Parity Matrix — `pull_request_target` checkout 风险 ✅
- **去重关系**: 关联 INTENT-SEC-007, INTENT-SEC-008
- **来源 Agent**: compat-diff

### INTENT-COMPAT-028
- **状态**: 准入
- **维度标签**: `[compatibility, usability]`
- **优先级**: P0
- **标题**: 迁移报错质量——报错能否指明「这是 GitCode 不支持/需改写」
- **覆盖的风险项**: RISK-USE-01, RISK-USE-02
- **覆盖的能力项**: Parity Matrix — 迁移报错质量 ❓
- **去重关系**: 关联 USE-001~USE-003, USE-006, USE-010, USE-012, USE-013, USE-014, USE-015, USE-018
- **来源 Agent**: compat-diff

### INTENT-COMPAT-001
- **状态**: 准入
- **维度标签**: `[compatibility, usability]`
- **优先级**: P1
- **标题**: workflow 文件存放目录差异（`.github/workflows/` → `.gitcode/workflows/`）
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 工作流文件目录 🟡
- **去重关系**: 关联 USE-001
- **来源 Agent**: compat-diff

### INTENT-COMPAT-002
- **状态**: 准入
- **维度标签**: `[compatibility, usability]`
- **优先级**: P1
- **标题**: YAML 中未知/不支持字段的处理方式
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 未知/不支持字段处理 ❓
- **去重关系**: 关联 USE-006
- **来源 Agent**: compat-diff

### INTENT-COMPAT-003
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 核心上下文对象命名差异（`github.*` → `atomgit.*`）
- **覆盖的风险项**: RISK-COMPAT-01, RISK-COMPAT-02
- **覆盖的能力项**: Parity Matrix — 上下文对象命名 `atomgit.*` ❌
- **去重关系**: 关联 USE-002
- **来源 Agent**: compat-diff

### INTENT-COMPAT-004
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 系统环境变量前缀差异（`GITHUB_*` → `ATOMGIT_*`）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — 环境变量前缀差异
- **去重关系**: 关联 USE-003
- **来源 Agent**: compat-diff

### INTENT-COMPAT-005
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 自动生成的 workflow token 名称差异（`GITHUB_TOKEN` → `ATOMGIT_TOKEN`）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — Token 名称差异
- **去重关系**: 关联 USE-003
- **来源 Agent**: compat-diff

### INTENT-COMPAT-006
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 状态函数的调用语法差异（`success()` → `success`）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — 状态函数无括号 ❌
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-007
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 失败状态函数的名称差异（`failure()` → `failed`）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — 状态函数命名 ❌
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-008
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 表达式函数边界行为差异（空值/类型转换/大小写）
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-02
- **覆盖的能力项**: Parity Matrix — 表达式函数边界 ❓
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-009
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 数字字面量的类型处理差异（整数 → 浮点）
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-02
- **覆盖的能力项**: Parity Matrix — 表达式类型系统 ❓
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-010
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `pull_request` 事件的 `types` 取值命名差异
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — 触发过滤语义
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-011
- **状态**: 准入
- **维度标签**: `[compatibility, reliability]`
- **优先级**: P1
- **标题**: `paths` 路径过滤的匹配上限（300 文件）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — paths 过滤语义
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-012
- **状态**: 准入
- **维度标签**: `[compatibility, reliability]`
- **优先级**: P1
- **标题**: `schedule` cron 触发语义与调度边界
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-02
- **覆盖的能力项**: Parity Matrix — `schedule` cron 最短间隔 🟡
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-013
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `workflow_dispatch` / `workflow_call` 的 `inputs` 类型支持限制
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — `workflow_dispatch.inputs` 类型 🟡
- **去重关系**: 关联 USE-013
- **来源 Agent**: compat-diff

### INTENT-COMPAT-015
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `stages` 阶段机制（GitCode 特有扩展）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — `stages` 阶段机制 ❌, `post` 后处理阶段 ❌
- **去重关系**: 关联 USE-012
- **来源 Agent**: compat-diff

### INTENT-COMPAT-016
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `post` 后处理阶段（GitCode 特有扩展）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — `post` 后处理阶段 ❌
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-017
- **状态**: 准入
- **维度标签**: `[compatibility, reliability]`
- **优先级**: P1
- **标题**: `concurrency` 并发控制语法与语义差异
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — `concurrency.max` 1-5 + QUEUE/IGNORE 🟡
- **去重关系**: 关联 REL-001, REL-002, REL-003
- **来源 Agent**: compat-diff

### INTENT-COMPAT-018
- **状态**: 准入
- **维度标签**: `[compatibility, security]`
- **优先级**: P1
- **标题**: `permissions` 权限域命名差异
- **覆盖的风险项**: RISK-COMPAT-01, RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — `permissions` 权限域命名 ❌
- **去重关系**: 关联 USE-014, SEC-011, SEC-012
- **来源 Agent**: compat-diff

### INTENT-COMPAT-019
- **状态**: 准入
- **维度标签**: `[compatibility, security]`
- **优先级**: P1
- **标题**: `permissions` 默认权限范围差异
- **覆盖的风险项**: RISK-COMP-02, RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — `permissions` 默认权限 ❓
- **去重关系**: 关联 SEC-011
- **来源 Agent**: compat-diff

### INTENT-COMPAT-020
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `runs-on` Runner 标签体系差异
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — `runs-on` 标签体系 🟡
- **去重关系**: 关联 USE-015
- **来源 Agent**: compat-diff

### INTENT-COMPAT-021
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `runner` 上下文字段值格式差异（大小写）
- **覆盖的风险项**: RISK-COMPAT-02, RISK-USE-02
- **覆盖的能力项**: Parity Matrix — runner 上下文格式
- **去重关系**: 关联 USE-004
- **来源 Agent**: compat-diff

### INTENT-COMPAT-022
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: 默认 shell 选择差异
- **覆盖的风险项**: RISK-COMP-02
- **覆盖的能力项**: Parity Matrix — 默认 shell
- **去重关系**: 无
- **来源 Agent**: compat-diff

### INTENT-COMPAT-025
- **状态**: 准入
- **维度标签**: `[compatibility, security]`
- **优先级**: P1
- **标题**: `cache` action 在 fork PR 场景下的隔离策略
- **覆盖的风险项**: RISK-SEC-04
- **覆盖的能力项**: Parity Matrix — `cache` fork 场景隔离 ❓
- **去重关系**: 关联 SEC-009, SEC-010
- **来源 Agent**: compat-diff

### INTENT-COMPAT-026
- **状态**: 准入
- **维度标签**: `[compatibility, security]`
- **优先级**: P1
- **标题**: 内置 action 的引用写法与版本锁定差异
- **覆盖的风险项**: RISK-COMPAT-01, RISK-SEC-07
- **覆盖的能力项**: Parity Matrix — 内置 action 差异
- **去重关系**: 关联 SEC-014
- **来源 Agent**: compat-diff

### INTENT-COMPAT-027
- **状态**: 准入
- **维度标签**: `[compatibility, usability]`
- **优先级**: P1
- **标题**: 废弃 workflow 命令的降级方式差异
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 废弃命令降级
- **去重关系**: 关联 USE-010
- **来源 Agent**: compat-diff

### INTENT-COMPAT-029
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P1
- **标题**: `jobs` 顶层字段与 `stages` 嵌套的结构兼容性
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — stages/jobs 结构
- **去重关系**: 关联 USE-012
- **来源 Agent**: compat-diff

### INTENT-COMPAT-014
- **状态**: 准入
- **维度标签**: `[compatibility]`
- **优先级**: P2
- **标题**: `workflow_call` 可重用 workflow 嵌套层数上限差异（2 vs 4）
- **覆盖的风险项**: RISK-COMPAT-01
- **覆盖的能力项**: Parity Matrix — `workflow_call` 嵌套层数 🟡
- **去重关系**: 关联 REL-024, USE-018
- **来源 Agent**: compat-diff

### INTENT-COMPAT-001-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[compatibility, usability]`
- **优先级**: P1
- **标题**: 上下文对象与变量命名差异（`atomgit.*` / `ATOMGIT_*`）
- **覆盖的风险项**: RISK-COMPAT-01, RISK-USE-01
- **去重关系**: **被 COMPAT-003 + COMPAT-004 拆分覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: ID 与 compat.md INTENT-COMPAT-001 冲突；内容被 compat-diff 拆分为更细粒度意图

---

## 三、reliability 维度（25 条准入 + 4 条未准入）

### INTENT-REL-005
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P0
- **标题**: needs 依赖的 matrix job 全成功但上游初始化 job 失败时下游行为
- **覆盖的风险项**: RISK-REL-02
- **覆盖的能力项**: Parity Matrix — 执行模型失败传播
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-001
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: concurrency.max=5 边界——第 6 个同 group 触发时的策略行为
- **覆盖的风险项**: RISK-REL-01
- **覆盖的能力项**: Parity Matrix — `concurrency.max` 1-5 + QUEUE/IGNORE 🟡
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-002
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 并发洪泛——短时间内高频触发同仓库 workflow 的排队与公平性
- **覆盖的风险项**: RISK-REL-01
- **覆盖的能力项**: Parity Matrix — 并发洪泛
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-003
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: concurrency preemption 抢占——新 MR push 取消旧运行
- **覆盖的风险项**: RISK-REL-01
- **覆盖的能力项**: Parity Matrix — concurrency 抢占策略
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-004
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: matrix max-parallel 边界——矩阵展开数超过限制时的并发度限制
- **覆盖的风险项**: RISK-REL-01
- **覆盖的能力项**: Parity Matrix — `strategy.matrix` 组合数上限 ❓
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-006
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: stages.fail_fast=true 时单 job 失败立即终止同阶段其他 job
- **覆盖的风险项**: RISK-REL-02
- **覆盖的能力项**: Parity Matrix — `stages` 阶段机制 ❌
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-007
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: matrix fail-fast=true 时单实例失败取消其余实例
- **覆盖的风险项**: RISK-REL-02
- **覆盖的能力项**: Parity Matrix — matrix fail-fast
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-008
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 超大 matrix 边界——矩阵组合数逼近/越过上限
- **覆盖的风险项**: RISK-REL-01（间接）
- **覆盖的能力项**: Parity Matrix — `strategy.matrix` 组合数上限 ❓
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-009
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 超长日志——单 step 输出 50MB 文本日志的实时性与完整性
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — 日志完整性
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-010
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 大仓库 checkout——1GB+ 仓库克隆的耗时与资源稳定性
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — Git 大文件克隆/推送
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-011
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 接近 timeout 边界——job 运行 350 分钟观察正常终止 vs 超时 kill
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — `timeout-minutes` 默认 360 分钟 ✅
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-012
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 超多 step——单 job 50 个 step 的调度与状态回写完整性
- **覆盖的风险项**: RISK-REL-02（间接）
- **覆盖的能力项**: Parity Matrix — step 调度完整性
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-013
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 磁盘满故障注入——runner 磁盘写满后 job 行为与报错清晰度
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — Runner 资源边界
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-014
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: CPU 饱和故障注入——stress CPU 时 step 超时与心跳保活
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — Runner 资源边界
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-015
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: Runner 进程被 kill（模拟 runner 崩溃）——job 状态迁移与重调度
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — Runner 环境隔离 / 一次性 ❓
- **去重关系**: 关联 SEC-016
- **来源 Agent**: reliability

### INTENT-REL-016
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 网络分区故障注入——断开 runner 外网后观察依赖下载失败与重试
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — 网络出站策略
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-017
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 依赖 action 不可用（模拟 action 服务故障）——workflow 失败与报错
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — action 可用性
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-018
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: API 速率限制——高频触发下正确返回 429 与 Retry-After
- **覆盖的风险项**: RISK-REL-03
- **覆盖的能力项**: Parity Matrix — API 速率限制
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-019
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: Webhook 投递失败——模拟接收端 5xx 时观察重试间隔与风暴抑制
- **覆盖的风险项**: RISK-REL-04
- **覆盖的能力项**: Parity Matrix — Webhook 投递可靠性 ❓
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-020
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: artifact 大小边界——上传 500MB / 1GB / 2GB 文件观察上限与报错
- **覆盖的风险项**: RISK-REL-05（间接）
- **覆盖的能力项**: Parity Matrix — `upload-artifact` / `download-artifact` 🟡
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-021
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: cache 大小边界——写入 500MB / 1GB / 2GB 缓存观察上限与 LRU 淘汰
- **覆盖的风险项**: RISK-REL-05（间接）
- **覆盖的能力项**: Parity Matrix — `cache` fork 场景隔离 ❓
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-022
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: Package 大文件上传中断——500MB 包中途断网观察断点续传/重试
- **覆盖的风险项**: RISK-REL-06
- **覆盖的能力项**: Parity Matrix — Package 上传大文件中断
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-023
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 内存溢出边界——small runner(8GB) 上申请 12GB 内存观察 OOM kill 行为
- **覆盖的风险项**: RISK-REL-05
- **覆盖的能力项**: Parity Matrix — Runner 内存配额
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-024
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: workflow_call 嵌套层数边界——3 层嵌套观察报错
- **覆盖的风险项**: RISK-REL-02（间接）
- **覆盖的能力项**: Parity Matrix — `workflow_call` 嵌套层数 🟡
- **去重关系**: 关联 COMPAT-014, USE-018
- **来源 Agent**: reliability

### INTENT-REL-025
- **状态**: 准入
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: rerun 次数边界——连续请求第 4 次 rerun 观察拒绝行为
- **覆盖的风险项**: RISK-REL-02（间接）
- **覆盖的能力项**: Parity Matrix — `rerun` 次数限制 🟡
- **去重关系**: 无
- **来源 Agent**: reliability

### INTENT-REL-001-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: 并发控制 `concurrency.max`（1–5）+ QUEUE/IGNORE 策略
- **覆盖的风险项**: RISK-REL-01
- **去重关系**: **被 REL-001 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: reliability.md INTENT-REL-001 对边界场景描述更详细

### INTENT-REL-003-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: API 速率限制与 429/Retry-After 返回
- **覆盖的风险项**: RISK-REL-03
- **去重关系**: **被 REL-018 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: reliability.md INTENT-REL-018 对限流语义与 HTTP 标准对齐描述更完整；原 ID 与 REL-003 冲突

### INTENT-REL-004-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[reliability]`
- **优先级**: P1
- **标题**: Webhook 投递失败的重试与超时控制
- **覆盖的风险项**: RISK-REL-04
- **去重关系**: **被 REL-019 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: reliability.md INTENT-REL-019 对重试风暴抑制描述更完整；原 ID 与 REL-004 冲突

### INTENT-REL-006-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[reliability, usability]`
- **优先级**: P2
- **标题**: 大文件包上传中断与恢复
- **覆盖的风险项**: RISK-REL-06, RISK-USE-05
- **去重关系**: **被 REL-022 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: reliability.md INTENT-REL-022 对断点续传/重试策略描述更详细；原 ID 与 REL-006 冲突

---

## 四、security 维度（20 条准入 + 5 条未准入）

### INTENT-SEC-001
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: fork PR 触发 pull_request 事件时严禁读取目标仓库 secrets
- **覆盖的风险项**: RISK-SEC-01
- **覆盖的能力项**: Parity Matrix — fork PR 的 secret 隔离 ✅
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-002
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: secret 表达式脱敏机制不得被基础绕过手段穿透
- **覆盖的风险项**: RISK-SEC-05
- **覆盖的能力项**: Parity Matrix — `secrets` 日志脱敏 🟡
- **去重关系**: 关联 COMPAT-023
- **来源 Agent**: security

### INTENT-SEC-003
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: secret 值不得通过制品（artifact）或缓存元数据外泄
- **覆盖的风险项**: RISK-SEC-05
- **覆盖的能力项**: Parity Matrix — artifact/cache 安全
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-004
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: 不可信 PR 元数据（标题/分支名/提交信息）不得注入 run 脚本导致命令执行
- **覆盖的风险项**: RISK-SEC-02
- **覆盖的能力项**: Parity Matrix — 表达式注入防护
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-005
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: issue_comment / workflow_dispatch 等事件中的不可信输入不得注入脚本
- **覆盖的风险项**: RISK-SEC-02
- **覆盖的能力项**: Parity Matrix — 多源输入注入防护
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-006
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: 通过 ATOMGIT_ENV / ATOMGIT_OUTPUT 文件写入的污染数据不得破坏后续步骤执行上下文
- **覆盖的风险项**: RISK-SEC-02
- **覆盖的能力项**: Parity Matrix — step 间环境隔离
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-007
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: pull_request_target 事件中 checkout PR 头分支代码后不得直接执行不可信构建脚本
- **覆盖的风险项**: RISK-SEC-03
- **覆盖的能力项**: Parity Matrix — `pull_request_target` checkout 风险 ✅
- **去重关系**: 关联 COMPAT-024
- **来源 Agent**: security

### INTENT-SEC-008
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: pull_request_target 的 workflow 文件必须来自目标仓库 base 分支，不得被 fork 篡改
- **覆盖的风险项**: RISK-SEC-03
- **覆盖的能力项**: Parity Matrix — workflow 文件来源校验
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-011
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: 未声明 permissions 时 ATOMGIT_TOKEN 默认权限不得过大
- **覆盖的风险项**: RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — `permissions` 默认权限 ❓
- **去重关系**: 关联 COMPAT-019
- **来源 Agent**: security

### INTENT-SEC-012
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: job 级 permissions 必须正确覆盖顶层 permissions，不得出现继承漏洞
- **覆盖的风险项**: RISK-SEC-06
- **覆盖的能力项**: Parity Matrix — `permissions` 权限域命名 ❌
- **去重关系**: 关联 COMPAT-018
- **来源 Agent**: security

### INTENT-SEC-013
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: 低权限角色（Developer/Reporter）不得触发或访问高于其角色权限的 workflow 资源
- **覆盖的风险项**: RISK-SEC-09
- **覆盖的能力项**: Parity Matrix — 仓库成员角色 ❓, 组织管理 ❓
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-009
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: fork PR 不得污染目标仓库主分支的 cache 内容
- **覆盖的风险项**: RISK-SEC-04
- **覆盖的能力项**: Parity Matrix — `cache` fork 场景隔离 ❓
- **去重关系**: 关联 COMPAT-025
- **来源 Agent**: security

### INTENT-SEC-010
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 跨仓库 cache key 不得发生碰撞导致数据泄露或投毒
- **覆盖的风险项**: RISK-SEC-04
- **覆盖的能力项**: Parity Matrix — cache key 全局隔离
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-014
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 浮动 action ref（tag/branch）被篡改后，后续运行不得自动执行被篡改代码
- **覆盖的风险项**: RISK-SEC-07（关联）
- **覆盖的能力项**: Parity Matrix — action 版本锁定
- **去重关系**: 关联 COMPAT-026
- **来源 Agent**: security
- **优先级裁决理由**: 原 agent 未对齐直接风险编号。Orchestrator 关联至 RISK-SEC-07（Package/供应链投毒，P1），维持 P1。

### INTENT-SEC-015
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 本地 action（uses: ./path）不得通过路径遍历引用仓库外的恶意代码
- **覆盖的风险项**: RISK-SEC-06（关联）
- **覆盖的能力项**: Parity Matrix — 本地 action 路径安全
- **去重关系**: 无
- **来源 Agent**: security
- **优先级裁决理由**: 无直接风险编号，属权限越界/文件系统安全泛化场景，参照 RISK-SEC-06 定为 P1。

### INTENT-SEC-016
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 复用型 Runner 不得跨 job/跨运行残留敏感文件或环境变量
- **覆盖的风险项**: RISK-SEC-06（关联）
- **覆盖的能力项**: Parity Matrix — Runner 环境隔离 / 一次性 ❓
- **去重关系**: 关联 REL-015
- **来源 Agent**: security
- **优先级裁决理由**: 无直接风险编号，属信息泄露/环境隔离泛化场景，参照 RISK-SEC-06 定为 P1。

### INTENT-SEC-017
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: Package 仓库不得被低权限或无权限用户覆盖/删除已有版本
- **覆盖的风险项**: RISK-SEC-07
- **覆盖的能力项**: Parity Matrix — 包版本管理与淘汰 ❓, 包访问权限控制 ❓
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-018
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: Webhook secret 不得在配置界面明文回显，且签名验证不得被绕过
- **覆盖的风险项**: RISK-SEC-08
- **覆盖的能力项**: Parity Matrix — 仓库 Webhook ❓
- **去重关系**: 无
- **来源 Agent**: security

### INTENT-SEC-019
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 审计日志必须完整记录权限变更、secret 访问与高危 workflow 触发事件
- **覆盖的风险项**: RISK-SEC-09（关联）
- **覆盖的能力项**: Parity Matrix — 审计日志 ❓
- **去重关系**: 无
- **来源 Agent**: security
- **优先级裁决理由**: 无直接风险编号，属提权审计追溯需求，参照 RISK-SEC-09 定为 P1（审计是 P0 的辅助证据，非独立 blocker）。

### INTENT-SEC-020
- **状态**: 准入
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 自托管 Runner 注册令牌不得在工作流日志或环境变量中泄露
- **覆盖的风险项**: RISK-SEC-06（关联）
- **覆盖的能力项**: Parity Matrix — Runner 注册安全
- **去重关系**: 无
- **来源 Agent**: security
- **优先级裁决理由**: 无直接风险编号，属基础设施 token 泄露泛化场景，参照 RISK-SEC-06 定为 P1。

### INTENT-SEC-001-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: fork PR 的 secret 隔离（pull_request 事件）
- **覆盖的风险项**: RISK-SEC-01
- **去重关系**: **被 SEC-001 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: security.md INTENT-SEC-001 判定证据与负向断言更完整

### INTENT-SEC-002-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: 不可信输入导致的脚本注入 + secret 脱敏混合验证
- **覆盖的风险项**: RISK-SEC-02, RISK-SEC-05
- **去重关系**: **被 SEC-002（脱敏）+ SEC-004（脚本注入）拆分覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: security agent 将混合意图拆分为两个更专业的独立意图

### INTENT-SEC-003-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[security]`
- **优先级**: P0
- **标题**: `pull_request_target` checkout 不可信代码风险
- **覆盖的风险项**: RISK-SEC-03
- **去重关系**: **被 SEC-007 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: security.md INTENT-SEC-007 + SEC-008 拆分更细（防御层生效 + workflow 文件来源）

### INTENT-SEC-004-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: cache 跨 fork/跨分支隔离
- **覆盖的风险项**: RISK-SEC-04
- **去重关系**: **被 SEC-009 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: ID 与 security.md INTENT-SEC-004 冲突；security.md INTENT-SEC-009/010 拆分更细

### INTENT-SEC-007-SPEC（未准入）
- **状态**: 打回（未准入）
- **维度标签**: `[security]`
- **优先级**: P1
- **标题**: 包访问权限控制与防恶意覆盖
- **覆盖的风险项**: RISK-SEC-07
- **去重关系**: **被 SEC-017 覆盖**
- **来源 Agent**: spec-analyst
- **未准入原因**: ID 与 security.md INTENT-SEC-007 冲突；security.md INTENT-SEC-017 判定证据更完整

---

## 五、usability 维度（19 条准入 + 0 条未准入）

### INTENT-USE-004
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P0
- **标题**: `runner.os` 文档值与实际返回值不一致的开发者困惑
- **覆盖的风险项**: RISK-USE-02
- **覆盖的能力项**: Parity Matrix — runner 上下文格式
- **去重关系**: 关联 COMPAT-021
- **来源 Agent**: usability

### INTENT-USE-005
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P0
- **标题**: `vars` 上下文文档声明与平台实际不支持的落差
- **覆盖的风险项**: RISK-USE-02
- **覆盖的能力项**: Parity Matrix — vars 上下文支持状态
- **去重关系**: 无
- **来源 Agent**: usability

### INTENT-USE-017
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P0
- **标题**: 官方文档中残留 GitHub 措辞的自洽性
- **覆盖的风险项**: RISK-USE-02
- **覆盖的能力项**: Parity Matrix — 文档一致性
- **去重关系**: 无
- **来源 Agent**: usability

### INTENT-USE-001
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: 迁移报错应指明路径差异（`.github/workflows/` → `.gitcode/workflows/`）
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 迁移报错质量 ❓
- **去重关系**: 关联 COMPAT-001
- **来源 Agent**: usability

### INTENT-USE-002
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: 迁移报错应指明上下文命名差异（`github.*` → `atomgit.*`）
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 上下文对象命名 ❌
- **去重关系**: 关联 COMPAT-003
- **来源 Agent**: usability

### INTENT-USE-003
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: 迁移报错应指明令牌名称差异（`GITHUB_TOKEN` → `ATOMGIT_TOKEN`）
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 系统环境变量前缀 ❌
- **去重关系**: 关联 COMPAT-004, COMPAT-005
- **来源 Agent**: usability

### INTENT-USE-006
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: YAML 静态校验报错应给出精确字段路径与有效值
- **覆盖的风险项**: RISK-USE-03
- **覆盖的能力项**: Parity Matrix — 未知/不支持字段处理 ❓
- **去重关系**: 关联 COMPAT-002
- **来源 Agent**: usability

### INTENT-USE-008
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: MR 触发 CI 失败后通知的时效性与信息完整性
- **覆盖的风险项**: RISK-USE-04
- **覆盖的能力项**: Parity Matrix — 站内通知/邮件通知
- **去重关系**: 无
- **来源 Agent**: usability

### INTENT-USE-010
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: 废弃 workflow 命令日志应给出带行号的替换指引
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — 废弃命令降级
- **去重关系**: 关联 COMPAT-027
- **来源 Agent**: usability

### INTENT-USE-011
- **状态**: 准入
- **维度标签**: `[usability, security]`
- **优先级**: P1
- **标题**: Secret 掩码被绕过时日志应发出暴露预警
- **覆盖的风险项**: RISK-USE-01（迁移安全习惯差异）
- **覆盖的能力项**: Parity Matrix — `secrets` 日志脱敏 🟡
- **去重关系**: 关联 SEC-002, COMPAT-023
- **来源 Agent**: usability
- **备注**: `eval: llm_assisted`

### INTENT-USE-012
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: `stages` 与 `jobs` 混用报错应解释 GitCode 特有的阶段机制
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — `stages` 阶段机制 ❌
- **去重关系**: 关联 COMPAT-015, COMPAT-029
- **来源 Agent**: usability
- **备注**: `eval: llm_assisted`

### INTENT-USE-013
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: `workflow_dispatch` / `workflow_call` 非 string 输入类型迁移报错应说明平台限制
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — `workflow_dispatch.inputs` 类型 🟡
- **去重关系**: 关联 COMPAT-013
- **来源 Agent**: usability

### INTENT-USE-014
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: `permissions` 使用 GitHub 命名时报错应列出 GitCode 权限域映射
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — `permissions` 权限域命名 ❌
- **去重关系**: 关联 COMPAT-018
- **来源 Agent**: usability

### INTENT-USE-015
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: `runs-on` 标签不匹配时报错应给出三段式格式示例
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — `runs-on` 标签体系 🟡
- **去重关系**: 关联 COMPAT-020
- **来源 Agent**: usability

### INTENT-USE-016
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: 工作流命令 `::error::` / `::warning::` 注解在 UI 中的可读性与定位能力
- **覆盖的风险项**: RISK-USE-01（调试体验）
- **覆盖的能力项**: Parity Matrix — `ATOMGIT_STEP_SUMMARY` Markdown 🟡, 运行状态机 ✅
- **去重关系**: 无
- **来源 Agent**: usability
- **备注**: `eval: llm_assisted`

### INTENT-USE-019
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P1
- **标题**: 站内通知与邮件通知的及时性与完整性
- **覆盖的风险项**: RISK-USE-04
- **覆盖的能力项**: Parity Matrix — 站内通知/邮件通知
- **去重关系**: 无
- **来源 Agent**: spec-analyst
- **备注**: 原 ID `INTENT-USE-004`，因与 usability.md INTENT-USE-004 冲突，Orchestrator 重编号为 USE-019

### INTENT-USE-007
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P2
- **标题**: `workflow_dispatch` 缺少必填参数时 API 报错应指明参数名与来源
- **覆盖的风险项**: RISK-USE-03
- **覆盖的能力项**: Parity Matrix — API 错误信息质量
- **去重关系**: 无
- **来源 Agent**: usability

### INTENT-USE-009
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P2
- **标题**: 制品库版本冲突报错应包含包名、版本号与操作指引
- **覆盖的风险项**: RISK-USE-05
- **覆盖的能力项**: Parity Matrix — Package 版本冲突提示
- **去重关系**: 无
- **来源 Agent**: usability

### INTENT-USE-018
- **状态**: 准入
- **维度标签**: `[usability]`
- **优先级**: P2
- **标题**: `workflow_call` 嵌套超过 2 层时的报错应给出深度与调用链
- **覆盖的风险项**: RISK-USE-01
- **覆盖的能力项**: Parity Matrix — `workflow_call` 嵌套层数 🟡
- **去重关系**: 关联 COMPAT-014, REL-024
- **来源 Agent**: usability

---

## 六、覆盖盲区清单

### 6.1 Blocker 风险项覆盖检查

| 风险 ID | 优先级 | 是否 blocker | 覆盖 Intent | 状态 |
|---|---|---|---|---|
| RISK-SEC-01 | P0 | 是 | SEC-001, COMPAT-024 | ✅ 已覆盖 |
| RISK-SEC-02 | P0 | 是 | SEC-004, SEC-005, SEC-006 | ✅ 已覆盖 |
| RISK-SEC-03 | P0 | 是 | SEC-007, SEC-008, COMPAT-024 | ✅ 已覆盖 |
| RISK-SEC-05 | P0 | 是 | SEC-002, SEC-003, COMPAT-023 | ✅ 已覆盖 |
| RISK-SEC-06 | P0 | 是 | SEC-011, SEC-012, SEC-013, SEC-015, SEC-016, GIT-002, MR-003, AUTH-002 | ✅ 已覆盖 |
| RISK-SEC-09 | P0 | 是 | SEC-009, SEC-013, SEC-019 | ✅ 已覆盖 |
| RISK-COMP-01 | P0 | 是 | GIT-001, MR-001, ISSUE-001, AUTH-003, HOOK-002 | ✅ 已覆盖 |
| RISK-REL-02 | P0 | 是 | MR-004, REL-005 | ✅ 已覆盖 |
| RISK-USE-02 | P0 | 是 | USE-004, USE-005, USE-017, COMPAT-028 | ✅ 已覆盖 |

> **结论**: 全部 9 个 blocker 风险项均有 P0 intent 覆盖，无盲区。

### 6.2 Parity Matrix 「部分/不支持/未知」能力项覆盖检查

| 能力项 | 状态 | 覆盖 Intent | 盲区说明 |
|---|---|---|---|
| 工作流文件目录 `.gitcode/workflows/` | 🟡 | COMPAT-001 | — |
| 未知/不支持字段处理 | ❓ | COMPAT-002, USE-006 | — |
| `push` 触发 + branches/paths 过滤 | ✅ | — | 已在 spec 中验证，无需独立 intent |
| `pull_request` vs `pull_request_target` 隔离 | ✅ | SEC-001, COMPAT-024 | — |
| `schedule` cron 最短间隔 | 🟡 | COMPAT-012 | — |
| `workflow_call` 嵌套层数 | 🟡 | COMPAT-014, REL-024, USE-018 | — |
| `stages` 阶段机制 | ❌ | COMPAT-015, USE-012 | — |
| `post` 后处理阶段 | ❌ | COMPAT-016 | — |
| `timeout-minutes` 默认 360 分钟 | ✅ | REL-011 | — |
| `rerun` 次数限制 | 🟡 | REL-025 | — |
| `runs-on` 标签体系 | 🟡 | COMPAT-020, USE-015 | — |
| Runner 环境隔离 / 一次性 | ❓ | SEC-016, REL-015 | — |
| `secrets` 日志脱敏 `***` | 🟡 | SEC-002, COMPAT-023, USE-011 | — |
| `permissions` 默认权限 | ❓ | COMPAT-019, SEC-011 | — |
| `permissions` 权限域命名 | ❌ | COMPAT-018, USE-014 | — |
| `pull_request_target` checkout 风险 | ✅ | SEC-007, SEC-008, COMPAT-024 | — |
| `upload-artifact` / `download-artifact` | 🟡 | REL-020 | — |
| `cache` fork 场景隔离 | ❓ | SEC-009, SEC-010, COMPAT-025 | — |
| 运行状态机 + 日志完整性 | ✅ | REL-009, REL-012 | — |
| `ATOMGIT_STEP_SUMMARY` Markdown | 🟡 | USE-016 | — |
| 上下文对象命名 `atomgit.*` | ❌ | COMPAT-003, USE-002 | — |
| 状态函数无括号 `success`/`failed` | ❌ | COMPAT-006, COMPAT-007 | — |
| 表达式函数 `contains`/`hashFiles`/`toJson` | ❓ | COMPAT-008 | — |
| `workflow_dispatch.inputs` 类型 | 🟡 | COMPAT-013, USE-013 | — |
| 迁移报错质量 | ❓ | COMPAT-028, USE-001~003, USE-006, USE-010, USE-012~016, USE-018 | — |
| `concurrency.max` 1-5 + QUEUE/IGNORE | 🟡 | REL-001~003, COMPAT-017 | — |
| `strategy.matrix` 组合数上限 | ❓ | REL-004, REL-008 | — |
| Git Clone（HTTPS/SSH） | ✅ | GIT-001 | — |
| Git Push（HTTPS/SSH） | 🟡 | GIT-001 | — |
| 分支创建与删除 | ❓ | GIT-004 | — |
| 标签创建与删除 | ❓ | GIT-004 | — |
| 分支保护规则 | ❓ | GIT-002 | — |
| 强制推送（force push）控制 | ❓ | GIT-002 | — |
| 代码审查（Code Review） | ❓ | MR-003 | — |
| 大文件存储（LFS） | ❓ | GIT-003 | — |
| **仓库镜像/同步** | ❓ | — | **盲区：无 intent 覆盖** |
| **子模块（Submodule）支持** | ❓ | — | **盲区：无 intent 覆盖** |
| MR 创建与关闭 | ✅ | MR-001 | — |
| MR 列表与筛选 | ✅ | MR-001 | — |
| MR 详情查看 | ❓ | MR-002 | — |
| 合并策略（Merge/Squash/Rebase） | ❓ | MR-001 | — |
| 代码审查与行级评论 | ❓ | MR-003 | — |
| CI 门禁（MR 必须过 CI） | ❓ | MR-004 | — |
| 冲突检测与解决提示 | ❓ | MR-002 | — |
| MR 模板（Description Template） | ❓ | MR-005, USE-012 | — |
| Draft/WIP MR | ❓ | MR-001 | — |
| Issue 创建与关闭 | ✅ | ISSUE-001 | — |
| Issue 列表与筛选 | ✅ | ISSUE-001 | — |
| Issue 评论 | ❓ | ISSUE-003 | — |
| 标签（Label）管理 | ❓ | ISSUE-002 | — |
| 里程碑（Milestone）管理 | ❓ | ISSUE-002 | — |
| **Issue 模板** | ❓ | — | **盲区：无 intent 覆盖** |
| Issue 关联 MR/Commit | ❓ | ISSUE-004 | — |
| **看板（Board/Kanban）** | ❓ | — | **盲区：无 intent 覆盖** |
| npm 包上传与下载 | ❓ | PKG-001 | — |
| Maven 包上传与下载 | ❓ | PKG-001 | — |
| PyPI 包上传与下载 | ❓ | PKG-001 | — |
| Docker 镜像上传与下载 | ❓ | PKG-001 | — |
| NuGet/Gradle/Go 模块支持 | ❓ | PKG-001 | — |
| 包版本管理与淘汰 | ❓ | SEC-017 | — |
| 包访问权限控制 | ❓ | SEC-017 | — |
| 包与仓库关联 | ❓ | PKG-001 | — |
| 用户认证（OAuth2/Token） | ✅ | AUTH-001 | — |
| 仓库成员角色（Owner/Maintainer/Developer） | ❓ | AUTH-002 | — |
| 组织（Organization）管理 | ❓ | AUTH-003, SEC-009, SEC-013 | — |
| 团队（Team）与权限继承 | ❓ | AUTH-003 | — |
| **外部协作者（Collaborator）** | ❓ | — | **盲区：无 intent 覆盖** |
| **SSO / LDAP 集成** | ❓ | — | **盲区：无 intent 覆盖** |
| 审计日志（Audit Log） | ❓ | SEC-019 | — |
| **两步验证（2FA）** | ❓ | — | **盲区：无 intent 覆盖** |
| 仓库 Webhook（Push/MR/Issue） | ❓ | HOOK-001 | — |
| Webhook 投递可靠性 | ❓ | REL-019, HOOK-001 | — |
| CI 状态回写（Commit Status） | ❓ | HOOK-002 | — |

### 6.3 盲区汇总

| 盲区类别 | 具体项 | 建议补全方向 |
|---|---|---|
| Git Repository | 仓库镜像/同步 | 新增 INTENT-GIT-006 |
| Git Repository | 子模块（Submodule）支持 | 新增 INTENT-GIT-007 |
| Issues | Issue 模板 | 新增 INTENT-ISSUE-005 |
| Issues | 看板（Board/Kanban） | 新增 INTENT-ISSUE-006（P2） |
| 用户与权限 | 外部协作者（Collaborator） | 新增 INTENT-AUTH-004 |
| 用户与权限 | SSO / LDAP 集成 | 新增 INTENT-AUTH-005（企业级，P2） |
| 用户与权限 | 两步验证（2FA） | 新增 INTENT-AUTH-006 |
| 风险登记册 | RISK-COMPAT-03（Git 客户端 sparse-checkout 兼容性，P2） | spec-analyst 已注明本次未覆盖，可后续 run 补 |

> **纪律声明**: 以上盲区已如实暴露，未为「看起来完整」而隐藏。  
> 五个维度均已有准入 intent，安全维度准入 20 条，不可为空。

---

## 附录：统计速查

| 维度 | 准入条数 | P0 | P1 | P2 | 未准入条数 |
|---|---|---|---|---|---|
| completeness | 20 | 8 | 12 | 0 | 3 |
| compatibility | 29 | 3 | 25 | 1 | 1 |
| reliability | 25 | 1 | 24 | 0 | 4 |
| security | 20 | 11 | 9 | 0 | 5 |
| usability | 19 | 3 | 13 | 3 | 0（含 1 条重编号） |
| **合计** | **113** | **26** | **83** | **4** | **13** |

> 注：跨维度 intent 在各维度分别计数一次，故按维度求和为 113（因 USE-019 从 spec 移入 usability，总数为 113 条准入 + 13 条未准入 = 126 条记录在库；原始输入 127 条中 5 条合并/拆分后无独立记录）。
