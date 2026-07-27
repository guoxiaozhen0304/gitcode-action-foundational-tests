用例 ID:   SEC-NAME-01-004
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-041
参照来源:  inputs/gitcode-spec/security-permissions/using-secrets.md
母意图:    —
标题:      与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值

前置条件:
  - fixture 仓库可触发手动 workflow
  - 即使管理面命名拦截（SEC-NAME-01-003）存在旁路，本用例验证环境层第二道防线

操作步骤:
  1. 触发一个 workflow，在 job 级 env 中声明与平台系统变量同名的项（如 ATOMGIT_ENV，值指向测试占位路径）
  2. job 内读取该系统变量的实际取值，与平台注入值比对
  3. 记录 workflow 是否被拒绝、告警或静默放行

预期结果:
  - 系统变量取值与平台注入值一致，不被同名用户值替换；或平台拒绝/告警该声明
  - 写协议路径与凭据相关系统变量保持完整

验证点:
  - [正向] job 正常运行，平台注入的系统变量可用
  - [负向] job 环境中系统变量值绝不应被同名用户自定义值替换

清理:      重置 fixture 仓库
