# COMPAT-PERM-01-001

- **标题**: 未声明 permissions 时默认 TOKEN 读操作权限范围
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**未声明 permissions 时默认 TOKEN 读操作权限范围**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-002

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, contains="README"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | read repo file | `cat README.md` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-read:
    name: Test default read permissions
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: read repo file
        run: |
          cat README.md
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
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | contains=README | ✅ GENUINE | README: GENUINE |

---