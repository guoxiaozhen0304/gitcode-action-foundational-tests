# USE-SECNAME-01-002
- **标题**: Secret 名称以数字开头时应给出命名规则错误
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**Secret 名称以数字开头时应给出命名规则错误**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-028
通过标准：
1. 不应仅报 Secret not found
2. 报错中是否包含命名格式说明

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | use invalid secret name | `echo "val=${{ secrets.1SECRET }}"` | 无 | 预期校验阶段报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals COMPLETED | negative | `${{ secrets.1SECRET }}` 涉及 secret 名称校验 | ✅ GENUINE | secret 名称规则校验是平台真实行为 |
| 2 | error_message eval=llm_assisted | nonfunctional | LLM 判定报错命名格式说明 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定报错内容 |

### 问题
断言 2 依赖 LLM 辅助判定，无法在当前分析中确证。
---
