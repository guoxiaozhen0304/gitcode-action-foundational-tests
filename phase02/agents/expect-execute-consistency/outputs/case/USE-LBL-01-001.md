# USE-LBL-01-001
- **标题**: runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证使用完全不存在的标签组合 [nonexistent-os, x64, small] 时平台应在超时后给出明确失败原因，报错应包含用户指定的标签原文和可用标签列表。

## 做了什么
workflow 使用不存在的标签组合声明 runs-on，step 执行 echo。期望平台因找不到匹配 runner 而失败并报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 无匹配 runner 应导致失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错含用户指定标签原文 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
