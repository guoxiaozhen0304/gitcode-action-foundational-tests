# USE-UNKN-01-003

- **标题**: step 标识 id 与 identifier 命名双轨的接受一致性与文档说明
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**step 标识 id 与 identifier 命名双轨的接受一致性与文档说明**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-036

通过标准：
1. type=positive, target=validation_result, eval=deterministic
2. type=negative, target=documentation, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|
| 1 | produce value | `echo "result=ok" >> $ATOMGIT_OUTPUT` |  | ❌ VACUOUS |
| 2 | consume value | `echo "via-id=[${{ steps.producer.outputs.result }}]"` |  | ✅ GENUINE |
| 3 | produce value alt | `echo "result=ok" >> $ATOMGIT_OUTPUT` |  | ❌ VACUOUS |

<details>
<summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  with-id:
    name: step using document field name
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: produce value
        id: producer
        run: |
          echo "result=ok" >> $ATOMGIT_OUTPUT
      - name: consume value
        run: |
          echo "via-id=[${{ steps.producer.outputs.result }}]"
  with-identifier:
    name: step using sample field name
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: produce value alt
        identifier: producer
        run: |
          echo "result=ok" >> $ATOMGIT_OUTPUT
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
| 1 | validation_result | positive | eval=deterministic | ✅ GENUINE | 通用断言匹配 |
| 2 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---