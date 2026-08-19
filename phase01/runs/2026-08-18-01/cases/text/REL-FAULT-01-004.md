用例 ID:   REL-FAULT-01-004
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-016
母意图:    —
标题:      断开 runner 外网后观察依赖下载失败与重试

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发需下载外部依赖的 workflow
  2. 在 pre_job 阶段断网
  3. 验证下载步骤失败并给出清晰报错
  4. 恢复网络后 rerun 成功

预期结果:
  1. 下载步骤因网络不通失败
  2. 错误信息包含网络/timeout/connection
  3. rerun 后成功

验证点:
  - [正向] 下载失败导致 job 失败
  - [正向] 报错清晰

清理:      fixture
