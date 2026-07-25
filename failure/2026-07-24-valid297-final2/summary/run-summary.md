# 全量汇总 · 2026-07-24-valid297-final2

## 执行摘要

| 判定 | 数量 | 占比 |
|---|---|---|
| PASS | 131 | 44.1% |
| FAIL | 82 | 27.6% |
| COMPILE_ERROR | 63 | 21.2% |
| TIMEOUT | 16 | 5.4% |
| ENV_ERROR | 4 | 1.3% |
| INCONCLUSIVE | 1 | 0.3% |

执行覆盖率: 213/297 = 71.7%
fingerprint: 0/213 不匹配
门禁: BLOCKED（5 维度全不达标）

## FAIL 归因分布

| 根因 | 数量 | 占比 |
|---|---|---|
| 产品缺陷 | ~30 | ~37% |
| 用例问题 | ~15 | ~18% |
| 环境问题 | ~20 | ~24% |
| 标记不匹配/编译缺口 | ~10 | ~12% |
| 需人工判断 | ~7 | ~9% |

详见 report/ 子目录下的逐条归因报告。

## 非 FAIL 统计

| 判定 | 主因 |
|---|---|
| COMPILE_ERROR 63 | 54 条 intent_ref 格式不合规 |
| TIMEOUT 16 | 9 条 harness 300s 截断 + 7 条平台排队 |
| ENV_ERROR 4 | dispatch_workflow HTTP 400 |
| INCONCLUSIVE 1 | fork_pr 需第二账号 |

详见 abnormal/ 子目录。

## 运行时

- 开始: 2026-07-24 21:30
- 结束: 2026-07-24 22:25
- 总耗时: **约 55 分钟**（schema 2s + compile 3s + pool ~54min + report 2s + 归因 ~5min → 总计 ~60min）
