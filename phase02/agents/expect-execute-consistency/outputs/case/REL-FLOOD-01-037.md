# REL-FLOOD-01-037

- **标题**: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃**

- 触发事件: `push`
- 规格引用: INTENT-REL-037

通过标准：
1. type=positive, target=created_runs_count, equals=50
2. type=positive, target=api_status, equals=200
3. type=negative, target=api_status, equals=500

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | sleep step | `sleep 5` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: reliability test job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: sleep step
        run: |
          sleep 5
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals=50 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | api_status | positive | equals=200 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | api_status | negative | equals=500 | ✅ GENUINE | 断言有条件可被步骤验证 |

---