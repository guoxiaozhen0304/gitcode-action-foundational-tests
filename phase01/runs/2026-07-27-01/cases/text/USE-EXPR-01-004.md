用例 ID:   USE-EXPR-01-004
维度标签:   ['usability']
维度:      usability
优先级:    P2
溯源意图:  INTENT-USE-039
参照来源:  inputs/workflow-samples/cann/ops-nn_action.yml; inputs/workflow-samples/testorg/full_pr.yaml; inputs/gitcode-spec/syntax-reference/expressions.md
母意图:    —
标题:      未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链）

前置条件:
  - 真实样本已就绪；文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 抽取样本中实际出现的表达式函数名集合
  2. 与 expressions.md 函数表函数名集合做包含检查
  3. 提交含 default() 条件表达式的探针 workflow 记录求值行为

预期结果:
  平台支持的函数应在函数表有完整条目；函数表函数名集合应包含样本实际出现的函数名集合

验证点:
  - [负向] 函数表缺少样本实际使用的函数每 1 个即一条缺陷
  - [正向] 记录 default() 的实际求值结果
  - [非功能] 若为内部函数，文档应说明不建议使用

清理:      无
