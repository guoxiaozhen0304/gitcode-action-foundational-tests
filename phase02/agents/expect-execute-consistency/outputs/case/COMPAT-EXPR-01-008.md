# COMPAT-EXPR-01-008
- **标题**: toJson 表达式输出格式差异（pretty-print vs compact）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**toJson 表达式输出格式差异**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-008
通过标准：
1. toJson 输出应为合法 JSON
2. 输出格式应与 GitHub Actions 行为一致
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Output object via toJson | `echo '${{ toJson({'key1': 'value1', 'key2': 'value2'}) }}'` | — | toJson 序列化结果 |
| 2 | Output array via toJson | `echo '${{ toJson(['a', 'b', 'c']) }}'` | — | toJson 数组序列化结果 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs must_contain "key1" | positive | — | ✅ GENUINE | 步骤使用 ${{ toJson(...) }} 表达式求值，"key1" 仅当 toJson 正确输出对象时出现在日志中 |
| 2 | run_logs eval=llm_assisted | nonfunctional | — | 🔶 LLM_DEPENDENT | 格式合法性由 LLM 判定 |
### 问题
- 断言2（LLM判定）被跳过，不影响评级；断言1为 GENUINE
---
