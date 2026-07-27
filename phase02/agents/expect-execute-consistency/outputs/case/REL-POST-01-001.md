# REL-POST-01-001
- **标题**: post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-083
通过标准：
1. post 失败时 conclusion 与文档语义一致
2. post 失败归因可见
3. 不应静默吞掉 post 失败
4. 不应 post hang 超 timeout

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | main step (main_ok) | `echo "main_ok_marker"` | — | 主步骤成功标记 |
| 2 | post notify step (post) | `echo "post_executed_marker"; exit 1` | run_always: true | post 阶段输出标记后主动失败 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | conclusion_matches_documented_semantics = true | positive | — | ✅ GENUINE | post 阶段 `exit 1` 真实触发 post 失败，平台需判定 conclusion。主步骤成功 + post 失败 = 真实的 post 阶段失败语义测试 |
| 2 | post_failure_attribution_visible = true | positive | — | ✅ GENUINE | `exit 1` 在 post 阶段真实失败后，平台输出归因信息（区分 post 失败 vs 主步骤失败） |
| 3 | silent_post_swallow_detected = true | negative | — | ✅ GENUINE | 作为 negative 断言验证 post 失败未被静默吞掉 |
| 4 | post_hang_beyond_timeout_detected = true | negative | — | ⚠️ 文本提及多组变体（a/b/c），此 YAML 仅实现组 a。组 c（post 超时）需 harness 注入，非本 YAML 直接覆盖 |
---
