# COMPAT-TOKEN-01-002
- **标题**: GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-020
通过标准：
1. [负向] GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN
2. [非功能] 报错信息应提示使用 ATOMGIT_TOKEN 替代

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use GITHUB_TOKEN for API call | `STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}" -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}")` → `echo "api_status=$STATUS"` → `echo "done"` | - | `api_status=<http_code>`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 api_status 不为 200 |
| 2 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：需 LLM 评估替代提示 |

---
