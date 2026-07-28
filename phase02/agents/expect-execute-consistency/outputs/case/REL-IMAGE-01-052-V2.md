# REL-IMAGE-01-052-V2
- **标题**: 镜像拉取性能——5GB 自定义 container 环境准备耗时基准
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
使用 ~5GB 量级镜像（pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime）的 container job，验证镜像拉取 ≤600s、失败时有明确归因、不应 pending 后无解释失败。
## 做了什么
YAML 定义 container image:pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime，step python --version 验证。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | image_pull_time_seconds | nonfunctional | le 600 | COVERED | YAML 使用真实大镜像 + python --version，harness 测量拉取耗时 |
| 2 | job_status | positive | equals success | COVERED | YAML assert job_status=success，对应文本"5GB 镜像在 10min 内完成拉取并启动" |
