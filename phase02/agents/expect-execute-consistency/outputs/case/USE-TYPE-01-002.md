# USE-TYPE-01-002

- 标题: 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示
- 维度: 易用性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

用例 ID:   USE-TYPE-01-002
维度标签:   ['usability', 'compatibility']
维度:      usability/compatibility
优先级:    P1
溯源意图:  INTENT-USE-009
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      使用 GitHub types 命名 opened/synchronize 时应给出可理解提示

前置条件:
  - workflow 文件位于 .gitcode/workflows/

操作步骤:
  1. 配置 on: pull_request: types: [opened, synchronize]

预期结果:
  YAML 校验报错，列出 GitCode 支持的 types 取值，并给出 GitHub 对应关系

验证点:
  - [负向] 不应静默通过校验并在运行时永远不被触发
  - [非功能] 报错中应列出 merge/open/reopen/update 并指出对应关系

清理:      无

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | echo event | run: echo "hello" | 否 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  pull_request:
    types:
      - opened
      - synchronize
    branches: [main]
jobs:
  bad-types:
    name: test github types error
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: echo event
        run: |
          echo "hello"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | pull_request |
| as | maintainer |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 不应静默通过校验并在运行时永远不被触发 | ✅ COVERED | 断言 type=negative target=run_status equals COMPLETED，harness 可直接观测 run_status；若平台正确校验 types，workflow 在 YAML 校验阶段即被拒绝，run_status 不会为 COMPLETED，步骤内容在此场景下无关（校验先行于步骤执行） |
| [非功能] 报错中应列出 merge/open/reopen/update 并指出对应关系 | 🔄 UNVERIFIABLE | 断言 type=nonfunctional target=error_message eval=llm_assisted，需 LLM 辅助评估平台返回的错误信息是否包含正确的 types 列表及对应关系，步骤自身无法产出该内容 |

### 问题

- **验证点 2 — UNVERIFIABLE**：断言为 nonfunctional + llm_assisted，依赖 LLM 分析平台校验错误信息的内容质量。workflow 步骤仅 echo "hello"，不参与错误信息的生产或验证。

## 5. 评级理由

第一个验证点（负向 run_status）可由 harness 直接观测平台是否阻止了使用非法 types 的 workflow 执行，判定为 COVERED。第二个验证点为 nonfunctional + llm_assisted，无法通过步骤分析判定，为 UNVERIFIABLE。综合评级为部分不符。
