用例 ID:   REL-FAULT-01-001
维度标签:   ['reliability']
维度:      reliability
优先级:    P1
溯源意图:  INTENT-REL-013
母意图:    —
标题:      runner 磁盘写满后 job 行为与报错清晰度

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 触发 workflow 并在执行中注入磁盘满故障
  2. 观察 job 失败模式
  3. 验证报错是否指明磁盘空间不足

预期结果:
  1. job 因磁盘满失败
  2. 错误信息包含磁盘/空间/no space
  3. 后续 step 被跳过

验证点:
  - [正向] job 失败
  - [正向] 报错清晰
  - [负向] 后续 step 未执行

清理:      fixture
