## 失败分诊 · REL-STAGES-01-029 · stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — Cannot deserialize value of type `java.util.LinkedHashMap<java.lang.String,com.huawei.devcloud.cloudpipeline.v2.domain.entity.pac2.gitcode.structs.GitcodeStage>` from Array value (token `JsonToken.START_ARRAY`)
 at [Source: UNKNOWN; byte offset: #UNKNOWN] (through reference chain: com.huawei.devcloud.cloudpipeline.v2.domain.entity.pac2.gitcode.GitcodePipelineDefinition["stages"])


### 根因初判

**根因**: 文档冲突 — stages 反序列化错误 (array vs map)
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: reliability | **优先级**: P1 | **触发器**: workflow_dispatch
- **标题**: stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs
- **断言**: 2 positive / 0 negative

**Workflow 摘要**:
```yaml
on:
  workflow_dispatch:
stages:
  - name: test_stage
    fail_fast: true
    jobs:
      job_a:
        name: stage job A
        runs-on: [dedicate-hosted, x64, large]
        steps:
          - name: fail step
            run: |
              exit 1
      job_b:
        name: stage job B
        runs-on: [dedicate-hosted, x64, large]
        steps:
          - name: sleep step
            run: |
              sleep 30
      job_c:
        name: stage job C
        runs-on: [dedicate-hosted, x64, large]
        steps:
          - name: sleep step
... (截断)
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   REL-STAGES-01-029
维度标签:   [reliability]
维度:      稳定性
优先级:    P1
标题:      stages fail_fast 机制——阶段内任一 job 失败应立即终止同阶段其他 jobs
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/writing-pipelines/configure-dependencies-order.md`

> 文档展示 stages array 和 map 两种格式，但平台只接受 map 格式。

### 影响评估

- **阻塞性**: 🔴阻塞 — YAML 无法通过校验，workflow 无法部署运行
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：文档冲突——stages 反序列化错误 (array vs map)

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 平台团队更新文档以描述实际行为: stages 反序列化错误 (array vs map)

---
