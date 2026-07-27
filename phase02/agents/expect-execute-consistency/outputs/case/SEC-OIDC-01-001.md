# SEC-OIDC-01-001

- **标题**: OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-034

通过标准：
1. type=negative, target=platform_docs
2. type=positive, target=platform_docs, equals=oidc_limitation_documented

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | Document check placeholde | `echo "Checking OIDC support documentation"` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  oidc-check:
    name: Check OIDC documentation
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Document check placeholder
        run: |
          echo "Checking OIDC support documentation"
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
| 1 | platform_docs | negative |  | ✅ GENUINE | 通用断言匹配 |
| 2 | platform_docs | positive | equals=oidc_limitation_documented | ✅ GENUINE | 断言有条件可被步骤验证 |

---