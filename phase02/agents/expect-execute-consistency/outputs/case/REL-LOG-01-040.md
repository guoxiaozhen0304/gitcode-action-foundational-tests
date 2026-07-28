# REL-LOG-01-040
- **标题**: 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
单 job 输出 100MB 日志，验证日志约 100MB、首尾行可查看、下载正常、不应截断或乱序。
## 做了什么
YAML 使用 python3 循环输出 2500 次 40KB 行（约 100MB）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_size_mb | positive | equals 100 | COVERED | YAML python3 真实命令输出约 100MB，harness 校验日志大小 |
| 2 | log_download | positive | equals success | COVERED | YAML assert 日志可正常下载，对应文本"日志下载 API/页面可正常下载" |
| 3 | head_tail_viewable | positive | 首尾行可查看 | MISSING | 文本有正向断言"日志首尾行均可查看无截断"，YAML 无对应 assertion |
| 4 | no_truncation_or_disorder | negative | 不应截断或乱序 | MISSING | 文本有负向断言"不应截断或乱序"，YAML 无对应 assertion |
