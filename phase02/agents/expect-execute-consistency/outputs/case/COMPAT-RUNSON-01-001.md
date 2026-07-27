# COMPAT-RUNSON-01-001
- **标题**: runs-on 标签体系——三段式数组正常匹配
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runs-on 标签体系——三段式数组正常匹配**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-027
通过标准：
1. [正向] 工作流成功启动并执行
2. [正向] 日志中显示 Runner 标签与声明一致
3. [负向] 不应因数组格式而被平台拒绝解析

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | (TC) echo runner info | `echo "RUNSON_ARRAY_OK"` → `echo "Runner labels: dedicate-hosted x64 large"` | - | `RUNSON_ARRAY_OK`, `Runner labels: ...` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed_success | ✅ GENUINE | Job 级 `runs-on: [ubuntu-latest, x64, small]` 需平台正确调度三段式标签，调度失败则 never run |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认 RUNSON_ARRAY_OK 出现 |
| 3 | workflow_parse | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认数组格式未被拒绝 |

---
