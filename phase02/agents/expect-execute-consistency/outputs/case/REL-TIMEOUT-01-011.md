# REL-TIMEOUT-01-011
- **标题**: 自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-075
通过标准：
1. 行为确定可归因：接受或拒绝
2. 不应静默截断

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | timeout probe step | `echo "timeout_720_probe_marker"` | — | 探针标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | config_outcome = accepted_or_explicitly_rejected | positive | — | ✅ GENUINE | `timeout-minutes: 720` 超出默认 360，由平台在解析/执行阶段判定接受或拒绝。step 为纯 echo 探针 |
| 2 | silent_truncation_to_360_detected = true | negative | — | ✅ GENUINE | 验证不应静默截断 |
| 3 | rejection_error_contains_limit = true_if_rejected | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
