# COMP-DIR-01-001

- **标题**: .gitcode/workflows/ 下的 YAML 被正确识别并触发
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `.gitcode/workflows/ci.yml` 被平台识别为合法 workflow，push 事件触发执行。

## 做了什么
workflow 在 `push` 事件下只 echo `"workflow recognized"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | push 触发 → workflow 成功执行 |
| 2 | run_file_path | positive | equals: .gitcode/workflows/ci.yml | COVERED | 平台级元数据校验，harness 验证运行记录的 file_path |
