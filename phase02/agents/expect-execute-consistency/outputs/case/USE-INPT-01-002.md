# USE-INPT-01-002
- **标题**: 使用 boolean 类型 input 时报错应提示仅支持 string
- **维度**: 易用性/兼容性
- **评级**: 部分不符

## 想测什么
验证 workflow_dispatch inputs 声明 type: boolean 时平台应报错并明确说明 GitCode 仅支持 string 类型，不应静默降级。

## 做了什么
workflow 声明一个 boolean 类型的 dry_run input，step 引用 `${{ inputs.dry_run }}`。期望平台在 YAML 校验阶段拒绝此写法。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | boolean 类型应触发校验失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错说明仅支持 string 并给转换指引 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
