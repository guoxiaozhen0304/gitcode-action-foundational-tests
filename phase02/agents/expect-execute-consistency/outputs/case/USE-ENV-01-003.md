# USE-ENV-01-003

- **标题**: ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-044

通过标准：
1. type=positive, target=run_logs, contains="ATOMGIT_"
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | dump atomgit env vars | `env | grep "^ATOMGIT_" | sort` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: atomgit env injection probe
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: dump atomgit env vars
        run: |
          env | grep "^ATOMGIT_" | sort
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
| 1 | run_logs | positive | contains=ATOMGIT_ | ✅ GENUINE | ATOMGIT_: GENUINE |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---