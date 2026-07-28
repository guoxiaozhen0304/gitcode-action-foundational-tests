# COMP-ARTIFACT-01-003

- **标题**: artifact 保留期设置生效
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `retention-days: 1` 设置后在保留期内可下载、超过保留期后不可下载。

## 做了什么
workflow 上传 artifact 并设置 `retention-days: 1`；测试 harness 在保留期内和超过保留期后分别验证可用性。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | artifact_available | positive | equals: yes_within_retention | COVERED | harness 在保留期内检测 artifact 是否可下载，workflow 实际产生的 artifact 是检测对象 |
| 2 | artifact_available_after_expiry | negative | equals: no_after_1_day | COVERED | harness 在超过保留期后检测 assert 404，外部验证机制有效 |
