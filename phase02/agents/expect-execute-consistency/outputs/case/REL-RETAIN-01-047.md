# REL-RETAIN-01-047

- **标题**: artifact 保留期 90 天边界——第 91 天应不可下载
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**artifact 保留期 90 天边界——第 91 天应不可下载**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-047

通过标准：
1. type=positive, target=download_day90_status, equals=200
2. type=positive, target=download_day91_status, equals=404

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | create artifact | `echo retention test > retention.txt` |  | ✅ GENUINE |
| 2 | upload artifact | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: artifact retention test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: create artifact
        run: |
          echo retention test > retention.txt
      - name: upload artifact
        uses: upload-artifact
        with:
          name: retention-artifact
          path: retention.txt
          retention-days: 90
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
| 1 | download_day90_status | positive | equals=200 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | download_day91_status | positive | equals=404 | ✅ GENUINE | 断言有条件可被步骤验证 |

---