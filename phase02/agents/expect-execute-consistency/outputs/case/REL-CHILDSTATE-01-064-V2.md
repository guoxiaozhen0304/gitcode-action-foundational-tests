# REL-CHILDSTATE-01-064-V2
- **标题**: 子任务状态传播——workflow_call 未拉起时父 workflow 不应假阳性完成
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
引用不存在的子 workflow 时父 workflow=failure，下游 skip。

## 做了什么
父 workflow 通过 uses: 调用不存在的 child_missing.yml；下游 job needs call_child。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | parent_status | positive | equals "failure" | COVERED | 引用不存在的 workflow 文件应导致调用失败 |
| 2 | downstream_status | positive | equals "skipped" | COVERED | needs 依赖失败时下游 skip |
| 3 | parent_status | negative | equals "success" | COVERED | 资源不存在时父不应假阳性 |
