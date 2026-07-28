# USE-DISP-01-003
- **标题**: workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
手动触发 UI 渲染字段集合与 YAML inputs 集合一致，required 标星、default 预填、description 呈现。

## 做了什么
workflow 定义 5 个 inputs（含 required、default），trigger 为 workflow_dispatch。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui | positive | UI 渲染字段集合与 YAML inputs 集合一致 | COVERED | harness 打开手动触发 UI 枚举表单字段，与 YAML 定义做 diff |
| 2 | ui | negative | UI 不应渲染未定义字段/漏渲染已定义字段 | COVERED | 与上一条互补判定 |
| 3 | ui | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定 required 标星、default 预填、description 提示呈现 |

