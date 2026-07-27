# COMP-ATOMGIT-01-047

- **标题**: atomgit 核心上下文属性可访问性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**atomgit 核心上下文属性可访问性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-047

通过标准：
1. [正向] 各核心属性输出不为空 —— 断言 run_logs must_contain SHA=、REF=refs/、REPO=

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print core properties | 15 行 echo 语句，每行引用 `${{ atomgit.* }}` 上下文属性 | - | 平台上下文的值：SHA=xxx, REF=refs/heads/xxx, REPO=xxx 等 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA= | ✅ GENUINE | echo 引用 `${{ atomgit.sha }}`，平台上下文求值是真实被测行为 |
| 2 | run_logs | positive | must_contain: REF=refs/ | ✅ GENUINE | echo 引用 `${{ atomgit.ref }}`，验证 ref 格式含 refs/ 前缀 |
| 3 | run_logs | positive | must_contain: REPO= | ✅ GENUINE | echo 引用 `${{ atomgit.repository }}`，验证仓库属性可访问 |

