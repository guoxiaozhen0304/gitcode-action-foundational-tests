# USE-INPT-01-002

- 标题: 使用 boolean 类型 input 时报错应提示仅支持 string
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-INPT-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-008
参照来源:  inputs/gitcode-spec/
母意图:    —
标题:      使用 boolean 类型 input 时报错应提示仅支持 string

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 声明 workflow_dispatch inputs 的 type: boolean

预期结果:
  YAML 校验报错，明确说明 GitCode 仅支持 string 类型，并给出转换指引

验证点:
  - [负向] 不应静默降级为 string
  - [非功能] 报错中应包含 string 与类型转换相关提示

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | echo input (bad-input) | echo "dry_run=${{ inputs.dry_run }}"  | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不应静默降级为 string | 覆盖 | negative status assertion |
| 报错中应包含 string 与类型转换相关提示 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | COMPLETED | CONSISTENT | negative status assertion |
| 2 | error_message | nonfunctional | 报错信息必须包含 GitCode 仅支持 string 类型或等效说明，并给出在 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息必须包含 GitCode 仅支持 string 类型或等效说明，并给出在步骤中使用表达式转换类 |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
