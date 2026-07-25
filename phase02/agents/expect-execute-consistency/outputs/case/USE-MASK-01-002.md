# USE-MASK-01-002

- 标题: 直接 echo secrets 值时文档描述的绕过风险与实际一致
- 维度: 易用性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   USE-MASK-01-002
维度标签:   ['usability', 'security']
维度:      usability/security
优先级:    P0
溯源意图:  INTENT-USE-016
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      直接 echo secrets 值时文档描述的绕过风险与实际一致

前置条件:
  - 仓库配置了 TEST_SECRET
  - 文档声明 echo secrets 可能绕过脱敏

操作步骤:
  1. 在 workflow 中直接执行 echo ${{ secrets.TEST_SECRET }}

预期结果:
  实际行为与文档声明一致；若确实可绕过，文档已给出缓解建议

验证点:
  - [负向] 若绕过确实发生，日志中可能出现明文
  - [非功能] 文档是否给出不要在 run 中直接 echo secrets 的缓解建议

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | direct echo secret (bypass-mask) | echo "secret=${{ secrets.TEST_SECRET }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 若绕过确实发生，日志中可能出现明文 | 未覆盖 | 缺少负向断言 |
| 文档是否给出不要在 run 中直接 echo secrets 的缓解建议 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | 若文档声明存在绕过风险，必须同时给出正确写法与错误写法的代码示例对比；仅有风险声 | LLM_DEPENDENT | LLM/nonfunctional assertion: 若文档声明存在绕过风险，必须同时给出正确写法与错误写法的代码示例对比；仅有风险声明而无缓解建议的视为可 |

### 问题

- 验证点 `若绕过确实发生，日志中可能出现明文` → 未覆盖: 缺少负向断言

---
