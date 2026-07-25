# COMP-PERMS-01-001

- 标题: permissions 空对象时 ATOMGIT_TOKEN 仅 repository read
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-PERMS-01-001
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-013
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      permissions 空对象时 ATOMGIT_TOKEN 仅 repository read

前置条件:
  - 仓库具备写权限测试条件

操作步骤:
  1. 配置 permissions: {}
  2. 尝试使用 ATOMGIT_TOKEN 推送代码

预期结果:
  - 写操作因权限不足失败
  - TOKEN 仅拥有 repository:read 权限

验证点:
  - [正向] permissions: {} 下无法执行写操作
  - [负向] 推送代码应返回 403

清理:      none


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt write | run: git config user.email "test@test.com"
git config user.name "Test"
echo "change" >> README.md
git add README.md
git commit -m "test"
git push https://x | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions: {}
jobs:
  verify:
    name: Verify empty permissions
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write
        run: |
          git config user.email "test@test.com"
          git config user.name "Test"
          echo "change" >> README.md
          git add README.md
          git commit -m "test"
          git push https://x-access-token:$ATOMGIT_TOKEN@${{ atomgit.server_url }}/${{ atomgit.repository }}.git HEAD:${{ atomgit.ref }}

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] permissions: {} 下无法执行写操作 | ✅ COVERED | steps have real logic |
| [负向] 推送代码应返回 403 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
