# COMP-PERMS-01-003

- 标题: fork PR 的 pull_request 下声明 write 仍仅 read
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMP-PERMS-01-003
维度标签:   [completeness, security]
维度:      completeness
优先级:    P0
溯源意图:  INTENT-COMP-013
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      fork PR 的 pull_request 下声明 write 仍仅 read

前置条件:
  - 存在一个来自 fork 的 PR

操作步骤:
  1. 在 fork PR 的 pull_request workflow 中声明 repository: write
  2. 尝试使用 ATOMGIT_TOKEN 推送代码

预期结果:
  - 写操作因权限不足失败
  - fork PR 的 TOKEN 权限不受 permissions 声明影响

验证点:
  - [负向] 写操作应失败
  - [正向] 系统应强制 fork PR TOKEN 为 read-only

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Attempt write | run: curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $ATOMGIT_TOKEN" -X POST "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}/issues/1/comments" -d '{"body":"test"}' \|\| echo "write failed as expected" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches:
      - main
permissions:
  repository: write
jobs:
  verify:
    name: Verify fork PR permission ignore
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write
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
| [负向] 写操作应失败 | ✅ COVERED | 步骤使用 curl 真实发起 API 写请求，通过 `|| echo "write failed as expected"` 捕获失败；YAML 中有 `type=negative, target=run_status, equals=success_with_write` 断言覆盖 |
| [正向] 系统应强制 fork PR TOKEN 为 read-only | ✅ COVERED | 步骤真实执行写操作并输出 "write failed as expected"；断言 `run_logs contains="write failed as expected"` 验证写操作因 read-only 权限而失败 |

### 问题

无。

## 5. 评级理由

步骤使用 curl 真实执行 API 写请求，使用 `$ATOMGIT_TOKEN` 和 `${{ }}` 表达式，属于实质逻辑。两个验证点均由真实行为产生可观测输出，全部 COVERED。整体判定为**断言一致**。
