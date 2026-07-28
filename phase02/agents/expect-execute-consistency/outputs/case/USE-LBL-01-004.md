# USE-LBL-01-004
- **标题**: quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
验证 quick-start 文档中单标签字符串形式的 runs-on: ubuntu-latest 是否可被平台接受并成功调度，即文档示例本身是否正确。

## 做了什么
workflow 按文档示例使用 `runs-on: ubuntu-latest` 单标签字符串写法，执行 echo。同时检查若平台拒绝单标签写法则 quick-start 示例为错误示例。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功 | COVERED | 平台实际调度行为可观察 → GENUINE |
| 2 | documentation | negative | 若平台拒绝单标签则 quick-start 示例为错误 | COVERED | eval: deterministic，运行结果与文档示例差异判定可程序化 |
