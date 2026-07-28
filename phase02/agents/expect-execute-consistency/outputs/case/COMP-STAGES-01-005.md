# COMP-STAGES-01-005

- **标题**: list 形式 stages 的实际处理裁定记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 list 形式 stages 的平台处理行为（校验报错或等价解析）。

## 做了什么
stages: - name: build-stage 的 list 格式，step 仅 `echo "LIST_STAGE_ONE"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_validation | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工记录平台校验结果 |
| 2 | run_logs | negative | eval=llm_assisted | LLM_DEPENDENT | 需人工判断 stages 是否被静默忽略 |
