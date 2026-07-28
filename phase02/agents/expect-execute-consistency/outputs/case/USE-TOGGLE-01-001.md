# USE-TOGGLE-01-001  - **标题**: 隐藏安全开关 ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS 默认值与文档缺失   - **维度**: usability   - **评级**: 断言一致

## 想测什么

所有影响安全行为的开关应在语法参考集中列出名称、默认值与安全影响；文档不应缺失

## 做了什么

- 1. 在 step 中读取该开关环境变量的实际默认值
- 2. 检查 workflow-commands.md 与 using-script-commands.md 是否列出该开关及其默认值与安全影响

- - [正向] 记录开关的实际默认值
- - [负向] 平台不应存在影响安全行为但文档未提的开关
- - [非功能] 开关清单应标注每个开关的安全影响与默认值

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | eval=deterministic | COVERED | run_logs+deterministic: ${ATOMGIT_ACTIONS_ALLOW_UNSECURE_COMMANDS}→真实平台环境变量读取→GENUINE |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 文档开关清单完整性确定性检查 |
