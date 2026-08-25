# Intent Library — Run 2026-08-25-01

> 汇总 usability + completeness 两个维度的 UI 测试意图。
> 阶段 A 发散完成：共 24 条原始 intent → 汇总后 24 条（无重复）。

---

## Usability Intents (12)

| ID | dimensions | priority | title |
|---|---|---|---|
| INTENT-USE-001 | [usability] | P0 | Issue 创建流程的表单可用性与异常提示验证 |
| INTENT-USE-002 | [usability] | P0 | Issue 列表筛选与排序的交互响应及状态保持 |
| INTENT-USE-003 | [usability] | P0 | Merge Request 创建时源/目标分支选择与差异预览可用性 |
| INTENT-USE-004 | [usability, completeness] | P0 | Merge 按钮的权限控制与冲突状态交互反馈 |
| INTENT-USE-005 | [usability] | P1 | 仓库文件树在大目录下的加载与浏览体验 |
| INTENT-USE-006 | [usability] | P1 | 分支切换器在仓库浏览场景的搜索与切换体验 |
| INTENT-USE-007 | [usability, completeness] | P1 | 全局搜索的输入响应与结果分类展示 |
| INTENT-USE-008 | [usability] | P1 | 用户工作台通知中心的读取与批量操作体验 |
| INTENT-USE-009 | [usability] | P2 | 登录流程的多因子与错误提示可用性 |
| INTENT-USE-010 | [usability, completeness] | P2 | 个人设置页表单保存与即时反馈 |
| INTENT-USE-011 | [usability] | P2 | 代码查看页的行内评论与锚点分享体验 |
| INTENT-USE-012 | [usability] | P2 | 无权限/404 页面的友好提示与返回引导 |

## Completeness Intents (12)

| ID | dimensions | priority | title |
|---|---|---|---|
| INTENT-COMP-001 | [completeness] | P0 | Issue 详情页核心信息渲染与评论操作覆盖 |
| INTENT-COMP-002 | [completeness] | P0 | Issue 标签与里程碑管理页面的存在性与绑定功能 |
| INTENT-COMP-003 | [completeness] | P0 | Merge Request 差异对比页与代码评审评论的完整渲染 |
| INTENT-COMP-004 | [completeness] | P0 | MR 生命周期状态流转（关闭、重新打开、合并后锁定） |
| INTENT-COMP-005 | [completeness] | P1 | 仓库文件在线编辑、预览与提交记录查看 |
| INTENT-COMP-006 | [completeness] | P1 | 分支列表管理、保护规则与分支对比功能覆盖 |
| INTENT-COMP-007 | [completeness] | P1 | 仓库成员管理页面的邀请、列表与角色变更 |
| INTENT-COMP-008 | [completeness] | P1 | 组织设置与仓库级集成配置页面的核心功能可达性 |
| INTENT-COMP-009 | [completeness] | P1 | 仓库 Fork 流程与 Fork 后仓库的独立导航 |
| INTENT-COMP-010 | [completeness] | P2 | 全局看板/Projects 页面的列表与卡片交互覆盖 |
| INTENT-COMP-011 | [completeness] | P2 | 代码 Blame 视图与 Raw 文件查看的页面可达性 |
| INTENT-COMP-012 | [completeness, usability] | P2 | 合并冲突时的 Web 冲突解决入口与状态提示覆盖 |

---

## 门禁评审摘要

### 去重
- USE-001 与 COMP-001 均涉及 Issue，但前者聚焦表单可用性/异常提示，后者聚焦详情页信息渲染与评论 → **不合并**，保留两条，互标关联。
- USE-003 与 COMP-003 均涉及 MR diff，前者聚焦分支选择/预览可用性，后者聚焦 diff 渲染/行评论 → **不合并**，保留两条。
- USE-004 与 COMP-004 均涉及 MR 合并按钮/状态，前者聚焦权限/冲突反馈，后者聚焦状态流转（关闭/重开/锁定）→ **不合并**，保留两条。
- USE-007 与 COMP-009 均涉及搜索/Fork，无重叠 → 保留。
- 其余 intent 无重复。

### 优先级裁决
- P0 × 8：Issue/MR 核心路径（创建、详情、评论、标签、diff、状态流转、权限）
- P1 × 8：仓库浏览、分支、成员、设置、搜索、Fork
- P2 × 8：登录、个人设置、行评论、404、看板、Blame、冲突

### 准入状态
**全部 24 条 intent 准入** ✅

### 与已有 UI 用例的关联
| 已有用例 | 覆盖 Intent | 说明 |
|---|---|---|
| UI-ISSUE-01-002 | USE-001（部分） | 已覆盖创建 Issue 正向路径，未覆盖异常提示 |
| UI-MR-01-002 | USE-003（部分） | 已覆盖 MR 创建，未覆盖分支选择/无 diff 提示 |
| UI-MR-01-003 | USE-004（部分） | 已覆盖合并成功，未覆盖冲突/权限/关闭重开 |

**缺口**: 21 条 intent 需要新增用例覆盖。

---

## 状态

`gated`（已准入，等待阶段 B 展开）
