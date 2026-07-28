# COMP-STAGES-01-004

- **标题**: map 形式 stages 按定义顺序串行执行（回归保护）
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证 map 形式 stages（build_stage 先于 test_stage）按定义顺序串行执行。

## 做了什么
build_stage: `echo "STAGE_ONE_DONE"`。test_stage: `echo "STAGE_TWO_DONE"`。均为字面量 echo，无 real 命令。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | STATUS_GUARANTEED | 所有 steps 均为 echo，无条件失败路径 |
| 2 | run_logs | positive | must_contain STAGE_ONE_DONE | TRIVIAL | step 仅 echo 字面量，无 ${{ }}、无 real 命令 |
| 3 | run_logs | positive | must_contain STAGE_TWO_DONE | TRIVIAL | step 仅 echo 字面量 |
| 4 | stage_order | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工对比日志时间戳 |
