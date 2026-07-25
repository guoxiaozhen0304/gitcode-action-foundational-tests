# COMP-EXPR-01-055

- 标题: hashFiles 函数边界行为
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action
- 仓库根目录存在 package.json

操作步骤:
1. 在 env 或 run 中使用 hashFiles 计算单文件和多文件哈希
2. 验证输出为 64 位十六进制字符串

预期结果:
- hashFiles 返回 64 位十六进制 SHA256 值，多文件时组合计算

验证点:
- [正向] 单文件 hashFiles 输出 64 位 hex
- [正向] 多文件 hashFiles 输出 64 位 hex
- [正向] 不匹配路径返回空或固定值

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Single file hash | echo "HASH_SINGLE=${{ hashFiles('package.json') }}" | 是 |
| 2 | Multi pattern hash | echo "HASH_MULTI=${{ hashFiles('src/**', 'package.json') }}" | 是 |
| 3 | No match hash | echo "HASH_NONE=${{ hashFiles('nonexistent.xyz') }}" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-EXPR-01-055
dimensions: [completeness]
dimension: completeness
priority: P1
title: hashFiles 函数边界行为
intent_ref: KEEP-TC-186
setup:
  repo_fixture: default
  secrets: []
  variables: {}
  branch_protection: default
fault_injection: null
workflow: |
  on:
    workflow_dispatch:
  jobs:
    verify:
      name: Verify hashFiles boundary
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Single file hash
          run: |
            echo "HASH_SINGLE=${{ hashFiles('package.json') }}"
        - name: Multi pattern hash
          run: |
            echo "HASH_MULTI=${{ hashFiles('src/**', 'package.json') }}"
        - name: No match hash
          run: |
            echo "HASH_NONE=${{ hashFiles('nonexistent.xyz') }}"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: HASH_SINGLE=
  - type: positive
    target: run_logs
    must_contain: HASH_MULTI=
  - type: positive
    target: run_logs
    must_contain: HASH_NONE=
teardown:
  reset: fixture
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo | default |
| Secrets | (none) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 单文件 hashFiles 输出 64 位 hex | ❌ TRIVIAL | 步骤 echo HASH_SINGLE= 但断言仅检查 = 存在，未校验输出为 64 位 hex 格式 |
| [正向] 多文件 hashFiles 输出 64 位 hex | ❌ TRIVIAL | 同上，仅检查 HASH_MULTI= 存在 |
| [正向] 不匹配路径返回空或固定值 | ❌ TRIVIAL | 断言仅检查 HASH_NONE= 存在，未校验值为空或固定值具体内容 |

### 问题

- 所有 hashFiles 验证仅检查输出标签存在（= 存在），未校验 hash 值的格式（64 位 hex）或边界值（不匹配时为空/固定值）

---
