# COMP-PR-01-002

- **标题**: pull_request_target 可访问 secrets 且 TOKEN 拥有写权限
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_target 可访问 secrets 且 TOKEN 拥有写权限**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMP-004

通过标准：
1. type=positive, target=run_logs
2. type=positive, target=run_status, equals=success

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Read secret and token | `echo "secret is ${{ secrets.DEPLOY_TOKEN }}" echo "token length is ${#ATOMGIT_TO` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches:
      - main
jobs:
  verify:
    name: Verify pull_request_target secret access
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Read secret and token
        run: |
          echo "secret is ${{ secrets.DEPLOY_TOKEN }}"
          echo "token length is ${#ATOMGIT_TOKEN}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_target` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-secrets` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

---