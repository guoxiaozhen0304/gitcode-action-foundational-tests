# REL-LOGPERF-01-051
- **标题**: 日志加载性能——50MB 日志下载与查看耗时
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**50MB 日志下载与查看性能**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-051
通过标准：
1. 下载≤30s
2. 大小/行数 100% 一致
3. 不应 UI 卡死

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate 50MB log | `for i in $(seq 1 50000); do echo LOG_LINE_${{i}} $(date +%s%N); done` | - | 约 50MB 日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_time_seconds le 30 | nonfunctional | - | 🔶 LLM_DEPENDENT | 性能指标需运行时测量 |
| 2 | log_integrity = 100% | positive | - | ✅ GENUINE | 步骤包含 `${{i}}` 表达式 + `date` 真实命令生成可校验日志 |
---
