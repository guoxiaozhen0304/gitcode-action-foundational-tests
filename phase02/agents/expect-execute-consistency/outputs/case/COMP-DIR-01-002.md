# COMP-DIR-01-002

- **标题**: .github/workflows/ 下的 YAML 不被识别为 workflow
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**.github/workflows/ 下的 YAML 不被识别为 workflow**

- 触发事件: `push`
- 规格引用: INTENT-COMP-001

通过标准：
1. type=negative, target=run_list, equals=no_run_from_github_dir

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `push` |
| 触发身份 | `maintainer` |
| Repo 环境 | `github-workflows-dir` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | equals=no_run_from_github_dir | ✅ GENUINE | 断言有条件可被步骤验证 |

---