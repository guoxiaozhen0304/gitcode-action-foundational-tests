# COMP-EXPR-01-059

- **标题**: 未文档化函数 default() 的存在性与求值记录
- **维度**: 完备性
- **优先级**: P2
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**未文档化函数 default() 的存在性与求值记录**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-022

通过标准：
1. [正向/记录] if 引用 default() 的实际求值结果 —— 断言 run_logs must_contain WITNESS_RAN
2. [负向] 未文档化函数不应被静默求值为常量 —— 🔶 LLM_DEPENDENT（跳过）
3. [非功能] 与手动触发表单是否存在联动 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark gated job | `echo "DEFAULT_FN_JOB_RAN"` | (job 级) `if: ${{ default() }}` | 仅当 default() 求值允许 job 运行时输出 |
| 2 | Mark witness | `echo "WITNESS_RAN"` | - | 无条件 witness 输出 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: WITNESS_RAN | ❌ VACUOUS | witness job 仅 echo 字面量字符串，无 if:、无 ${{ }}、无 uses: action。gated job 的 `if: ${{ default() }}` 是真实行为，但其输出 DEFAULT_FN_JOB_RAN 未被断言 |
| 2 | default_fn_eval | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |
| 3 | default_fn_eval | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

### 问题

**断言 1 — VACUOUS**: WITNESS_RAN 来自无条件 witness job 的纯 echo 步骤。真正测试 default() 函数的是 gated job（job 级 if: ${{ default() }}），但该 job 的输出 DEFAULT_FN_JOB_RAN 未被任何断言覆盖。witness 断言未能验证 default() 的行为。

