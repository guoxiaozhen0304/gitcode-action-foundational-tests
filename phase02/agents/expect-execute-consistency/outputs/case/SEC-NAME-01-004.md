# SEC-NAME-01-004
- **标题**: 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值   - **维度**: 安全性   - **评级**: 部分不符
## 想测什么
job级env中与系统变量同名的用户定义不应覆盖平台注入的系统变量值。
## 做了什么
YAML workflow中job级env声明ATOMGIT_ENV=/tmp/fixture-shadow-path，step仅echo描述性文字。断言target job_env为抽象环境面，无具体检查逻辑。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | job_env | positive | equals "system_var_integrity_preserved" | UNVERIFIABLE | job_env为抽象目标，workflow步骤未实际比对系统变量值 |
| 2 | job_env | negative | must_not_equal "user_value_shadows_system_var" | UNVERIFIABLE | 同上，无具体检测步骤可对应 |
