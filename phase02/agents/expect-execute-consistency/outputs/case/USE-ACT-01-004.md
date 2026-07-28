# USE-ACT-01-004
- **标题**: 文档短名与市场名两种写法解析一致性验证
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
分别用文档短名（cache）与市场目录名（AtomgitCache）引用同一插件，验证解析到同一插件。

## 做了什么
workflow 中分别使用 `uses: cache` 和 `uses: AtomgitCache` 引用。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | 记录两种写法的解析结果是否一致 | COVERED | harness 分别运行两个 job 并对比解析结果，可判定一致性 |
| 2 | validation_result | negative | 两种写法指向不同插件或其一报错而文档未说明即不合格 | COVERED | 与上一条为互补判定，harness 对比后判定 |

