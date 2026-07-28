# COMP-CTX-01-051
- **标题**: 上下文在 workflow job step 各级注入验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
atomgit / env / job 上下文在 workflow 级 env、job 级 env、step 级 run 中均可正常解析注入。

## 做了什么
1. workflow 级 env: `WF_REF: ${{ atomgit.ref }}`
2. job 级 env: `JOB_REF: ${{ env.WF_REF }}`
3. step `Step context`：`echo "WF_REF=$WF_REF"`、`echo "JOB_REF=$JOB_REF"`、`echo "JOB_STATUS=${{ job.status }}"`、`echo "ATOMGIT_REF=${{ atomgit.ref }}"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: WF_REF=refs/ | COVERED | $WF_REF 从 workflow 级 env 继承，值来自 ${{ atomgit.ref }} |
| 2 | run_logs | positive | must_contain: JOB_REF=refs/ | COVERED | $JOB_REF 从 job 级 env 继承，值来自 ${{ env.WF_REF }} |
| 3 | run_logs | positive | must_contain: JOB_STATUS= | COVERED | ${{ job.status }} 表达式输出 |
