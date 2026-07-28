# REL-ARTCONC-01-063
- **标题**: 制品并发写一致性——多 job 同时 upload-artifact 同名 artifact
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
多 job 并行 upload 同名 artifact 后下载内容确定、非混合态。

## 做了什么
matrix 3 实例并行，各生成 AAA/BBB/CCC 内容，upload 到同名 "concurrent-artifact"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_content | positive | in ['AAA','BBB','CCC'] | MISSING | workflow 仅有 upload step，无 download+verify step；断言依赖 harness 外部下载验证，YAML 内无对应步骤输出 |
| 2 | download_content | negative | contains_mixed="false" | MISSING | 同上，工作流自身不产出可判定混合态的输出；需 harness 侧外部分析 |
