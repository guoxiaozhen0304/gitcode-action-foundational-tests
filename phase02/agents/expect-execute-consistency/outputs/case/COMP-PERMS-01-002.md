# COMP-PERMS-01-002

- **标题**: 声明 repository write 后 TOKEN 可推送代码
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**声明 repository write 后 TOKEN 可推送代码**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-013

通过标准：
1. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Push code | `git config user.email "test@test.com" git config user.name "Test" echo "change" ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions:
  repository: write
jobs:
  verify:
    name: Verify write permission
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Push code
        run: |
          git config user.email "test@test.com"
          git config user.name "Test"
          echo "change" >> README.md
          git add README.md
          git commit -m "test"
          git push https://x-access-token:$ATOMGIT_TOKEN@${{ atomgit.server_url }}/${{ atomgit.repository }}.git HEAD:${{ atomgit.ref }}
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

---