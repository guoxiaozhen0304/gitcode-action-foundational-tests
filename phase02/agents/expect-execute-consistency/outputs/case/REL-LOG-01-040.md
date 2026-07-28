# REL-LOG-01-040
- **标题**: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
100MB 日志大小≈100MB，首尾行可查看，可下载，不截断不乱序。

## 做了什么
echo LOG_HEAD_MARKER → 循环输出 2500 行 × 40960 字节 → echo LOG_TAIL_MARKER。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_size_mb | positive | equals "100" | COVERED | 2500 × 40960 ≈ 100MB，日志大小由平台存储，可观测 |
| 2 | log_download | positive | equals "success" | COVERED | 平台日志下载行为可验证 |
| 3 | run_logs | positive | contains "LOG_HEAD_MARKER" | COVERED | echo 输出首标记，日志中可观测 |
| 4 | run_logs | positive | contains "LOG_TAIL_MARKER" | COVERED | echo 输出尾标记，日志中可观测 |
| 5 | truncated_or_disordered_detected | negative | equals "true" | COVERED | 首尾标记均在则无截断 |
