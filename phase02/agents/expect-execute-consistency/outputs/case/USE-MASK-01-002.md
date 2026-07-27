# USE-MASK-01-002
- **标题**: 直接 echo secrets 值时文档描述的绕过风险与实际一致
- **维度**: usability
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**直接 echo secrets 值时文档描述的绕过风险与实际一致**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-016
通过标准：
1. 若绕过确实发生，日志中可能出现明文
2. 文档是否给出不要在 run 中直接 echo secrets 的缓解建议

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | direct echo secret | `echo "secret=${{ secrets.TEST_SECRET }}"` | 无 | 可能泄露明文 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs eval=llm_assisted | nonfunctional | 虽步骤含 `${{ secrets.TEST_SECRET }}` 表达式，但断言为 nonfunctional + llm_assisted | 🔶 LLM_DEPENDENT | 断言依赖 LLM 辅助判定文档声明与实际行为是否一致 |

### 问题
唯一断言为 nonfunctional + llm_assisted，步骤虽有 `${{ }}` 表达式但断言方式依赖 LLM 判定文档-行为一致性。
---
