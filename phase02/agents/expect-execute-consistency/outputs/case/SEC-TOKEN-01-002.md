# SEC-TOKEN-01-002

- **标题**: fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝**

- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-003

通过标准：
1. type=negative, target=run_logs, equals=push_denied_or_403
2. type=positive, target=run_status, equals=completed

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt push | `git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.re` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    branches: [main]
jobs:
  token-write-denied:
    name: Test token write denied
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt push
        run: |
          git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git repo
          cd repo
          echo test > test.txt
          git add test.txt
          git commit -m "test"
          git push origin main || echo "push denied"
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
| 1 | run_logs | negative | equals=push_denied_or_403 | ✅ GENUINE | 日志断言无特定字符串匹配要求 |
| 2 | run_status | positive | equals=completed | ✅ GENUINE | 状态断言 completed 可被步骤行为验证 |

---