用例 ID:   API-PKG-01-001
维度标签:   ['completeness', 'compatibility']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-PKG-001
母意图:    —
标题:      上传 npm 格式包并验证元数据

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 上传 npm 包
  2. 验证包列表包含该包
  3. 验证版本号正确

预期结果:
  1. 包上传成功
  2. 版本号与上传一致

验证点:
  - [正向] 包上传成功

清理:      fixture
