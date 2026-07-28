# REL-YAMLCACHE-01-060
- **标题**: Workflow YAML 缓存失效——修改后无旧代码残留
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
关键修复：YAML 原同时含 marker_v1 和 marker_v2 两个 echo 步骤——run2 日志必然含 marker_v1，负向断言必败。本 YAML 应为「修改后」的 v2 版本，已删除 v1 步骤仅留 marker_v2，并加注释说明 v1 由 fixture/harness 在 run1 使用。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run1_logs | positive | contains marker_v1 | ✅ GENUINE | run1 由 fixture v1 workflow 产出 |
| 2 | run2_logs | positive | contains marker_v2 | ✅ GENUINE | run2 由本 v2 workflow 真实输出 |
| 3 | run2_logs | negative | contains marker_v1 | ✅ GENUINE | v2 无 v1 步骤，缓存失效则不残留 |
