# COMPAT-LIMIT-01-001
- **标题**: 单次推送多个 tag 的事件生成上限行为
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
workflow 步骤增强：除 TAG_RUN_REF 外增输 TAG_RUN_SHA（均为 ${{ }} 表达式，GENUINE），为 run 计数对账提供材料；rubric 明确化并加注释说明探针性质。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | positive | llm_assisted | 🔶 LLM_DEPENDENT | 4 个 tag 实际生成 run 数（4/部分/0）是被测未知数 |
| 2 | run_list | negative | llm_assisted | 🔶 LLM_DEPENDENT | 静默丢弃判定需事后查询运行列表 |

### 残留问题
本质不可确定化：平台对批量 tag push 的事件生成上限是被探明对象，workflow 步骤无法产出确定期望值。已保留 llm_assisted 并在 YAML 中注释说明。
