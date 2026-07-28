# SEC-WCMD-01-002
- **标题**: 跨运行 artifact 必须被视为不可信数据
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原步骤仅 echo 声明（TRIVIAL）。改为真实检查：ls 下载内容，若 payload 存在则标记 UNTRUSTED_PAYLOAD_PRESENT；若存在 pwned_marker.txt（被隐式执行的副作用）则输出 auto_executed 并 exit 1；否则 ARTIFACT_TREATED_AS_DATA_OK。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain auto_executed | ✅ GENUINE | 真实检查执行副作用，被执行时输出并 exit 1 |
| 2 | run_logs | positive | must_contain ARTIFACT_TREATED_AS_DATA_OK | ✅ GENUINE | 真实检查后输出 |
| 3 | run_status | positive | equals completed | ✅ GENUINE | 存在真实失败路径 |
