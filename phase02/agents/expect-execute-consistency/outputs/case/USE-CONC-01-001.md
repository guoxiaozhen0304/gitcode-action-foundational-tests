# USE-CONC-01-001
- **标题**: concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-027
通过标准：
1. 不应静默截断为边界值
2. 报错中是否包含 1、5、范围等关键词

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
| 1 | run_status | negative | equals: COMPLETED | ✅ GENUINE | YAML 中 concurrency.max=10 超出平台有效范围（应为 1-5），平台应拒绝该 YAML/运行。这是平台验证型测试 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定报错文本是否包含有效范围 |

### 问题
(无 — 断言 1 为平台 YAML 验证测试，报错由平台产生而非步骤代码。步骤 echo 仅为 placeholder。)
---
