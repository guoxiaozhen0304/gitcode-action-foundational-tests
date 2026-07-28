# REL-RUNNER-01-050
- **标题**: 架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证架构标签（runs-on x64 vs arm64）调度正确性：x64 job 必须落在 x86_64 节点，arm64 job 必须落在 aarch64 节点，架构错配次数为 0（#48/#96 回归点）。
## 做了什么
分别触发 runs-on x64 和 arm64 的探针 job（job 内打印 uname -m），各采样 10 次。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | x64_job_arch | positive | equals "x86_64" | COVERED | harness 解析 uname -m 输出 |
| 2 | arm64_job_arch | positive | equals "aarch64" | COVERED | harness 解析 uname -m 输出 |
| 3 | arch_mismatch_count | positive | equals "0" | COVERED | harness 统计 20 次采样中架构错配次数 |
| 4 | x64_job_arch | negative | equals "aarch64" | COVERED | 验证 x64 job 不应落在 arm64 节点 |
| 5 | no_matching_runner_behavior | nonfunctional | equals "queued_or_explicit_error" | COVERED | harness 验证无匹配架构 idle runner 时行为合理 |
