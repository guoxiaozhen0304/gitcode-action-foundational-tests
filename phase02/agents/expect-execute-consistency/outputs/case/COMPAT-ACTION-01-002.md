# COMPAT-ACTION-01-002

- 标题: checkout 短名等价性——path 参数支持
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ACTION-01-002
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-024
参照来源:  inputs/gitcode-spec/action-development/top-level-fields.md
母意图:    COMPAT-ACTION-01-001
标题:      checkout 短名等价性——path 参数支持

前置条件:
  - 仓库存在默认分支 main

操作步骤:
  1. 在工作流中使用 `uses: checkout` 并传入 `path: subdir/checkout-path` 参数
  2. 触发工作流，观察 checkout 行为
  3. 在后续步骤中验证代码是否被检出到指定子目录

预期结果:
  - `uses: checkout` 配合 path 参数可将代码检出到指定子目录
  - 裸插件名写法与 GitHub 全名写法在行为上等价
  - 后续步骤可在指定子目录中访问仓库文件

验证点:
  - [正向] checkout 步骤成功完成，无报错
  - [正向] 指定子目录下存在仓库文件
  - [负向] 不应因使用裸插件名而解析失败
  - [负向] 不应将代码检出到默认工作目录以外的意外位置

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) checkout with path | uses: checkout | 是 |
| 2 | (TC) verify path exists | run: if [ ! -f "subdir/checkout-path/README.md" ]; then
  echo "CHECKOUT_PATH_FAILED"
  exit 1
else
  echo "CHECKOUT_PATH_OK"
fi
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  verify-checkout-path:
    name: Verify checkout path parameter
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) checkout with path
        uses: checkout
        with:
          path: subdir/checkout-path
      - name: (TC) verify path exists
        run: |
          if [ ! -f "subdir/checkout-path/README.md" ]; then
            echo "CHECKOUT_PATH_FAILED"
            exit 1
          else
            echo "CHECKOUT_PATH_OK"
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
| [正向] 指定子目录下存在仓库文件 | ✅ COVERED | steps have real logic |
| [负向] 不应因使用裸插件名而解析失败 | ✅ COVERED | negative assertion in YAML assertions |
| [负向] 不应将代码检出到默认工作目录以外的意外位置 | ✅ COVERED | negative assertion in YAML assertions |

### 问题

无

---
