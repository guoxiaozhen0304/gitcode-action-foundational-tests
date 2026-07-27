# COMP-ACT-01-001

- **标题**: action inputs.required 未传参时平台不自动校验
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**action inputs.required 未传参时平台不自动校验**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-026

通过标准：
1. [正向] workflow 不在调度层失败（运行可进入 action 执行）—— 断言 run_status=success
2. [正向] action 内读取到该输入对应环境变量为空值 —— 断言 run_logs must_contain REQ_INPUT_EMPTY
3. [非功能] 若平台后续加入校验，文档与行为需同步 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Call without required input | `uses: ./.gitcode/actions/req-check` | - | action 内部输出 REQ_INPUT_EMPTY |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | local-action-required |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | uses: 调用本地 action，action 内部执行真实逻辑 |
| 2 | run_logs | positive | must_contain: REQ_INPUT_EMPTY | ✅ GENUINE | action 内部脚本检测到空环境变量后输出该字符串 |
| 3 | nonfunctional | - | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过，非自动化可判定 |

