# COMPAT-RUNNER-01-007
- **标题**: Runner 预装工具链规格清单与实测全面对账
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**Runner 预装工具链规格清单与实测全面对账**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-047
通过标准：
1. [正向] 规格清单逐项实测：java/mvn/gradle/node/go/kubectl/aws-cli 版本存在性
2. [负向] 不应出现文档列出但实测缺失的工具而无记录
3. [非功能] 对账结果回写文档或登记文档缺陷

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Probe java and maven and gradle | `java -version 2>&1 \| head -1 \|\| echo "JAVA_MISSING"` etc. | - | 工具版本或 MISSING 标记 |
| 2 | Probe node go kubectl awscli | `node --version 2>&1 \|\| echo "NODE_MISSING"` etc. → `echo "AUDIT_DONE"` | - | 工具版本或 MISSING 标记, `AUDIT_DONE` |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain="AUDIT_DONE" | ✅ GENUINE | 步骤先执行 java/mvn/node/go 等实质命令探测工具链再 echo 哨兵 |
| 2 | run_logs | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 逐项比对工具版本与规格清单 |
| 3 | run_logs | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 确认无未记录缺陷 |

---
