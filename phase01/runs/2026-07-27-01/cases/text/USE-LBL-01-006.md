用例 ID:   USE-LBL-01-006
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-040
参照来源:  inputs/workflow-samples/cann/; inputs/gitcode-spec/runner-management/selecting-runner-labels.md
母意图:    —
标题:      含资源池名的 runs-on 写法平台识别验证

前置条件:
  - 隔离测试实例配置了 dedicate-hosted 资源池

操作步骤:
  1. 以样本中的含资源池名写法声明 runs-on 并提交 workflow
  2. 观察平台是否识别并进入对应资源池调度

预期结果:
  平台应识别该写法并按资源池调度；识别结果回写文档一致性判定

验证点:
  - [正向] 平台应接受含资源池名的写法并成功调度
  - [非功能] 识别结果与文档缺失事实共同构成文档缺陷证据链（平台行为由 COMP-029 裁定）

清理:      无
