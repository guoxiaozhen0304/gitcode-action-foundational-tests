# COMP-ARTIFACT-01-001

- **标题**: artifact 可在同 workflow 的 job 间正确传递
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**artifact 可在同 workflow 的 job 间正确传递**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-015

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, contains="hello artifact"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create artifact | `mkdir -p dist echo "hello artifact" > dist/app.txt` |  | ✅ GENUINE |
| 2 | Upload artifact | `upload-artifact` |  | ✅ GENUINE |
| 3 | Download artifact | `download-artifact` |  | ✅ GENUINE |
| 4 | Verify content | `cat dist/app.txt` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  build:
    name: Build and upload
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create artifact
        run: |
          mkdir -p dist
          echo "hello artifact" > dist/app.txt
      - name: Upload artifact
        uses: upload-artifact
        with:
          name: app-dist
          path: dist/
  verify:
    name: Download and verify
    runs-on: [ubuntu-latest, x64, small]
    needs: build
    steps:
      - name: Download artifact
        uses: download-artifact
        with:
          name: app-dist
          path: dist/
      - name: Verify content
        run: |
          cat dist/app.txt
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
| 1 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |
| 2 | run_logs | positive | contains=hello artifact | ✅ GENUINE | hello artifact: GENUINE |

---