# REL-IMAGE-01-052-V2
- **标题**: 镜像拉取性能——5GB 自定义 container 环境准备耗时基准
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
pytorch (~5GB) 镜像拉取≤600s，job success。

## 做了什么
container: image=pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime，step: python --version。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | image_pull_time_seconds | nonfunctional | le 600 | LLM_DEPENDENT | 非功能性能指标，需 harness 测量 |
| 2 | job_status | positive | equals "success" | COVERED | 镜像拉取成功 + python --version 正常 → success |
