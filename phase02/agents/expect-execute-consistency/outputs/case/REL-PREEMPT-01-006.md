# REL-PREEMPT-01-006
- **标题**: preemption events 越界值——配置 11 个应被拒绝
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**preemption events 越界值——配置 11 个应被拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-006
通过标准：
1. YAML 校验被拒绝

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo step | `echo test` | — | 固定字符串输出 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | yaml_validation = rejected | positive | — | ❌ MISSING_SOURCE | 断言 `yaml_validation = rejected` 期望 YAML 解析阶段被拒绝，但此 YAML 本身语法合法（11 个 events 值可能被解析但语义越界）。若平台在 YAML 解析阶段拒绝，workflow 根本不会触发，则不产生任何 run，断言无法由 workflow 内部验证。需由 harness 观测平台的校验 API 拒绝响应 |
### 问题
- 同 REL-PATHS-01-015，断言期望的行为（解析拒绝）发生在 workflow 运行之前，workflow 内部步骤不可验证。完全依赖 harness 外部观测平台 API 校验行为
- step 仅为 `echo test`，完全不参与验证
---
