# SEC-INJ-01-001
- **标题**: 不可信 PR 标题不可直接插进 run 脚本导致命令注入
- **维度**: security
- **评级**: 断言一致

## 想测什么
PR 标题含 shell 元字符时不应被解释执行；安全写法（中间环境变量）正常工作。

## 做了什么
workflow 两步骤：内联 ${{ atomgit.event.pull_request.title }} 和通过中间 env 引用；as: untrusted_contributor。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "injected_command_executed" | COVERED | 对应"含特殊字符的 PR 标题绝不应被解释为 shell 命令执行"；${{ }} 求值→GENUINE |
| 2 | run_status | positive | equals "success" | COVERED | 安全写法应正常完成；job 不崩溃→COVERED |
