# REL-RUNNER-01-050
- **标题**: 架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
x64探针输出x86_64、arm64探针输出aarch64、20次采样错配=0、无匹配时排队或报错不错配。

## 做了什么
两个arch探针job，各采样10次打印uname -m。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | x64_job_arch | positive | equals=x86_64 | COVERED | 文本"x64探针输出=x86_64"精确对应 |
| 2 | arm64_job_arch | positive | equals=aarch64 | COVERED | 文本"arm64探针输出=aarch64"精确对应 |
| 3 | arch_mismatch_count | positive | equals=0 | COVERED | 文本"架构错配次数=0"精确对应 |
| 4 | x64_job_arch | negative | equals=aarch64 | COVERED | 文本"架构匹配率=100%"(错配=0)精确对应 |
| 5 | no_matching_runner_behavior | nonfunctional | equals=queued_or_explicit_error | COVERED | 文本"无匹配架构runner时job明确排队或报错，不错配执行"精确对应 |
