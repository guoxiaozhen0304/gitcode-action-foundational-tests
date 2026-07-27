# SEC-WCMD-01-001
- **标题**: Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的 secret 值**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-028
通过标准：
1. workflow 命令的响应中绝不应包含被遮蔽前的 secret 原值
2. 命令执行日志应仅显示命令骨架，不含 payload

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mask secret | `echo "::add-mask::${{ secrets.API_KEY }}"` | - | 发出 add-mask 命令，runner 处理并可能输出响应 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | [API_KEY] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret: "API_KEY" | ✅ GENUINE | 步骤使用 `${{ secrets.API_KEY }}` 真实发出 add-mask 命令，检测 runner 响应是否泄露 |
| 2 | run_logs | positive | equals: "mask_command_without_payload" | ❌ MISSING_SOURCE | 无任何步骤或 runner 输出产生该字符串。echo 输出的是 `::add-mask::***` 而非该标记 |

### 问题
**断言 2 — MISSING_SOURCE**: 步骤 echo `::add-mask::<secret>`，runner 响应不包含 "mask_command_without_payload" 字符串。无来源产生该断言期望的值。
---
