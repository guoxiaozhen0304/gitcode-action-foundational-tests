# REL-VCJOB-01-001
- **标题**: 【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归**
- 触发事件: `manual`
- 规格引用: INTENT-REL-089
通过标准：
1. 标准 vcjob 格式任务正常解析并运行
2. 不应出现 vcjob 字段被静默丢弃

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | workflow: null | 无 workflow 定义 | — | — |

## 3. 触发与运行环境
| 触发事件 | manual |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | vcjob_parse_status = success | positive | — | ❌ MISSING_SOURCE | `workflow: null`，YAML 中无任何 workflow 定义。vcjob 格式任务是 K8s Volcano 作业，不属于 GitHub Actions workflow 模型。YAML 无对应 step |
| 2 | vcjob_run_status = Running | positive | — | ❌ MISSING_SOURCE | 无 workflow 步骤 |
| 3 | vcjob_field_handling | negative | eval: llm_assisted | 🔶 LLM_DEPENDENT | LLM 辅助评估 |
### 问题
- `workflow: null` 且 `event: manual`，测试的是 vcjob（Volcano Job）提交行为而非 GitHub Actions workflow
- vcjob 属于 K8s/Volcano 调度器领域，不属于本 YAML 的 workflow 步骤范畴
- 两个 positive 断言完全没有对应步骤来源
---
