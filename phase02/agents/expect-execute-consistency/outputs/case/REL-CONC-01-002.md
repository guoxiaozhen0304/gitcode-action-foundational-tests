# REL-CONC-01-002
- **标题**: concurrency.max=6 配置应被系统拒绝
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**concurrency.max=6 的 YAML 应被平台校验拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-002
通过标准：
1. YAML 校验失败或保存被拒
2. 不应静默截断为 5

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 10` | - | 普通 sleep |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | yaml_validation = rejected | positive | - | ✅ COVERED | YAML 中 concurrency.max=6 超出规范上限，平台校验应拒绝；用例通过 batch_validate.py 即可验证，不需要实际 dispatch |
| 2 | run_status = should_not_start | negative | - | ✅ COVERED | YAML 校验拒绝后 run 不会启动 |
---
