# COMPAT-PR-01-009
- **标题**: pull_request 触发时 atomgit.sha/ref 的代码版本语义
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
确定atomgit.sha/ref在PR触发时的取值语义（head sha vs 试合并sha），并与GitHub merge commit模型对齐。

## 做了什么
step1输出 `echo "CTX_SHA=${{ atomgit.sha }}"` + `echo "CTX_REF=${{ atomgit.ref }}"` + `echo "ENV_SHA=$ATOMGIT_SHA"`；step2使用 `uses: checkout`；step3输出 `echo "CHECKOUT_HEAD=$(git rev-parse HEAD)"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive must_contain | "PROBE_DONE" | COVERED | step3中echo "PROBE_DONE"直接覆盖(R1 GENUINE) |
| 2 | run_logs | positive llm | "比对CTX_SHA与head/base/试合并sha定位语义" | COVERED | step1输出${{ atomgit.sha }}/atomgit.ref(GENUINE R1)；step3 git rev-parse为真实命令(GENUINE)，LLM辅助比对(R5) |
| 3 | run_logs | negative llm | "CHECKOUT_HEAD不应与CTX_SHA指向版本不一致" | COVERED | CHECKOUT_HEAD来自git rev-parse(真实命令GENUINE)，CTX_SHA来自${{ }}(GENUINE)，两者在同一日志中可对比 |
