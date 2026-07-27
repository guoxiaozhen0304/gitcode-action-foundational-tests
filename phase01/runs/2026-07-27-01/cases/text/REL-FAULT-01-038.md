用例 ID:   REL-FAULT-01-038
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-081
参照来源:  testing-focus.md §8/§12; gitcode-spec（upload-download-artifacts）
母意图:    —
标题:      故障注入——artifact 上传中途 runner 被杀，半成品不得作为有效 artifact 出现

前置条件:
  - 具备故障注入能力（runner 进程 SIGKILL）
  - fixture 仓库可接受破坏性测试
  - 备有 100MB 测试文件

操作步骤:
  1. 触发 job：生成 100MB 文件并执行 upload-artifact
  2. 上传进度约 50% 时对 runner 进程注入 SIGKILL
  3. 检查 artifact 列表与可下载性；随后 rerun 同名上传并校验 MD5

预期结果:
  - job 状态=failure；该 artifact 在列表中不存在或被明确标记 incomplete
  - 不存在「可下载且 HTTP 200 但内容截断」的 artifact
  - rerun 后同名 artifact 上传成功、下载 MD5 一致

验证点:
  - [正向] job 状态=failure，半成品不可见或明确标记 incomplete
  - [负向] 不应存在可下载但内容截断的 artifact（数据完整性红线；发现即 blocker 级缺陷）
  - [正向] rerun 后同名 artifact 重传成功且 MD5 一致

恢复预期:  明确报错（job 标记失败），rerun 后自动恢复成功
清理:      重置 fixture 仓库（清理残留 artifact）
