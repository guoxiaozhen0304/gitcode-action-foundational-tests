# COMPAT-RUNNER-01-007

- **标题**: Runner 预装工具链规格清单与实测全面对账
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**Runner 预装工具链规格清单与实测全面对账**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-047

通过标准：
1. type=positive, target=run_logs, must_contain="AUDIT_DONE"
2. type=positive, target=run_logs, eval=llm_assisted
3. type=negative, target=run_logs, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Probe java and maven and  | `java -version 2>&1 | head -1 || echo "JAVA_MISSING" mvn -version 2>&1 | head -1 ` |  | ✅ GENUINE |
| 2 | Probe node go kubectl aws | `node --version 2>&1 || echo "NODE_MISSING" go version 2>&1 || echo "GO_MISSING" ` |  | ✅ GENUINE |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  probe:
    name: Audit preinstalled toolchain against spec
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Probe java and maven and gradle
        run: |
          java -version 2>&1 | head -1 || echo "JAVA_MISSING"
          mvn -version 2>&1 | head -1 || echo "MVN_MISSING"
          gradle -version 2>&1 | head -3 || echo "GRADLE_MISSING"
      - name: Probe node go kubectl awscli
        run: |
          node --version 2>&1 || echo "NODE_MISSING"
          go version 2>&1 || echo "GO_MISSING"
          kubectl version --client 2>&1 | head -1 || echo "KUBECTL_MISSING"
          aws --version 2>&1 || echo "AWSCLI_MISSING"
          echo "AUDIT_DONE"
```

</details>

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain=AUDIT_DONE | ✅ GENUINE | AUDIT_DONE: GENUINE |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---