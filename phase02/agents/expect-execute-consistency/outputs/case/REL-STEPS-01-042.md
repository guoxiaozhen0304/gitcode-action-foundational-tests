# REL-STEPS-01-042
- **标题**: 超多 step——单 job 内 50 个 step 应全部串行执行无丢失
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
单job内50个step全部出现在运行详情、每个含唯一标识、无丢失或错乱。

## 做了什么
50个step各echo唯一序号("step 01"到"step 50")。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_count | positive | equals=50 | COVERED | 文本"50个step全部出现在运行详情页"对应 |
| 2 | step_order | positive | equals=correct | COVERED | 文本"每个step日志包含唯一标识"+"不应顺序错乱"对应 |
