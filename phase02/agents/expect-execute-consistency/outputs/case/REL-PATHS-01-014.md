# REL-PATHS-01-014
- **标题**: paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 push 触发 paths 过滤的边界：变更恰好 300 个文件时，只要至少 1 个匹配 paths 规则（src/**），workflow 应被正确触发。
## 做了什么
push 变更恰好 300 个文件，其中 1 个匹配 `src/**` 路径规则；workflow on.push.paths 仅监听 `src/**`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(success)" | COVERED | 平台 API 查询 run 是否被创建并成功完成 |
