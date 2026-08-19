# Discussion & Notification 技术规格

> 来源：`gitcode-docs/讨论与通知`（分散于各模块文档）
> 整理日期：2026-08-18
> 覆盖：评论系统、@提及、通知机制、邮件提醒、Webhooks

---

## 1. 功能概述

### 1.1 评论与讨论

GitCode 的评论系统贯穿多个模块，支持：
- **行级评论**：在 MR 的 diff 中针对具体代码行发表评论
- **全局评论**：在 MR/Issue 的讨论区发表评论
- **建议修改（Suggestion）**：在评论中提供可直接应用的代码修改建议
- **回复线程**：评论支持嵌套回复，形成讨论线程
- **@提及**：使用 `@username` 提及用户，触发通知

### 1.2 通知机制

通知渠道包括：
- **站内通知**：GitCode 平台内消息中心
- **邮件通知**：发送至用户注册邮箱
- **Webhooks**：HTTP POST 回调到外部系统

触发通知的事件：
- Issue/MR 被创建、关闭、合并、重新打开
- 被指派为评审人或指派人
- 评论中被 `@提及`
- CI 构建状态变更

### 1.3 Webhooks

仓库可配置 Webhook，在事件发生时向指定 URL 发送 Payload：
- 支持签名验证（`X-GitCode-Signature` 或类似头）
- 支持 SSL 验证
- 支持自定义 Content-Type
- 失败时支持重试（具体策略待确认）

---

## 2. API 端点

### 2.1 评论管理

#### Issue / MR 通用评论

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/issues/{number}/comments` | 获取 Issue 评论 |
| POST | `/api/v5/repos/{owner}/{repo}/issues/{number}/comments` | 创建 Issue 评论 |
| GET | `/api/v5/repos/{owner}/{repo}/issues/comments/{id}` | 获取指定评论 |
| PATCH | `/api/v5/repos/{owner}/{repo}/issues/comments/{id}` | 更新评论 |
| DELETE | `/api/v5/repos/{owner}/{repo}/issues/comments/{id}` | 删除评论 |

> 注：MR 评论与 Issue 评论通常共用同一套接口（`issues` 路径兼容 `pulls`）。

#### 行级评论（Review Comments）

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments` | 获取 MR 行级评论 |
| POST | `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments` | 创建行级评论 |
| GET | `/api/v5/repos/{owner}/{repo}/pulls/comments/{id}` | 获取指定行级评论 |
| PATCH | `/api/v5/repos/{owner}/{repo}/pulls/comments/{id}` | 更新行级评论 |
| DELETE | `/api/v5/repos/{owner}/{repo}/pulls/comments/{id}` | 删除行级评论 |

#### POST /api/v5/repos/{owner}/{repo}/pulls/{number}/comments — 创建行级评论

**请求体：**
```json
{
  "body": "这里应该添加空值检查",
  "commit_id": "abc123def456",
  "path": "src/main.py",
  "position": 42,
  "side": "RIGHT"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `body` | string | ✅ | 评论内容（支持 Markdown） |
| `commit_id` | string | ✅ | 评论针对的 commit SHA |
| `path` | string | ✅ | 文件路径 |
| `position` | integer | ✅ | 文件中的行号（基于 diff） |
| `side` | string | ❌ | `LEFT`（旧版本）或 `RIGHT`（新版本） |
| `line` | integer | ❌ | 绝对行号（与 `position` 二选一） |
| `start_line` | integer | ❌ | 多行评论起始行 |
| `start_side` | string | ❌ | 多行评论起始 side |

---

### 2.2 通知

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/notifications` | 获取当前用户通知列表 |
| PATCH | `/api/v5/notifications` | 标记通知为已读 |
| PUT | `/api/v5/notifications/threads/{id}` | 标记单条通知已读 |
| GET | `/api/v5/notifications/threads/{id}` | 获取单条通知详情 |

#### GET /api/v5/notifications

**查询参数：**
| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `all` | boolean | ❌ | 是否返回已读通知，默认 `false` |
| `participating` | boolean | ❌ | 仅返回参与的通知 |
| `since` | string | ❌ | 起始时间（ISO 8601） |
| `before` | string | ❌ | 截止时间（ISO 8601） |
| `per_page` | integer | ❌ | 每页数量，默认 30，最大 100 |
| `page` | integer | ❌ | 页码 |

**响应示例：**
```json
[
  {
    "id": "notification-uuid-123",
    "repository": { "full_name": "owner/repo" },
    "subject": {
      "title": "Bug: login fails",
      "url": "https://gitcode.com/api/v5/repos/owner/repo/issues/101",
      "latest_comment_url": "...",
      "type": "Issue"
    },
    "reason": "mention",
    "unread": true,
    "updated_at": "2026-08-18T10:00:00Z",
    "last_read_at": null
  }
]
```

