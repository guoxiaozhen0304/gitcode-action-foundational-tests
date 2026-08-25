用例 ID:   REL-PKG-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-022
母意图:    —
标题:      500MB 包中途断网观察断点续传或重试

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 上传 500MB 包到包仓库
  2. 中途模拟断网
  3. 验证客户端是否重试或支持断点续传
  4. 验证服务端最终状态一致

预期结果:
  1. 上传最终成功，或报错清晰可恢复
  2. 无部分文件残留导致元数据不一致

验证点:
  - [正向] 返回预期状态码

清理:      fixture
