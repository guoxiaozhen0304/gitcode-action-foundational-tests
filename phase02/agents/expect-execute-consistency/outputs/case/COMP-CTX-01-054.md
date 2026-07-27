# COMP-CTX-01-054

- **标题**: pull_request 触发下 inputs 上下文求值裁定
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pull_request 触发下 inputs 上下文求值裁定**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-020

通过标准：
1. [正向/记录] inputs.pr_id 的实际求值结果逐字记录 —— 断言 run_logs must_contain INPUT_PR_ID=
2. [负向] 同一引用在不同运行间结果应一致 —— 🔶 LLM_DEPENDENT（跳过）
3. [非功能] 若报错，报错应指明 inputs 不可用 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo inputs reference | `echo "INPUT_PR_ID=${{ inputs.pr_id }}"` | - | 平台在 pull_request 触发下对 inputs.pr_id 的求值结果 |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | pr-default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: INPUT_PR_ID= | ✅ GENUINE | `${{ inputs.pr_id }}` 在非 dispatch 触发下的上下文求值是真实被测行为 |
| 2 | inputs_determinism | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |
| 3 | inputs_eval | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

