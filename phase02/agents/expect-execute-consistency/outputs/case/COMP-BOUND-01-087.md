# COMP-BOUND-01-087

- 标题: 步骤输出与跨 job 传递边界验证
- 维度: 完备性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

前置条件:
- 仓库已启用 AtomGit Action

操作步骤:
1. 在 step 中通过 ATOMGIT_OUTPUT 写入输出
2. 在同 job 后续 step 中引用 steps.id.outputs

预期结果:
- ATOMGIT_OUTPUT 写入的键值对可在同 job 后续 step 中通过 steps.id.outputs 引用

验证点:
- [正向] ATOMGIT_OUTPUT 写入后同 job 可读取
- [正向] 多行输出值被正确处理
- [负向] 跨 job 未声明 outputs 时引用为空

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容（前80字） | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Write output | echo "key1=val1" >> "$ATOMGIT_OUTPUT"; echo "key2=val2" >> "$ATOMGIT_OUTPUT" | 是 |
| 2 | Read output | echo "K1=${{ steps.writer.outputs.key1 }}"; echo "K2=${{ steps.writer.outputs.key2 }}" | 是 |

<details>
<summary>完整 workflow YAML</summary>

```yaml
id: COMP-BOUND-01-087
dimensions: [completeness]
dimension: completeness
priority: P1
title: 步骤输出与跨 job 传递边界验证
intent_ref: KEEP-TC-331~333
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
      name: Verify output boundary
      runs-on: [ubuntu-latest, x64, small]
      steps:
        - name: Write output
          id: writer
          run: |
            echo "key1=val1" >> "$ATOMGIT_OUTPUT"
            echo "key2=val2" >> "$ATOMGIT_OUTPUT"
        - name: Read output
          run: |
            echo "K1=${{ steps.writer.outputs.key1 }}"
            echo "K2=${{ steps.writer.outputs.key2 }}"
            echo "output_ok"
trigger:
  event: workflow_dispatch
  as: maintainer
  params: {}
assertions:
  - type: positive
    target: run_logs
    must_contain: K1=val1
  - type: positive
    target: run_logs
    must_contain: K2=val2
  - type: positive
    target: run_logs
    must_contain: output_ok
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
| [正向] ATOMGIT_OUTPUT 写入后同 job 可读取 | ✅ COVERED | 步骤2 通过 steps.writer.outputs.key1/key2 读取，断言 K1=val1, K2=val2 |
| [正向] 多行输出值被正确处理 | ✅ COVERED | 写入两个键值对 key1 和 key2，均被正确读取和断言 |
| [负向] 跨 job 未声明 outputs 时引用为空 | ❌ UNVERIFIABLE | 当前 workflow 仅含单 job；跨 job 引用测试缺失 |

### 问题

- 跨 job 未声明 outputs 时引用为空：该负向验证点需要第二个 job 尝试引用 writer 的 outputs，当前仅在同 job 内验证

---
