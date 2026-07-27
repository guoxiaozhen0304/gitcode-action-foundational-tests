# COMP-VARREF-01-084
- **标题**: ${gitcode_*} 与 ${PIPELINE_*} 非标准插值的求值行为记录
- **维度**: 完备性
- **优先级**: P2
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**平台对 ${...} 风格占位符的处理确定：求值 / 原样保留 / 报错**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-032
通过标准：
1. ${gitcode_*} 与 ${PIPELINE_*} 的实际求值结果
2. 未求值占位符不应以字面量静默流入下游
3. 与 ${{ env.* }} 混用时的行为一致性
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Probe interpolation styles | `echo 'GC_LIT=${gitcode_SOURCE_BRANCH}' ... echo "PL_SHELL=${PIPELINE_RUN_ID}"` | — | GC_LIT=..., PL_LIT=..., GC_SHELL=, PL_SHELL= |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain GC_LIT= | positive | — | ❌ VACUOUS | 步骤仅单引号 echo 字面量，无条件分支或平台行为验证 |
| 2 | must_contain PL_LIT= | positive | — | ❌ VACUOUS | 步骤仅单引号 echo 字面量，无条件分支或平台行为验证 |
| 3 | interpolation_eval | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 4 | silent_literal | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
### 问题
两个 positive 断言均为字面量 echo 的自证预言，不验证平台是否对 ${...} 插值求值。实际探测行为完全依赖 LLM 断言。
---
