用例 ID:   USE-EXPR-01-003
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-035
参照来源:  inputs/gitcode-spec/syntax-reference/expressions.md; inputs/gitcode-spec/COMPAT-NOTES.md
母意图:    —
标题:      expressions 函数表语法标记可解析性与状态关键字术语区分

前置条件:
  - 文档版本为 2026-07-20 抓取版本

操作步骤:
  1. 抽取 expressions.md 函数表语法列每行示意字符串
  2. 检查是否存在无法通过表达式 parser 的字符串（如多余括号）
  3. 检查文档是否把无括号状态关键字与函数混称而不加区分

预期结果:
  函数表语法示意应可粘贴即用；状态关键字应与真正函数明确分区

验证点:
  - [负向] 语法列含多余括号等无法解析的字符串即不合格
  - [负向] 文档把 success 等无括号关键字称为函数且不加区别说明即不合格
  - [非功能] 状态关键字与函数应在章节或视觉上有明确区分

清理:      无
