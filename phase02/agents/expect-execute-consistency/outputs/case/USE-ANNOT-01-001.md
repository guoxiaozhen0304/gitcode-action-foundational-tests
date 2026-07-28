# USE-ANNOT-01-001
- **标题**: workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
日志中保留 ::error:: 和 ::warning:: 原始命令文本，不静默吞掉。

## 做了什么
workflow step 中直接 echo 输出 `::error file=src/main.js,line=10::Missing semicolon` 和 `::warning` workflow 命令。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: ::error file=src/main.js,line=10::Missing semicolon | COVERED | `echo "::error file=src/main.js,line=10::Missing semicolon"` — `::error::` 工作流命令，真实文本 |
| 2 | run_logs | positive | contains: ::warning file=src/util.js,line=5::Deprecated function | COVERED | `echo "::warning file=src/util.js,line=5::Deprecated function"` — `::warning::` 工作流命令，真实文本 |

