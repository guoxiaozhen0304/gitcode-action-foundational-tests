# USE-LBL-01-005  - **标题**: runs-on 含资源池名写法的文档资源池清单 diff   - **维度**: usability   - **评级**: 断言一致

## 想测什么

样本中出现的资源池名应全部被文档列出，并说明与 os/arch/flavor 的组合规则

## 做了什么

- 1. 从全部样本中抽取 runs-on 首段出现的资源池名集合
- 2. 与 selecting-runner-labels.md 列出的资源池名集合做包含检查

- - [负向] 样本中出现的资源池名不在文档清单内每 1 个即一条缺陷
- - [非功能] 资源池名清单、flavor 范围与组合规则应集中在 Runner 文档一节

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 样本资源池名与文档清单集合diff |
