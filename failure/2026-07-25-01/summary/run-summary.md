# 全量汇总 · 2026-07-25-01

## 执行结果

| 判定 | 数量 |
|---|---|
| PASS | 166 |
| FAIL | 88 |
| TIMEOUT | 27 |
| ENV_ERROR | 11 |
| COMPILE_ERROR | 7 |
| INCONCLUSIVE | 1 |

覆盖率: 254/300 = 84.7%

## FAIL 归因分布

| 根因 | 数量 | 占比 |
|---|---|---|
| 产品缺陷 | ~16 | 18% |
| 用例问题/标记不匹配 | ~30 | 34% |
| 环境问题 | ~25 | 28% |
| 需人工判断 | ~17 | 19% |

详见 report/ 子目录。

## 非 FAIL 统计

| 判定 | 数量 | 主因 |
|---|---|---|
| COMPILE_ERROR | 7 | schedule cron + fault_injection + step name |
| ENV_ERROR | 11 | dispatch HTTP 400（workflow YAML 自身问题） |
| TIMEOUT | 27 | harness 300s 截断 + 平台排队 |
| INCONCLUSIVE | 1 | fork_pr 需第二账号 |

## 用时

- 开始: 2026-07-25 12:10
- 结束: 2026-07-25 14:20
- 总耗时: ~130min（含 3 次重跑 + 归因）
