用例 ID:   REL-RUNNER-01-050
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-074
参照来源:  history/issues-encountered.md #48/#96; platform-config/instance-config.md
母意图:    —
标题:      架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）

前置条件:
  - 实例同时存在 x64 与 arm64 runner 池
  - fixture 仓库可触发指定 runs-on 架构标签的探针 job

操作步骤:
  1. 分别触发 runs-on 声明 x64 与 arm64 的探针 job（job 内打印 uname -m）
  2. 两种架构档位各采样 10 次
  3. 对无匹配架构空闲 runner 的场景观察排队/报错行为

预期结果:
  - x64 job 的 uname -m 输出=x86_64；arm64 job 输出=aarch64
  - 20 次采样架构匹配率=100%
  - 无匹配架构 runner 时 job 明确排队或报错，不错配执行

验证点:
  - [正向] x64 探针输出=x86_64，arm64 探针输出=aarch64
  - [负向] 任一档位 10 次采样中架构错配次数=0（#48/#96 回归点）
  - [非功能] 无对应架构空闲 runner 时状态=queued 或明确报错，而非错配执行

清理:      无需重置（探针 job 无副作用）
