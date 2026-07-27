用例 ID:   REL-VCJOB-01-001
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
溯源意图:  INTENT-REL-089
参照来源:  inputs/existing-cases/gitcode-pipeline-test-cases.xlsx「NPU用例」sheet 第 11 条（实测：不通过——已知失败实证）
母意图:    —
标题:      【回归】vcjob（volcano job）格式任务解析与运行——当前已知不通过，修复后回归

前置条件:
  - 已接入含 NPU 节点的 K8s 集群，集群已部署 volcano 调度器
  - 平台支持 vcjob 格式任务提交
  - ⚠️ 回归背景：xlsx 实测 vcjob 格式不通过，格式兼容存在缺陷；本用例断言按修复后的正确行为编写，修复前预期失败

操作步骤:
  1. 按 vcjob（volcano job）标准格式构造并提交 1 个请求 NPU 的训练任务
  2. 观察平台对该 vcjob 的解析结果与任务运行状态
  3. 核对 vcjob 内各 task/pod 的资源分配是否符合声明

预期结果:
  - 标准 vcjob 格式任务被正常解析并运行，各 task 按声明获得 NPU 资源
  - 当前已知不通过，修复后回归：修复前本用例预期失败，缺陷修复后必须通过
  - 不应出现格式解析失败、字段被静默丢弃或资源声明被忽略

验证点:
  - [正向][回归] 标准 vcjob 格式任务正常解析并运行（已知失败，修复后必须回归）
  - [负向] 不应出现 vcjob 字段被静默丢弃或 NPU 资源声明被忽略

清理:      删除测试 vcjob，按 fixture 重置测试实例
