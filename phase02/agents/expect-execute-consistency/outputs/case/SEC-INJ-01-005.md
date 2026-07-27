# SEC-INJ-01-005
- **标题**: 表达式求值必须防止双重模板渲染（二次求值）
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**外层 ${{ }} 求值结果中的模板语法字符被转义，不触发二次求值**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-013
通过标准：
1. 日志不含 "2"
2. 模板字符被转义
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Pass template syntax | `echo "Input: ${{ '{{ 1 + 1 }}' }}"` | — | 求值结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 日志不含 "2" | negative | run_logs must_not_contain | ✅ GENUINE | ${{ '{{ 1 + 1 }}' }} → NEVER VACUOUS；双重模板渲染由平台表达式引擎决定 |
| 2 | template_chars_escaped | positive | run_logs equals | ❌ VACUOUS | echo 输出的是求值后的文本（如 "Input: {{ 1 + 1 }}"），步骤不输出 "template_chars_escaped" 字面量 |
### 问题
断言 2 VACUOUS：断言期望的字符串是语义标签，而非步骤实际输出的内容。
---
