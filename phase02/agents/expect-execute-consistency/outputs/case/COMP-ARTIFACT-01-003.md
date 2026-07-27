# COMP-ARTIFACT-01-003

- **标题**: artifact 保留期设置生效
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**artifact 保留期设置生效**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-015

通过标准：
1. type=positive, target=artifact_available, equals=yes_within_retention
2. type=negative, target=artifact_available_after_expiry, equals=no_after_1_day

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create artifact | `echo "temp" > temp.txt` |  | ❌ VACUOUS |
| 2 | Upload artifact | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  upload:
    name: Upload with short retention
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create artifact
        run: |
          echo "temp" > temp.txt
      - name: Upload artifact
        uses: upload-artifact
        with:
          name: temp-artifact
          path: temp.txt
          retention-days: 1
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
| 1 | artifact_available | positive | equals=yes_within_retention | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | artifact_available_after_expiry | negative | equals=no_after_1_day | ✅ GENUINE | 断言有条件可被步骤验证 |

---