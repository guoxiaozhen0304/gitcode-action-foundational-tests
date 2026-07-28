# COMP-BOUND-01-084
- **标题**: 路径与分支过滤组合及否定模式边界验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
branches + paths 组合过滤为 AND 关系，否定模式 ! 需与肯定模式组合生效。

## 做了什么
1. step `Print trigger context`：`echo "TRIGGER_REF=${{ atomgit.ref }}"` 和 `echo "filter_boundary_ok"`
2. 正向侧：推送匹配肯定且未被排除的分支/路径触发 workflow

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | 真实 push 触发，有 ${{ }} 表达式输出 |
| 2 | run_logs | positive | must_contain: TRIGGER_REF=refs/ | COVERED | `echo "TRIGGER_REF=${{ atomgit.ref }}"` 使用 ${{ }} 表达式 |
| 3 | run_logs | negative | llm_assisted | LLM_DEPENDENT | eval=llm_assisted，排除侧观测需多次运行对比 |
