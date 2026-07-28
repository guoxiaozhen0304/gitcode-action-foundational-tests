# REL-ART-01-042
- **标题**: artifact 大小上限探测——2GB 上传应完整成功或上传阶段明确拒绝
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
探测artifact 2GB上传的边界行为——上传成功且MD5一致，或上传阶段明确拒绝并给出上限值。

## 做了什么
job1(upload): `dd if=/dev/urandom of=big-artifact.bin bs=1M count=2048` + `md5sum big-artifact.bin > expected.md5` + `uses: upload-artifact`；job2(download, needs upload): `uses: download-artifact` + `md5sum big-artifact-2gb`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | upload_outcome | positive | 上传成功或明确拒绝 | COVERED | dd+upload-artifact(GENUINE R1+R6)；上传结局通过job状态+error可观测 |
| 2 | md5_match | positive | 上传成功时MD5一致 | COVERED | md5sum为真实命令(GENUINE R1)；上传job生成expected.md5，下载job校验 |
| 3 | ghost_artifact_detected | negative | 不应上传报成功但下载404 | COVERED | upload-artifact+download-artifact为uses(GENUINE R6)；上下游job通过needs关联 |
| 4 | measured_artifact_limit | nonfunctional | 实测上限值记录完整 | LLM_DEPENDENT | R5: nonfunctional；需人工/LLM回写platform-config |
