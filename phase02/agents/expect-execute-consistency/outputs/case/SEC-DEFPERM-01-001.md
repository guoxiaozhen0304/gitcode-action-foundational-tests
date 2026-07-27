# SEC-DEFPERM-01-001

- **标题**: ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-036

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=403_or_permission_denied

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt write | `curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcod` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
permissions:
  repository: read
jobs:
  inherit-test:
    name: Test permission inheritance
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write
        run: |
          curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/${{ atomgit.repository }}/issues" \n            -H "Authorization: token ${{ atomgit.token }}" \n            -d '{"title": "test"}'
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
| 1 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | positive | equals=403_or_permission_denied | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---