# USE-VARS-01-002
- **标题**: 变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测
- **维度**: usability
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**变量插值双语法与 atomgit 属性名的文档清单 diff 及求值探测**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-038
通过标准：
1. 记录遗留插值语法是否被求值
2. 若遗留语法已废弃，平台应在解析时给出 deprecation 警告而非静默
3. atomgit 上下文属性应有完整且大小写明确的官方列表

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | legacy dollar brace vars | `echo "legacy1=[${gitcode_SOURCE_BRANCH}]"` / `echo "legacy2=[${PIPELINE_RUN_ID}]"` / `echo "std=[${{ atomgit.repository }}]"` | 无 | 三种插值语法求值结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs 确定性检查遗留插值语法是否求值 | positive | `${gitcode_SOURCE_BRANCH}` / `${PIPELINE_RUN_ID}` 为平台注入环境变量，`${{ atomgit.repository }}` 为表达式 | ✅ GENUINE | 环境变量注入 + 表达式求值均涉及平台真实行为 |
| 2 | documentation 确定性校验：样本插值与属性名集合与文档清单 diff | negative | 确定性文档/样本集合 diff | ✅ COVERED | 确定性文档校验 |
---
