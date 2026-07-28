# COMP-STATUS-01-002
- **标题**: 失败 step 的日志完整保留且可查看
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
step 1 原裸 echo（TRIVIAL），增输 ${{ atomgit.run_number }} 表达式；补 run_status equals failure 断言（规格：失败 step 场景，运行应记录为失败）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals failure | ✅ GENUINE | step 2 真实 exit 1（故意失败合法） |
| 2 | run_logs | positive | contains BEFORE_FAILURE_MARKER | ✅ GENUINE | 步骤含 ${{ }} 表达式 |
| 3 | run_logs | positive | contains ERROR_MARKER | ✅ GENUINE | 失败前真实输出 |
