# SEC-TOKEN-01-004

- **标题**: 残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**残留于 cache/artifact 的 token 在新 run 中绝不应通过鉴权**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-037

通过标准：
1. type=positive, target=run_logs, equals=current_run_token_operational
2. type=negative, target=api_response

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt auth with residua | `echo "RESIDUAL_TOKEN_AUTH_ATTEMPT: harness supplies residual token from prior ru` |  | ❌ VACUOUS |
| 2 | Confirm current run token | `echo "CURRENT_RUN_TOKEN_CHECK: in scope read with own token"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  residue-check:
    name: Residual token must not authenticate
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt auth with residual token
        run: |
          echo "RESIDUAL_TOKEN_AUTH_ATTEMPT: harness supplies residual token from prior run artifact"
      - name: Confirm current run token works
        run: |
          echo "CURRENT_RUN_TOKEN_CHECK: in scope read with own token"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-artifacts` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals=current_run_token_operational | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | api_response | negative |  | ✅ GENUINE | 通用断言匹配 |

---