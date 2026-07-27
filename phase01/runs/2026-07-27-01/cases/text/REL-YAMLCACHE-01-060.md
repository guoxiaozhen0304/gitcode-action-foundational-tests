用例 ID:   REL-YAMLCACHE-01-060
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-060
参照来源:  inputs/gitcode-spec/core-concepts/workflow-job-step-action.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      Workflow YAML 缓存失效——修改后无旧代码残留

前置条件:
  - 仓库具备 workflow 修改与触发权限

操作步骤:
  1. 第一轮执行记录输出 marker_v1（workflow 中仅启用 marker_v1 步骤）
  2. 修改 workflow 输出为 marker_v2 并 push（两轮执行：修改→push→再运行，由 harness 编排；
     YAML 层将 marker_v1/marker_v2 两个步骤并列呈现，harness 在第一轮运行前注释/移除
     marker_v2 步骤，第二轮启用 marker_v2 步骤并移除 marker_v1 步骤）
  3. 立即触发 workflow（第二轮运行）

预期结果:
  - 第一轮运行日志出现 marker_v1
  - 第二轮（新触发）运行日志中出现 marker_v2
  - 第二轮日志不应出现 marker_v1 缓存残留

验证点:
  - [正向] 第一轮日志打印 marker_v1
  - [正向] 第二轮日志打印 marker_v2
  - [负向] 第二轮日志不应打印 marker_v1

清理:      重置 fixture 仓库
