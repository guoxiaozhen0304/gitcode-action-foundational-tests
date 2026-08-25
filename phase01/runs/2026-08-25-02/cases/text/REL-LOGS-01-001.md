用例 ID:   REL-LOGS-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-009
母意图:    —
标题:      单 step 输出 50MB 文本日志的实时性与完整性

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发输出 50MB 日志的 workflow
  2. 通过 API 下载 job 日志
  3. 验证日志开头、中间、尾部均完整
  4. 验证实时性（无过度延迟）

预期结果:
  1. 日志文件大小接近 50MB
  2. 日志尾部包含 LOG_END_MARKER
  3. 下载时间合理

验证点:
  - [正向] 日志尾部完整
  - [非功能] 日志下载在 5 分钟内完成

清理:      fixture
