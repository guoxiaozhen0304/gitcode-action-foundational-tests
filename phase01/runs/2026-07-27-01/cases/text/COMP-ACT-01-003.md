用例 ID:   COMP-ACT-01-003
维度标签:   [completeness, reliability]
维度:      完备性
优先级:    P1
溯源意图:  INTENT-COMP-028
参照来源:  runs/2026-07-27-01/intents/spec.md; inputs/gitcode-spec/action-development/top-level-fields.md L111-144; 关联上轮 GAP-008
母意图:    —
标题:      手动取消时 action runs.post 由调度服务调用

前置条件:
  - 仓库已启用 AtomGit Action
  - fixture 仓库含声明 runs.post 的本地 action（main 长时间运行便于中途取消，post 输出 POST_CLEANUP_DONE 标记）

操作步骤:
  1. 手动触发 workflow，待 job 运行至约 50% 时手动取消
  2. 观察 action 的 post 入口是否被调度服务调用（以清理副作用标记为证据）
  3. 记录取消到 post 被调用的时延，及运行终态

预期结果:
  - 取消运行中的 workflow 时，声明 runs.post 的 action 的 post 入口被调用；运行进入 cancelled 终态；取消到 post 调用的时延有上界（记录实测值）

验证点:
  - [正向] 取消后 post 逻辑被执行（日志含清理标记）
  - [负向] 取消后不应出现 post 未执行且无痕迹可查
  - [非功能] 取消到 post 被调用的时延记录实测上界；post 失败不改变 cancelled 终态

清理:      重置 fixture 仓库
