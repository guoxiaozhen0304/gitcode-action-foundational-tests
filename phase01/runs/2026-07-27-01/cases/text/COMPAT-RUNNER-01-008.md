```
用例 ID:   COMPAT-RUNNER-01-008
维度标签:   [compatibility]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-047
参照来源:  inputs/github-reference（hosted runner 能力基线）; inputs/gitcode-spec/syntax-reference/runner-images-tools.md
母意图:    —（变体自 COMPAT-RUNNER-01-007：与 GitHub hosted image 的能力差距面）
标题:      与 GitHub hosted image 的关键能力差距（docker 守护进程、浏览器）探测

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个探测 docker 守护进程可用性与常见浏览器（chrome/firefox）存在性的 workflow
  2. 触发并记录实测结论

预期结果:
  - docker、浏览器等 GitHub 常见预装能力的可用性得到确定结论
  - 与 GitHub hosted image 的差距清单进入迁移文档

验证点:
  - [正向] docker 守护进程可用性结论确定
  - [正向] 浏览器可用性结论确定
  - [非功能] 差距清单进入迁移文档

清理:      重置 fixture 仓库
```
