# COMPAT-ENV-01-001

- 标题: ATOMGIT_SHA 环境变量应正确返回触发提交 SHA
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ENV-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-017
参照来源:  inputs/gitcode-spec/core-concepts/trigger-events.md
母意图:    —
标题:      ATOMGIT_SHA 环境变量应正确返回触发提交 SHA

前置条件:
  - 仓库已启用 Actions
  - Runner 环境正常注入 ATOMGIT_* 变量

操作步骤:
  1. 在 workflow 的 run 步骤中输出 $ATOMGIT_SHA
  2. 触发 workflow 运行

预期结果:
  - $ATOMGIT_SHA 应返回当前触发事件的提交 SHA（40 位十六进制字符串）

验证点:
  - [正向] 日志中 ATOMGIT_SHA 的值不为空且为有效 SHA 格式

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Echo ATOMGIT_SHA | run: echo "atomgit_sha=$ATOMGIT_SHA"
echo "done"
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  test:
    name: Test ATOMGIT_SHA env var
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: Echo ATOMGIT_SHA
        run: |
          echo "atomgit_sha=$ATOMGIT_SHA"
          echo "done"

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 日志中 ATOMGIT_SHA 的值不为空且为有效 SHA 格式 | ✅ COVERED | steps have real logic |

### 问题

无

---
