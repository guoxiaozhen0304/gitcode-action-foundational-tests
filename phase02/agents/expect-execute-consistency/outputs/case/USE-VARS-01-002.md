# USE-VARS-01-002  - **标题**: 变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测   - **维度**: usability   - **评级**: 断言一致

## 想测什么

文档应列出平台支持的全部插值语法与 atomgit 上下文合法属性清单；样本出现而文档未列的数量应为 0

## 做了什么

- 1. 提交含美元单括号遗留插值与标准双花括号插值的探针 workflow
- 2. 观察各语法是否被求值
- 3. 对样本插值语法与属性名集合和文档清单做 diff

- - [正向] 记录遗留插值语法是否被求值
- - [负向] 若遗留语法已废弃，平台应在解析时给出 deprecation 警告而非静默
- - [非功能] atomgit 上下文属性应有完整且大小写明确的官方列表

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | eval=deterministic | COVERED | run_logs+deterministic: ${gitcode_SOURCE_BRANCH}等平台变量→真实求值; ${{ atomgit.repository }}→表达式求值→GENUINE |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 插值语法与属性名文档diff→确定性检查 |
