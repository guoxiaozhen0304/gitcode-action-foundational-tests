用例 ID:   REL-POST-01-001
维度标签:   [reliability, completeness]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-083
参照来源:  gitcode-spec/00-overview.md（post 后处理阶段，默认 run_always=true）
母意图:    —
标题:      post 后处理阶段失败语义——run_always=true 下 post 失败对 workflow 结论的影响应确定可预期

前置条件:
  - fixture 仓库可提交含顶层 post 阶段的 workflow
  - post 为 GitCode 特有阶段（GitHub 无对应物），失败语义需实测确认
  - 若平台拒绝 post 字段（unknown property），记为规格-平台差异并关联 COMP 维度

操作步骤:
  1. 组 a：主 steps 全部成功 + post 阶段 step 失败，观察 conclusion 与日志归因
  2. 组 b：主 step 失败 + post（run_always）正常，观察 post 是否仍执行
  3. 组 c：post 内 sleep 超过 job timeout 残余时间，观察是否 hang 不收敛

预期结果:
  - 三组终态均与文档声明语义一致：conclusion 与 post 失败的关系确定，日志明确归因 post 阶段
  - 主 step 失败时 post（run_always=true）仍执行
  - post 不 hang；超时后收敛

验证点:
  - [正向] post 失败时 conclusion 与文档语义一致，且日志明确归因 post 阶段
  - [正向] 主 step 失败时 post（run_always）仍执行
  - [负向] 不应 post 失败无任何标注而 conclusion=success（静默吞掉），除非文档明确如此
  - [负向] 不应 post 阶段 hang 导致 job 超过 timeout 仍不收敛

清理:      重置 fixture 仓库
