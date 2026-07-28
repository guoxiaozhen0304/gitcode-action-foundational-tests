# REL-IMAGE-01-052
- **标题**: 镜像拉取性能——500MB 自定义 container 环境准备耗时基准
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
使用 ~500MB 量级镜像（node:18）的 container job，验证镜像拉取 ≤2min、失败时有明确归因、不应 pending 10min 后无解释失败。
## 做了什么
YAML 定义 container image:node:18，step node --version 验证环境正常。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | image_pull_time_seconds | nonfunctional | le 120 | COVERED | YAML 使用 node:18 真实容器镜像 + node --version 真实命令，harness 测量拉取耗时 |
| 2 | job_status | positive | equals success | COVERED | YAML assert job_status=success，对应文本"拉取 ≤2min 完成并启动"；job success 隐含未 pending 10min 无解释失败 |
