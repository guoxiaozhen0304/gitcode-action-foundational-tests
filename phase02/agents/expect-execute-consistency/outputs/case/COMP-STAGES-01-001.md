# COMP-STAGES-01-001

- **标题**: stages 阶段间串行、阶段内 job 并行执行
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 stages 阶段间串行、阶段内 job 并行，通过时间戳可观测。

## 做了什么
各 job 步骤运行 `date +%s` 输出时间戳标记（BUILD_A_START、BUILD_A_END、BUILD_B_START/END、TEST_START/END）。`date +%s` 是真实命令，`echo "BUILD_A_START=$(date +%s)"` 使用 `$(...)` 命令替换。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | step 含真实命令 date +%s + 命令替换，非必然成功 |
| 2 | run_logs | positive | must_contain BUILD_A_START= | COVERED | step 运行 date 真实命令产生时间戳 |
| 3 | run_logs | positive | must_contain BUILD_B_START= | COVERED | 同上 |
| 4 | run_logs | positive | must_contain TEST_START= | COVERED | 同上 |
| 5 | stage_order | positive | equals serial_across_stages | COVERED | harness 对比各 stage job 时间戳判断串行 |
| 6 | job_parallelism | positive | equals parallel_within_stage | COVERED | harness 对比同 stage 内 job 时间戳重叠度判断并行 |
