# USE-CONC-01-002
- **标题**: concurrency.max 配置 -1 时报错应提示有效范围
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**concurrency.max 配置 -1 时报错应提示有效范围**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-027
通过标准：
1. 不应静默截断
2. 报错中是否包含有效范围说明

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step | `echo "hello"` | - | 仅 echo |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | ✅ GENUINE | YAML 中 concurrency.max=-1 为非法负值，平台应拒绝该 YAML/运行。平台验证型测试 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定报错文本 |
---
