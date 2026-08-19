用例 ID:   USE-DOCS-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-017
母意图:    —
标题:      官方文档中 GitHub 专有措辞应已替换为 GitCode 术语

前置条件:
  - 仓库 fixture: ComputingActionTest/gitcode_api

操作步骤:
  1. 抓取 GitCode 官方文档页面
  2. 扫描页面内容中的 GitHub 专有术语
  3. 验证关键术语已替换

预期结果:
  1. 文档中 github.actions 已替换为 gitcode.actions
  2. GITHUB_TOKEN 说明已替换为 ATOMGIT_TOKEN
  3. 无残留 GitHub Actions 品牌名

验证点:
  - [负向] 不含 GitHub Actions 品牌名
  - [正向] 使用 GitCode 品牌名

清理:      none
