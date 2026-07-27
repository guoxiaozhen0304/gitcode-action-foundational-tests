# COMPAT-ENV-01-001
- **标题**: ATOMGIT_SHA 环境变量应正确返回触发提交 SHA
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**$ATOMGIT_SHA 应返回当前触发事件的提交 SHA（40 位十六进制字符串）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-017
通过标准：
1. 日志中 ATOMGIT_SHA 的值不为空且为有效 SHA 格式
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo ATOMGIT_SHA | `echo "atomgit_sha=$ATOMGIT_SHA"` | — | atomgit_sha=<40位SHA> |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status=success | positive | — | ⚠️ STATUS_GUARANTEED | 全步骤仅 echo（依赖平台注入的 shell 变量但步骤自身无条件分支） |
| 2 | run_logs 40 位 HEX SHA | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
### 问题
run_status 为 STATUS_GUARANTEED（echo 无条件成功），环境变量值的格式验证完全依赖 LLM。
---
