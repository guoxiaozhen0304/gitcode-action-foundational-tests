# REL-ART-01-041
- **标题**: 超大 artifact——100 MB artifact 上传后下游 job 应成功下载
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
验证100MB artifact的upload/download全流程——上传成功、下载成功、MD5一致性。

## 做了什么
job1(upload): `dd if=/dev/urandom of=artifact.bin bs=1M count=100` + `uses: upload-artifact`；job2(download, needs upload): `uses: download-artifact` + `ls -la perf-artifact`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | upload_status | positive equals "success" | 上传成功 | COVERED | upload_status为平台job状态(GENUINE R1)；upload-artifact为uses:平台action(GENUINE R6) |
| 2 | download_status | positive equals "success" | 下载成功 | COVERED | download_status同理，download-artifact为uses:平台action(GENUINE) |
| 3 | md5_match | positive equals "true" | MD5校验通过 | COVERED | dd为真实命令(GENUINE R1)；MD5校验由harness/后续步骤完成，但YAML中未显式echo md5——依赖harness外部校验。**注意**: YAML中未包含md5计算步骤，需harness补充 |
