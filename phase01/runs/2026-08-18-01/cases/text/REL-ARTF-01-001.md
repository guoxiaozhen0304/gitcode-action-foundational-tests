用例 ID:   REL-ARTF-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-020
母意图:    —
标题:      上传 500MB artifact 观察上限与报错

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 生成 500MB 文件并作为 artifact 上传
  2. 验证上传成功或给出清晰的超限报错

预期结果:
  1. 上传成功或返回明确的大小限制错误

验证点:
  - [正向] workflow 完成
  - [正向] 日志包含上传结果

清理:      fixture
