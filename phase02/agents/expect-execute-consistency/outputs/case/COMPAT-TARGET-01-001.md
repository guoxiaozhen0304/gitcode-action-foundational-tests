# COMPAT-TARGET-01-001
- **标题**: pull_request_target 默认 checkout 应为 base 分支而非 head 分支
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证pull_request_target触发下checkout检出的是base分支(目标分支)代码而非fork PR的head commit。

## 做了什么
step1使用 `uses: checkout`；step2输出 `echo "Current SHA: ${{ atomgit.sha }}"` + `echo "Base SHA: ${{ atomgit.event.pull_request.base.sha }}"` + `echo "Head SHA: ${{ atomgit.event.pull_request.head.sha }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative llm | "当前检出SHA不应等于fork PR head SHA" | COVERED | 三步输出${{ atomgit.sha }}, base.sha, head.sha均为GENUINE(R1上下文表达式)，三个SHA在同一日志可对比 |
| 2 | run_logs | positive llm | "检出SHA等于base分支SHA" | COVERED | 同#1，SHA值来源于平台上下文(GENUINE) |
| 3 | run_status | positive equals success deterministic | workflow成功 | COVERED | run_status平台可观测 |
