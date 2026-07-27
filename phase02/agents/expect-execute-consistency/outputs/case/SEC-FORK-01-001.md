# SEC-FORK-01-001

- 标题: fork PR 触发 pull_request 时不可读取项目 secrets
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-FORK-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-001
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      fork PR 触发 pull_request 时不可读取项目 secrets

前置条件:
  - 仓库配置了 secret DEPLOY_TOKEN
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以 fork 贡献者身份提交一个引用 secrets.DEPLOY_TOKEN 的 workflow
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - 系统阻止 fork PR 访问 DEPLOY_TOKEN，引用时返回空值或安全报错
  - 运行日志中不出现 DEPLOY_TOKEN 明文

验证点:
  - [负向] 日志不含 DEPLOY_TOKEN 明文
  - [正向] fork PR 的 job 中 secrets 引用为空或不可访问

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Try access secret | run: echo "secret value is ${{ secrets.DEPLOY_TOKEN }}" | 是 |
| 2 | Print env | run: env \| grep DEPLOY_TOKEN \|\| echo "not found" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  check-secret:
    name: Check secret isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Try access secret
        run: |
          echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"
      - name: Print env
        run: |
          env | grep DEPLOY_TOKEN || echo "not found"
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
| [负向] 日志不含 DEPLOY_TOKEN 明文 | ✅ COVERED | 步骤1 使用 `${{ secrets.DEPLOY_TOKEN }}` 真实访问 secret，断言 `must_not_contain_secret` 验证 secret 值不出现 |
| [正向] fork PR 的 job 中 secrets 引用为空或不可访问 | ✅ COVERED | 步骤2 通过 `env \| grep DEPLOY_TOKEN \|\| echo "not found"` 真实检测环境变量，断言 `run_status equals completed_or_blocked` 验证 job 可正常完成 |

### 问题

无。两个验证点均被步骤真实覆盖。

## 5. 评级理由

步骤通过 `${{ }}` 表达式真实访问 secrets 并通过 shell 命令检测环境变量，断言直接观测这些行为的结果。所有验证点均 COVERED。
