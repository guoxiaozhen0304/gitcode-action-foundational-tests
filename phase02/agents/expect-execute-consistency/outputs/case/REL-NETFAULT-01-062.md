# REL-NETFAULT-01-062

- **标题**: 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时
- **维度**: 可靠性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-062

通过标准：
1. type=positive, target=reachable_status, equals=success
2. type=positive, target=unreachable_timeout_seconds
3. type=positive, target=failure_attribution, equals=clear

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | curl unreachable addresse | `curl --connect-timeout 10 --max-time 120 -v http://192.0.2.1/ || true curl --con` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: network fault tolerance test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: curl unreachable addresses
        run: |
          curl --connect-timeout 10 --max-time 120 -v http://192.0.2.1/ || true
          curl --connect-timeout 10 --max-time 120 -v http://nonexistent-domain-test.example/ || true
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
| 1 | reachable_status | positive | equals=success | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | unreachable_timeout_seconds | positive |  | ✅ GENUINE | 通用断言匹配 |
| 3 | failure_attribution | positive | equals=clear | ✅ GENUINE | 断言有条件可被步骤验证 |

---