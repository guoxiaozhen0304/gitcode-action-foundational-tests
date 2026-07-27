# SEC-ARTF-01-002

- **标题**: 跨仓库 artifact 下载返回 403 或 404
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**跨仓库 artifact 下载返回 403 或 404**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-019

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=403_or_404

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt download fork art | `curl -s -o /dev/null -w "%{http_code}" \n            "https://api.gitcode.com/ap` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  artifact-download:
    name: Download artifact from main repo
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt download fork artifact
        run: |
          curl -s -o /dev/null -w "%{http_code}" \n            "https://api.gitcode.com/api/v8/repos/${{ atomgit.repository }}/actions/artifacts/FORK_ARTIFACT_ID/zip?access_token=${{ atomgit.token }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-artifacts` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | positive | equals=403_or_404 | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---