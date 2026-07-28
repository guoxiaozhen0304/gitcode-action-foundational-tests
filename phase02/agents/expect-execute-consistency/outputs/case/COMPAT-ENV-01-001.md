# COMPAT-ENV-01-001
- **标题**: ATOMGIT_SHA 环境变量应正确返回触发提交 SHA
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原步骤仅 echo（run_status TRIVIAL、格式判定 llm）。改为 workflow 内真实校验：grep -qE '^[0-9a-f]{40}$' 验证 SHA 格式，不符则 exit 1；断言全部确定化。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | 存在真实失败路径（格式不符 exit 1） |
| 2 | run_logs | positive | must_contain ATOMGIT_SHA_FORMAT_OK | ✅ GENUINE | grep 校验通过后输出 |
| 3 | run_logs | negative | must_not_contain ATOMGIT_SHA_FORMAT_BAD | ✅ GENUINE | 格式异常时输出并 exit 1 |
