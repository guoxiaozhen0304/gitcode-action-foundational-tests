# USE-LOG-01-001
- **标题**: 多 step 日志按时间线组织且边界清晰
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**多 step 日志按时间线组织且边界清晰**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-017
通过标准：
1. step 按定义顺序排列，含时间戳前缀，长输出可折叠
2. 用户能在 3 秒内定位到失败 step

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | step one prepare | `echo "prepare done"` | 无 | 标记日志 |
| 2 | step two build | `echo "build done"` | 无 | 标记日志 |
| 3 | step three test | `echo "test done"` | 无 | 标记日志 |
| 4 | step four package | `echo "package done"` | 无 | 标记日志 |
| 5 | step five summary | `echo "summary done"` | 无 | 标记日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "step one prepare" | positive | 步骤纯 echo，无 `${{ }}` / `if:` / `uses:` / 真实命令 | ⚠️ STATUS_GUARANTEED | 所有 step 均为纯 echo 硬编码字符串，无任何平台行为依赖；成功必然输出该字符串 |
| 2 | ui_layout eval=llm_assisted | nonfunctional | LLM 判定 UI 定位体验 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定 UI 布局 |

### 问题
断言 1 为纯 echo 无平台行为依赖，trivially guaranteed；断言 2 依赖 LLM。
---
