# COMP-ACT-01-002

- **标题**: 含连字符 input_id 的 INPUT_ 环境变量命名裁定
- **维度**: 完备性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**含连字符 input_id 的 INPUT_ 环境变量命名裁定**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-027

通过标准：
1. [正向] 大写化与空格转换与文档一致 —— 断言 run_status=success
2. [正向/记录] 含连字符 input_id 的实际环境变量名逐字记录 —— 断言 run_logs must_contain INPUT_DRY
3. [非功能] 同一 input_id 经 with 传参与环境变量两条路径取值一致 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Call with hyphenated input | `uses: ./.gitcode/actions/hyphen-input` with: dry-run: "yes" | - | action 内部枚举并输出 INPUT_DRY* 环境变量 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | local-action-hyphen |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | uses: 调用本地 action，真实执行 |
| 2 | run_logs | positive | must_contain: INPUT_DRY | ✅ GENUINE | action 内部脚本输出环境变量名，真实来源于平台上下文转换 |
| 3 | env_naming | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

