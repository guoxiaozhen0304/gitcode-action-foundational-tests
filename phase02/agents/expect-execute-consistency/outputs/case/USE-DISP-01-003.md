# USE-DISP-01-003
- **标题**: workflow_dispatch 手动触发 UI 与 YAML inputs 定义的集合一致性
- **维度**: usability
- **评级**: 断言一致

## 想测什么
手动触发 UI 应逐一渲染 YAML 定义的 5 个 inputs；required 标星、default 预填。

## 做了什么
workflow 定义 5 个 inputs（含 required、default），step `echo "dispatched"` 为 marker。断言指向 ui 确定性评估。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui | positive | eval:deterministic | COVERED | UI 渲染字段集合与 YAML inputs diff；harness 外部完成 |
| 2 | ui | negative | eval:deterministic | COVERED | 同上，不应多渲染或漏渲染 |
| 3 | ui | nonfunctional | eval:deterministic | COVERED | required/default/description 在 UI 的呈现检查 |
