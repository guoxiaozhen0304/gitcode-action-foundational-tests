# USE-DOC-01-007

- **标题**: environment 字段能力描述存在而语法参考缺失及平台报错指引
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**environment 字段能力描述存在而语法参考缺失及平台报错指引**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-043

通过标准：
1. type=positive, target=error_message, eval=deterministic
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | marker step | `echo "deploy"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  deploy:
    name: job with environment field
    runs-on: [ubuntu-latest, x64, small]
    environment: production
    steps:
      - name: marker step
        run: |
          echo "deploy"
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
| 1 | error_message | positive | eval=deterministic | ✅ GENUINE | 平台级断言 error_message — 由 harness 在运行时观测 |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---