# COMPAT-RUNNER-01-008
- **标题**: 与 GitHub hosted image 的关键能力差距探测
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
探测docker守护进程和浏览器(chrome/firefox)在GitCode Runner上的可用性，记录与GitHub hosted image的能力差距。

## 做了什么
step1执行 `docker info` + `echo "DOCKER_MISSING"` fallback；step2执行 `which google-chrome`/`which firefox` + `echo "CAPABILITY_PROBE_DONE"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive must_contain | "CAPABILITY_PROBE_DONE" | COVERED | step2中echo "CAPABILITY_PROBE_DONE"直接覆盖(R1 GENUINE) |
| 2 | run_logs | positive llm | "docker与浏览器可用性确定结论" | COVERED | docker info/which为真实命令(GENUINE R1)，输出在日志中可观测 |
| 3 | run_logs | nonfunctional llm | "差距清单写入迁移文档" | LLM_DEPENDENT | R5: nonfunctional + llm → LLM_DEPENDENT；文档回写需人工/LLM |
