# COMPAT-EXPR-01-011
- **标题**: join() 函数缺失时的降级行为
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**join() 函数缺失时的降级行为**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-010
通过标准：
1. 平台对不支持的 join() 函数给出明确的校验错误或运行时错误
2. 不应静默求值并返回意外结果
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Test join function in run block | `RESULT="${{ join(['a', 'b', 'c'], '-') }}"` 后 `echo "join-result=$RESULT"` | — | join-result=a-b-c 或错误 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_not_contain "join-result=a-b-c" | negative | — | ✅ GENUINE | 步骤使用 ${{ join(...) }} 真实表达式；若平台不支持 join() 则不会输出此字符串，若静默支持则断言失败 |
| 2 | error_message eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 错误信息质量由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过
---
