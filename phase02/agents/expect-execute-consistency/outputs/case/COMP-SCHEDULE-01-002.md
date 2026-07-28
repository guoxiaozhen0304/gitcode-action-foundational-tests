# COMP-SCHEDULE-01-002

- **标题**: 非默认分支的 schedule workflow 不应触发
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证非默认分支的 schedule workflow 不触发（差异记录类用例）。

## 做了什么
workflow 指定 `repo_fixture: multi-branch` 在非默认分支创建，step 仅 `echo "should not run"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | negative | equals no_run_on_non_default_branch | COVERED | "无运行"即观测点；差异记录类用例（Calibration 7）；type=negative 直接覆盖 |
