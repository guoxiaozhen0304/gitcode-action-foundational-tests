# REL-BIGRUNNER-01-066
- **标题**: 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
xlarge/2xlarge 各触发 10 次编译，成功率≥90%，失败归因明确，无 flaky。

## 做了什么
单 workflow 含两个 job（compile_xlarge/compile_2xlarge），各执行 gcc 编译+运行，echo COMPILE_OK_* 标记。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | gcc 编译与运行成功则 job 成功；workflow 有真实编译步骤 |
| 2 | run_logs | positive | must_contain "COMPILE_OK_XLARGE" | COVERED | compile step 真实 echo 该标记 |
| 3 | run_logs | positive | must_contain "COMPILE_OK_2XLARGE" | COVERED | compile step 真实 echo 该标记 |
| 4 | success_rate | positive | ge 90 | MISSING | workflow 自身只执行 1 次运行；成功率需跨多次运行聚合统计，由 harness 管理，YAML 内无多次迭代逻辑 |
| 5 | failure_attribution | positive | eval llm_assisted | LLM_DEPENDENT | 归因分析依赖 LLM 判读日志 |
