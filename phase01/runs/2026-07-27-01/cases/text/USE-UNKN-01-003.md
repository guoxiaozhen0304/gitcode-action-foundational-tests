用例 ID:   USE-UNKN-01-003
维度标签:   ['usability', 'compatibility']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-036
参照来源:  inputs/workflow-samples/cann/ops-nn_action.yml; inputs/gitcode-spec/writing-pipelines/configure-steps.md
母意图:    —
标题:      step 标识 id 与 identifier 命名双轨的接受一致性与文档说明

前置条件:
  - 隔离测试实例可正常调度 workflow；真实样本 cann/ops-nn_action.yml 已就绪

操作步骤:
  1. 分别用文档字段名与样本字段名声明 step 标识并提交
  2. 记录平台对两种写法的接受与行为是否一致
  3. 检查文档是否说明双名关系

预期结果:
  若两种写法等价，文档应显式声明；若只接受其一，平台应对另一种给出明确报错而非静默忽略

验证点:
  - [正向] 记录平台对两种写法的接受情况与行为一致性
  - [负向] 两种写法并存且行为不同而文档未说明差异即不合格
  - [非功能] 平台对废弃名应给出 deprecation 警告而非静默接受

清理:      无
