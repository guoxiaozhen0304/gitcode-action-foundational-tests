# SEC-PERM-01-001

- **标题**: 显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-016

通过标准：
1. type=positive, target=run_logs, equals=read_operations_successful
2. type=negative, target=run_logs

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
jobs:
  perm-read:
    name: Test permissions read only
    runs-on: [ubuntu-latest, x64, small]
    permissions:
      repository: read
      pr: none
      issue: none
      note: none
      project: none
      hook: none
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
| 1 | run_logs | positive | equals=read_operations_successful | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---