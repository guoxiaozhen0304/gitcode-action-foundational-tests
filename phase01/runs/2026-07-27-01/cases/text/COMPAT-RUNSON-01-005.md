```
用例 ID:   COMPAT-RUNSON-01-005
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-054
参照来源:  inputs/github-reference（hosted runner OS 矩阵）; inputs/gitcode-spec/runner-management/selecting-runner-labels.md; baseline/parity-matrix.md（缺行，盲区 B1）
母意图:    —（2026-07-27 STOP① 用户裁决增补；关联 INTENT-COMPAT-NEW-008 不支持标签报错、INTENT-COMP-029）
标题:      Runner OS 多样性探测：windows-latest 的调度结局（不支持应明确报错）

前置条件:
  - 仓库已启用 GitCode Action

操作步骤:
  1. 提交一个 runs-on 指定 windows-latest 标签的 workflow
  2. 观察校验/调度阶段响应并逐字记录结局

预期结果:
  - 结局确定：调度成功（平台提供 Windows Runner）或校验/调度期明确报错并列出受支持 OS
  - 不应表现为 job 无限 queued 且无任何提示

验证点:
  - [正向/记录] windows-latest 的调度结局逐字记录
  - [负向] 指定不支持 OS 的 job 不应无限 queued 无提示
  - [非功能] 结论回写 parity-matrix 新增 Runner OS 多样性能力行

清理:      重置 fixture 仓库
```
