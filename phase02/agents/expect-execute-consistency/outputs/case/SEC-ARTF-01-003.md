# SEC-ARTF-01-003

- **标题**: 宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载
- **维度**: 安全性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**宽通配打包含敏感文件名的 artifact 绝不应在无警示情况下静默成功且可被无痕下载**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-045

通过标准：
1. type=negative, target=run_logs
2. type=negative, target=artifact_download
3. type=nonfunctional, target=documentation, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Create placeholder sensit | `echo "placeholder-not-a-real-secret" > .env.fixture echo "placeholder-credential` |  | ✅ GENUINE |
| 2 | Upload workspace with wid | `upload-artifact` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  artifact-hygiene:
    name: Wide glob artifact upload check
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Create placeholder sensitive named files
        run: |
          echo "placeholder-not-a-real-secret" > .env.fixture
          echo "placeholder-credential" > credentials.fixture
      - name: Upload workspace with wide glob
        uses: upload-artifact
        with:
          name: workspace-bundle
          path: .
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-sensitive-files` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | artifact_download | negative |  | ✅ GENUINE | 通用断言匹配 |
| 3 | documentation | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---