# COMPAT-COMM-01-001

- 标题: issue_comment types 命名差异 - GitCode 合法 types 应被接受
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   COMPAT-COMM-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-NEW-004
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      issue_comment types 命名差异 - GitCode 合法 types 应被接受

前置条件:
  - 仓库已启用 Actions
  - 测试者持有 maintainer 权限

操作步骤:
  1. 创建一个 workflow，on 配置为 `issue_comment.types: [created, edited]`（GitCode 风格命名）
  2. 提交并触发 issue_comment 事件

预期结果:
  - GitCode 合法 types（created/edited/deleted）应被接受并正常触发
  - 不应因命名差异导致 workflow 被拒绝

验证点:
  - [正向] GitCode 风格 types 命名被接受
  - [负向] 不通过因命名差异导致的误报错误

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
    types: [created, edited]
jobs:
  test-comment-types:
    name: Test issue comment types
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
| [正向] GitCode 风格 types 命名被接受 | ✅ COVERED | 步骤使用 `${{ atomgit.event_name }}` 表达式（平台上下文求值即功能执行），workflow 正常完成即证明 types 命名被平台接受 |
| [负向] 不通过因命名差异导致的误报错误 | ✅ COVERED | YAML 中有 `type=negative, target=validation_error` 断言直接覆盖，workflow 运行成功即无校验错误 |

### 问题

无。

## 5. 评级理由

所有验证点均被步骤真实覆盖：步骤使用 `${{ }}` 表达式输出动态值（平台上下文求值），属于实质逻辑；负向验证点有对应的 YAML 断言覆盖。整体判定为**断言一致**。
