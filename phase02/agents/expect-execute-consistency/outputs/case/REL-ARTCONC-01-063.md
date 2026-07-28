# REL-ARTCONC-01-063
- **标题**: 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
matrix 3 实例并行上传同名 artifact，验证下载内容确定（非混合态），内容完整无损。
## 做了什么
YAML 使用 matrix instance=[1,2,3] 并行，每实例用 python3 生成不同内容文件（A/B/C），通过 upload-artifact action 上传到同名 `concurrent-artifact`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_content | positive | 在['AAA','BBB','CCC']中 | COVERED | YAML 使用 python3 真实命令生成不同内容，upload-artifact action 上传，assertion 判定下载内容归属于确定单一值 |
| 2 | download_content | negative | contains_mixed=false | COVERED | YAML 显式 asserts 不含混合态，对应文本"不应出现 ABA/BAB 等混合态" |
