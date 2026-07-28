# REL-CHILDSTATE-01-064-V2
- **标题**: 子任务状态传播——workflow_call 未拉起时父 workflow 不应假阳性完成
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
workflow_call 引用不存在的子 workflow（child_missing.yml），验证父 workflow 状态=failure、下游 job 被 skip、父不应显示 success。
## 做了什么
YAML 使用 `uses: ./.gitcode/workflows/child_missing.yml`（不存在），下游 job needs: call_child。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | parent_status | positive | equals failure | COVERED | YAML uses 不存在的工作流 → 平台校验/执行期报错 → parent_status=failure，对应文本"父 workflow 明确标记 failure" |
| 2 | downstream_status | positive | equals skipped | COVERED | YAML assert downstream_status=skipped，对应文本"下游默认 job 被 skip" |
| 3 | parent_status | negative | equals success | COVERED | YAML 负向断言 parent_status ≠ success，对应文本"父 workflow 不应显示 success" |
