# USE-ENV-01-003
- **标题**: ATOMGIT 系统环境变量实际注入集合与文档清单双向 diff
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
实际注入的 ATOMGIT 前缀环境变量与文档清单一致。

## 做了什么
workflow 中 `env | grep "^ATOMGIT_" | sort` 导出全部 ATOMGIT 前缀环境变量。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: ATOMGIT_ | COVERED | `env | grep "^ATOMGIT_" | sort` 真实命令导出实际注入的环境变量集合 |
| 2 | documentation | negative | 实际与文档清单双向 diff，差集且未说明即不合格 | COVERED | harness 将实际集合与文档清单做 diff |

