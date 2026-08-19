# Repository / Project 技术规格

> 来源：`gitcode-docs/项目.md` + `gitcode-docs/项目/*`> 整理日期：2026-08-18
> 覆盖：项目创建、分支管理、保护分支、成员权限、LFS、Release、Wiki

---

## 1. 功能概述

GitCode 项目是代码托管的核心单元，支持：
- **版本控制**：Git 仓库的创建、克隆、推送、分支管理
- **协作**：多成员协作、代码审查、合并请求
- **问题跟踪**：Issue 创建与管理
- **发布管理**：Release、Tag 管理
- **扩展**：LFS 大文件、Wiki、Pages

### 1.1 成员角色及权限

| 角色 | 权限范围 | 说明 |
|---|---|---|
| `Owner` | 全部控制权限（删除项目、更改信息、管理成员） | 项目创建者或组织继承 |
| `Maintainer` | 管理项目设置、合并请求、保护分支 | 组织项目可从组织继承 |
| `Developer` | 查看并提交更改，不可删除项目 | 可 push 代码、创建 MR |
| `Reporter` | 查看项目内容，不可提交更改 | 只读权限 |

> 注：个人用户的项目不支持邀请其他用户成为管理员；组织项目只支持从组织继承管理员。

### 1.2 分支保护规则

保护分支可配置以下规则：
- `force_push`：是否允许强制推送
- `allow_push`：允许推送的用户/角色
- `allow_merge`：允许合并的用户/角色
- `require_ci_pass`：是否要求 CI 检查通过
- `require_review`：是否要求代码评审通过

---

## 2. API 端点

### 2.1 项目管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/user/repos` | 获取当前用户项目列表 |
| GET | `/api/v5/users/{username}/repos` | 获取指定用户项目列表 |
| GET | `/api/v5/orgs/{org}/repos` | 获取组织项目列表 |
| POST | `/api/v5/user/repos` | 创建新项目 |
| GET | `/api/v5/repos/{owner}/{repo}` | 获取项目详情 |
| PATCH | `/api/v5/repos/{owner}/{repo}` | 更新项目信息 |
| DELETE | `/api/v5/repos/{owner}/{repo}` | 删除项目 |
| POST | `/api/v5/repos/{owner}/{repo}/forks` | Fork 项目 |

#### POST /api/v5/user/repos — 创建项目

**请求体（Body）：**
```json
{
  "name": "project-name",
  "description": "项目描述",
  "private": false,
  "auto_init": true,
  "gitignore_template": "Python",
  "license_template": "mit"
}
```

**字段说明：**
| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | ✅ | 项目名称（仅字母、数字、-、_） |
| `description` | string | ❌ | 项目描述 |
| `private` | boolean | ❌ | 是否私有，默认 `false` |
| `auto_init` | boolean | ❌ | 是否初始化 README，默认 `false` |
| `gitignore_template` | string | ❌ | .gitignore 模板名称 |
| `license_template` | string | ❌ | 开源协议模板 |

**响应示例：**
```json
{
  "id": 12345,
  "name": "project-name",
  "full_name": "owner/project-name",
  "private": false,
  "html_url": "https://gitcode.com/owner/project-name",
  "clone_url": "https://gitcode.com/owner/project-name.git",
  "default_branch": "main",
  "created_at": "2026-08-18T10:00:00Z",
  "updated_at": "2026-08-18T10:00:00Z"
}
```

---

### 2.2 分支管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/branches` | 获取分支列表 |
| GET | `/api/v5/repos/{owner}/{repo}/branches/{branch}` | 获取分支详情 |
| POST | `/api/v5/repos/{owner}/{repo}/branches` | 创建新分支 |
| DELETE | `/api/v5/repos/{owner}/{repo}/git/refs/heads/{branch}` | 删除分支 |

#### POST /api/v5/repos/{owner}/{repo}/branches — 创建分支

**请求体：**
```json
{
  "branch_name": "feature-x",
  "ref": "main"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `branch_name` | string | ✅ | 新分支名称 |
| `ref` | string | ✅ | 基于哪个分支/提交创建 |

---

### 2.3 保护分支

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/protected_branches` | 获取保护分支列表 |
| GET | `/api/v5/repos/{owner}/{repo}/protected_branches/{branch}` | 获取保护分支规则 |
| PUT | `/api/v5/repos/{owner}/{repo}/protected_branches/{branch}` | 设置/更新保护分支规则 |
| DELETE | `/api/v5/repos/{owner}/{repo}/protected_branches/{branch}` | 解除分支保护 |

