# COMP-RUNNER-01-082

- **标题**: flow-mapping 写法 runs-on 的处理结果裁定
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 runs-on 用 flow-mapping 写法 `{ubuntu-24, x64, small}` 的平台处理行为。

## 做了什么
runs-on: {ubuntu-24, x64, small}，step 仅 `echo "FLOW_MAPPING_RUNNER_RAN"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_validation | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工记录平台校验期行为 |
| 2 | runner_mismatch | negative | eval=llm_assisted | LLM_DEPENDENT | 需人工判断调度是否非预期 |
