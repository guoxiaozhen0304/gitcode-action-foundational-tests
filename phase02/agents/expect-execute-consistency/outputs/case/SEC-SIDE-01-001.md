# SEC-SIDE-01-001

- **标题**: Secret 不经 output 侧信道绕过脱敏外泄
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Secret 不经 output 侧信道绕过脱敏外泄**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-032

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="API_KEY"
2. type=negative, target=step_output, must_not_contain_secret="API_KEY"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Write secret to output | `echo "result=${{ secrets.API_KEY }}" >> $ATOMGIT_OUTPUT` |  | ✅ GENUINE |
| 2 | Check output masked | `echo "output is ${{ steps.step1.outputs.result }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  side-output:
    name: Test secret in output
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Write secret to output
        id: step1
        run: |
          echo "result=${{ secrets.API_KEY }}" >> $ATOMGIT_OUTPUT
      - name: Check output masked
        run: |
          echo "output is ${{ steps.step1.outputs.result }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['API_KEY']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | !secret=API_KEY | ✅ GENUINE | 步骤使用 API_KEY，secret 脱敏断言有验证对象（故意暴露测试） |
| 2 | step_output | negative | !secret=API_KEY | ✅ GENUINE | 步骤使用 API_KEY，secret 脱敏断言有验证对象（故意暴露测试） |

---