# REL-RERUN-01-011
- **标题**: rerun 边界值——单条运行连续重新运行 3 次应全部成功
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
对失败运行执行Re-run all 3次，每次创建新运行(sha/ref一致)、全部success，不应复用旧记录。

## 做了什么
harness对失败运行依次执行3次rerun。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_count | positive | equals=3 | COVERED | 文本"第1-3次rerun均创建新运行"对应(rerun_count=3) |
| 2 | run_status | positive | equals=completed(success) | COVERED | 文本"3次新运行均success"对应 |
| 3 | (文本) 运行编号递增 | — | — | MISSING | 文本"运行编号递增"在YAML中无独立断言 |
| 4 | (文本负向) 不应复用旧运行记录 | — | — | MISSING | 文本"不应复用旧运行记录"在YAML中无独立negative断言 |
