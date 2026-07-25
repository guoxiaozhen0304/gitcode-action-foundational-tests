# COMP-BOUND-01-085

- 标题: cron 表达式格式与位置边界验证
- 维度: 完备性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 配置 schedule 的 cron 使用各种合法符号
2. 验证平台接受合法 cron

预期结果:
- cron 五段式格式正确，支持 * 任意值 , 列表 - 范围 / 步长，分钟/小时/日/月/星期位置正确

验证点:
- [正向] 含 * 的 cron 通过校验
- [正向] 含 , 的 cron 通过校验
- [正向] 含 - 和 / 的 cron 通过校验

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ok | echo "cron_boundary_ok" | 否 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-BOUND-01-085
dimensions: [completeness]
dimension: completeness
priority: P1
title: cron 表达式格式与位置边界验证
intent_ref: KEEP-TC-475~512
setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default
fault_injection: null
workflow: |
  on:
    schedule:
      - cron: "*/5 * * * *"
      - cron: "0 2,14 * * *"
      - cron: "0 9-17 * * 1-5"
  jobs:
    verify:
      name: Verify cron boundary
      runs-on: [dedicate-hosted, x64, large]
      steps:
        - name: Echo ok
          run: |
            echo "cron_boundary_ok"
trigger:
  event: schedule
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_status
    equals: success
  - type: positive
    target: run_logs
    must_contain: cron_boundary_ok
teardown:
  reset: fixture
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | schedule |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |
| 阻塞 | schedule 触发不可控，无法在单次测试中验证 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 含 * 的 cron 通过校验 | ❌ BLOCKED | schedule 触发无法在测试环境中即时验证 |
| [正向] 含 , 的 cron 通过校验 | ❌ BLOCKED | 同上 |
| [正向] 含 - 和 / 的 cron 通过校验 | ❌ BLOCKED | 同上 |

### 问题

- 触发事件为 schedule，无法在可控的测试环境中即时执行和验证
- 步骤仅有 echo，无实质 cron 校验逻辑

---
