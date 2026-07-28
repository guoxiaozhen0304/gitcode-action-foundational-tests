# COMPAT-EXPR-01-002
- **标题**: success() 函数的处理行为差异
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
workflow 重写对齐规格：job-b 的 step 真实使用 `if: ${{ success() }}` 作为探针（原 YAML 完全未使用 success()）；job-a 改为 checkout + 真实校验（ls 非空，失败 exit 1），run_status 不再 TRIVIAL；保存期接受/拒绝判定按 workflow_parse llm 模式（与 COMP-JOB-01-066 等既有用例一致）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | job-a 有真实失败路径 |
| 2 | run_logs | positive | must_contain JOB_A_VERIFIED | ✅ GENUINE | 真实命令校验后输出 |
| 3 | workflow_parse | positive | llm_assisted | 🔶 LLM_DEPENDENT | 平台对 success() 的保存期响应（接受/拒绝）判读 |
| 4 | workflow_parse | negative | llm_assisted | 🔶 LLM_DEPENDENT | 静默忽略判定 |

### 残留问题
success() 接受与否的判读依赖保存期响应内容，保留 llm_assisted（YAML 已注释）；可执行部分已全部确定化。
