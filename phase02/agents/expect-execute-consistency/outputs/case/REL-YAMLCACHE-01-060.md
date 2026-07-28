# REL-YAMLCACHE-01-060
- **标题**: Workflow YAML 缓存失效——修改后无旧代码残留
- **维度**: reliability
- **评级**: 断言一致

## 想测什么
修改 workflow 后新触发执行新版本，旧版本 marker 不应残留。

## 做了什么
workflow 中仅含 marker_v2 echo 步骤；harness 两轮执行：run1 用 v1 workflow、run2 用本 YAML(v2)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run1_logs | positive | contains "marker_v1" | COVERED | 对应"第一轮日志出现 marker_v1"；platform-logs→GENUINE |
| 2 | run2_logs | positive | contains "marker_v2" | COVERED | 对应"第二轮日志出现 marker_v2"；workflow 中 echo marker_v2→GENUINE |
| 3 | run2_logs | negative | contains "marker_v1" | COVERED | 对应"第二轮日志不应出现 marker_v1"；如果平台缓存失效，run2 不会输出该串→NOT_VACUOUS（non-trivial observable） |
