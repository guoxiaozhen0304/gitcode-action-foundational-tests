# SEC-WCMD-01-002

- **标题**: 跨运行 artifact 必须被视为不可信数据
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**跨运行 artifact 必须被视为不可信数据**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-029

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_status, equals=completed

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Download untrusted artifa | `download-artifact` |  | ✅ GENUINE |
| 2 | Do not auto execute | `echo "Artifact downloaded but not executed automatically"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  artifact-trust:
    name: Test artifact trust boundary
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Download untrusted artifact
        uses: download-artifact
        with:
          name: untrusted-artifact
      - name: Do not auto execute
        run: |
          echo "Artifact downloaded but not executed automatically"
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_status | positive | equals=completed | ✅ GENUINE | 状态断言 completed 可被步骤行为验证 |

---