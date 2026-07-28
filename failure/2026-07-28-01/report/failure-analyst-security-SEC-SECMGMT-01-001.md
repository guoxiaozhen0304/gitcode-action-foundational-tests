## 失败分诊 · SEC-SECMGMT-01-001 · Secret 写入后任何 API/UI 路径绝不应回读明文

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, run_logs, value): 期望 `log contains 'masked_with_asterisks'`，实际 `absent`
- assertions[1] (config_probe): pass=true, configured — **DEPLOY_TOKEN 已配置**

**根因初判**: 标记不匹配

**责任人**: Phase 01 — `compile_asserts.py` 中关键词 `masked_with_asterisks` 未正确映射到实际的 secret 脱敏检测逻辑（`***` 模式匹配），导致断言引擎对日志做字面字符串查找而非脱敏检测

**证据**:

- **Job 日志全量**（5 行，真实执行，secret 已正确脱敏）:
  ```
  [2026/07/28 13:21:26.357 GMT+08:00] [INFO] Job(1531652805653708800_1531652805620154375) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../63e20263-5176-4ece-8d0d-e6bd7f88166f.sh
  ::debug::Executing: bash -e .../63e20263-5176-4ece-8d0d-e6bd7f88166f.sh
  SECRET_REFERENCE_CHECK: ***
  ```
  关键行（第 5 行）：`SECRET_REFERENCE_CHECK: ***` —— **secret 值已被平台正确替换为 `***`，脱敏正常工作**

- **预期行为**（Phase 01 文本用例 SEC-SECMGMT-01-001，P1，安全性）:
  - 操作步骤 3: "触发一个正常引用 DEPLOY_TOKEN 的 workflow，确认引用侧可用且日志脱敏"
  - 预期结果: "workflow 正常引用该 secret，日志中显示为脱敏形式"
  - 验证点: "[正向] 授权管理员可创建/更新 secret，workflow 正常引用且日志脱敏"

- **实际行为**:
  - Secret 引用侧**完全正常**：workflow 成功执行（run_status=COMPLETED）、DEPLOY_TOKEN 在日志中正确显示为 `***`
  - config_probe 确认 DEPLOY_TOKEN 已配置
  - **断言引擎误报 FAIL**：YAML 断言 `equals: "masked_with_asterisks"` 在编译后执行的是对日志文本进行字面搜索 "masked_with_asterisks"——该字符串不在日志中（日志实际含 `***`）
  - 平台行为完全符合文档承诺，FAIL 是断言引擎关键词映射缺陷导致的假阳性

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/security-permissions/using-secrets.md`:
  - 第 62-66 行"Secret 安全机制"表格：
    | 安全措施 | 说明 |
    |--------|------|
    | **日志遮掩** | Secret 值在日志中自动替换为 `***` |
  - 该文档精确承诺了 secret 在日志中显示为 `***`——日志第 5 行的 `SECRET_REFERENCE_CHECK: ***` 完全符合此承诺
  - 测试 YAML 中 `echo "SECRET_REFERENCE_CHECK: ${{ secrets.DEPLOY_TOKEN }}"` 的写法与规格第 38 行示例完全对应

- **断言编译链路缺陷**:
  - YAML 断言（由 Phase 01 生成）：`equals: "masked_with_asterisks"` 
  - 语义意图：验证日志中 secret 显示为脱敏形式（即 `***`）
  - 编译器行为：将 `masked_with_asterisks` 当作字面搜索关键词，未将其映射为实际的 `***` 模式检测
  - 断言引擎行为：在日志中搜索字面字符串 "masked_with_asterisks" → 未找到 → absent → FAIL
  - 关键词映射缺失导致断言引擎无法正确评估 secret 脱敏状态

- **API 侧断言未评估**:
  - YAML 还定义了断言 `type: negative, target: secret_mgmt_api, must_not_contain_secret: "DEPLOY_TOKEN"`
  - 该断言在 assertion_results 中未出现——`secret_mgmt_api` 作为 target 类型可能不被断言引擎/编译器支持（编译缺口）
  - 这使得 'API/UI 绝不应回读明文' 的 API 侧验证完全缺失

**置信度**: 高（日志直接证据：第 5 行 `***` 脱敏正确；config_probe 证实 secret 已配置；平台行为完全正确，FAIL 是关键词映射缺陷所致）

**影响**:
- **阻塞性**: ⚪无影响 — 假阳性，平台 secret 脱敏功能正常工作
- **静默性**: ⚪无影响 — 平台正确脱敏，用户可见 `***`
- **影响面**: 🟢单用例 — 仅影响本断言关键词映射，其他 secret 脱敏测试可能受影响（如 ASSUME_1XX→`*`、EMPTY→空 等关键词未确认映射）
- **综合**: 无影响——纯断言引擎关键词映射缺陷（"masked_with_asterisks" 映射缺失），平台 secret 脱敏行为完全符合 GitCode 文档承诺
- **是否有规避手段**: 否——断言引擎的关键词映射缺陷无法由用户规避；需 Phase 01 修复编译器关键词映射表

**建议**:
- **Phase 01 `compile_asserts.py`** 将 `masked_with_asterisks`（及同类脱敏描述词）映射为实际日志脱敏模式检测（检查 secret 值是否在日志中出现了 `***` 取代原文），而非字面搜索该关键词本身
- 将 `secret_mgmt_api` 加入编译器支持的 target 类型清单，确保 API 侧 secret 读取验证不被静默跳过
- 对所有脱敏相关断言关键词做一次全面排查：`masked_with_asterisks`、`masked`、`redacted`、`***` 等，确认映射关系完整
- 相关用例: 所有使用 `equals: "masked_with_asterisks"` 或类似脱敏关键词的秘密管理用例
