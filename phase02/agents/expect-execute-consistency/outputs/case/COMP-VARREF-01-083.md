# COMP-VARREF-01-083
- **标题**: YAML 表达式与 Shell 环境变量引用方式验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**${{ env.VAR }} 与 $VAR 引用同一变量时值一致，${{ atomgit.sha }} 与 $ATOMGIT_SHA 值一致**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-083
通过标准：
1. 表达式引用与环境变量引用结果相同
2. atomgit 上下文与 ATOMGIT_* 环境变量值一致
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Compare references | `echo "EXPR=${{ env.TEST_VAR }}" ... echo "ref_ok"` | — | EXPR=hello, ENV=hello, SHA_EXPR=..., SHA_ENV=..., ref_ok |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | must_contain EXPR=hello | positive | — | ✅ GENUINE | 步骤使用 `${{ env.TEST_VAR }}` 表达式求值 |
| 2 | must_contain ENV=hello | positive | — | ✅ GENUINE | 步骤使用 shell 环境变量 $TEST_VAR（workflow env 设置） |
| 3 | must_contain ref_ok | positive | — | ✅ GENUINE | 步骤含 ${{ }} 表达式，非纯 echo 步骤 |
---
