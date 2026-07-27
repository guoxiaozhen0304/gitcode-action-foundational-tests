# SEC-SUPPLY-01-002

- **标题**: commit hash 不匹配时第三方 Action 应被拒绝执行
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**commit hash 不匹配时第三方 Action 应被拒绝执行**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-014

通过标准：
1. type=negative, target=run_status
2. type=positive, target=run_logs, equals=action_not_found_or_sha_mismatch

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use invalid hash action | `docker/build-push-action@0000000000000000000000000000000000000000` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  hash-mismatch:
    name: Test hash mismatch rejection
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Use invalid hash action
        uses: docker/build-push-action@0000000000000000000000000000000000000000
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
| 1 | run_status | negative |  | ✅ GENUINE | 状态断言  可被步骤行为验证 |
| 2 | run_logs | positive | equals=action_not_found_or_sha_mismatch | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---