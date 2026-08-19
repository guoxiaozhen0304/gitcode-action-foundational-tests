用例 ID:   SEC-INJ-01-002
维度标签:   ['security']
维度:      security
优先级:    P0
溯源意图:  INTENT-SEC-004
母意图:    —
标题:      分支名含 shell 元字符时不应破坏 run 脚本

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 推送分支名含 shell 元字符（如 `feat;rm -rf /`）
  2. 验证 workflow 正常执行
  3. 验证命令未被破坏

预期结果:
  1. 分支名被正确引用
  2. rm -rf 未执行

验证点:
  - [负向] 未执行破坏性命令
  - [正向] workflow 正常完成

清理:      fixture
