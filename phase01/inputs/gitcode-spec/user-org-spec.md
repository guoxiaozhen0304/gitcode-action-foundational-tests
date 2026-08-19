# User & Organization 技术规格

> 来源：`gitcode-docs/用户/*` + `gitcode-docs/组织.md`
> 整理日期：2026-08-18
> 覆盖：用户认证、PAT 令牌、组织管理、成员角色、权限继承

---

## 1. 功能概述

### 1.1 用户认证

GitCode 支持以下认证方式：
- **OAuth2 授权码模式**：第三方应用获取用户授权
- **Personal Access Token（PAT）**：个人访问密钥，用于脚本/API 调用
- **SSH 密钥**：Git 操作鉴权
- **用户名密码**：Web 登录（不推荐用于 API）

PAT 是 API 调用的主要凭证，支持：
- 配置权限范围（scope）限制访问
- 设置过期时间
- 代替密码进行 HTTPS Git 操作（`https://oauth2:<token>@gitcode.com/...`）

### 1.2 组织（Organization）

组织是多人协作的顶层容器，特点：
- 可创建多个项目仓库
- 成员角色继承到组织下的所有项目
- 支持团队（Team）作为成员组，批量分配权限
- 个人项目**不支持**邀请外部管理员；组织项目权限仅从组织继承

### 1.3 成员角色

| 角色 | 权限范围 | 适用场景 |
|---|---|---|
| `Owner` | 全部控制权限（删除、设置、成员管理） | 组织创建者/仓库创建者 |
| `Maintainer` | 管理设置、合并请求、保护分支 | 组织项目可从组织继承 |
| `Developer` | 查看并提交更改，不可删除项目 | 普通开发人员 |
| `Reporter` | 查看项目内容，不可提交更改 | 只读访客 |

---

## 2. API 端点

### 2.1 用户管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/user` | 获取当前用户信息 |
| GET | `/api/v5/users/{username}` | 获取指定用户信息 |
| PATCH | `/api/v5/user` | 更新当前用户信息 |
| GET | `/api/v5/user/followers` | 获取当前用户粉丝列表 |
| GET | `/api/v5/user/following` | 获取当前用户关注列表 |
| PUT | `/api/v5/user/following/{username}` | 关注用户 |
| DELETE | `/api/v5/user/following/{username}` | 取消关注 |

#### GET /api/v5/user — 获取当前用户

**响应示例：**
```json
{
  "id": 12345,
  "login": "username",
  "name": "Display Name",
  "email": "user@example.com",
  "avatar_url": "https://gitcode.com/avatar/12345",
  "html_url": "https://gitcode.com/username",
  "type": "User",
  "created_at": "2025-01-01T00:00:00Z"
}
```

### 2.2 组织管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/user/orgs` | 获取当前用户所属组织 |
| GET | `/api/v5/orgs/{org}` | 获取组织信息 |
| GET | `/api/v5/orgs/{org}/members` | 获取组织成员列表 |
| GET | `/api/v5/orgs/{org}/teams` | 获取组织团队列表 |
| GET | `/api/v5/orgs/{org}/repos` | 获取组织项目列表 |

#### GET /api/v5/orgs/{org} — 获取组织信息

**响应示例：**
```json
{
  "id": 67890,
  "login": "my-org",
  "name": "My Organization",
  "description": "Organization description",
  "html_url": "https://gitcode.com/my-org",
  "avatar_url": "https://gitcode.com/avatar/67890",
  "type": "Organization",
  "created_at": "2025-06-01T00:00:00Z"
}
```

### 2.3 组织成员与团队

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/orgs/{org}/members/{username}` | 获取成员在组织中的角色 |
| PUT | `/api/v5/orgs/{org}/memberships/{username}` | 更新成员角色 |
| DELETE | `/api/v5/orgs/{org}/members/{username}` | 移除成员 |
| GET | `/api/v5/teams/{id}` | 获取团队信息 |
| GET | `/api/v5/teams/{id}/members` | 获取团队成员列表 |
| GET | `/api/v5/teams/{id}/repos` | 获取团队有权访问的仓库 |

#### PUT /api/v5/orgs/{org}/memberships/{username}

**请求体：**
```json
{
  "role": "admin"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `role` | string | ✅ | `admin`（Owner 级）或 `member`（普通成员） |

---

### 2.4 密钥与授权

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/user/keys` | 获取用户 SSH 公钥列表 |
| POST | `/api/v5/user/keys` | 添加 SSH 公钥 |
| DELETE | `/api/v5/user/keys/{id}` | 删除 SSH 公钥 |

#### POST /api/v5/user/keys

**请求体：**
```json
{
  "title": "Work Laptop",
  "key": "ssh-ed25519 AAAAC3NzaC... user@host"
}
```

---

## 3. 枚举值

### 3.1 用户类型
| 值 | 说明 |
|---|---|
| `User` | 个人用户 |
| `Organization` | 组织 |
| `Bot` | 机器人账号 |

### 3.2 组织成员角色
| 值 | 说明 |
|---|---|
| `admin` | 管理员（Owner 级权限） |
| `member` | 普通成员 |

### 3.3 仓库成员权限
| 值 | 说明 |
|---|---|
| `Owner` | 全部权限 |
| `Maintainer` | 管理权限（设置、MR、保护分支） |
| `Developer` | 开发权限（push、创建 MR） |
| `Reporter` | 只读权限 |

### 3.4 PAT 权限范围（Scopes）
| Scope | 说明 |
|---|---|
| `repo` | 仓库完全控制 |
| `repo:status` | 仓库状态读写 |
| `repo_deployment` | 部署状态读写 |
| `public_repo` | 公开仓库访问 |
| `admin:repo_hook` | 仓库 Webhook 管理 |
| `admin:org` | 组织管理 |
| `user` | 用户信息读写 |
| `read:user` | 用户信息只读 |
| `issues` | Issue 管理 |
| `pull_requests` | MR/PR 管理 |
| `delete_repo` | 删除仓库 |
| `write:packages` | 包上传 |
| `read:packages` | 包下载 |
| `admin:gpg_key` | GPG 密钥管理 |
| `admin:ssh_key` | SSH 密钥管理 |

---

## 4. 配置示例

### 4.1 获取当前用户信息（curl）
```bash
curl -X GET https://gitcode.com/api/v5/user \
  -H "Authorization: Bearer <TOKEN>"
```

### 4.2 获取组织成员列表（curl）
```bash
curl -X GET https://gitcode.com/api/v5/orgs/my-org/members \
  -H "Authorization: Bearer <TOKEN>"
```

### 4.3 添加 SSH 公钥（curl）
```bash
curl -X POST https://gitcode.com/api/v5/user/keys \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "CI Server",
    "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAID... ci@server"
  }'
```

### 4.4 更新组织成员角色（curl）
```bash
curl -X PUT https://gitcode.com/api/v5/orgs/my-org/memberships/username \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"role": "admin"}'
```

### 4.5 使用 PAT 进行 Git 操作
```bash
# Clone 私有仓库
git clone https://oauth2:<TOKEN>@gitcode.com/owner/repo.git

# Push 代码
git push https://oauth2:<TOKEN>@gitcode.com/owner/repo.git main
```
