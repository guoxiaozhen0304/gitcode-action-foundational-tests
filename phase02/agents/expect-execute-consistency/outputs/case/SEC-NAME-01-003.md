# SEC-NAME-01-003
- **标题**: 可遮蔽系统变量的 secret 命名（ATOMGIT_前缀/非法字符/数字开头）创建时必须被拒
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
加注释说明平台操作型设计（harness 经 secret 管理 API 逐一尝试创建，workflow null 属设计）；报错文案判读保留 llm。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | secret_mgmt_api | positive | equals valid_name_created | ✅ COVERED | 合法名创建可判定 |
| 2 | secret_mgmt_api | negative | must_not_equal invalid_name_accepted | ✅ COVERED | 非法名拒绝可判定 |
| 3 | error_message | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 报错文案是否指明命名规则属判读 |

### 残留问题
报错文案质量判读保留 llm_assisted（YAML 已注释）。
