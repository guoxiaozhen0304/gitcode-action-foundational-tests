# COMPAT-PERM-01-002

- **标题**: 未声明 permissions 时 fork PR 写操作隔离
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**未声明 permissions 时 fork PR 写操作隔离**

- 触发事件: `fork_pr`
- 规格引用: INTENT-COMPAT-002

通过标准：
1. type=negative, target=run_status, equals=success
2. type=negative, target=run_logs

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | attempt write | `git config user.email "test@example.com" git config user.name "Test" echo "test"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test-write:
    name: Test fork write isolation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: attempt write
        run: |
          git config user.email "test@example.com"
          git config user.name "Test"
          echo "test" > test_file.txt
          git add test_file.txt
          git commit -m "test commit"
          git push origin HEAD
```

</details>

## 3. 触发与运行环境

| 触发事件 | `fork_pr` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---