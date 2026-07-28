# COMPAT-MATRIX-01-003
- **标题**: matrix 三维展开不被支持时的差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
workflow 已真实声明三维 matrix 并逐维输出 ${{ matrix.* }} 值（GENUINE，无需改动）；rubric 明确化（8 实例标记/保存期报错），加注释说明探针性质。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | llm_assisted | 🔶 LLM_DEPENDENT | 三维 matrix 被接受展开还是拒绝是被测未知数 |
| 2 | run_status | negative | llm_assisted | 🔶 LLM_DEPENDENT | 静默忽略（部分实例且无报错）需对比实例数判定 |

### 残留问题
本质不可确定化：三维 matrix 支持与否是平台探明对象，已保留 llm_assisted 并在 YAML 中注释说明。
