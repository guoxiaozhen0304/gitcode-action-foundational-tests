# Issue 技术规格

> 来源：`gitcode-docs/Issue.md`
> 整理日期：2026-08-18
> 覆盖：Issue 创建、标签、里程碑、评论、指派、筛选、通知

---

## 1. 功能概述

Issue 是 GitCode 项目跟踪问题、bug、任务和改进请求的核心工具。支持以下能力：
- **创建与关闭**：标题/描述/标签/指派人/里程碑
- **评论与讨论**：支持 Markdown、@提及、引用其他 Issue/MR
- **标签管理**：自定义颜色/名称/描述，预置默认标签
- **里程碑管理**：按截止日期聚合 Issue/MR，追踪进度
- **筛选与搜索**：按状态/标签/指派人/里程碑筛选
- **关联追溯**：通过关键字（`close`/`fix`/`resolve`）自动关联 MR/Commit

### 1.1 默认标签（预置）

| 标签名 | 颜色 | 用途 |
|---|---|---|
| `bug` | `#d73a4a` | 缺陷报告 |
| `duplicate` | `#cfd3d7` | 重复 Issue |
| `enhancement` | `#a2eeef` | 功能增强 |
| `help wanted` | `#008672` | 寻求帮助 |
| `invalid` | `#e4e669` | 无效 Issue |
| `question` | `#d876e3` | 疑问 |
| `wontfix` | `#ffffff` | 不修复 |
| `documentation` | `#0075ca` | 文档相关 |

### 1.2 Issue 状态流转

```
[open] --关闭--> [closed]
  ↑____________|
```

已关闭的 Issue 可随时重新打开。

---

## 2. API 端点

### 2.1 Issue 管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/issues` | 获取 Issue 列表 |
| POST | `/api/v5/repos/{owner}/{repo}/issues` | 创建 Issue |
| GET | `/api/v5/repos/{owner}/{repo}/issues/{number}` | 获取 Issue 详情 |
| PATCH | `/api/v5/repos/{owner}/{repo}/issues/{number}` | 更新 Issue |

#### POST /api/v5/repos/{owner}/{repo}/issues — 创建 Issue

