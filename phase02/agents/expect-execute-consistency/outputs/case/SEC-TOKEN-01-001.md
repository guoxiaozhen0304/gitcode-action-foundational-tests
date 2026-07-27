# SEC-TOKEN-01-001

- **标题**: fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限**

- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-003

通过标准：
1. type=positive, target=run_logs, equals=clone_successful
2. type=negative, target=run_logs

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Clone with token | `git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.re` |  | ✅ GENUINE |
| 2 | Attempt write via API | `curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcod` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  token-read:
    name: Test token read only
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Clone with token
        run: |
          git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git test-clone
      - name: Attempt write via API
        run: |
          curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/${{ atomgit.repository }}/issues" \n            -H "Authorization: token ${{ atomgit.token }}" \n            -d '{"title": "test"}'
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals=clone_successful | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_logs | negative |  | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---