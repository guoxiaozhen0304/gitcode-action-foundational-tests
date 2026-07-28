# COMPAT-SHELL-01-003
- **标题**: Windows runner 默认 shell 差异
- **维度**: 兼容性
- **评级**: 部分不符

## 想测什么
验证Windows Runner上默认shell是否正常执行Windows命令。

## 做了什么
workflow配置 `runs-on: [windows-latest, x64, small]`，step输出 `echo %OS%` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive llm | "默认shell正确执行Windows命令" | VACUOUS | 若windows-latest不支持(RUNSON-005/006同理)，workflow不会调度到Windows Runner，%OS%命令永远不会执行(R4★)；即使调度成功，`echo %OS%`为Windows cmd语法，在Linux bash上执行会输出字面量`%OS%`而非OS名，无法验证Windows默认shell行为 |
| 2 | run_logs | positive llm | "若默认shell不是powershell应有明确说明" | COVERED | 若平台无Windows Runner则在error_message/解析阶段报错(GENUINE R1)；但断言获取的是run_logs而非error_message |

**部分不符原因**: 断言目标是Windows Runner上的默认shell行为，但若平台不支持Windows Runner（与COMPAT-RUNSON-005关联），则%OS%永远不会在真正的Windows Runner上执行。即使触发，YAML步骤的触发条件(workflow_dispatch)和runs-on依赖与断言前提不匹配。断言#1期望的"正确执行Windows命令"与步骤能做到的之间存在gap。
