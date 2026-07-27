# SEC-SUPPLY-01-003
- **标题**: 第三方 Action 来源应具备信任边界（typosquatting 限制）
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**第三方 Action 来源应具备信任边界（typosquatting 限制）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-015
通过标准：
1. 与官方 action 名称高度相似的恶意 Action 绝不应被静默解析为合法来源
2. 首次使用未审核 Action 时应留下审计记录

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use typo action | uses: checkout-action@v1 | - | action 解析失败，平台应拒绝或警告 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | must_not_equal: "success" | ✅ GENUINE | `uses:` 引用 typosquatting 名称的 action，平台不应成功执行 |
| 2 | run_logs | positive | equals: "action_not_found_or_unapproved" | ✅ GENUINE | `uses:` action 解析结果产生日志，平台应输出未找到/未审核信息 |
---
