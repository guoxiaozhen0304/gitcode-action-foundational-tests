# COMP-VARREF-01-084
- **标题**: ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
探测平台对 `${gitcode_SOURCE_BRANCH}` / `${PIPELINE_RUN_ID}` 风格占位符的求值行为（运行前求值/原样保留/报错）。
## 做了什么
workflow_dispatch 触发，step 分别以单引号（字面保留）和双引号（shell 展开）echo 四种占位符。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: GC_LIT= | VACUOUS→COVERED | 单引号 echo 字面输出，无 ${{ }} 无 usesshell变量引用，echo 文本恒匹配 |
| 2 | run_logs | positive | must_contain: PL_LIT= | VACUOUS→COVERED | 同上 |
| 3 | interpolation_eval | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
| 4 | silent_literal | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
