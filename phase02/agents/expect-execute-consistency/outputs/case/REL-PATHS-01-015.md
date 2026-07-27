# REL-PATHS-01-015
- **标题**: paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断**
- 触发事件: `push`
- 规格引用: INTENT-REL-015
通过标准：
1. workflow 不触发

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo triggered | `echo triggered by paths` | — | 固定字符串输出 |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status = not_triggered | positive | — | ❌ IMPOSSIBLE | 断言 `run_status = not_triggered` 不可由 workflow 自身验证——若 workflow 未被触发，则此 YAML 根本不会运行，断言成为悖论。验证"不触发"需由 harness 在外部确认无 run 记录 |
### 问题
- 断言期望 workflow 不触发（not_triggered），但 workflow YAML 仅在触发后才可能执行。这是规范设计问题：验证"不触发"的行为不能由 workflow 内部步骤证明
- step 为纯静态 echo，完全 VACUOUS
---
