# Merge Request 技术规格

> 来源：`gitcode-docs/合并请求/*`
> 整理日期：2026-08-18
> 覆盖：MR 创建、代码评审、草稿 MR、冲突解决、快进合并

---

## 1. 功能概述

合并请求（Merge Request, MR）是 GitCode 代码协作的核心机制，用于将功能分支的更改合并到目标分支。支持以下核心能力：
- **创建与关闭**：基于分支对比创建 MR，支持标题、描述、指派人、评审人
- **代码评审**：行级评论、建议修改、批量解决、Approve/Reject
- **草稿状态**：通过 `[WIP]` 标记草稿 MR，禁止直接合并
- **冲突解决**：内置在线冲突解决工具，支持自动解决与手动编辑
- **快进合并**：无冲突且线性历史时直接应用到目标分支，不创建合并提交
- **合并策略**：支持普通合并、Squash 合并、Rebase 合并

### 1.1 MR 状态机

| 状态 | 说明 |
|---|---|
| `open` | 新建或重新打开，等待评审/合并 |
| `closed` | 手动关闭，未合并 |
| `merged` | 已成功合并到目标分支 |
| `draft` | 草稿状态（标题含 `[WIP]`），不可合并 |

### 1.2 合并策略

| 策略 | 说明 | 适用场景 |
|---|---|---|
| `merge` | 创建合并提交，保留完整分支历史 | 需要追溯分支来源 |
| `squash` | 压缩所有提交为一个，再合并 | 功能分支提交较凌乱 |
| `rebase` | 变基到目标分支顶部，线性历史 | 要求干净的提交历史 |
| `fast-forward` | 无冲突时直接前移分支指针 | 简单线性变更 |

---

## 2. API 端点

### 2.1 MR 管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/pulls` | 获取 MR 列表 |
| POST | `/api/v5/repos/{owner}/{repo}/pulls` | 创建 MR |
| GET | `/api/v5/repos/{owner}/{repo}/pulls/{number}` | 获取 MR 详情 |
| PATCH | `/api/v5/repos/{owner}/{repo}/pulls/{number}` | 更新 MR |
| POST | `/api/v5/repos/{owner}/{repo}/pulls/{number}/merge` | 执行合并 |

#### POST /api/v5/repos/{owner}/{repo}/pulls — 创建 MR

**请求体：**
```json
{
  "title": "[WIP] Add new feature",
  "head": "feature-branch",
  "base": "main",
  "body": "## 变更内容\n- 添加新功能\n- 修复已知问题",
  "assignee": "username",
  "reviewers": ["reviewer1", "reviewer2"],
  "labels": ["enhancement"],
  "milestone": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `title` | string | ✅ | MR 标题；前缀 `[WIP]` 表示草稿 |
| `head` | string | ✅ | 源分支名称 |
| `base` | string | ✅ | 目标分支名称 |
| `body` | string | ❌ | MR 描述（支持 Markdown） |
| `assignee` | string | ❌ | 指派人用户名 |
| `reviewers` | array | ❌ | 评审人用户名列表 |
| `labels` | array | ❌ | 标签名称列表 |
| `milestone` | integer | ❌ | 里程碑 ID |

**响应示例：**
```json
{
  "number": 42,
  "title": "[WIP] Add new feature",
  "state": "open",
  "head": { "ref": "feature-branch", "sha": "abc123" },
  "base": { "ref": "main", "sha": "def456" },
  "user": { "login": "author" },
  "created_at": "2026-08-18T10:00:00Z",
  "updated_at": "2026-08-18T10:00:00Z",
  "mergeable": true,
  "mergeable_state": "clean"
}
```

#### POST /api/v5/repos/{owner}/{repo}/pulls/{number}/merge — 执行合并

**请求体：**
```json
{
  "merge_method": "merge",
  "commit_title": "Merge pull request #42",
  "commit_message": "Approved by reviewer1"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `merge_method` | string | ❌ | 合并策略：`merge`、`squash`、`rebase` |
| `commit_title` | string | ❌ | 合并提交的标题 |
| `commit_message` | string | ❌ | 合并提交的描述 |

---

### 2.2 MR 评审

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/pulls/{number}/reviews` | 获取评审列表 |
| POST | `/api/v5/repos/{owner}/{repo}/pulls/{number}/reviews` | 提交评审 |
| POST | `/api/v5/repos/{owner}/{repo}/pulls/{number}/reviews/{id}/events` | 提交评审事件（APPROVE/REQUEST_CHANGES） |
| GET | `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments` | 获取评论列表 |
| POST | `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments` | 创建行级评论 |

#### POST /api/v5/repos/{owner}/{repo}/pulls/{number}/reviews

**请求体：**
```json
{
  "body": "代码质量良好，建议补充单元测试",
  "event": "APPROVE",
  "comments": [
    {
      "path": "src/main.py",
      "position": 5,
      "body": "建议添加异常处理"
    }
  ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `body` | string | ❌ | 评审总结评论 |
| `event` | string | ❌ | `APPROVE`、`REQUEST_CHANGES`、`COMMENT` |
| `comments` | array | ❌ | 行级评论列表 |

---

### 2.3 冲突检测

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/pulls/{number}/merge` | 获取合并可行性状态 |

**响应：**
```json
{
  "mergeable": true,
  "mergeable_state": "clean",
  "base_commit": "sha...",
  "head_commit": "sha..."
}
```

| 字段 | 说明 |
|---|---|
| `mergeable` | 是否可自动合并 |
| `mergeable_state` | `clean`（无冲突）、`conflict`（有冲突）、`unknown`（检测中） |

---

## 3. 枚举值

### 3.1 MR 状态
| 值 | 说明 |
|---|---|
| `open` | 打开状态 |
| `closed` | 已关闭 |
| `merged` | 已合并 |
| `all` | 查询时返回全部 |

### 3.2 合并策略
| 值 | 说明 |
|---|---|
| `merge` | 普通合并，保留分支历史 |
| `squash` | 压缩提交后合并 |
| `rebase` | 变基合并 |

### 3.3 评审事件
| 值 | 说明 |
|---|---|
| `APPROVE` | 批准合并 |
| `REQUEST_CHANGES` | 请求修改 |
| `COMMENT` | 仅评论，不影响合并状态 |

### 3.4 可合并状态
| 值 | 说明 |
|---|---|
| `clean` | 无冲突，可合并 |
| `conflict` | 存在冲突 |
| `unknown` | 正在检测中 |
| `blocked` | 被规则阻止（如 CI 未通过） |

---

## 4. 配置示例

### 4.1 创建 MR（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/pulls \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Feature: add user auth",
    "head": "feature/auth",
    "base": "main",
    "body": "## 变更\n- 添加 OAuth2 登录\n- 添加 JWT 验证",
    "reviewers": ["reviewer1"]
  }'
```

### 4.2 审批 MR（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/pulls/42/reviews \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "body": "LGTM",
    "event": "APPROVE"
  }'
```

### 4.3 执行合并（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/pulls/42/merge \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "merge_method": "squash",
    "commit_title": "feat: add user auth (#42)"
  }'
```
