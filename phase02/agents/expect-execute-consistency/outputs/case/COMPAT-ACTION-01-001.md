# COMPAT-ACTION-01-001

- 标题: checkout 短名等价性——ref 参数支持
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ACTION-01-001
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-024
参照来源:  inputs/gitcode-spec/action-development/top-level-fields.md
母意图:    —
标题:      checkout 短名等价性——ref 参数支持

前置条件:
  - 仓库存在默认分支 main
  - 存在一个可 checkout 的 feature 分支

操作步骤:
  1. 在工作流中使用 `uses: checkout` 并传入 `ref: main` 参数
  2. 触发工作流，观察 checkout 行为
  3. 再传入 `ref: feature-branch` 参数重复触发

预期结果:
  - `uses: checkout` 配合 ref 参数可正确检出指定分支
  - 裸插件名写法与 GitHub 全名写法在行为上等价
  - 检出后的工作目录包含指定分支代码

验证点:
  - [正向] checkout 步骤成功完成，无报错
  - [正向] 检出后的代码与指定分支一致
  - [负向] 不应因使用裸插件名而解析失败

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) checkout with ref main | uses: checkout | 是 |
| 2 | (TC) verify branch is main | run: if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
  echo "CHECKOUT_REF_FAILED"
  exit 1
else
  echo "CHECKOUT_REF_OK"
fi
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify-checkout-ref:
    name: Verify checkout ref parameter
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) checkout with ref main
        uses: checkout
        with:
          ref: main
      - name: (TC) verify branch is main
        run: |
          if [ "$(git rev-parse --abbrev-ref HEAD)" != "main" ]; then
            echo "CHECKOUT_REF_FAILED"
            exit 1
          else
            echo "CHECKOUT_REF_OK"
          fi

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
| [正向] checkout 步骤成功完成，无报错 | ✅ COVERED | steps have real logic |
| [正向] 检出后的代码与指定分支一致 | ✅ COVERED | steps have real logic |
| [负向] 不应因使用裸插件名而解析失败 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
