# COMP-PERMS-01-002

- 标题: 声明 repository write 后 TOKEN 可推送代码
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMP-PERMS-01-002
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-013
参照来源:  inputs/gitcode-spec/
母意图:    —
标题:      声明 repository write 后 TOKEN 可推送代码

前置条件:
  - 仓库具备写权限测试条件

操作步骤:
  1. 配置 permissions: repository: write
  2. 使用 ATOMGIT_TOKEN 推送代码

预期结果:
  - 写操作成功

验证点:
  - [正向] 推送代码成功返回 200/201

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Push code | run: git config user.email "test@test.com"
git config user.name "Test"
echo "change" >> README.md
git add README.md
git commit -m "test"
git push https://x | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions:
  repository: write
jobs:
  verify:
    name: Verify write permission
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Push code
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
| [正向] 推送代码成功返回 200/201 | ✅ COVERED | steps have real logic |

### 问题

无

---
