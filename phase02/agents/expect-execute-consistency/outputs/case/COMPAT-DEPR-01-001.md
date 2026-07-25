# COMPAT-DEPR-01-001

- 标题: ::set-env:: 废弃命令应被拒绝或给出迁移指引
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-DEPR-01-001
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-012
参照来源:  inputs/gitcode-spec/syntax-reference/workflow-commands.md; inputs/github-reference/reference/workflow-commands.md
母意图:    —
标题:      ::set-env:: 废弃命令应被拒绝或给出迁移指引

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，在 run 步骤中使用废弃命令 `echo '::set-env name=MY_VAR::hello'`
  2. 触发 workflow

预期结果:
  - GitHub 行为：给出弃用警告，但命令仍生效（向后兼容）
  - GitCode 行为：应明确拒绝该命令或给出弃用警告及替代方案
  - 不应静默忽略导致用户误以为配置生效

验证点:
  - [负向] 不通过命令被静默忽略且 workflow 成功（用户误以为生效）
  - [正向] 系统给出明确响应：报错拒绝、或警告+替代方案
  - [正向] 若给出警告，应包含 `ATOMGIT_ENV` 文件协议的替代示例

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Use deprecated set-env (test-deprecated-set-env) | echo '::set-env name=MY_VAR::hello' echo "MY_VAR=$MY_VAR" echo "done"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不通过命令被静默忽略且 workflow 成功（用户误以为生效） | 覆盖 | LLM/nonfunctional assertion: 不应静默忽略导致 workflow 成功且 MY_VAR 未被设置 |
| 系统给出明确响应：报错拒绝、或警告+替代方案 | 覆盖 | LLM/nonfunctional assertion: 系统给出明确响应：报错拒绝、或警告+替代方案 |
| 若给出警告，应包含 `ATOMGIT_ENV` 文件协议的替代示例 | 覆盖 | LLM/nonfunctional assertion: 系统给出明确响应：报错拒绝、或警告+替代方案 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 不应静默忽略导致 workflow 成功且 MY_VAR 未被设置 | LLM_DEPENDENT | LLM/nonfunctional assertion: 不应静默忽略导致 workflow 成功且 MY_VAR 未被设置 |
| 2 | error_message | positive | 系统给出明确响应：报错拒绝、或警告+替代方案 | LLM_DEPENDENT | LLM/nonfunctional assertion: 系统给出明确响应：报错拒绝、或警告+替代方案 |
| 3 | error_message | positive | 若给出警告，应包含 ATOMGIT_ENV 文件协议的替代示例 | LLM_DEPENDENT | LLM/nonfunctional assertion: 若给出警告，应包含 ATOMGIT_ENV 文件协议的替代示例 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
