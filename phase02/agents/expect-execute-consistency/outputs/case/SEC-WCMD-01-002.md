# SEC-WCMD-01-002
- **标题**: 跨运行 artifact 必须被视为不可信数据
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**跨运行 artifact 必须被视为不可信数据**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-029
通过标准：
1. 不可信来源的 artifact 绝不应被特权运行隐式信任执行
2. artifact 来源可被追溯判定

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Download untrusted artifact | uses: download-artifact | - | 下载 artifact 到工作目录 |
| 2 | Do not auto execute | `echo "Artifact downloaded but not executed automatically"` | - | 仅 echo 标记 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-artifacts |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain: "auto_executed" | ❌ MISSING_SOURCE | 无任何步骤输出 "auto_executed"。步骤 echo 的是 "Artifact downloaded but not executed automatically"，不含该子串 |
| 2 | run_status | positive | equals: "completed" | ✅ GENUINE | 步骤使用 `uses: download-artifact` action，存在真实执行路径（artifact 可能不存在导致失败） |

### 问题
**断言 1 — MISSING_SOURCE**: 无步骤产生 "auto_executed" 字符串，断言在任何情况下均为真（空洞检查）。步骤 2 的 echo 文本不含该子串。
---
