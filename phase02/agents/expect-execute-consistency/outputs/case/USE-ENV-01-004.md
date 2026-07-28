# USE-ENV-01-004  - **标题**: job env 在 shell 层与表达式层取值一致性（文档承诺兑现验证）   - **维度**: usability   - **评级**: 断言一致

## 想测什么

文档承诺 job env 对该 job 内所有 step 可见；shell 层与表达式层取值应一致；不一致即文档承诺未兑现

## 做了什么

- 1. 在 job 级声明 env，在同一 job 的 step 中分别以 shell 变量与表达式两种方式读取并打印
- 2. 比对两层取值是否一致

- - [正向] 表达式层应取到 job env 值
- - [正向] shell 层应取到 job env 值（文档明文承诺）；取不到即实证文档承诺未兑现
- - [非功能] 平台行为修复前文档应给出显式 workaround

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains=`expr=[prod]` | COVERED | run_logs+contains: ${{ env.APP_ENV }}表达式求值→GENUINE; 平台日志可验证 |
| 2 | run_logs | positive | contains=`shell=[prod]` | COVERED | run_logs+contains: shell变量$APP_ENV由job env注入→GENUINE; 运行后可观察 |
| 3 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 文档承诺与平台行为对照可确定性验证 |
