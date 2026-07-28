# COMPAT-MATRIX-01-004
- **标题**: matrix include 无基础变量不被支持时的差异
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
workflow 已真实声明 include-only matrix 并输出 ${{ matrix.* }} 值（GENUINE，无需改动）；rubric 明确化，加注释说明探针性质。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | llm_assisted | 🔶 LLM_DEPENDENT | include 无基础变量被接受还是拒绝是被测未知数 |
| 2 | run_status | negative | llm_assisted | 🔶 LLM_DEPENDENT | 静默忽略判定需观察实例生成情况 |

### 残留问题
本质不可确定化：平台探针，已保留 llm_assisted 并在 YAML 中注释说明。
