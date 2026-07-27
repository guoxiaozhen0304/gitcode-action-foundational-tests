# SEC-TOKEN-01-003

- **标题**: run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-037

通过标准：
1. type=positive, target=run_logs, equals=in_run_token_operational
2. type=negative, target=api_response
3. type=nonfunctional, target=rerun_behavior, equals=new_token_issued_or_explicit_reuse

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use token for in scope re | `git ls-remote https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgi` |  | ✅ GENUINE |
| 2 | Emit in run marker | `echo "IN_RUN_TOKEN_OPERATIONAL: token worked within scope during run"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  token-lifecycle:
    name: Check token validity during run
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Use token for in scope read
        run: |
          git ls-remote https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git HEAD
      - name: Emit in run marker
        run: |
          echo "IN_RUN_TOKEN_OPERATIONAL: token worked within scope during run"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals=in_run_token_operational | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | api_response | negative |  | ✅ GENUINE | 通用断言匹配 |
| 3 | rerun_behavior | nonfunctional | equals=new_token_issued_or_explicit_reuse | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---