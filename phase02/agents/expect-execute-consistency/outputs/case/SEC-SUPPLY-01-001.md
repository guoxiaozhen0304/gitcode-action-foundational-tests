# SEC-SUPPLY-01-001

- **标题**: 第三方 Action 引用应支持完整 commit hash 固定
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**第三方 Action 引用应支持完整 commit hash 固定**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-014

通过标准：
1. type=positive, target=run_status, equals=success_or_action_executed
2. type=negative, target=run_logs

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Use pinned action | `docker/build-push-action@1234567890abcdef1234567890abcdef12345678` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  hash-pin:
    name: Test commit hash pinning
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Use pinned action
        uses: docker/build-push-action@1234567890abcdef1234567890abcdef12345678
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
| 1 | run_status | positive | equals=success_or_action_executed | ✅ GENUINE | 状态断言 success_or_action_executed 可被步骤行为验证 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---