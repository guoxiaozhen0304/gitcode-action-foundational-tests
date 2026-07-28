# USE-ACT-01-004
- **标题**: 文档短名与市场名两种写法解析一致性验证
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补互补的负向断言（两种写法指向不同插件或其一报错而文档未说明即不通过），使判定闭环。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | deterministic criterion | ✅ COVERED | 两 job 分别真实引用 cache/AtomgitCache，harness 对比解析结果 |
| 2 | validation_result | negative | deterministic criterion | ✅ COVERED | 互补负向判定 |
