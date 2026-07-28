## 失败分诊 · COMP-RUNNER-01-082 · flow-mapping 写法 runs-on 的处理结果裁定

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `runs-on` 使用了 `{}` 对象/flow-mapping 格式，平台仅支持数组格式
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 1（Runner 标签格式 — 只用数组格式，禁止 `{}` 对象格式）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
      runs-on: {ubuntu-24, x64, small}
  
  # 应改为（若希望通过校验）:
      runs-on: [ubuntu-latest, x64, small]
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 1: "只用数组格式，禁止 `{}` 对象格式。`runs-on: {ubuntu-24, x64, small}` — unknown property"

**置信度**: 高（平台 Schema 明确拒绝，规则 1 直接列出此写法为 ❌ 错误）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，但用例本身预期此行为
- **静默性**: 🟢明确报错 — 平台返回 `unknown property`
- **影响面**: 所有尝试使用 flow-mapping 格式 `{...}` 的 runs-on 配置
- **综合**: 负向用例验证 flow-mapping 被拒绝，平台行为与预期一致
- **是否有规避手段**: 否 — 此用例目的即为测试 flow-mapping 格式被拒绝，正因平台正确拒绝才被分入 INVALID；应标注为"预期拒绝"负向用例

**建议**:
- 此用例为预期被拒绝的负向测试，平台行为正确
- 将用例标注为 `expected_rejection`（预期校验拒绝），在 rubric 中记录平台返回 `unknown property`
- 无需修改 YAML，标记为 SKIP（无法通过 API 提交执行，但校验期的拒绝行为已由平台 API 返回值验证）
