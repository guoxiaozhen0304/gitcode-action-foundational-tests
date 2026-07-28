# USE-CLI-01-001
- **标题**: Runner 无 gh 等效 CLI 时迁移指引的替代方案说明
- **维度**: usability
- **评级**: 断言一致

## 想测什么
Runner 上探测 gh/gitcode/atomgit CLI 命令存在性；若不存在，文档应有替代方案说明。

## 做了什么
step `command -v gh || echo "gh=NOTFOUND"` 等显式探测各 CLI 命令存在性。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | eval:deterministic | COVERED | step 显式输出各 CLI 存在性结果，可确定比对 |
| 2 | documentation | negative | eval:deterministic | COVERED | 文档扫描检查，无需 workflow 步骤 |
