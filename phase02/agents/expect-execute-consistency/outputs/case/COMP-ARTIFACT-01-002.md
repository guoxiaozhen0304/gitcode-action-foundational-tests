# COMP-ARTIFACT-01-002

- **标题**: 下载全部制品功能正常
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**下载全部制品功能正常**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-015

通过标准：
1. type=positive, target=run_status, equals=success
2. type=positive, target=run_logs, contains="app"
3. type=positive, target=run_logs, contains="report"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create artifacts | `mkdir -p dist reports echo "app" > dist/app.txt echo "report" > reports/coverage` |  | ✅ GENUINE |
| 2 | Upload app | `upload-artifact` |  | ✅ GENUINE |
| 3 | Upload reports | `upload-artifact` |  | ✅ GENUINE |
| 4 | Download all | `download-artifact` |  | ✅ GENUINE |
| 5 | Verify all | `cat artifacts/app/app.txt cat artifacts/reports/coverage.txt` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  build:
    name: Build multiple artifacts
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create artifacts
        run: |
          mkdir -p dist reports
          echo "app" > dist/app.txt
          echo "report" > reports/coverage.txt
      - name: Upload app
        uses: upload-artifact
        with:
          name: app
          path: dist/
      - name: Upload reports
        uses: upload-artifact
        with:
          name: reports
          path: reports/
  verify:
    name: Download all artifacts
    runs-on: [ubuntu-latest, x64, small]
    needs: build
    steps:
      - name: Download all
        uses: download-artifact
        with:
          path: artifacts/
      - name: Verify all
        run: |
          cat artifacts/app/app.txt
          cat artifacts/reports/coverage.txt
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
| 2 | run_logs | positive | contains=app | ✅ GENUINE | app: GENUINE |
| 3 | run_logs | positive | contains=report | ✅ GENUINE | report: GENUINE |

---