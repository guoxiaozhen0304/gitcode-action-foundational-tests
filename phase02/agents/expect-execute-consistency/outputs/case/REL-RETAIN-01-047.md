# REL-RETAIN-01-047
- **标题**: artifact 保留期 90 天边界——第 91 天应不可下载
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**artifact 保留期 90 天边界——第 91 天应不可下载**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-047
通过标准：
1. 第 90 天可下载（HTTP 200）
2. 第 91 天不可下载（HTTP 404）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | create artifact | `echo retention test > retention.txt` | — | 创建测试文件 |
| 2 | upload artifact | `uses: upload-artifact` with name/retention-days=90 | — | 上传 artifact 设置 90 天保留期 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | download_day90_status = 200 | positive | — | ✅ GENUINE | `uses: upload-artifact` 真实上传 artifact，`retention-days: 90` 设置保留期。下载验证由 harness 在特定天执行 |
| 2 | download_day91_status = 404 | positive | — | ✅ GENUINE | 同上，harness 在第 91 天下载验证 expiration 行为 |
---
