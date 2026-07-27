# SEC-FORK-01-002

- 标题: fork PR 中 secrets 引用返回空值且 job 不崩溃
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   SEC-FORK-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-001
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    SEC-FORK-01-001
标题:      fork PR 中 secrets 引用返回空值且 job 不崩溃

前置条件:
  - 仓库配置了 secret API_KEY
  - 存在一个来自外部 fork 的 PR

操作步骤:
  1. 以 fork 贡献者身份提交一个将 secrets.API_KEY 注入环境变量的 workflow
  2. 在 fork PR 场景下触发该 workflow

预期结果:
  - secrets.API_KEY 返回空字符串，环境变量未设置
  - job 正常完成，不因 secret 不可访问而失败

验证点:
  - [负向] 环境变量 API_KEY 为空或未定义
  - [正向] job 状态为成功完成

清理:      重置 fixture 仓库

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Check env empty | run: if [ -z "$API_KEY" ]; then echo "API_KEY is empty as expected"; else echo "API_KEY is not empty"; exit 1; fi | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  test-empty:
    name: Test empty secret
    runs-on: [ubuntu-latest, x64, small]
    env:
      API_KEY: ${{ secrets.API_KEY }}
    steps:
      - name: Check env empty
        run: |
          if [ -z "$API_KEY" ]; then
            echo "API_KEY is empty as expected"
          else
            echo "API_KEY is not empty"
            exit 1
          fi
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
| [负向] 环境变量 API_KEY 为空或未定义 | ✅ COVERED | 步骤通过 `if [ -z "$API_KEY" ]` 真实检测变量是否为空，env 层使用 `${{ secrets.API_KEY }}` 注入，断言 `must_not_contain_secret` 验证 secret 值不泄露 |
| [正向] job 状态为成功完成 | ✅ COVERED | 步骤包含真实条件分支：为空则正常输出，非空则 `exit 1` 故意失败；断言 `run_status equals success` 验证 fork 场景下 secret 为空时 job 成功 |

### 问题

无。两个验证点均被步骤真实覆盖。

## 5. 评级理由

步骤使用 `if [ -z "$API_KEY" ]` 真实条件逻辑和 `exit 1` 失败路径，第0层的 `${{ secrets.API_KEY }}` 表达式在 fork PR 场景下的求值行为即为被测功能本身。所有验证点均 COVERED。
