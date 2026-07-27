# REL-POST-01-001

- **标题**: post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-083

通过标准：
1. type=positive, target=conclusion_matches_documented_semantics, equals=true
2. type=positive, target=post_failure_attribution_visible, equals=true
3. type=negative, target=silent_post_swallow_detected, equals=true
4. type=negative, target=post_hang_beyond_timeout_detected, equals=true

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | main step | `echo "main_ok_marker"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  main_ok:
    name: main success job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: main step
        run: |
          echo "main_ok_marker"
post:
  run_always: true
  steps:
    - name: post notify step
      run: |
        echo "post_executed_marker"
        exit 1
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
| 1 | conclusion_matches_documented_semantics | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | post_failure_attribution_visible | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | silent_post_swallow_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 4 | post_hang_beyond_timeout_detected | negative | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |

---