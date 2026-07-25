# COMP-PR-01-002

- 标题: pull_request_target 可访问 secrets 且 TOKEN 拥有写权限
- 维度: 完备性 | 优先级: P0
- 评级: 完全不符

---

## 1. 想测什么（规格）

用例 ID:   COMP-PR-01-002
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-004
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      pull_request_target 可访问 secrets 且 TOKEN 拥有写权限

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自 fork 的 PR

操作步骤:
  1. 在 fork PR 场景下触发 pull_request_target workflow
  2. workflow 中引用 secrets.DEPLOY_TOKEN

预期结果:
  - workflow 能获取 DEPLOY_TOKEN（日志中脱敏显示为 ***）
  - ATOMGIT_TOKEN 拥有写权限

验证点:
  - [正向] pull_request_target 可访问 secrets
  - [正向] 日志中 secret 显示为 ***（脱敏生效）

清理:      重置 fixture 仓库


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Read secret and token | run: echo "secret is ${{ secrets.DEPLOY_TOKEN }}"
echo "token length is ${#ATOMGIT_TOKEN}"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches:
      - main
jobs:
  verify:
    name: Verify pull_request_target secret access
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Read secret and token
        run: |
          echo "secret is ${{ secrets.DEPLOY_TOKEN }}"
          echo "token length is ${#ATOMGIT_TOKEN}"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo Fixture | with-secrets |
| Secrets | DEPLOY_TOKEN |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] pull_request_target 可访问 secrets | 🚫 BLOCKED | trigger=pull_request_target, trigger=pull_request_target |
| [正向] 日志中 secret 显示为 ***（脱敏生效） | 🚫 BLOCKED | trigger=pull_request_target, trigger=pull_request_target |

### 问题

- [正向] pull_request_target 可访问 secrets: BLOCKED - trigger=pull_request_target, trigger=pull_request_target
- [正向] 日志中 secret 显示为 ***（脱敏生效）: BLOCKED - trigger=pull_request_target, trigger=pull_request_target

---
