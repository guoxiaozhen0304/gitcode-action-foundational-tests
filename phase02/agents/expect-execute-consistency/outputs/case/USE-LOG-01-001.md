# USE-LOG-01-001

- 标题: 多 step 日志按时间线组织且边界清晰
- 维度: 易用性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-LOG-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-017
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      多 step 日志按时间线组织且边界清晰

前置条件:
  - workflow 含多个 steps

操作步骤:
  1. 触发一个含 5 个以上 steps 的 workflow
  2. 在日志面板查看组织方式

预期结果:
  step 按定义顺序排列，含时间戳前缀，长输出可折叠

验证点:
  - [正向] 日志面板中 step 按定义顺序排列，step 内 shell 输出内容（如 "prepare done"）可在 run_logs 中检索到
  - [非功能] 用户能在 3 秒内定位到失败 step

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | step one prepare (multi-step) | echo "prepare done"  | VACUOUS |
| 2 | step two build (multi-step) | echo "build done"  | VACUOUS |
| 3 | step three test (multi-step) | echo "test done"  | GENUINE |
| 4 | step four package (multi-step) | echo "package done"  | VACUOUS |
| 5 | step five summary (multi-step) | echo "summary done"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 日志面板中 step 按定义顺序排列，step 内 shell 输出内容（如 "prepare done"）可在 run_logs 中检索到 | 空洞 | no step produces 'step one prepare' |
| 用户能在 3 秒内定位到失败 step | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | step one prepare | MISSING_SOURCE | no step produces 'step one prepare' |
| 2 | ui_layout | nonfunctional | 在 UI 上，用户能在 3 秒内定位到失败的 step（通过视觉层级、颜色或状态 | LLM_DEPENDENT | LLM/nonfunctional assertion: 在 UI 上，用户能在 3 秒内定位到失败的 step（通过视觉层级、颜色或状态图标区分）；日志下载文 |

### 问题

- 验证点 `日志面板中 step 按定义顺序排列，step 内 shell 输出内容（如 "prepare done"）可在 run_logs 中检索到` → 空洞: no step produces 'step one prepare'

- 断言 `[positive] run_logs` → MISSING_SOURCE: no step produces 'step one prepare'

---
