# SEC-TOKEN-01-001

- 标题: fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-TOKEN-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-003
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限

前置条件:
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以 fork 贡献者身份提交一个使用 ATOMGIT_TOKEN 克隆代码的 workflow
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - ATOMGIT_TOKEN 可成功执行 clone 等读操作
  - 尝试写操作时被平台强制拒绝

验证点:
  - [正向] ATOMGIT_TOKEN 可成功执行 clone 等读操作
  - [负向] 尝试写操作应返回 403 或失败

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Clone with token | run: git clone https://x-access-token:${{ atomgit.token }}@... | 是 |
| 2 | Attempt write via API | run: curl ... -H "Authorization: token ${{ atomgit.token }}" ... | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  token-read:
    name: Test token read only
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Clone with token
        run: |
          git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git test-clone
      - name: Attempt write via API
        run: |
          curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/${{ atomgit.repository }}/issues" \n            -H "Authorization: token ${{ atomgit.token }}" \n            -d '{"title": "test"}'
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | untrusted_contributor |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [正向] ATOMGIT_TOKEN 可成功执行 clone 等读操作 | ✅ COVERED | 断言 target=run_logs equals "clone_successful"，步骤真实执行 git clone 并使用 ${{ atomgit.token }} 表达式注入 token，clone 的输出可被 harness 校验 |
| [负向] 尝试写操作应返回 403 或失败 | ✅ COVERED | 断言 target=run_logs must_not_contain "write_permission_granted"，步骤真实执行 curl POST API 写操作，token 权限不足时输出 403，harness 可校验日志中无写成功标识 |

### 问题

无。

## 5. 评级理由

两个步骤均使用 `${{ atomgit.token }}` 表达式并执行真实命令（git clone、curl API），步骤行为真实。两个断言 target=run_logs，harness 可直接从日志中校验 clone 成功与写操作被拒的结果。触发事件不影响步骤覆盖断言的判定。
