# SEC-LOG-01-002
- **标题**: 导出/历史日志副本中 secret 原值命中数必须为 0，遮蔽状态不可回退
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**日志导出件与历史日志中 secret 原值命中数为 0，遮蔽状态不回退**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-040
通过标准：
1. 日志可下载导出
2. 导出日志不含 secret
3. 历史日志不含 secret
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Reference secret in log | `echo "MASKED_SECRET_LINE: ${{ secrets.DEPLOY_TOKEN }}"` | — | 遮蔽后的 secret |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 下载成功 | positive | log_api equals "download_ok" | ❌ MISSING_SOURCE | target=log_api 为外部接口，workflow 无日志下载步骤 |
| 2 | 导出日志不含 secret | negative | exported_logs must_not_contain_secret | ❌ UNEXERCISED | target=exported_logs 非 run_logs，且为 must_not_contain_secret；步骤在 run_logs 中使用 secret，但 exported_logs 无对应步骤 |
| 3 | 历史日志不含 secret | negative | historical_logs must_not_contain_secret | ❌ UNEXERCISED | 同上，无 historical_logs 相关步骤 |
### 问题
断言 1 MISSING_SOURCE（外部接口），断言 2/3 UNEXERCISED（target 非 run_logs 且无对应步骤）。
---
