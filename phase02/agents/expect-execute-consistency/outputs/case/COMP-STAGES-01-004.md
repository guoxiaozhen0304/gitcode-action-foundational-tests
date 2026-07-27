# COMP-STAGES-01-004
- **标题**: map 形式 stages 按定义顺序串行执行（回归保护）
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**map 形式 stages 按定义顺序串行执行（回归保护）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-019
通过标准：
1. 两个 stage 的 job 均运行成功并输出标记（正向）
2. stage 按定义顺序串行，日志时间戳可证（正向）
3. 不应出现 stage 顺序被打乱或全部并行且无说明（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark stage one | `echo "STAGE_ONE_DONE"` | - | STAGE_ONE_DONE |
| 2 | Mark stage two | `echo "STAGE_TWO_DONE"` | - | STAGE_TWO_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 所有步骤仅 echo 字面量，无 if/uses/${{ }}/实质命令 |
| 2 | run_logs | positive | must_contain: STAGE_ONE_DONE | ❌ VACUOUS | 步骤仅 echo 字面量，未验证 stage 顺序语义 |
| 3 | run_logs | positive | must_contain: STAGE_TWO_DONE | ❌ VACUOUS | 步骤仅 echo 字面量，未验证 stage 顺序语义 |
| 4 | stage_order | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估日志时间戳确认串行语义 |
### 问题
**断言 2,3 — VACUOUS**: 步骤仅 echo 了字面量字符串，未执行任何验证 stage 顺序的实质逻辑。要验证串行语义，应输出实际时间戳或计数器，而非固定字面量。
---
