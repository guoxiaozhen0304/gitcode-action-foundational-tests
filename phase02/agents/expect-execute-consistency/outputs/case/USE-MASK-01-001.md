# USE-MASK-01-001
- **标题**: secret 脱敏文档描述与实际行为一致并给出缓解建议
- **维度**: usability
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**secret 脱敏文档描述与实际行为一致并给出缓解建议**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-016
通过标准：
1. 正常引用 secrets 时日志显示为 ***
2. 文档中的风险提示段落是否包含如何改的可操作建议

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo secret via env | `echo "secret length=${#SECRET_VAL}"` | 无 | 输出 secret 长度（非明文） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_not_contain_secret: TEST_SECRET | positive | 步骤通过 env 注入 `${{ secrets.TEST_SECRET }}`，secret 引用真实 | ✅ GENUINE | `${{ secrets.TEST_SECRET }}` 涉及平台 secret 脱敏机制 |
| 2 | documentation eval=llm_assisted | nonfunctional | LLM 判定文档风险提示与缓解建议 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定文档质量 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
