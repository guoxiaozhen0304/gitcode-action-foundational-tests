# USE-RUN-01-001
- **标题**: 使用三段式标签时 job 正常调度
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证使用标准三段式标签 `runs-on: [ubuntu-latest, x64, small]` 时 job 可被成功调度到匹配的 runner。

## 做了什么
workflow 使用标准三段式标签声明 runs-on，step 执行 echo "runner ok"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功完成 | COVERED | 平台调度行为可观察 → GENUINE |
