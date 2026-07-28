# USE-PERM-01-002
- **标题**: 使用 GitHub 权限域命名时报错应给出 GitCode 对照表
- **维度**: 易用性/兼容性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
新增确定性断言 error_message must_contain permissions（平台 unknown property 报错含字段名）；对照表质量保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals COMPLETED | ✅ GENUINE | permissions 为平台不支持字段应拒绝 |
| 2 | error_message | positive | must_contain permissions | ✅ COVERED | 报错应含字段名（固定串） |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | GitHub/GitCode 命名对照质量判读 |

### 残留问题
保留 llm_assisted（文案质量部分）。
