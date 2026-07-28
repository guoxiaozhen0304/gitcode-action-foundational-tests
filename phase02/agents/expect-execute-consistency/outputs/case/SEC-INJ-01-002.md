# SEC-INJ-01-002
- **标题**: 不可信分支名不可直接插进 run 脚本导致命令注入
- **维度**: security
- **评级**: 断言一致

## 想测什么
分支名含 shell 元字符时不应被解释执行；安全写法正常工作。

## 做了什么
workflow 两步骤：内联 ${{ atomgit.head_ref }} 和通过中间 env 引用；as: untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "injected_command_executed" | COVERED | 对应"含特殊字符的分支名绝不应被解释为 shell 命令"；${{ }}→GENUINE |
| 2 | run_status | positive | equals "success" | COVERED | 安全写法正常工作 |