#### PUT /api/v5/repos/{owner}/{repo}/protected_branches/{branch}

**请求体：**
```json
{
  "force_push": false,
  "allow_push_roles": ["Maintainer", "Owner"],
  "allow_merge_roles": ["Maintainer", "Owner"],
  "require_ci_pass": true,
  "require_review_count": 1
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `force_push` | boolean | ❌ | 是否允许强制推送，默认 `false` |
| `allow_push_roles` | array | ❌ | 允许推送的角色列表 |
| `allow_merge_roles` | array | ❌ | 允许合并的角色列表 |
| `require_ci_pass` | boolean | ❌ | 是否要求 CI 通过 |
| `require_review_count` | integer | ❌ | 要求的最小评审人数 |

---

### 2.4 成员管理

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/collaborators` | 获取项目成员列表 |
| PUT | `/api/v5/repos/{owner}/{repo}/collaborators/{username}` | 添加/更新成员 |
| DELETE | `/api/v5/repos/{owner}/{repo}/collaborators/{username}` | 移除成员 |

#### PUT /api/v5/repos/{owner}/{repo}/collaborators/{username}

**请求体：**
```json
{
  "permission": "Developer"
}
```

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `permission` | string | ✅ | 角色：`Owner`、`Maintainer`、`Developer`、`Reporter` |

---

### 2.5 Tags & Releases

| Method | Endpoint | 描述 |
|---|---|---|
| GET | `/api/v5/repos/{owner}/{repo}/tags` | 获取标签列表 |
| GET | `/api/v5/repos/{owner}/{repo}/releases` | 获取 Release 列表 |
| GET | `/api/v5/repos/{owner}/{repo}/releases/{id}` | 获取 Release 详情 |
| POST | `/api/v5/repos/{owner}/{repo}/releases` | 创建 Release |
| DELETE | `/api/v5/repos/{owner}/{repo}/releases/{id}` | 删除 Release |

#### POST /api/v5/repos/{owner}/{repo}/releases

**请求体：**
```json
{
  "tag_name": "v1.0.0",
  "name": "First Release",
  "body": "Release notes...",
  "draft": false,
  "prerelease": false,
  "target_commitish": "main"
}
```

---

### 2.6 LFS 大文件存储

| Method | Endpoint | 描述 |
|---|---|---|
| POST | `/api/v5/repos/{owner}/{repo}/lfs/objects` | 创建 LFS 对象 |
| GET | `/api/v5/repos/{owner}/{repo}/lfs/objects/{oid}` | 获取 LFS 对象信息 |

LFS 操作主要通过 Git 命令行 + LFS 服务器完成，API 仅用于对象管理。

---

## 3. 枚举值

### 3.1 项目可见性
| 值 | 说明 |
|---|---|
| `public` | 公开项目 |
| `private` | 私有项目 |
| `internal` | 组织内可见（如支持） |

### 3.2 成员角色
| 值 | 权限级别 |
|---|---|
| `Owner` | 最高权限 |
| `Maintainer` | 管理权限 |
| `Developer` | 开发权限 |
| `Reporter` | 只读权限 |

### 3.3 分支保护 — 允许推送/合并角色
| 值 | 说明 |
|---|---|
| `Owner` | 仅仓库所有者 |
| `Maintainer` | 维护者及以上 |
| `Developer` | 开发者及以上 |
| `No one` | 禁止直接推送/合并（仅通过 MR） |

---

## 4. 配置示例

### 4.1 创建项目（curl）
```bash
curl -X POST https://gitcode.com/api/v5/user/repos \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "smoke-test-project",
    "description": "冒烟测试 fixture",
    "private": false,
    "auto_init": true
  }'
```

### 4.2 设置保护分支（curl）
```bash
curl -X PUT https://gitcode.com/api/v5/repos/owner/repo/protected_branches/main \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "force_push": false,
    "require_ci_pass": true,
    "require_review_count": 1
  }'
```

### 4.3 添加项目成员（curl）
```bash
curl -X PUT https://gitcode.com/api/v5/repos/owner/repo/collaborators/username \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"permission": "Developer"}'
```
