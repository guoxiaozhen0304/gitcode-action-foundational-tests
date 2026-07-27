# COMP-ARTIFACT-01-002

- **标题**: 下载全部制品功能正常
- **维度**: completeness
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**下载全部制品功能正常**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-015

通过标准：
1. [正向] 所有 artifact 文件均存在 —— 断言 run_logs contains "app"、contains "report"
2. 运行状态成功 —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Create artifacts | `echo "app" > dist/app.txt && echo "report" > reports/coverage.txt` | - | 生成文件 |
| 2 | Upload app | `uses: upload-artifact` with name: app | - | 上传制品 |
| 3 | Upload reports | `uses: upload-artifact` with name: reports | - | 上传制品 |
| 4 | Download all | `uses: download-artifact` without name (下载全部) | - | 恢复全部制品 |
| 5 | Verify all | `cat artifacts/app/app.txt; cat artifacts/reports/coverage.txt` | - | 真实读取制品文件输出 "app" 和 "report" |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | uses: upload/download artifact 是真实 action |
| 2 | run_logs | positive | contains: app | ✅ GENUINE | cat 输出来自制品恢复的文件内容 |
| 3 | run_logs | positive | contains: report | ✅ GENUINE | cat 输出来自制品恢复的文件内容 |

