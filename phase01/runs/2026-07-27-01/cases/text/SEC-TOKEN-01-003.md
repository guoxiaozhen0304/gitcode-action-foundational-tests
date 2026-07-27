用例 ID:   SEC-TOKEN-01-003
维度标签:   [security]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-037
参照来源:  inputs/security-knowledge/issues.md §2; inputs/gitcode-spec/security-permissions/token-permissions.md
母意图:    —
标题:      run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效

前置条件:
  - fixture 仓库可触发手动 workflow
  - harness 持有测试管理面凭据，可在 run 结束后持旧 token 发起 API 调用

操作步骤:
  1. 触发一个 workflow，run 进行中用 ATOMGIT_TOKEN 完成一次其权限内的只读操作（如 clone），并记录 run_id 与 token 获取时点（token 值经测试内部通道留存，不落日志）
  2. 待该 run 结束后，harness 持该旧 token 调用只读 API（GET /api/v8/repos/{owner}/{repo}/actions/runs/{run_id}）
  3. 对该 run 执行 rerun，观察 rerun 使用的 token 与原 token 的关系

预期结果:
  - run 进行中 token 在其权限范围内可用
  - run 结束后旧 token 调用任何 API 返回 401/403
  - rerun 签发新 token 或明确复用未过期 token，行为可判定

验证点:
  - [正向] run 进行中 token 可完成权限内只读操作
  - [负向] run 结束后旧 token 任何 API 调用绝不应成功（返回 401/403）
  - [非功能] rerun 的 token 签发行为可确定性判定（新 token 或明示复用）

清理:      重置 fixture 仓库
