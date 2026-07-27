用例 ID:   USE-LBL-01-003
维度标签:   ['usability']
维度:      usability
优先级:    P0
溯源意图:  INTENT-USE-031
参照来源:  inputs/gitcode-spec/01-quick-start.md; inputs/gitcode-spec/00-overview.md; inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/gitcode-spec/writing-pipelines/configure-jobs.md
母意图:    —
标题:      runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）

前置条件:
  - 文档版本为 2026-07-20 抓取的 50 页 gitcode-spec 全集

操作步骤:
  1. 对 gitcode-spec 全文检索 runs-on: 的所有示例写法
  2. 归纳形态类别（单标签字符串 / 数组三段式 / 花括号三段式 / 自托管对象式）
  3. 检查是否存在任一处集中说明各形态等价关系或推荐写法

预期结果:
  同一字段在全集文档中形态应统一，或在 Runner 文档一处集中声明等价关系与推荐写法

验证点:
  - [负向] 同一字段在 3 个以上官方页面给出互不相同形态且无任何一处说明等价关系，即为缺陷
  - [非功能] 选择 Runner 标签页应列出全部合法形态并标注推荐项

清理:      无
