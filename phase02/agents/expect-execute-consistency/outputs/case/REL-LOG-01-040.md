# REL-LOG-01-040
- **标题**: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
日志生成首尾加 LOG_HEAD_MARKER/LOG_TAIL_MARKER（尾标记存在即证明未截断）；补三条断言：首尾标记可见 + 不应截断或乱序（negative）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_size_mb | positive | equals 100 | ✅ COVERED | harness 校验日志大小 |
| 2 | log_download | positive | equals success | ✅ COVERED | 下载验证 |
| 3 | run_logs | positive | contains LOG_HEAD_MARKER | ✅ GENUINE | 首行标记 |
| 4 | run_logs | positive | contains LOG_TAIL_MARKER | ✅ GENUINE | 尾行标记（截断则缺失） |
| 5 | truncated_or_disordered_detected | negative | equals true | ✅ COVERED | 负向验证 |
