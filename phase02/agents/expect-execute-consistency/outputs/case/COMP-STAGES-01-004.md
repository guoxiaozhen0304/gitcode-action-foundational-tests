# COMP-STAGES-01-004
- **标题**: map 形式 stages 按定义顺序串行执行（回归保护）
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原两 stage 均为裸 echo（TRIVIAL + stage_order llm）。改为产物接力证明串行：build_stage 生成 stage_one.out 并 upload-artifact；test_stage download 后 grep 校验——只有 build 先完成，STAGE_ORDER_OK 才可能出现，串行语义由数据依赖确定性证明，替代时间戳 llm 判读。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | grep 校验有真实失败路径 |
| 2 | run_logs | positive | must_contain STAGE_ONE_DONE | ✅ GENUINE | 真实写文件后输出 |
| 3 | run_logs | positive | must_contain STAGE_TWO_DONE | ✅ GENUINE | 真实校验后输出 |
| 4 | run_logs | positive | must_contain STAGE_ORDER_OK | ✅ GENUINE | 串行证明：build 产物在 test 可读 |
| 5 | run_logs | negative | must_not_contain STAGE_ORDER_BROKEN | ✅ GENUINE | 顺序破坏时输出并 exit 1 |
