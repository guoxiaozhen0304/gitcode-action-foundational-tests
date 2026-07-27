# REL-REG-01-001
- **标题**: 新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**新仓库 workflow 注册——首次 push 含合法流水线配置即应触发，无需手动再改一次**
- 触发事件: `push`
- 规格引用: INTENT-REL-072
通过标准：
1. 3/3 仓库首次 push 后 run 被创建
2. 不应出现 workflow 文件存在但 push 无任何 run 记录的静默丢失
3. 注册延迟 ≤5 分钟（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | probe step | `echo "first_push_registration_probe"` | — | 探针标记 |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | fresh-repo |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created = true | positive | — | ✅ GENUINE | `repo_fixture: fresh-repo` + `push` 事件，step 为纯 echo，但被测的是新仓库首次 push 的 workflow 注册行为。若平台正确注册则 echo 的 run 会被创建 |
| 2 | run_records_count = 0 | negative | — | ✅ GENUINE | 验证不应出现 0 条 run 记录（即应有 run 被创建） |
| 3 | registration_delay_seconds ≤ 300 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 4 | successful_repo_ratio = 3/3 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
