# COMP-PERMS-01-001

- **标题**: permissions 空对象时 ATOMGIT_TOKEN 仅 repository read
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**permissions 空对象时 ATOMGIT_TOKEN 仅 repository read**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-013

通过标准：
1. type=negative, target=run_status, equals=success
2. type=positive, target=run_logs, contains=403

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt write | `git config user.email "test@test.com" git config user.name "Test" echo "change" ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions: {}
jobs:
  verify:
    name: Verify empty permissions
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write
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
| 1 | run_status | negative | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | contains=403 | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---