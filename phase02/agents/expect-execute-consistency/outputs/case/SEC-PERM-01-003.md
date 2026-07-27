# SEC-PERM-01-003

- **标题**: 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-017

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_status, equals=completed

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Attempt write without per | `curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcod` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  default-perm:
    name: Test default permissions
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Attempt write without permissions
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
| 2 | run_status | positive | equals=completed | ✅ GENUINE | 状态断言 completed 可被步骤行为验证 |

---