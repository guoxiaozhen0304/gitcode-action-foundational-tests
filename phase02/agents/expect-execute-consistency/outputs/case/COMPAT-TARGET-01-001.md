# COMPAT-TARGET-01-001

- **标题**: pull_request_target 默认 checkout 应为 base 分支而非 head 分支
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request_target 默认 checkout 应为 base 分支而非 head 分支**

- 触发事件: `pull_request_target`
- 规格引用: INTENT-COMPAT-032

通过标准：
1. type=negative, target=run_logs, eval=llm_assisted
2. type=positive, target=run_logs, eval=llm_assisted
3. type=positive, target=run_status, equals=success, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | checkout source | `checkout` |  | ✅ GENUINE |
| 2 | print sha info | `echo "Current SHA: ${{ atomgit.sha }}" echo "Base SHA: ${{ atomgit.event.pull_re` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request_target:
    branches: [main]
jobs:
  check-sha:
    name: Verify checkout base sha
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: checkout source
        uses: checkout
      - name: print sha info
        run: |
          echo "Current SHA: ${{ atomgit.sha }}"
          echo "Base SHA: ${{ atomgit.event.pull_request.base.sha }}"
          echo "Head SHA: ${{ atomgit.event.pull_request.head.sha }}"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `pull_request_target` |
| 触发身份 | `untrusted_contributor` |
| Repo 环境 | `with-fork-pr` |
| Secrets | `['DEPLOY_TOKEN']` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_status | positive | equals=success | ✅ GENUINE | 存在真实可执行步骤，有行为观测价值 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---