# COMP-SYSENV-01-059
- **标题**: ATOMGIT 系统环境变量关键变量存在性   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: SHA_SET=yes | COVERED | step echo SHA_SET=\$([ -n "\$ATOMGIT_SHA" ] && echo yes || echo no) |
| 2 | run_logs | positive | must_contain: REF_SET=yes | COVERED | step 条件检测 ATOMGIT_REF |
| 3 | run_logs | positive | must_contain: EVENT_NAME_SET=yes | COVERED | step 条件检测 ATOMGIT_EVENT_NAME |
| 4 | run_logs | positive | must_contain: WORKSPACE_SET=yes | COVERED | step 条件检测 ATOMGIT_WORKSPACE |
| 5 | run_logs | positive | must_contain: REPO_SET=yes | COVERED | step 条件检测 ATOMGIT_REPOSITORY |
| 6 | run_logs | positive | must_contain: RUN_ID_SET=yes | COVERED | step 条件检测 ATOMGIT_RUN_ID |
