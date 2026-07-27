```
用例 ID:   COMPAT-RUNSON-01-006
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-054
参照来源:  inputs/github-reference（hosted runner OS 矩阵）; inputs/gitcode-spec/runner-management/selecting-runner-labels.md; baseline/parity-matrix.md（缺行，盲区 B1）
母意图:    —（变体自 COMPAT-RUNSON-01-005：macos-latest 探测；2026-07-27 STOP① 增补）
标题:      Runner OS 多样性探测：macos-latest 的调度结局（不支持应明确报错）

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 runs-on 指定 macos-latest 标签的 workflow
  2. 观察校验/调度阶段响应并逐字记录结局

预期结果:
  - 结局确定：调度成功（平台提供 macOS Runner）或校验/调度期明确报错并列出受支持 OS
  - 不应表现为 job 无限 queued 且无任何提示

验证点:
  - [正向/记录] macos-latest 的调度结局逐字记录
  - [负向] 指定不支持 OS 的 job 不应无限 queued 无提示
  - [非功能] 结论与 windows 案合并回写 parity-matrix Runner OS 多样性行

清理:      重置 fixture 仓库
```
