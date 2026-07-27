# SEC-NAME-01-004

- **标题**: 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-041

通过标准：
1. type=positive, target=job_env, equals=system_var_integrity_preserved
2. type=negative, target=job_env

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Verify system variable in | `echo "SYSTEM_VAR_CHECK: comparing system variable values against platform inject` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  shadow-check:
    name: System variable shadowing check
    runs-on: [ubuntu-latest, x64, small]
    env:
      ATOMGIT_ENV: /tmp/fixture-shadow-path
    steps:
      - name: Verify system variable integrity
        run: |
          echo "SYSTEM_VAR_CHECK: comparing system variable values against platform injected values"
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
| 1 | job_env | positive | equals=system_var_integrity_preserved | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | job_env | negative |  | ✅ GENUINE | 通用断言匹配 |

---