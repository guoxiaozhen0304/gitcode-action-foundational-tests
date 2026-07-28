# USE-ENV-01-003
- **标题**: ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff
- **维度**: usability
- **评级**: 断言一致

## 想测什么
实际注入的 ATOMGIT 环境变量集合应与两页文档清单一致。

## 做了什么
step `env | grep "^ATOMGIT_" | sort` 显式导出并排序所有 ATOMGIT 前缀环境变量。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains:"ATOMGIT_" | COVERED | step 显式 grep/sort ATOMGIT_ 变量，精确匹配前缀 |
| 2 | documentation | negative | eval:deterministic | COVERED | 实际注入集合与两页文档清单双向 diff 检查 |
