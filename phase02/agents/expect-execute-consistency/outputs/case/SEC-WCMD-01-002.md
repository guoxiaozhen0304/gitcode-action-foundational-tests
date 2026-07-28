# SEC-WCMD-01-002
- **标题**: 跨运行 artifact 必须被视为不可信数据
- **维度**: 安全性
- **评级**: 部分不符

## 想测什么
不可信来源的 artifact 绝不应被特权运行隐式信任执行。

## 做了什么
workflow 下载 artifact 后仅 `echo "Artifact downloaded but not executed automatically"` — 未实际验证安全边界。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: auto_executed | TRIVIAL | `echo "Artifact downloaded but not executed automatically"` — 字面量声明，未执行任何 artifact 信任验证 |
| 2 | run_status | positive | completed | COVERED | 平台运行状态可观测 |

