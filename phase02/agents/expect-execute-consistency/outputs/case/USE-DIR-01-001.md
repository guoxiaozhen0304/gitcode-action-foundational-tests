# USE-DIR-01-001
- **标题**: workflow 放置于 .gitcode/workflows/ 下可正常触发
- **维度**: 易用性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**workflow 放置于 .gitcode/workflows/ 下可正常触发**
- 触发事件: `push`
- 规格引用: INTENT-USE-001
通过标准：
1. 运行记录列表中出现该 workflow 的运行
2. 运行状态为成功或至少进入执行态

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | check directory | `echo "workflow triggered from .gitcode/workflows/"` | - | 仅 echo 固定字符串 |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: COMPLETED | ⚠️ STATUS_GUARANTEED | 仅一个 `echo` 步骤，无 if:、无 ${{ }}、无 uses:、无实质命令，不可能失败 |

### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅为 `echo` 固定字符串，workflow 在任何情况下都将成功完成。断言永远为真——不能区分 "workflow 被正确触发" 和 "workflow 未被触发因此无运行记录" 两种情况。测试从未验证反向情况。
---
