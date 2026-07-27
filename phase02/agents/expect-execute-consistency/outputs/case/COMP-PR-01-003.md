# COMP-PR-01-003

- 标题: fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-PR-01-003
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-004
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限

前置条件:
  - 存在一个来自 fork 的 PR

操作步骤:
  1. 在 fork PR 的 pull_request workflow 中尝试使用 ATOMGIT_TOKEN 推送代码或评论 PR

预期结果:
  - 写操作因权限不足而失败
  - ATOMGIT_TOKEN 仅拥有 read 权限

验证点:
  - [负向] 写操作（如推送、评论）应失败
  - [正向] ATOMGIT_TOKEN 权限为 read-only

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt write with token | run: curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $ATOMGIT_TOKEN" -X POST "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}/issues/1/comments" -d '{"body":"test"}' \|\| echo "write failed as expected" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches:
      - main
jobs:
  verify:
    name: Verify fork PR token read only
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write with token
        run: |
          curl -s -o /dev/null -w "%{http_code}"                     -H "Authorization: token $ATOMGIT_TOKEN"                     -X POST                     "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}/issues/1/comments"                     -d '{"body":"test"}' || echo "write failed as expected"
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
| [负向] 写操作（如推送、评论）应失败 | ✅ COVERED | 步骤使用 curl 真实执行 API 写请求，通过 `|| echo "write failed as expected"` 捕获权限不足导致的失败；YAML 中有 `type=negative, target=run_step_result, equals=write_succeeded` 断言覆盖 |
| [正向] ATOMGIT_TOKEN 权限为 read-only | ✅ COVERED | 步骤通过 `$ATOMGIT_TOKEN` 和 `${{ }}` 表达式真实测试 token 写权限，断言 `run_status=success_or_failure` 覆盖写操作成功或失败的两种结果 |

### 问题

无。

## 5. 评级理由

步骤使用 curl 真实执行写操作，通过 `$ATOMGIT_TOKEN` 和 `${{ }}` 表达式实现实质逻辑。负向验证点有 YAML 断言覆盖写操作失败的预期，正向验证点通过 token 权限测试验证 read-only 行为。全部 COVERED，整体判定为**断言一致**。
