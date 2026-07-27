# SEC-DOS-01-001

- **标题**: 大 artifact / 大 cache 必须受配额与边界限制
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**大 artifact / 大 cache 必须受配额与边界限制**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-033

通过标准：
1. type=negative, target=run_status
2. type=positive, target=run_logs, equals=size_limit_exceeded_error

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create large file | `dd if=/dev/zero of=large.bin bs=1M count=1100` |  | ✅ GENUINE |
| 2 | Upload large artifact | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  quota-test:
    name: Test size quota
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create large file
        run: |
          dd if=/dev/zero of=large.bin bs=1M count=1100
      - name: Upload large artifact
        uses: upload-artifact
        with:
          name: large-artifact
          path: large.bin
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
| 2 | run_logs | positive | equals=size_limit_exceeded_error | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---