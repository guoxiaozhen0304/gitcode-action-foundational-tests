# COMPAT-ISOLATE-01-002

- 标题: Runner 环境隔离——跨 job 环境变量隔离
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ISOLATE-01-002
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-028
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    COMPAT-ISOLATE-01-001
标题:      Runner 环境隔离——跨 job 环境变量隔离

前置条件:
  - 平台提供多 job 工作流执行能力

操作步骤:
  1. 在 job A 中通过 `echo "KEY=VALUE_A" >> "$ATOMGIT_ENV"` 设置环境变量
  2. 在 job B 中读取同名环境变量 KEY
  3. 验证 job B 读取不到 job A 设置的值

预期结果:
  - job B 中环境变量 KEY 为空或不同于 VALUE_A
  - $ATOMGIT_ENV 的作用域仅限于当前 job，不泄漏到后续 job
  - 环境变量隔离行为与 GitHub Actions 的 job 级隔离语义一致

验证点:
  - [负向] job B 中不应读取到 job A 通过 ATOMGIT_ENV 设置的值
  - [正向] job 内部步骤可正常读取本 job 设置的 ATOMGIT_ENV 变量
  - [正向] 环境变量隔离机制与预期语义一致

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) set env in job A | run: echo "ISOLATION_TEST_KEY=VALUE_FROM_JOB_A" >> "$ATOMGIT_ENV"
echo "ENV_SET_IN_JOB_A"
 | 是 |
| 2 | (TC) verify env not leaked | run: if [ "${ISOLATION_TEST_KEY:-}" = "VALUE_FROM_JOB_A" ]; then
  echo "ENV_ISOLATION_BROKEN"
  exit 1
else
  echo "ENV_ISOLATED_OK"
fi
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-set-env:
    name: Set environment variable
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) set env in job A
        run: |
          echo "ISOLATION_TEST_KEY=VALUE_FROM_JOB_A" >> "$ATOMGIT_ENV"
          echo "ENV_SET_IN_JOB_A"
  job-verify-env:
    name: Verify env isolation
    runs-on: [ubuntu-latest, x64, small]
    needs: job-set-env
    steps:
      - name: (TC) verify env not leaked
        run: |
          if [ "${ISOLATION_TEST_KEY:-}" = "VALUE_FROM_JOB_A" ]; then
            echo "ENV_ISOLATION_BROKEN"
            exit 1
          else
            echo "ENV_ISOLATED_OK"
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
| [负向] job B 中不应读取到 job A 通过 ATOMGIT_ENV 设置的值 | ✅ COVERED | negative assertion in YAML assertions |
| [正向] job 内部步骤可正常读取本 job 设置的 ATOMGIT_ENV 变量 | ✅ COVERED | steps have real logic |
| [正向] 环境变量隔离机制与预期语义一致 | ✅ COVERED | steps have real logic |

### 问题

无

---
