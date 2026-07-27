# COMPAT-RUNNER-01-008
- **标题**: 与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-047
通过标准：
1. [正向] docker 守护进程可用性结论确定
2. [正向] 浏览器可用性结论确定
3. [非功能] 差距清单进入迁移文档

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Probe docker daemon | `docker info 2>&1 \| head -5 \|\| echo "DOCKER_MISSING"` | - | docker info 或 DOCKER_MISSING |
| 2 | Probe browsers | `which google-chrome 2>&1 \|\| echo "CHROME_MISSING"` etc. → `echo "CAPABILITY_PROBE_DONE"` | - | 路径或 MISSING, `CAPABILITY_PROBE_DONE` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain="CAPABILITY_PROBE_DONE" | ✅ GENUINE | 步骤先执行 `docker info`、`which google-chrome` 等实质探测命令再 echo 哨兵 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 评估 docker/browser 可用性结论 |
| 3 | run_logs | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能：差距清单写入迁移文档 |

---
