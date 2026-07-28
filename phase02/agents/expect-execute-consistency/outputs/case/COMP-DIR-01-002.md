# COMP-DIR-01-002

- **标题**: .github/workflows/ 下的 YAML 不被识别为 workflow
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `.github/workflows/` 目录下的 YAML 不被平台识别为 workflow，push 事件不产生对应运行。

## 做了什么
YAML 位于 `.github/workflows/` 目录，workflow 字段为空（无内联 workflow 步骤）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | equals: no_run_from_github_dir | COVERED | 差异记录类用例：期望结果就是"不产生运行"，无运行即验证通过。harness 通过运行列表确认没有源自 .github/workflows/ 的运行 |
