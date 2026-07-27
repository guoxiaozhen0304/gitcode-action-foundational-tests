用例 ID:   REL-MATRIX-01-041
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-076
参照来源:  platform-config/README.md（max_matrix_size 未声明）; GitHub 行为（256 jobs/workflow 上限）
母意图:    REL-MATRIX-01-040（变体：300 组合越界行为）
标题:      matrix 组合数越界——300 组合超上限时应明确报错（含上限值）不得静默截断

前置条件:
  - fixture 仓库可提交大规模 matrix workflow
  - max-parallel=5 控速
  - 平台 max_matrix_size 未公开（探测型用例）

操作步骤:
  1. 提交 10×30=300 组合的 matrix workflow（每实例仅输出组合标记）
  2. 观察平台行为：全部展开、明确拒绝，或静默截断
  3. 若被拒绝，记录错误信息是否含实际上限数值

预期结果:
  - 300 组合若超上限应被明确报错，且错误信息含实际上限值
  - 若全部展开则记录实际上限 ≥300，回写 platform-config

验证点:
  - [正向] 拒绝时错误信息含实际上限数值；或全部展开且 job 数=300
  - [负向] 不应「声明 300 实际只跑 256（或前 N 个）且不报错」的静默截断（发现则升 P1）
  - [非功能] 实测上限值记录完整，可回写 platform-config/parity-matrix

清理:      无需重置（探测型，实例仅 echo 无副作用）
