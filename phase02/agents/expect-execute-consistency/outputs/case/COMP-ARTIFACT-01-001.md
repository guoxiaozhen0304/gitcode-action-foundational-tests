# COMP-ARTIFACT-01-001

- **标题**: artifact 可在同 workflow 的 job 间正确传递
- **维度**: completeness
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**artifact 可在同 workflow 的 job 间正确传递**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-015

通过标准：
1. [正向] download 后文件内容正确 —— 断言 run_logs contains "hello artifact"
2. [正向] 运行状态成功 —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Create artifact | `mkdir -p dist && echo "hello artifact" > dist/app.txt` | - | 生成文件 |
| 2 | Upload artifact | `uses: upload-artifact` with name: app-dist, path: dist/ | - | 平台存储制品 |
| 3 | Download artifact | `uses: download-artifact` with name: app-dist | - | 平台恢复制品 |
| 4 | Verify content | `cat dist/app.txt` | - | 真实读取制品文件输出 "hello artifact" |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: hello artifact | ✅ GENUINE | cat 输出来自制品恢复后的文件，制品传输机制是真实被测功能 |
| 2 | run_status | positive | equals: success | ✅ GENUINE | 步骤中有 uses: upload-artifact/download-artifact，真实行为 |

