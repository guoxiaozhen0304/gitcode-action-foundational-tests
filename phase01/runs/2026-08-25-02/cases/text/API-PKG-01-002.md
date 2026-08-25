用例 ID:   API-PKG-01-002
维度标签:   ['completeness', 'compatibility']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-PKG-001
母意图:    —
标题:      上传 Docker 镜像并验证拉取

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 推送 Docker 镜像到包仓库
  2. 验证镜像可通过 API 查询

预期结果:
  1. 镜像上传成功
  2. API 可查询到镜像标签

验证点:
  - [正向] 镜像上传成功

清理:      fixture
