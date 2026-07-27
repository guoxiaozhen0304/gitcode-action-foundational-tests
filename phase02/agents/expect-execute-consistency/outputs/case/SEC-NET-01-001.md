# SEC-NET-01-001

- **标题**: Runner 网络出站必须受控，防止 SSRF 与内网跳板
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner 网络出站必须受控，防止 SSRF 与内网跳板**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-023

通过标准：
1. type=negative, target=run_logs
2. type=positive, target=run_logs, equals=access_denied_or_timeout

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Access metadata endpoint | `curl -s --max-time 5 http://169.254.169.254/ || echo "access denied or timeout"` |  | ✅ GENUINE |
| 2 | Access internal IP | `curl -s --max-time 5 http://192.168.1.1/ || echo "access denied or timeout"` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  ssrf-test:
    name: Test SSRF prevention
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Access metadata endpoint
        run: |
          curl -s --max-time 5 http://169.254.169.254/ || echo "access denied or timeout"
      - name: Access internal IP
        run: |
          curl -s --max-time 5 http://192.168.1.1/ || echo "access denied or timeout"
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
| 2 | run_logs | positive | equals=access_denied_or_timeout | ✅ GENUINE | 日志断言无特定字符串匹配要求 |

---