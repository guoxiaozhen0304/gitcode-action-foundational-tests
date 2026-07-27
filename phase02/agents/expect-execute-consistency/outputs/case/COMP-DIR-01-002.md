# COMP-DIR-01-002

- **标题**: .github/workflows/ 下的 YAML 不被识别为 workflow
- **维度**: completeness
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**.github/workflows/ 下的 YAML 不被识别为 workflow**
- 触发事件: `push`
- 规格引用: INTENT-COMP-001

通过标准：
1. [负向] 运行列表中不存在源自 .github/workflows/ci.yml 的运行 —— 断言 run_list=no_run_from_github_dir

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| - | (空 workflow) | 无任务、无步骤 | - | 不产生任何运行 |

## 3. 触发与运行环境

| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | github-workflows-dir |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_list | negative | equals: no_run_from_github_dir | ✅ GENUINE | harness 级断言；将空 YAML 置于 .github/workflows/ 目录，验证平台不识别该路径下的 workflow 文件 |

