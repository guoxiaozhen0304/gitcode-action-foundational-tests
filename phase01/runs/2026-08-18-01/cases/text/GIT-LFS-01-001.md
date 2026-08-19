用例 ID:   GIT-LFS-01-001
维度标签:   ['completeness', 'reliability']
维度:      completeness
优先级:    P1
溯源意图:  INTENT-GIT-003
母意图:    —
标题:      Git LFS 跟踪并推送大文件

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 初始化 Git LFS
  2. 跟踪一个大于 100MB 的文件
  3. 提交并推送
  4. 验证 LFS 对象上传成功

预期结果:
  1. LFS 对象上传成功
  2. 指针文件正确替换为 LFS 对象

验证点:
  - [正向] LFS 推送成功
  - [正向] 输出包含 LFS 成功提示

清理:      fixture
