# USE-BADGE-01-001
- **标题**: workflow 运行完成后状态徽标及时回写且语义清晰
- **维度**: 易用性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**workflow 运行完成后状态徽标及时回写且语义清晰**
- 触发事件: `push`
- 规格引用: INTENT-USE-019
通过标准：
1. Commits 页面出现对应状态徽标
2. PR Checks 标签页汇总运行结果
3. 从运行完成到徽标刷新延迟小于 30 秒

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | success step | `echo "success"` | - | 仅 echo "success" |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: COMPLETED | ⚠️ STATUS_GUARANTEED | 仅一个 `echo "success"` 步骤，无条件分支、无 failure 路径，永远成功 |
| 2 | ui_visual | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 辅助判定 UI 徽标展示效果 |

### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅为 `echo "success"`，不可能失败。run_status 永远为 COMPLETED，断言空洞为真——测试从未验证 "workflow 可被检测到并触发" 的逆向情况。
---
