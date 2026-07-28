# USE-ANNOT-01-001
- **标题**: workflow 命令 ::error:: 与 ::warning:: 在日志中保留原文
- **维度**: usability
- **评级**: 断言一致

## 想测什么
run 步骤中输出的 ::error:: 和 ::warning:: 命令原文应在日志中保留，不静默吞掉。

## 做了什么
step 显式 echo 三条 workflow 命令（::error::, ::warning::, ::notice::）。断言检查日志中是否包含这些原文。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains:"::error file=src/main.js,line=10::Missing semicolon" | COVERED | step 显式 echo 该字符串，精确匹配 |
| 2 | run_logs | positive | contains:"::warning file=src/util.js,line=5::Deprecated function" | COVERED | step 显式 echo 该字符串，精确匹配 |
