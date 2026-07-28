# COMPAT-SHELL-01-002
- **标题**: 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录
- **维度**: 兼容性
- **评级**: 部分不符

## 想测什么
验证未显式声明working-directory时默认工作目录为仓库根目录。

## 做了什么
step1使用 `uses: checkout`；step2输出 `pwd` + `ls -la`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive contains | "README" | COVERED | pwd和ls -la为真实命令(GENUINE R1)，日志可观测文件列表 |

**部分不符原因**: YAML中只定义了1个断言(contains README)，但text/预期结果提出"工作目录路径与仓库根目录一致"和"可访问仓库根目录文件"两个正向验证点，而YAML仅预期日志含"README"——若仓库根目录无README.md则断言无法满足。缺少对外部仓库fixture内容的依赖声明。步骤2中ls -la输出全量文件列表可以验证，但断言仅check一个特定文件名不够稳健。
