# USE-ONBD-01-001
- **标题**: 新手快速开始路径端到端可复刻走查（判定方式：llm_assisted）
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证一名无 GitCode 经验的新手按 00-overview 到 01-quick-start 逐步操作能否在 30 分钟内看到第一次成功运行，记录全部卡壳点。

## 做了什么
纯文档/流程检查用例（workflow: null）。由评测者或 LLM 模拟新手逐步操作并记录卡壳点，同时检查 quick-start 前提清单是否遗漏 Action 功能开通步骤。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | nonfunctional | 每步有可观察验证点，卡壳点为 0，30 分钟内完成 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
| 2 | documentation | negative | quick-start 前提清单不含 Action 开通步骤即隐式前提缺陷 | COVERED | eval: deterministic，文档内容扫描可判定 |