**请求体：**
```json
{
  "title": "Bug: login fails with 500 error",
  "body": "## 复现步骤\n1. 打开登录页\n2. 输入账号密码\n3. 点击登录\n\n## 预期结果\n登录成功\n\n## 实际结果\n返回 500",
  "assignee": "developer1",
  "labels": ["bug", "help wanted"],
  "milestone": 2
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | ✅ | Issue 标题 |
| `body` | string | ❌ | Issue 描述（支持 Markdown） |
| `assignee` | string | ❌ | 指派人用户名 |
| `labels` | array | ❌ | 标签名称列表 |
| `milestone` | integer | ❌ | 里程碑 ID |

**响应示例：**
```json
{
  "number": 101,
  "title": "Bug: login fails with 500 error",
  "state": "open",
  "user": { "login": "reporter" },
  "labels": [
    { "name": "bug", "color": "d73a4a" }
  ],
  "assignee": { "login": "developer1" },
  "milestone": { "number": 2, "title": "v1.0.0" },
  "created_at": "2026-08-18T10:00:00Z",
  "updated_at": "2026-08-18T10:00:00Z",
  "comments": 0
}
```

#### PATCH /api/v5/repos/{owner}/{repo}/issues/{number} — 更新 Issue

**请求体：**
```json
{
  "title": "Updated title",
  "body": "Updated description",
  "state": "closed",
  "assignee": "new_assignee",
  "labels": ["enhancement"],
  "milestone": 3
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | ❌ | 新标题 |
| `body` | string | ❌ | 新描述 |
| `state` | string | ❌ | `open` 或 `closed` |
| `assignee` | string | ❌ | 新指派人（传 `null` 取消指派） |
| `labels` | array | ❌ | 新标签列表（覆盖原标签） |
| `milestone` | integer | ❌ | 新里程碑 ID（传 `null` 取消关联） |

---

### 2.2 Issue 评论

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/issues/{number}/comments` | 获取评论列表 |
| POST | `/api/v5/repos/{owner}/{repo}/issues/{number}/comments` | 创建评论 |
| PATCH | `/api/v5/repos/{owner}/{repo}/issues/comments/{id}` | 更新评论 |
| DELETE | `/api/v5/repos/{owner}/{repo}/issues/comments/{id}` | 删除评论 |

#### POST /api/v5/repos/{owner}/{repo}/issues/{number}/comments

**请求体：**
```json
{
  "body": "已复现，正在定位问题原因。\n\ncc @manager"
}
```

---

### 2.3 标签管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/labels` | 获取标签列表 |
| POST | `/api/v5/repos/{owner}/{repo}/labels` | 创建标签 |
| GET | `/api/v5/repos/{owner}/{repo}/labels/{name}` | 获取标签详情 |
| PATCH | `/api/v5/repos/{owner}/{repo}/labels/{name}` | 更新标签 |
| DELETE | `/api/v5/repos/{owner}/{repo}/labels/{name}` | 删除标签 |

#### POST /api/v5/repos/{owner}/{repo}/labels

**请求体：**
```json
{
  "name": "priority-high",
  "color": "ff0000",
  "description": "高优先级任务"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | ✅ | 标签名称（唯一） |
| `color` | string | ✅ | 颜色 hex 值（不含 `#`） |
| `description` | string | ❌ | 标签描述 |

---

### 2.4 里程碑管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/milestones` | 获取里程碑列表 |
| POST | `/api/v5/repos/{owner}/{repo}/milestones` | 创建里程碑 |
| GET | `/api/v5/repos/{owner}/{repo}/milestones/{number}` | 获取里程碑详情 |
| PATCH | `/api/v5/repos/{owner}/{repo}/milestones/{number}` | 更新里程碑 |
| DELETE | `/api/v5/repos/{owner}/{repo}/milestones/{number}` | 删除里程碑 |

#### POST /api/v5/repos/{owner}/{repo}/milestones

**请求体：**
```json
{
  "title": "v1.0.0",
  "description": "首个正式版本",
  "state": "open",
  "due_on": "2026-09-01T00:00:00Z"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | ✅ | 里程碑标题 |
| `description` | string | ❌ | 描述 |
| `state` | string | ❌ | `open`（默认）或 `closed` |
| `due_on` | string | ❌ | 截止日期（ISO 8601 格式） |

---

## 3. 枚举值

### 3.1 Issue 状态
| 值 | 说明 |
|---|---|
| `open` | 打开 |
| `closed` | 已关闭 |
| `all` | 查询时返回全部 |

### 3.2 Issue 排序字段
| 值 | 说明 |
|---|---|
| `created` | 创建时间 |
| `updated` | 更新时间 |
| `comments` | 评论数 |

### 3.3 排序方向
| 值 | 说明 |
|---|---|
| `asc` | 升序 |
| `desc` | 降序（默认） |

### 3.4 标签颜色
- Hex 字符串，**不含 `#`**，如 `d73a4a`

---

## 4. 配置示例

### 4.1 创建 Issue（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/issues \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Bug: API 返回 404",
    "body": "## 复现\n调用 /api/v5/user/repos 返回 404",
    "labels": ["bug"],
    "assignee": "developer1"
  }'
```

### 4.2 关闭 Issue（curl）
```bash
curl -X PATCH https://gitcode.com/api/v5/repos/owner/repo/issues/101 \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"state": "closed"}'
```

### 4.3 创建标签（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/labels \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "urgent",
    "color": "ff0000",
    "description": "紧急处理"
  }'
```

### 4.4 创建里程碑（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/milestones \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "v2.0.0",
    "due_on": "2026-12-01T00:00:00Z"
  }'
```
