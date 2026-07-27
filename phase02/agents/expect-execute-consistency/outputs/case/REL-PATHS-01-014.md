# REL-PATHS-01-014

- **标题**: paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效**

- 触发事件: `push`
- 规格引用: INTENT-REL-014

通过标准：
1. type=positive, target=run_status, equals=completed(success)

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo triggered | `echo triggered by paths` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
    paths:
      - 'src/**'
jobs:
  test:
    name: paths trigger test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo triggered
        run: |
          echo triggered by paths
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
| 1 | run_status | positive | equals=completed(success) | ✅ GENUINE | 状态断言 completed(success) 可被步骤行为验证 |

---