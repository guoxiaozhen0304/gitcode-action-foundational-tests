```
用例 ID:   COMPAT-EXPR-01-016
维度标签:   [compatibility]
维度:      兼容性
优先级:    P2
溯源意图:  INTENT-COMPAT-050
参照来源:  inputs/github-reference/reference/expressions.md; inputs/gitcode-spec/syntax-reference/expressions.md
母意图:    —（与 INTENT-COMPAT-009 互补：009 为运算符类型强转，本条为函数与字面量语法边界）
标题:      format() 花括号转义与字符串字面量引号规则边界

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个使用 format 双花括号转义模板与双单引号转义字符串的 workflow
  2. 触发并读取求值结果，与 GitHub 语义比对

预期结果:
  - format 的转义语义与 GitHub 对齐（支持双花括号转义），或文档声明不支持及替代写法
  - 字符串字面量引号规则（双单引号转义、双引号报错）与 GitHub 一致

验证点:
  - [正向] format 双花括号转义求值结果与 GitHub 对齐
  - [正向] 双单引号转义为字面单引号的行为与 GitHub 一致
  - [负向] 双引号字符串不应被静默接受却求值异常

清理:      重置 fixture 仓库
```