---

### 2.3 Webhooks

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/hooks` | 获取 Webhook 列表 |
| POST | `/api/v5/repos/{owner}/{repo}/hooks` | 创建 Webhook |
| GET | `/api/v5/repos/{owner}/{repo}/hooks/{id}` | 获取 Webhook 详情 |
| PATCH | `/api/v5/repos/{owner}/{repo}/hooks/{id}` | 更新 Webhook |
| DELETE | `/api/v5/repos/{owner}/{repo}/hooks/{id}` | 删除 Webhook |
| POST | `/api/v5/repos/{owner}/{repo}/hooks/{id}/tests` | 测试 Webhook |

#### POST /api/v5/repos/{owner}/{repo}/hooks — 创建 Webhook

**请求体：**
```json
{
  "name": "web",
  "active": true,
  "events": ["push", "pull_request", "issues"],
  "config": {
    "url": "https://example.com/webhook",
    "content_type": "json",
    "secret": "webhook-secret-key",
    "insecure_ssl": "0"
  }
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | ✅ | 固定值 `web` |
| `active` | boolean | ❌ | 是否激活，默认 `true` |
| `events` | array | ✅ | 监听事件列表 |
| `config.url` | string | ✅ | 回调 URL |
| `config.content_type` | string | ❌ | `json`（默认）或 `form` |
| `config.secret` | string | ❌ | 签名密钥 |
| `config.insecure_ssl` | string | ❌ | `0`（验证）或 `1`（跳过） |

#### Webhook 事件类型

| 事件名 | 说明 |
|---|---|
| `push` | 代码推送 |
| `pull_request` | MR 创建/更新/合并/关闭 |
| `issues` | Issue 创建/更新/关闭/重新打开 |
| `issue_comment` | Issue/MR 评论 |
| `pull_request_review` | MR 评审提交 |
| `pull_request_review_comment` | MR 行级评论 |
| `release` | Release 创建/发布 |
| `create` | 分支/标签创建 |
| `delete` | 分支/标签删除 |
| `member` | 仓库成员变更 |
| `watch` | 仓库被关注 |
| `fork` | 仓库被 Fork |
| `*` | 监听所有事件 |

---

## 3. 枚举值

### 3.1 通知原因（reason）
| 值 | 说明 |
|---|---|
| `mention` | 被 @提及 |
| `assign` | 被指派 |
| `author` | 自己是作者 |
| `comment` | 有新评论 |
| `invitation` | 收到邀请 |
| `manual` | 手动订阅 |
| `state_change` | 状态变更 |
| `subscribed` | 自动订阅 |
| `team_mention` | 团队被 @提及 |

### 3.2 通知主题类型（subject.type）
| 值 | 说明 |
|---|---|
| `Issue` | Issue |
| `PullRequest` | 合并请求 |
| `Commit` | 提交 |
| `Release` | 发布 |

### 3.3 Webhook Content-Type
| 值 | 说明 |
|---|---|
| `json` | `application/json` |
| `form` | `application/x-www-form-urlencoded` |

---

## 4. 配置示例

### 4.1 创建 Issue 评论（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/issues/101/comments \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"body": "问题已确认，正在修复中。cc @manager"}'
```

### 4.2 创建 MR 行级评论（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/pulls/42/comments \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "body": "建议添加类型检查",
    "commit_id": "abc123def456",
    "path": "src/app.py",
    "position": 15,
    "side": "RIGHT"
  }'
```

### 4.3 获取未读通知（curl）
```bash
curl -X GET "https://gitcode.com/api/v5/notifications?all=false&per_page=30" \
  -H "Authorization: Bearer <TOKEN>"
```

### 4.4 标记所有通知已读（curl）
```bash
curl -X PATCH https://gitcode.com/api/v5/notifications \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"read": true}'
```

### 4.5 创建 Webhook（curl）
```bash
curl -X POST https://gitcode.com/api/v5/repos/owner/repo/hooks \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "web",
    "active": true,
    "events": ["push", "pull_request", "issues"],
    "config": {
      "url": "https://jenkins.example.com/gitcode-webhook/",
      "content_type": "json",
      "secret": "my-secret-key",
      "insecure_ssl": "0"
    }
  }'
```

### 4.6 Webhook Payload 签名验证示例（Python）
```python
import hmac
import hashlib

def verify_signature(payload_body, secret, signature_header):
    """验证 Webhook 签名"""
    expected = 'sha256=' + hmac.new(
        secret.encode(),
        payload_body,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature_header)
```
