# COMPAT-LIMIT-01-002
- **标题**: workflow_dispatch 输入数量上限与非默认分支可用性
- **维度**: 兼容性
- **优先级**: P2
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
workflow 步骤由裸 echo 改为增输 DISPATCH_PROBE_BRANCH=${{ atomgit.ref }}（GENUINE），供非默认分支可用性核对；加注释说明探针性质。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | save_result | positive | llm_assisted | 🔶 LLM_DEPENDENT | 26 个 inputs 的保存期响应（报错/截断/接受）是被测未知数 |
| 2 | save_result | negative | llm_assisted | 🔶 LLM_DEPENDENT | 静默接受判定依赖保存校验响应 |
| 3 | run_list | positive | llm_assisted | 🔶 LLM_DEPENDENT | 非默认分支 dispatch 可用性需观察运行列表 |

### 残留问题
本质不可确定化：inputs 上限与非默认分支可用性均为平台行为探针，已保留 llm_assisted 并在 YAML 中注释说明。
