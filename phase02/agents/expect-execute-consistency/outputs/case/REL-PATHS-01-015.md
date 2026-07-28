# REL-PATHS-01-015
- **标题**: paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 push 触发 paths 过滤的越界：变更 301 个文件，仅第 301 个匹配 paths 规则时 workflow 不应被触发。
## 做了什么
push 变更 301 个文件，仅第 301 个匹配 `src/**` 路径规则；workflow on.push.paths 仅监听 `src/**`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "not_triggered" | COVERED | harness 验证 push 后无 run 被创建 |
