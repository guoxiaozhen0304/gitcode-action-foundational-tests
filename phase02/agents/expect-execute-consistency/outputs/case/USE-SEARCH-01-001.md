# USE-SEARCH-01-001
- **标题**: 日志搜索与下载功能可用且交互流畅
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证日志面板中的搜索功能匹配行高亮、下载为 UTF-8 文本、搜索响应时间小于 2 秒。

## 做了什么
workflow 产生含 INFO/ERROR/WARN 的多行日志输出。断言日志含 "ERROR: mock failure line 1" 以确认日志内容存在。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | 日志含 "ERROR: mock failure line 1" | COVERED | 平台日志输出 → GENUINE |
| 2 | ui_interaction | nonfunctional | 搜索框常驻、高亮对比度 ≥ 3:1、下载按钮有文字说明 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
