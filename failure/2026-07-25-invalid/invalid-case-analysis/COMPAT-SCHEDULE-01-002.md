## 失败分诊 · COMPAT-SCHEDULE-01-002 · schedule 不支持 timezone 字段差异

**判定结果**: INVALID (平台 API 校验驳回)
**分类**: 非预期非法 (需修复)
**诊断数**: 1 条

### 诊断信息

1. **[Error] L0:C0** — Cannot deserialize value of type `java.util.ArrayList<com.huawei.devcloud.cloudpipeline.v2.domain.entity.pac2.gitcode.on.GitcodeScheduleOn>` from Object value (token `JsonToken.START_OBJECT`)
 at [Source: UNKNOWN; byte offset: #UNKNOWN] (through reference chain: com.huawei.devcloud.cloudpipeline.v2.domain.entity.pac2.gitcode.GitcodePipelineDefinition["on"]->com.huawei.devcloud.cloudpipeline.v2.domain.entity.pac2.gitcode.on.GitcodeOn["schedule"])


### 根因初判

**根因**: 产品bug — schedule 反序列化错误——array 期望 vs object
**责任人**: 平台方

> 此 case YAML 描述的操作为合法且合理的功能需求，但被平台 API 校验拒绝，属于非预期拒绝。

### 证据

- **维度**: compatibility | **优先级**: P1 | **触发器**: schedule
- **标题**: schedule 不支持 timezone 字段差异
- **断言**: 0 positive / 1 negative

**Workflow 摘要**:
```yaml
on:
  schedule:
    cron: "0 12 * * *"
    timezone: "Asia/Shanghai"
jobs:
  verify:
    name: Verify schedule timezone rejection
    runs-on: [dedicate-hosted, x64, large]
    steps:
      - name: Echo schedule
        run: |
          echo "SCHEDULE_TIMEZONE_OK"
```

**预期行为** (Phase 01 文本用例):
```markdown
用例 ID:   COMPAT-SCHEDULE-01-002
维度标签:   [compatibility, usability]
维度:      兼容性
优先级:    P1
标题:      schedule 不支持 timezone 字段差异
前置条件:
操作步骤:
预期结果:
验证点:
```

### 对照 GitCode 规格

**规格文件**: `phase01/inputs/gitcode-spec/syntax-reference/trigger-events.md`

> 文档描述 schedule 期望数组，但平台期望 ArrayList。

### 影响评估

- **阻塞性**: 🔴阻塞 — YAML 无法通过校验，workflow 无法部署运行
- **静默性**: 🟢明确报错 — 平台明确报错，用户可定位问题
- **影响面**: 🟢单用例 — 仅影响当前测试场景

**综合**: 非预期拒绝：产品bug——schedule 反序列化错误——array 期望 vs object

**规避手段**: 需平台修复

**置信度**: 高（诊断信息明确，可直接定位根因）

### 建议

- 提交平台 bug: schedule 反序列化错误——array 期望 vs object
- 等待平台修复后重新验证

---
