用例 ID:   REL-MATRIX-01-040
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-076
参照来源:  platform-config/README.md（max_matrix_size 未声明）; GitHub 行为（256 jobs/workflow 上限）
母意图:    —
标题:      matrix 组合数边界——256 组合（GitHub 上限）应全部展开或被明确拒绝

前置条件:
  - fixture 仓库可提交大规模 matrix workflow
  - max-parallel=5 控速，避免压垮共享 runner 池
  - 平台 max_matrix_size 未公开（探测型用例）

操作步骤:
  1. 提交 8×32=256 组合的 matrix workflow（每实例仅输出组合标记）
  2. 观察平台行为：全部展开（job 数=256）或明确报错
  3. 记录展开/入队时延与实测上限线索

预期结果:
  - 256 组合全部展开（job 数=256），或平台在解析/触发阶段明确报错
  - 展开/入队时延 ≤600 秒

验证点:
  - [正向] job 数与声明组合数一致（256），或收到明确错误
  - [负向] 不应「声明 256 实际只跑更少组合且不报错」的静默截断（发现则升 P1）
  - [非功能] 展开/入队时延 ≤600 秒

清理:      无需重置（探测型，实例仅 echo 无副作用）
