# COMP-PR-01-004

- **标题**: pre-merge ref 在 PR 存续期可解析且语义裁定
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**pre-merge ref 在 PR 存续期可解析且语义裁定**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-033

通过标准：
1. [正向] PR 打开状态下 checkout 该 ref 成功 —— 断言 run_logs must_contain PRE_MERGE_MARKER
2. [正向/记录] 取到的代码内容符合实测裁定的语义 —— 断言 REF_CONTENT_DUMPED
3. [负向] 不应 ref 解析成功但内容为陈旧合并结果而无任何标识 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout merge ref | `uses: checkout` with: ref: refs/merge-requests/1/merge | - | checkout action 解析 merge ref |
| 2 | Inspect content | `cat pre_merge_marker.txt` + `echo "REF_CONTENT_DUMPED"` | - | 文件中内容（PRE_MERGE_MARKER）和标志 |

## 3. 触发与运行环境

| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | pr-merge-ref |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PRE_MERGE_MARKER | ✅ GENUINE | `cat` 读取的是 checkout 通过 merge ref 获取的源分支文件内容，merge ref 解析即真实被测行为 |
| 2 | run_logs | positive | must_contain: REF_CONTENT_DUMPED | ✅ GENUINE | 同一步骤内 cat 文件后再 echo 标志，非纯字面量步骤 |
| 3 | ref_semantics | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

