# COMP-BOUND-01-086
- **标题**: 矩阵构建 include exclude 与单值边界验证
- **维度**: completeness
- **评级**: 部分不符

## 想测什么
matrix include 添加额外组合，exclude 排除特定组合，单值变量正确展开。排除后产生 linux-1 和 linux-3 共 2 个实例。

## 做了什么
1. step `Matrix value`（在每个矩阵实例中执行）：`echo "INSTANCE=${{ matrix.os }}-${{ matrix.version }}"` 和 `echo "matrix_ok"`
2. matrix: os=[linux], version=[1,2], include: {os:linux, version:3}, exclude: {os:linux, version:2}

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: matrix_ok | COVERED | echo 在每个实例中执行 |
| 2 | run_logs | positive | must_contain: INSTANCE=linux-1 | COVERED | `${{ matrix.os }}-${{ matrix.version }}` 表达式输出 |
| 3 | run_logs | positive | must_contain: INSTANCE=linux-3 | COVERED | include 追加的组合 |
| 4 | run_logs | negative | must_not_contain: INSTANCE=linux-2 | COVERED | 被 exclude 排除，不会出现在任何实例日志中 |
| 5 | job_instance_count | positive | equals: 2 | UNVERIFIABLE | 目标不在 step 内产出，需外部平台 API 统计 job 实例数 |
