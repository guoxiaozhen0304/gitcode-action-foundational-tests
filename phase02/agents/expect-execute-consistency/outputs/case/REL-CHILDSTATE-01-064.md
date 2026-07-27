# REL-CHILDSTATE-01-064
- **标题**: 子任务状态传播——workflow_call 失败时父 workflow 不应假阳性完成
- **维度**: 稳定性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**子 workflow_call 失败时父 workflow 应正确标记 failure**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-064
通过标准：
1. 父 workflow 状态=failure
2. 下游 job 被 skip
3. 父 workflow 不应显示 success

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | call_child | `uses: ./.gitcode/workflows/child_fail.yml` | - | 调用会失败的子 workflow |
| 2 | downstream should not run | `echo downstream` | needs: call_child | 依赖失败的子 workflow，应 skip |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | parent_status = failure | positive | - | ✅ GENUINE | `uses:` 调用会失败的子 workflow，状态传播真实 |
| 2 | downstream_status = skipped | positive | - | ✅ GENUINE | needs: call_child 依赖失败 → 平台自动 skip |
| 3 | parent_status = success | negative | - | ✅ GENUINE | 父 workflow 真实因子失败而 failure |
---
