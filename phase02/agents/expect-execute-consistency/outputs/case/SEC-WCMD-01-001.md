# SEC-WCMD-01-001

- **标题**: Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-028

通过标准：
1. type=negative, target=run_logs, must_not_contain_secret="API_KEY"
2. type=positive, target=run_logs, equals=mask_command_without_payload

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Mask secret | `echo "::add-mask::${{ secrets.API_KEY }}"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  add-mask-test:
    name: Test add-mask response
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Mask secret
        run: |
          echo "::add-mask::${{ secrets.API_KEY }}"
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
| 2 | run_logs | positive | equals=mask_command_without_payload | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---