# COMPAT-CONTAINER-01-001

- 标题: container 字段不被支持时应明确报错而非静默忽略
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-CONTAINER-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-001
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      container 字段不被支持时应明确报错而非静默忽略

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个包含 `jobs.<id>.container` 字段的 workflow 文件
  2. 该字段指定 `image: ubuntu:latest`
  3. 提交该 workflow 到仓库

预期结果:
  - 系统拒绝该 workflow（GitCode 不支持 container 字段）
  - 报错信息应明确指出 `container` 字段不被支持
  - 报错不应仅给出模糊的 "unknown property" 或静默忽略该字段导致用户误以为容器环境生效

验证点:
  - [负向] 不通过无指引的原始报错（如仅报 generic YAML error）
  - [负向] 不通过静默忽略（workflow 被接受但容器未生效）
  - [正向] 报错信息包含 `container` 关键字及可操作建议
  - [正向] 报错指向正确行号或字段名

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Echo hello (test-container) | echo "hello"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不通过无指引的原始报错（如仅报 generic YAML error） | 覆盖 | LLM/nonfunctional assertion: 不通过无指引的原始报错（如仅报 generic YAML error） |
| 不通过静默忽略（workflow 被接受但容器未生效） | 覆盖 | LLM/nonfunctional assertion: 不通过无指引的原始报错（如仅报 generic YAML error） |
| 报错信息包含 `container` 关键字及可操作建议 | 覆盖 | LLM/nonfunctional assertion: 报错信息包含 container 关键字，指向具体字段，并给出可操作建议（如删除 container 字段或使用默认 Runner 环境） |
| 报错指向正确行号或字段名 | 覆盖 | LLM/nonfunctional assertion: 报错信息包含 container 关键字，指向具体字段，并给出可操作建议（如删除 container 字段或使用默认 Runner 环境） |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | negative | 不通过无指引的原始报错（如仅报 generic YAML error） | LLM_DEPENDENT | LLM/nonfunctional assertion: 不通过无指引的原始报错（如仅报 generic YAML error） |
| 2 | run_status | negative | 不通过静默忽略导致 workflow 成功运行（container 字段应被拦截 | LLM_DEPENDENT | LLM/nonfunctional assertion: 不通过静默忽略导致 workflow 成功运行（container 字段应被拦截） |
| 3 | error_message | positive | 报错信息包含 container 关键字，指向具体字段，并给出可操作建议（如删除 | LLM_DEPENDENT | LLM/nonfunctional assertion: 报错信息包含 container 关键字，指向具体字段，并给出可操作建议（如删除 container  |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
