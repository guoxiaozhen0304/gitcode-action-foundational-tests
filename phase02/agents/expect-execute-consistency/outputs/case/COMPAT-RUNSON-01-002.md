# COMPAT-RUNSON-01-002
- **标题**: runs-on 标签体系——单标签字符串应报错
- **维度**: 兼容性
- **评级**: 部分不符

## 想测什么
验证单标签字符串格式(如 `runs-on: ubuntu-latest`)不被平台接受，解析阶段应报错。

## 做了什么
workflow实际YAML中runs-on仍为三段式数组 `[ubuntu-latest, x64, small]`，不是单标签字符串。step输出 `echo "RUNSON_STRING_ACCEPTED"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | workflow_parse | negative llm | "单标签字符串runs-on应在解析阶段报错" | VACUOUS | YAML中runs-on实际为 `[ubuntu-latest, x64, small]` 三段式数组，非单标签字符串；step永远不会触发单标签字符串场景(R4★) |
| 2 | run_logs | positive llm | "错误信息应提示使用数组格式" | VACUOUS | 与#1同因——YAML配置本身是数组格式，不会产生预期的"单标签报错" |
| 3 | run_logs | negative llm | "不应出现RUNSON_STRING_ACCEPTED" | COVERED | step输出该echo字符串，日志可观测(R1 GENUINE) |

**部分不符原因**: YAML中runs-on写法与标题/意图不匹配——标题宣称测"单标签字符串应报错"但YAML实际使用了三段式数组 `[ubuntu-latest, x64, small]`。断言#1/#2期望触发单标签字符串场景，但YAML配置永远不会导致该场景，使其VACUOUS。
