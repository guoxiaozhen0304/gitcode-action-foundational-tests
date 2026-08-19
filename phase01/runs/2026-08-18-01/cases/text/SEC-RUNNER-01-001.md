用例 ID:   SEC-RUNNER-01-001
维度标签:   ['security']
维度:      security
优先级:    P1
溯源意图:  INTENT-SEC-016
母意图:    —
标题:      复用型 Runner 不得跨 job 残留敏感文件或环境变量

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api
  - 配置 secrets: ['DEPLOY_TOKEN']

操作步骤:
  1. job-a 写入含 secret 的文件到 /tmp 并设置环境变量
  2. job-b 检查 /tmp 和环境变量
  3. 验证无残留

预期结果:
  1. job-b 中 /tmp/secret_file.txt 不存在或内容为空
  2. SECRET_VAR 未定义或为空

验证点:
  - [负向] job-b 日志不含 secret
  - [正向] workflow 完成

清理:      fixture
