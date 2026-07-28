# REL-PATHS-01-015
- **标题**: paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
push变更301个文件(仅第301个匹配paths)，workflow不应触发。

## 做了什么
workflow on.push.paths:['src/**']，harness构造仅第301个文件在src/下。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=not_triggered | COVERED | 文本"workflow不触发"精确对应(not_triggered语义=无run创建) |
