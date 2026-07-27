# SEC-LOG-01-001

- **标题**: 无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-040

通过标准：
1. type=positive, target=log_api, equals=authorized_download_ok
2. type=negative, target=log_api
3. type=negative, target=log_api

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Emit log content | `echo "LOG_ACCESS_CONTROL_FIXTURE: log content produced"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  log-producer:
    name: Produce run logs
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Emit log content
        run: |
          echo "LOG_ACCESS_CONTROL_FIXTURE: log content produced"
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
| 1 | log_api | positive | equals=authorized_download_ok | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | log_api | negative |  | ✅ GENUINE | 通用断言匹配 |
| 3 | log_api | negative |  | ✅ GENUINE | 通用断言匹配 |

---