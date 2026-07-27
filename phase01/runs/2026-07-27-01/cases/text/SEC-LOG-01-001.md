用例 ID:   SEC-LOG-01-001
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-040
参照来源:  inputs/security-knowledge/issues.md §3; inputs/gitcode-spec/running-pipelines/view-job-logs.md
母意图:    —
标题:      无权限角色读取/下载运行日志必须被拒，过期日志绝不应可恢复

前置条件:
  - fixture 仓库存在已完成的 run
  - 存在无日志查看权限的测试成员角色
  - harness 可访问超过保留期的历史 run 记录（或平台声明的保留期配置）

操作步骤:
  1. 以有权限成员身份查看并下载该 run 日志（GET /api/v8/repos/{owner}/{repo}/actions/runs/{run_id}/jobs/{job_id}/download-log）
  2. 以无权限角色身份重复上述查看/下载请求，记录响应码
  3. 访问超过保留期的历史 run 日志，记录响应

预期结果:
  - 有权限成员正常查看/下载
  - 无权限角色请求返回 403/404
  - 过期日志返回不存在，不可恢复

验证点:
  - [正向] 有权限成员可查看/下载日志
  - [负向] 无权限角色绝不应读取或下载日志
  - [负向] 过期日志绝不应可恢复

清理:      重置 fixture 仓库
