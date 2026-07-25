# USE-SECNAME-01-002

- 标题: Secret 名称以数字开头时应给出命名规则错误
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-SECNAME-01-002
维度标签:   ['usability', 'security']
维度:      usability/security
优先级:    P1
溯源意图:  INTENT-USE-028
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      Secret 名称以数字开头时应给出命名规则错误

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 在 workflow 中引用 ${{ secrets.1SECRET }}

预期结果:
  系统给出命名规则提示，说明允许字符与格式

验证点:
  - [负向] 不应仅报 Secret not found
  - [非功能] 报错中是否包含命名格式说明

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | use invalid secret name (bad) | echo "val=${{ secrets.1SECRET }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应仅报 Secret not found | 覆盖 | negative status assertion |
| 报错中是否包含命名格式说明 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含 Secret 名称规则或命名格式相关说明，并列出允许字符（大写 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含 Secret 名称规则或命名格式相关说明，并列出允许字符（大写字母、数字、下划线） |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
