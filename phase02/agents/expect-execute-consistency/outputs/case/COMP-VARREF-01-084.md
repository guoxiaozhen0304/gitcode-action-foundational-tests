# COMP-VARREF-01-084

- **标题**: ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
记录 `${gitcode_*}` 与 `${PIPELINE_*}` 风格占位符在单引号保留与双引号展开两种形式下的求值行为。

## 做了什么
probe job 中 echo 单引号保留形式 'GC_LIT=${gitcode_SOURCE_BRANCH}' 和双引号 shell 展开形式 "GC_SHELL=${gitcode_SOURCE_BRANCH}"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: GC_LIT= | COVERED | run: echo 'GC_LIT=${gitcode_SOURCE_BRANCH}' 输出该前缀 |
| 2 | run_logs | positive | must_contain: PL_LIT= | COVERED | run: echo 'PL_LIT=${PIPELINE_RUN_ID}' 输出该前缀 |
| 3 | interpolation_eval | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工对比 LIT 行与 SHELL 行判定平台求值行为 |
| 4 | silent_literal | negative | llm_assisted | LLM_DEPENDENT | 需人工判定未求值占位符是否静默流入下游 |
