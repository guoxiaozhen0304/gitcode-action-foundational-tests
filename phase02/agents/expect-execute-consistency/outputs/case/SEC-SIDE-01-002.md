# SEC-SIDE-01-002

- **标题**: Secret 不经 artifact 侧信道绕过脱敏外泄
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Secret 不经 artifact 侧信道绕过脱敏外泄**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-032

通过标准：
1. type=negative, target=artifact_content, must_not_contain_secret="DEPLOY_TOKEN"
2. type=positive, target=run_status, equals=blocked_or_masked

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write secret to file | `echo "token=${{ secrets.DEPLOY_TOKEN }}" > secret.txt` |  | ✅ GENUINE |
| 2 | Upload artifact | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  side-artifact:
    name: Test secret in artifact
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write secret to file
        run: |
          echo "token=${{ secrets.DEPLOY_TOKEN }}" > secret.txt
      - name: Upload artifact
        uses: upload-artifact
        with:
          name: secret-artifact
          path: secret.txt
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_content | negative | !secret=DEPLOY_TOKEN | ✅ GENUINE | 步骤使用 DEPLOY_TOKEN，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | run_status | positive | equals=blocked_or_masked | ✅ GENUINE | 状态断言 blocked_or_masked 可被步骤行为验证 |

---