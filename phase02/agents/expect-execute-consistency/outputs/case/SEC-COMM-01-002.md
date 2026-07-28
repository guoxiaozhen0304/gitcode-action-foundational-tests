# SEC-COMM-01-002
- **标题**: 引用/反讽/代码块内嵌指令文本绝不应造成 pull_request_comment 预期外触发
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
trigger_audit 抽象断言（equals 字面值）改为显式 llm_assisted + rubric，明确判读内容与依据。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_trigger | positive | equals exact_command_triggers | ✅ COVERED | 精确指令触发可判定 |
| 2 | run_trigger | negative | must_not_equal triggered_by_quoted_or_embedded_text | ✅ COVERED | 边界评论不应触发 |
| 3 | trigger_audit | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 触发记录可回溯性属平台审计判读 |

### 残留问题
触发记录可回溯到评论内容的判定保留 llm_assisted（rubric 已明确）。
