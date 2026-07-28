# USE-CLI-01-001
- **标题**: Runner 无 gh 等效 CLI 时迁移指引的替代方案说明
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
Runner 上探测 CLI 存在性；若无等效 CLI，文档应有替代方案说明。

## 做了什么
workflow 中用 `command -v` 探测 gh、gitcode、atomgit 命令是否存在。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 记录 gh、gitcode、atomgit 存在性 | COVERED | `command -v gh || echo "gh=NOTFOUND"` 等，真实命令探测 CLI 存在性 |
| 2 | documentation | negative | CLI 不存在且文档无替代说明即不合格 | COVERED | 文档扫描验证（外部文档审查） |

