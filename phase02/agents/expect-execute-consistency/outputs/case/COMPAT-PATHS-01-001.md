# COMPAT-PATHS-01-001
- **标题**: paths 过滤器 300 条边界测试
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 on.push.paths 配置恰好 300 条路径规则时，workflow 能被平台接受并正常触发。

## 做了什么
配置 300 条 path 规则，step 中 echo "PATHS_300_OK"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | 300 条边界内 workflow 应正常执行 |
| 2 | run_logs | positive | must_contain "PATHS_300_OK" | COVERED | echo 输出可验证 step 执行 |
