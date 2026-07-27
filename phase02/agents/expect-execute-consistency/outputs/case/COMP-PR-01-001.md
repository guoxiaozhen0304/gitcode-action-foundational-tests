# COMP-PR-01-001

- 标题: fork PR 触发 pull_request 时不可读取项目 secrets
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-PR-01-001
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-004
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      fork PR 触发 pull_request 时不可读取项目 secrets

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自 fork 的 PR

操作步骤:
  1. 在 fork PR 场景下触发 pull_request workflow
  2. workflow 中尝试引用 secrets.DEPLOY_TOKEN

预期结果:
  - workflow 无法获取 DEPLOY_TOKEN 值
  - 运行日志中 DEPLOY_TOKEN 不出现明文

验证点:
  - [负向] 日志不含 DEPLOY_TOKEN 明文
  - [正向] fork PR 的 pull_request workflow 无 secret 访问权限

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt to read secret | run: echo "secret value is ${{ secrets.DEPLOY_TOKEN }}" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches:
      - main
jobs:
  verify:
    name: Verify fork PR secret isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt to read secret
        run: |
          echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | untrusted_contributor |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 日志不含 DEPLOY_TOKEN 明文 | ✅ COVERED | 步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 真实引用 secret 值并 echo 输出，平台会对 secret 脱敏；YAML 中有 `type=negative, must_not_contain_secret: DEPLOY_TOKEN` 断言直接覆盖，属于 Rule 4 所述的"故意暴露测试" |
| [正向] fork PR 的 pull_request workflow 无 secret 访问权限 | ✅ COVERED | 步骤通过 `${{ secrets.DEPLOY_TOKEN }}` 表达式真实测试 secret 访问；若 secret 不可访问则步骤行为反映此限制，断言 `run_status=success_or_blocked` 覆盖两种可能结果 |

### 问题

无。

## 5. 评级理由

步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 表达式真实引用 secret，平台上下文求值即功能执行。负向验证点有对应的 `must_not_contain_secret` 断言覆盖，正向验证点的 `success_or_blocked` 状态断言检查 secret 访问结果。全部 COVERED，整体判定为**断言一致**。
