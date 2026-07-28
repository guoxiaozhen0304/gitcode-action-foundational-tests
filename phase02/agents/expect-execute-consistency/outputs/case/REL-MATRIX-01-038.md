# REL-MATRIX-01-038
- **标题**: 大规模 matrix——20 个组合应全部生成并正确调度
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
20组合(2×2×5)的matrix全部生成、矩阵变量值正确、无重复遗漏。

## 做了什么
os×arch×compiler 三轴展开20个实例，每实例echo矩阵变量值。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | generated_jobs_count | positive | equals=20 | COVERED | 文本"20个jobs全部生成"精确对应 |
| 2 | run_status | positive | equals=completed(success) | COVERED | 文本"20个jobs全部completed(success)"对应 |
| 3 | (文本) 矩阵变量校验100%通过 | — | — | MISSING | 文本明确要求"矩阵变量校验100%通过"，YAML无独立变量校验断言，仅依赖全success |
| 4 | (文本负向) 不应重复或遗漏 | — | — | MISSING | 文本"不应出现重复组合或遗漏组合"在YAML中无独立negative断言 |
