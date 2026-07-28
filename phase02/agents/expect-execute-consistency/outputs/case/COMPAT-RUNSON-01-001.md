# COMPAT-RUNSON-01-001
- **标题**: runs-on 标签体系——三段式数组正常匹配
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `runs-on: [ubuntu-latest, x64, small]` 三段式数组格式能被平台正确解析并调度到匹配Runner。

## 做了什么
workflow_dispatch触发，step输出 `echo "RUNSON_ARRAY_OK"` + `echo "RUNNER_OS=${{ runner.os }}"` + `echo "RUNNER_ARCH=${{ runner.arch }}"` + `echo "RUNNER_NAME=${{ runner.name }}"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals completed_success | workflow成功完成 | COVERED | run_status平台可观测 |
| 2 | run_logs | positive must_contain | "RUNSON_ARRAY_OK" | COVERED | echo "RUNSON_ARRAY_OK"直接覆盖(R1 GENUINE) |
| 3 | run_logs | positive must_contain | "RUNNER_OS=" | COVERED | echo "RUNNER_OS=${{ runner.os }}"直接产生(R1 GENUINE上下文变量) |
| 4 | workflow_parse | negative llm | "不应因数组格式runs-on而解析失败" | COVERED | workflow_parse为平台校验日志(GENUINE R1) |
