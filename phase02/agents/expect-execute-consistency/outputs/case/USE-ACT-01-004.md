# USE-ACT-01-004
- **标题**: 文档短名与市场名两种写法解析一致性验证
- **维度**: usability
- **评级**: 断言一致

## 想测什么
文档短名与市场目录名引用同一插件时，平台应解析到同一插件。

## 做了什么
两个 job 分别使用 `uses: checkout`/`uses: cache`（短名）和 `uses: AtomgitCache`（市场名）。断言指向 validation_result。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | eval:deterministic | COVERED | 两个 job uses 真实 action 引用，平台解析结果可观察 |
| 2 | validation_result | negative | eval:deterministic | COVERED | 同上，两种写法指向不同插件即为不合格 |
