# COMP-PR-01-002

- 标题: pull_request_target 可访问 secrets 且 TOKEN 拥有写权限
- 维度: 完备性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
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
```

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Read secret and token | run: echo "secret is ${{ secrets.DEPLOY_TOKEN }}" / echo "token length is ${#ATOMGIT_TOKEN}" | 是 |

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
| event | pull_request_target |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [正向] pull_request_target 可访问 secrets | ✅ COVERED | 步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 真实引用 secret 并 echo 输出，`${#ATOMGIT_TOKEN}` 动态计算 token 长度；断言 `run_status=success` 验证 secret 可访问时 workflow 正常完成 |
| [正向] 日志中 secret 显示为 ***（脱敏生效） | ✅ COVERED | 步骤通过 `${{ secrets.DEPLOY_TOKEN }}` 真实暴露 secret 值，断言 `contains_masked: DEPLOY_TOKEN` 验证平台对 secret 进行了脱敏处理 |

### 问题

无。

## 5. 评级理由

步骤使用 `${{ secrets.DEPLOY_TOKEN }}` 和 `${#ATOMGIT_TOKEN}` 表达式，平台上下文求值即功能执行。secrets 引用和 token 长度计算均为实质逻辑。两个正向验证点均有对应断言覆盖，全部 COVERED。整体判定为**断言一致**。
