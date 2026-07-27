# REL-REG-01-001

- **标题**: 新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次**

- 触发事件: `push`
- 规格引用: INTENT-REL-072

通过标准：
1. type=positive, target=run_created, equals=true
2. type=negative, target=run_records_count, equals=0
3. type=nonfunctional, target=registration_delay_seconds
4. type=nonfunctional, target=successful_repo_ratio, equals=3/3

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | probe step | `echo "first_push_registration_probe"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  push:
jobs:
  test:
    name: first registration probe job
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: probe step
        run: |
          echo "first_push_registration_probe"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `fresh-repo` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | positive | equals=true | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | run_records_count | negative | equals=0 | ✅ GENUINE | 断言有条件可被步骤验证 |
| 3 | registration_delay_seconds | nonfunctional |  | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 4 | successful_repo_ratio | nonfunctional | equals=3/3 | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---