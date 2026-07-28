## 失败分诊 · SEC-TOKEN-01-003 · run 结束后旧 ATOMGIT_TOKEN 调用任何 API 必须失效

**判定结果**: FAIL

**失败断言**:
- assertions[0] (positive, run_logs, value): 期望 `log contains 'in_run_token_operational'`，实际 `absent`
- assertions[1] (negative, run_logs, leak): 期望 `plaintext 'http_2xx_with_post_run_token' 0 hits`，实际 `0` — **通过**
- assertions[2] (nonfunctional, rerun_behavior): **未在 assertion_results 中出现**（编译缺口，`rerun_behavior` target 不被支持）

**根因初判**: 标记不匹配

**责任人**: Phase 01 — 断言关键词 `in_run_token_operational`（小写）与 YAML workflow 中 echo 输出的实际内容 `IN_RUN_TOKEN_OPERATIONAL`（大写）大小写不匹配；断言引擎做精确大小写比较。平台 ATOMGIT_TOKEN 在运行期间行为完全正确（git ls-remote 成功）。另伴生：`rerun_behavior` target 不被支持（编译缺口）。

**证据**:

- **Job 日志全量**（10 行，真实执行，token 行为完全正确）:
  ```
  [2026/07/28 13:22:13.691 GMT+08:00] [INFO] Job(1531653004124233728_1531653004086484999) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../c48246b3-af15-488f-8f71-0fa45ff64a12.sh
  ::debug::Executing: bash -e .../c48246b3-af15-488f-8f71-0fa45ff64a12.sh
  a78212cffb34e20cdb28cfd108f5fe5fcd909a8a	HEAD              ← git ls-remote 成功！token 有效

  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../86e5ff1d-83b1-4e48-b516-b3a1e4ecc505.sh
  ::debug::Executing: bash -e .../86e5ff1d-83b1-4e48-b516-b3a1e4ecc505.sh
  IN_RUN_TOKEN_OPERATIONAL: token worked within scope during run   ← 标记存在，但为大写
  ```
  关键证据：
  - 第 5 行：`a78212cffb34e20cdb28cfd108f5fe5fcd909a8a	HEAD` —— `git ls-remote` 命令**成功执行**，ATOMGIT_TOKEN 在运行期间工作正常
  - 第 10 行：`IN_RUN_TOKEN_OPERATIONAL: token worked within scope during run` —— 标记**确实存在**于日志中，但为全大写

- **预期行为**（Phase 01 文本用例 SEC-TOKEN-01-003，P1，安全性）:
  - 操作步骤 1: "触发一个 workflow，run 进行中用 ATOMGIT_TOKEN 完成一次其权限内的只读操作（如 clone）"
  - 预期结果: "run 进行中 token 在其权限范围内可用"
  - 验证点: "[正向] run 进行中 token 可完成权限内只读操作"

- **实际行为**:
  - Token 在运行期间**完全正常工作**：`git ls-remote` 成功返回 commit SHA（`a78212cffb34e20cdb28cfd108f5fe5fcd909a8a`）
  - 日志**包含**标记字符串，但为大写 `IN_RUN_TOKEN_OPERATIONAL`
  - 断言关键词为小写 `in_run_token_operational`
  - 断言引擎做**精确大小写比较** → 小写关键词在日志中未找到 → 返回 `absent` → FAIL
  - **这是假阳性**：token 行为完全符合预期，FAIL 仅因断言大小写不匹配

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/security-permissions/token-permissions.md`:
  - 第 11-13 行："每次流水线运行时，AtomGit Action 自动生成 `ATOMGIT_TOKEN`，用于：克隆代码仓库..."
  - 第 20 行："`ATOMGIT_TOKEN` 的权限范围由 workflow 的 `permissions` 字段控制"
  - 测试 YAML 中 `${{ atomgit.token }}` 的引用方式与规格一致
  - 日志第 5 行的 `git ls-remote` 成功结果证明了 ATOMGIT_TOKEN 的自动生成和基本权限均正常

- **断言链路缺陷详情**:
  - YAML workflow echo: `echo "IN_RUN_TOKEN_OPERATIONAL: token worked within scope during run"` — **大写输出**
  - YAML 断言: `equals: "in_run_token_operational"` — **小写关键词**
  - 编译器行为：将 `in_run_token_operational` 按原样保留，未做大小写归一化
  - 断言引擎行为：在日志中精确匹配 `in_run_token_operational` → 不匹配大写版本 `IN_RUN_TOKEN_OPERATIONAL` → absent
  - **修复方向**：① 编译阶段做大小写归一化（将关键词和 echo 标记统一为小写），或 ② 断言引擎做大小写不敏感匹配

- **编译缺口（`rerun_behavior` target）**:
  - YAML 断言 3: `type: nonfunctional, target: rerun_behavior, equals: "new_token_issued_or_explicit_reuse"`
  - 该断言在 assertion_results 中未出现 → `rerun_behavior` 作为 target 类型不被编译器/断言引擎支持
  - **run 结束后 token 失效的验证实际上完全缺失**——本用例最核心的安全验证点被静默跳过

**置信度**: 高（日志直接证据：第 5 行 git ls-remote 成功、第 10 行标记存在但大小写不匹配；断言引擎精确大小写对比行为明确）

**影响**:
- **阻塞性**: ⚪无影响 — 假阳性，平台 ATOMGIT_TOKEN 在运行期间行为完全正确
- **静默性**: ⚪无影响 — 用户可见正常运行的 git ls-remote 结果
- **影响面**: 🟡同维度 — 所有依赖 `equals` 关键词大小写精确匹配的断言均可能受影响；`rerun_behavior` target 不支持意味着所有 token 生命周期测试的关键验证被跳过
- **综合**: 无影响——纯断言关键词大小写不匹配导致的假阳性；token 运行期间行为完全符合文档承诺。但 `rerun_behavior` target 缺失意味着"run 结束后旧 token 失效"这一核心安全验证从未被实际测试
- **是否有规避手段**: 否——断言引擎的精确大小写比较行为无法由用户规避

**建议**:
- **Phase 01 `compile_asserts.py`** 对 `equals`/`contains` 类断言关键词做**大小写归一化**（统一转小写），或配置断言引擎做大小写不敏感匹配
- **Phase 01 编译器** 添加 `rerun_behavior` 作为支持的 target 类型，确保 token 生命周期验证不被静默跳过——这是本用例最核心的安全断言
- 对 YAML workflow 中 echo 输出的标记字符串做一次规范检查，确保所有标记字符串与对应断言关键词的大小写一致
- 相关用例: SEC-TOKEN-01-001/002/004（token 生命周期系列）、所有使用 `equals:` 做日志标记匹配的用例
