# REL-IMAGE-01-052
- **标题**: 镜像拉取性能——500MB 自定义 container 环境准备耗时基准
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
node:18 (~500MB) 镜像拉取≤120s，job success。

## 做了什么
container: image=node:18，step: node --version。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | image_pull_time_seconds | nonfunctional | le 120 | LLM_DEPENDENT | 非功能性能指标，由 harness 从平台日志测量拉取耗时 |
| 2 | job_status | positive | equals "success" | COVERED | 镜像拉取成功 + node --version 正常执行 → success |
