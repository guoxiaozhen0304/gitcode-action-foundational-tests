# REL-IMAGE-01-052
- **标题**: 镜像拉取性能——500MB 自定义 container 环境准备耗时基准
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**500MB 容器镜像拉取性能**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-052
通过标准：
1. 拉取≤120s
2. job 状态=success

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | check python version | `python --version` | container: python:3.11-slim | Python 版本 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | image_pull_time_seconds le 120 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
| 2 | job_status = success | positive | - | ✅ GENUINE | container 配置触发真实镜像拉取；python --version 是真实命令 |
---
