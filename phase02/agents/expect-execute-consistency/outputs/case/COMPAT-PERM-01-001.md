# COMPAT-PERM-01-001
- **标题**: 未声明 permissions 时默认 TOKEN 读操作权限范围
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试未声明 permissions 块时，默认 TOKEN 拥有足够的读权限（checkout 和 cat README 成功）。

## 做了什么
不声明 permissions，执行 checkout 和 `cat README.md`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | 读操作成功退出码为 0 |
| 2 | run_logs | positive | contains "README" | COVERED | cat 输出 README 内容可验证读权限 |
