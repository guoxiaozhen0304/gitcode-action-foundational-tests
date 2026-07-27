# USE-CLI-01-001

- **标题**: Runner 无 gh 等效 CLI 时迁移指引的替代方案说明
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner 无 gh 等效 CLI 时迁移指引的替代方案说明**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-045

通过标准：
1. type=positive, target=run_logs, eval=deterministic
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | probe cli commands | `command -v gh || echo "gh=NOTFOUND" command -v gitcode || echo "gitcode=NOTFOUND` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: cli availability probe
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: probe cli commands
        run: |
          command -v gh || echo "gh=NOTFOUND"
          command -v gitcode || echo "gitcode=NOTFOUND"
          command -v atomgit || echo "atomgit=NOTFOUND"
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
| 1 | run_logs | positive | eval=deterministic | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---