# COMPAT-COMM-01-002

- 标题: issue_comment types:created 不支持时应给出降级指引
- 维度: 兼容性 | 优先级: P1
- 评级: 完全不符

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-COMM-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-004
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      issue_comment types:created 不支持时应给出降级指引

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，on 配置为 `issue_comment.types: [created]`
  2. 提交并触发 issue_comment 事件
  3. 观察系统行为

预期结果:
  - 若 types:created 不被支持，系统应明确报错或给出替代 types 列表
  - 不应静默忽略 types 配置导致所有 issue_comment 事件都触发

验证点:
  - [负向] 不通过静默忽略（types 配置失效）
  - [正向] 报错信息包含可接受的 types 列表

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo trigger info | run: echo "event_name=${{ atomgit.event_name }}" / echo "done" | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  issue_comment:
    types: [created]
jobs:
  test-comment-created:
    name: Test issue comment created type
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo trigger info
        run: |
          echo "event_name=${{ atomgit.event_name }}"
          echo "done"
```

</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | issue_comment |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|--------|:-----:|------|
| [负向] 不通过静默忽略（types 配置失效） | 🔄 UNVERIFIABLE | 步骤仅输出 `event_name=issue_comment`，无法区分 types 被正确过滤还是被静默忽略；单次 workflow 执行无法证明否定行为 |
| [正向] 报错信息包含可接受的 types 列表 | ❌ MISSING | 步骤只 echo 事件名和 "done"，无任何步骤产出报错信息；若 types:created 被支持则无报错产生，断言目标不可达 |

### 问题

- **[负向] 不通过静默忽略**: UNVERIFIABLE — 步骤仅 echo `event_name=issue_comment`，无论 types 是被正确处理还是静默忽略，步骤的输出完全相同，单次运行无法证明平台未静默忽略配置。
- **[正向] 报错信息包含可接受的 types 列表**: MISSING — 无任何步骤产生 error_message 输出；workflow 可能正常运行（types 已被支持），则根本不会产生报错信息。

## 5. 评级理由

两个验证点均未覆盖：[负向] 为 UNVERIFIABLE（单次运行无法证明否定行为），[正向] 为 MISSING（无步骤产生报错信息）。无任何 COVERED 项，整体判定为**完全不符**。
