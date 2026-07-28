# SEC-ORG-01-001
- **标题**: 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
范围内仓库可正常引用组织级secret，范围外仓库绝不应读到原值，可见性变更即时生效。
## 做了什么
YAML workflow中step echo ${{ secrets.ORG_SHARED_KEY }}。trigger params含repo_scope: outside_visibility。第三个断言target visibility_change为抽象面。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "ORG_SHARED_KEY" | COVERED | 日志搜索secret原值 |
| 2 | run_logs | positive | equals "empty_or_error_outside_scope" | COVERED | 范围外仓库的输出结果可判定 |
| 3 | visibility_change | nonfunctional | equals "effective_immediately_no_cache_window" | UNVERIFIABLE | visibility_change为抽象目标，无workflow步骤对应检测 |
