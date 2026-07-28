# REL-BIGRUNNER-01-066
- **标题**: 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
编译步骤由 `echo compiling; sleep 30`（STATUS_GUARANTEED）改为真实 gcc 编译 + 运行（编译错误/运行非零即真实失败）；增加 if always() 归因标记步骤；断言补 run_status/两个 COMPILE_OK 标记；failure_attribution 改 llm rubric。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | gcc 真实编译存在失败路径 |
| 2 | run_logs | positive | must_contain COMPILE_OK_XLARGE | ✅ GENUINE | 编译+运行成功后输出 |
| 3 | run_logs | positive | must_contain COMPILE_OK_2XLARGE | ✅ GENUINE | 同上 |
| 4 | success_rate | positive | ge 90 | ✅ COVERED | harness 跨 run 统计 |
| 5 | failure_attribution | positive | llm_assisted | 🔶 LLM_DEPENDENT | 归因明确性判读（材料：ATTRIBUTION_JOB 标记 + gcc 日志） |

### 残留问题
失败归因的"明确性"属判读性质，保留 llm_assisted（YAML 已注释）；归因材料已由确定性步骤产出。
