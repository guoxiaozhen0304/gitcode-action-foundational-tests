# COMPAT-TOKEN-01-001
- **标题**: ATOMGIT_TOKEN 应正确返回有效令牌
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**ATOMGIT_TOKEN 应正确返回有效令牌**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-020
通过标准：
1. [正向] API 调用返回 200，表明 TOKEN 有效
2. [负向] 日志中不应出现 TOKEN 明文

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use ATOMGIT_TOKEN for API call | `STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${{ atomgit.api_url }}/repos/${{ atomgit.repository }}" -H "Authorization: token $ATOMGIT_TOKEN")` → `echo "api_status=$STATUS"` → `echo "done"` | - | `api_status=<http_code>`, `done` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [ATOMGIT_TOKEN] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=success | ✅ GENUINE | 步骤执行 `curl` 实质命令发起真实 API 调用，含 `${{ }}` 表达式和 `$ATOMGIT_TOKEN` 环境变量 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 api_status 为 200 |
| 3 | run_logs | negative | must_not_contain_secret=ATOMGIT_TOKEN | ✅ GENUINE | 步骤引用 `$ATOMGIT_TOKEN` 环境变量，测试平台脱敏机制 |

---
