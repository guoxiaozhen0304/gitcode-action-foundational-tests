# REL-YAMLCACHE-01-060

- **标题**: Workflow YAML 缓存失效——修改后无旧代码残留
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**Workflow YAML 缓存失效——修改后无旧代码残留**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-060

通过标准：
1. type=positive, target=run_logs, contains="marker_v2"
2. type=negative, target=run_logs, contains="marker_v1"

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | echo marker | `echo marker_v1` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: YAML cache invalidation test
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo marker
        run: |
          echo marker_v1
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
| 1 | run_logs | positive | contains=marker_v2 | ❌ MISSING_SOURCE | marker_v2: MISSING_SOURCE (无步骤产出此字符串) |
| 2 | run_logs | negative | contains=marker_v1 | ❌ VACUOUS | marker_v1: VACUOUS (步骤仅 echo，未执行功能) |

### 问题

**断言 1 — MISSING_SOURCE**❌: marker_v2: MISSING_SOURCE (无步骤产出此字符串)

**断言 2 — VACUOUS**❌: marker_v1: VACUOUS (步骤仅 echo，未执行功能)

---