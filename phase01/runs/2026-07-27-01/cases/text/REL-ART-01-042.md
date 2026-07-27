用例 ID:   REL-ART-01-042
维度标签:   [reliability]
维度:      稳定性
优先级:    P2
溯源意图:  INTENT-REL-078
参照来源:  platform-config/README.md（max_artifact_size 未声明）
母意图:    —
标题:      artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝

前置条件:
  - fixture 仓库可触发大文件上传/下载 job（large runner，磁盘充足）
  - harness 可生成 2GB 文件并校验下载 MD5
  - 平台 max_artifact_size 未公开（探测型用例；5GB 档作为后续升档探测）

操作步骤:
  1. 上游 job 生成 2GB 文件并上传 artifact
  2. 下游 job 下载该 artifact 并校验 MD5 一致性
  3. 若上传被拒，记录错误信息是否含上限值；实测上限回写 platform-config

预期结果:
  - 上传完整成功且下载 MD5 一致；或上传阶段明确拒绝并给出上限值
  - 上传-下载完整性对账 100% 一致

验证点:
  - [正向] 上传成功 ↔ 下载 MD5 匹配；上传失败 ↔ 上传阶段明确报错
  - [负向] 不应「上传报成功但 artifact 列表查不到 / 下载 404 / MD5 不匹配」（发现则升 P1）
  - [非功能] 实测 artifact 上限值记录完整，可回写 platform-config

清理:      重置 fixture 仓库（清理大 artifact 存储）
