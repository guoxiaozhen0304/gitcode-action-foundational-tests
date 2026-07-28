# USE-LBL-01-006
- **标题**: 含资源池名的 runs-on 写法平台识别验证
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
验证平台是否接受 `runs-on: [dedicate-hosted, x64, large]` 的含资源池名写法并成功调度，与文档缺失事实构成证据链。

## 做了什么
workflow 使用含资源池名的三段式 runs-on，执行 marker step。若平台识别该写法，将调度到对应资源池。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功 | COVERED | 平台实际调度行为可观察 → GENUINE |
| 2 | documentation | nonfunctional | 若平台识别而文档未提，记文档缺陷 | COVERED | eval: deterministic，运行结果与文档现状交叉判定可程序化 |
