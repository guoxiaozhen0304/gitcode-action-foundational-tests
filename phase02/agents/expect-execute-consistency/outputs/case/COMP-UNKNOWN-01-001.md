# COMP-UNKNOWN-01-001

- **标题**: 包含未知顶层字段的 workflow 触发 YAML 校验失败
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证含 unknown_field 的畸 YAML 被平台校验期拒绝。

## 做了什么
workflow 含 `unknown_field: true`（非法字段），step: `echo "should not run"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals validation_failed | COVERED | 畸 YAML 平台校验应拒绝，通过 batch_validate.py 验证（Calibration 8） |
| 2 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工判断报错信息 |
