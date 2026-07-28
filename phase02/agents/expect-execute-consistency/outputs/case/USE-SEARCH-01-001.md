# USE-SEARCH-01-001  - **标题**: 日志搜索与下载功能可用且交互流畅   - **维度**: usability   - **评级**: 部分不符

## 想测什么

匹配行高亮显示，下载文件为 UTF-8 纯文本，大文件不崩溃

## 做了什么

- 1. 在日志面板输入关键词搜索
- 2. 点击下载日志按钮

- - [正向] 搜索后匹配行被高亮
- - [正向] 下载的日志文件为 UTF-8 文本
- - [非功能] 搜索响应时间小于 2 秒

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=`ERROR: mock failure line 1` | VACUOUS | run_logs+contains: echo 'ERROR: mock failure line 1'→仅字面量echo期望字符串→R1→VACUOUS; 步骤未执行真实错误产生逻辑 |
| 2 | log_download | positive | equals=`success` | COVERED | log_download+equals: 日志下载是平台功能→可验证 |
| 3 | ui_interaction | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: UI搜索交互与对比度需LLM评估 |
