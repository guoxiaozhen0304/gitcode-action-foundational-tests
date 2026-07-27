# REL-NEST-01-024

- **标题**: workflow_call 嵌套越界——3 层嵌套调用应被拒绝
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**workflow_call 嵌套越界——3 层嵌套调用应被拒绝**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-024

通过标准：
1. type=positive, target=run_status, equals=completed(failure)
2. type=positive, target=run_logs, contains="嵌套"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  call_level1:
    name: call level 1 workflow
    uses: ./.gitcode/workflows/level1_deep.yml
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
| 1 | run_status | positive | equals=completed(failure) | ✅ GENUINE | 状态断言 completed(failure) 可被步骤行为验证 |
| 2 | run_logs | positive | contains=嵌套 | ❌ MISSING_SOURCE | 嵌套: MISSING_SOURCE (无步骤产出此字符串) |

### 问题

**断言 2 — MISSING_SOURCE**❌: 嵌套: MISSING_SOURCE (无步骤产出此字符串)

---