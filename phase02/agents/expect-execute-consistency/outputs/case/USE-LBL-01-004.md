# USE-LBL-01-004
- **标题**: quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证
- **维度**: usability
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**quick-start 单标签写法 runs-on ubuntu-latest 的可调度性验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-031
通过标准：
1. 文档示例写法应可被平台接受并运行成功
2. 平台不应接受一种写法而文档示例给出另一种却不加说明

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | hello step | `echo "hello from single-label runs-on"` | 无 | 验证单标签 runs-on 写法能否调度 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals "success" | positive | 步骤虽为纯 echo，但 runs-on 单标签写法的接受性是平台调度真实行为 | ✅ GENUINE | 平台对 runs-on 写法的校验/调度是真实行为 |
| 2 | documentation 确定性校验 | negative | 若平台拒绝单标签写法则 quick-start 示例错误 | ✅ COVERED | 确定性文档校验，依赖断言 1 结果 |
---
