# SEC-WCMD-01-002
- **标题**: 跨运行 artifact 必须被视为不可信数据
- **维度**: security
- **评级**: 断言一致

## 想测什么
不可信来源的 artifact 不应被特权运行隐式信任执行；artifact 来源可追溯。

## 做了什么
step1 uses:download-artifact，step2 `ls -la` 检查文件并显式 echo "ARTIFACT_TREATED_AS_DATA_OK" 或 "auto_executed"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain:auto_executed | COVERED | step 仅在检测到 pwned_marker.txt 时输出该字符串，为有效负向验证 |
| 2 | run_logs | positive | must_contain:ARTIFACT_TREATED_AS_DATA_OK | COVERED | step 显式 echo 该字符串 |
| 3 | run_status | positive | equals:completed | COVERED | 平台 run_status，GENUINE |
