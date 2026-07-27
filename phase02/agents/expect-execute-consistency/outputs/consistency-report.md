# 断言-步骤一致性报告

**用例总数**: 369

---

## 1. 总览

| 评级 | 数量 | 说明 |
|------|:---:|------|
| 断言一致 | 170 | 所有验证点可被步骤真实覆盖 |
| 部分不符 | 171 | 部分验证点为 TRIVIAL / MISSING / UNVERIFIABLE |
| 完全不符 | 28 | 全部验证点未能由步骤产出 |
| 合计 | **369** | |

| 维度 | 断言一致 | 部分不符 | 完全不符 | 合计 |
|------|:---:|:---:|:---:|:---:|
| usability/compatibility | 3 | 4 | 4 | 11 |
| usability/security | 0 | 1 | 0 | 1 |
| 兼容性 | 70 | 35 | 2 | 107 |
| 可靠性 | 3 | 9 | 1 | 13 |
| 安全性 | 23 | 28 | 0 | 51 |
| 完备性 | 45 | 36 | 7 | 88 |
| 易用性 | 18 | 9 | 10 | 37 |
| 稳定性 | 8 | 49 | 4 | 61 |

---

## 断言一致 — 所有验证点真实覆盖（170 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-ARTIFACT-01-001](case/COMP-ARTIFACT-01-001.md) | artifact 可在同 workflow 的 job 间正确传递 | [正向] download 后文件内容正确: ✅ COVERED — 步骤4 cat dist/app.txt 输出"hello artif |
| 2 | [COMP-ARTIFACT-01-002](case/COMP-ARTIFACT-01-002.md) | 下载全部制品功能正常 | [正向] 所有 artifact 文件均存在: ✅ COVERED — 步骤5 cat 两个文件，断言 run_logs contains  |
| 3 | [COMP-ARTIFACT-01-003](case/COMP-ARTIFACT-01-003.md) | artifact 保留期设置生效 | [正向] 保留期内可下载 artifact: ✅ COVERED — 断言 artifact_available=yes_within_re |
| 4 | [COMP-CACHE-01-001](case/COMP-CACHE-01-001.md) | cache hit 时恢复缓存内容正确 | [正向] cache 步骤状态为 success: ✅ COVERED — 断言 cache_step=hit，run_status=suc |
| 5 | [COMP-CACHE-01-002](case/COMP-CACHE-01-002.md) | restore-keys 前缀匹配兜底生效 | [正向] cache 步骤通过 restore-keys 命中: ✅ COVERED — 断言 cache_step=restore_hit |
| 6 | [COMP-CALL-01-002](case/COMP-CALL-01-002.md) | 3 层 workflow_call 嵌套应被拒绝 | [负向] 运行不应成功完成: ✅ COVERED — negative assertion: run_status != success，r |
| 7 | [COMP-CTX-01-051](case/COMP-CTX-01-051.md) | 上下文在 workflow job step 各级注入验证 | [正向] workflow 级 env 可解析 atomgit 属性: ✅ COVERED — workflow env WF_REF=${ |
| 8 | [COMP-CTX-01-053](case/COMP-CTX-01-053.md) | 上下文在 Action 插件参数中注入验证 | [正向] with 参数中的上下文表达式被正确替换并传入 Action: ✅ COVERED — checkout action with  |
| 9 | [COMP-DIR-01-001](case/COMP-DIR-01-001.md) | .gitcode/workflows/ 下的 YAML 被正确识别并触发 | [正向] 运行记录存在且 file_path 为 .gitcode/workflows/ci.yml: ✅ COVERED — 断言 run |
| 10 | [COMP-DIR-01-002](case/COMP-DIR-01-002.md) | .github/workflows/ 下的 YAML 不被识别为 workflow | [负向] 运行列表中不存在源自 .github/workflows/ci.yml 的运行: ✅ COVERED — negative ass |
| 11 | [COMP-EXPR-01-057](case/COMP-EXPR-01-057.md) | format substring replace 函数边界行为 | [正向] format 输出拼接后的字符串: ✅ COVERED — 断言 FMT=Hello World，验证 'Hello {0}' 替 |
| 12 | [COMP-ISOLATION-01-002](case/COMP-ISOLATION-01-002.md) | 环境变量不跨 job 泄漏 | [负向] job 2 中环境变量值为空或未设置: ✅ COVERED — negative assertion: must_not_cont |
| 13 | [COMP-JOB-01-067](case/COMP-JOB-01-067.md) | job 可选字段 env if timeout-minutes needs 验证 | [正向] job env 在 step 中可访问: ✅ COVERED — job env JOB_VAR=job_value，断言 JOB |
| 14 | [COMP-JOB-01-068](case/COMP-JOB-01-068.md) | job strategy 矩阵与 continue-on-error 验证 | [正向] 矩阵变量在 step 中可访问: ✅ COVERED — 断言 VERSION=a 和 VERSION=b，证明矩阵展开为两个实例 |
| 15 | [COMP-PERMS-01-001](case/COMP-PERMS-01-001.md) | permissions 空对象时 ATOMGIT_TOKEN 仅 repositor | [正向] permissions: {} 下无法执行写操作: ✅ COVERED — steps have real logic; [负向] |
| 16 | [COMP-PERMS-01-002](case/COMP-PERMS-01-002.md) | 声明 repository write 后 TOKEN 可推送代码 | [正向] 推送代码成功返回 200/201: ✅ COVERED — steps have real logic |
| 17 | [COMP-PERMS-01-003](case/COMP-PERMS-01-003.md) | fork PR 的 pull_request 下声明 write 仍仅 read | [负向] 写操作应失败: ✅ COVERED — 步骤使用 curl 真实发起 API 写请求，通过 `; [正向] 系统应强制 fork  |
| 18 | [COMP-PR-01-001](case/COMP-PR-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secrets | [负向] 日志不含 DEPLOY_TOKEN 明文: ✅ COVERED — 步骤使用 `${{ secrets.DEPLOY_TOKEN  |
| 19 | [COMP-PR-01-002](case/COMP-PR-01-002.md) | pull_request_target 可访问 secrets 且 TOKEN 拥有 | [正向] pull_request_target 可访问 secrets: ✅ COVERED — 步骤使用 `${{ secrets.DE |
| 20 | [COMP-PR-01-003](case/COMP-PR-01-003.md) | fork PR 的 pull_request workflow ATOMGIT_TO | [负向] 写操作（如推送、评论）应失败: ✅ COVERED — 步骤使用 curl 真实执行 API 写请求，通过 `; [正向] ATO |
| 21 | [COMP-PUSH-01-002](case/COMP-PUSH-01-002.md) | 不匹配 branches 的 push 不触发 workflow | [负向] 运行列表中不存在该 push 触发的运行: ✅ COVERED — negative assertion in YAML asse |
| 22 | [COMP-RERUN-01-001](case/COMP-RERUN-01-001.md) | rerun 后 atomgit.sha 保持原始值 run_number 递增 | [正向] rerun 后 sha 与原始运行一致: ✅ COVERED — steps have real logic; [正向] reru |
| 23 | [COMP-RUNNER-01-001](case/COMP-RUNNER-01-001.md) | 三段式标签正确调度到对应规格 Runner | 运行状态为 success: 覆盖 — workflow can potentially fail; job 的 Runner 标签与声明一 |
| 24 | [COMP-RUNNER-01-002](case/COMP-RUNNER-01-002.md) | runs-on default 等效 ubuntu-latest x64 small | 运行状态为 success: 覆盖 — workflow can potentially fail; Runner 规格与 small（2核 |
| 25 | [COMP-RUNNER-01-080](case/COMP-RUNNER-01-080.md) | runner 上下文属性可访问性验证 | [正向] runner.name / temp / tool_cache 非空: ✅ COVERED — steps have real l |
| 26 | [COMP-SCRIPT-01-081](case/COMP-SCRIPT-01-081.md) | 仓库内脚本执行与路径验证 | [正向] 仓库内脚本成功执行: ✅ COVERED — steps have real logic; [正向] 脚本输出出现在日志中: ✅  |
| 27 | [COMP-SCRIPT-01-082](case/COMP-SCRIPT-01-082.md) | 脚本权限设置与直接执行验证 | [正向] chmod 后脚本可执行: ✅ COVERED — steps have real logic; [正向] 直接执行输出正确: ✅ |
| 28 | [COMP-SECRET-01-001](case/COMP-SECRET-01-001.md) | echo secret 在日志中被脱敏为 *** | [正向] 日志中包含 *** 而非真实 secret 值: ✅ COVERED — steps have real logic |
| 29 | [COMP-SECRET-01-002](case/COMP-SECRET-01-002.md) | secret 原始值不应以明文出现在标准日志中 | [负向] 日志中不包含 secret 原始明文: ✅ COVERED — negative assertion in YAML assert |
| 30 | [COMP-SECRET-01-003](case/COMP-SECRET-01-003.md) | base64 编码后的 secret 是否仍被脱敏 | [非功能] 记录 base64 编码输出是否被脱敏: ✅ COVERED — steps have real logic |
| 31 | [COMP-STAGES-01-002](case/COMP-STAGES-01-002.md) | fail_fast true 时 stage 内任一 job 失败终止同阶段其余 j | 同 stage 其余 job 被终止: 覆盖 — status assertion: skipped_for_should_skip; 后续 |
| 32 | [COMP-STATUS-01-002](case/COMP-STATUS-01-002.md) | 失败 step 的日志完整保留且可查看 | [正向] 失败 step 前的输出存在于日志: ✅ COVERED — steps have real logic; [正向] 失败 ste |
| 33 | [COMP-STEP-01-069](case/COMP-STEP-01-069.md) | step 必填与核心字段 name run uses 验证 | [正向] name + run 步骤正常执行: ✅ COVERED — steps have real logic; [正向] name + |
| 34 | [COMP-STEP-01-070](case/COMP-STEP-01-070.md) | step 可选字段 id env if with 验证 | [正向] id 定义的步骤可被后续引用 outputs: ✅ COVERED — steps have real logic; [正向] e |
| 35 | [COMP-SUMMARY-01-001](case/COMP-SUMMARY-01-001.md) | ATOMGIT_STEP_SUMMARY Markdown 表格与标题正确渲染 | [正向] 详情页显示格式化的 Markdown 内容: ✅ COVERED — steps have real logic; [正向] 表格 |
| 36 | [COMP-SUMMARY-01-002](case/COMP-SUMMARY-01-002.md) | summary 中不应暴露系统内部路径 | [负向] summary 中不出现 /tmp/runner-xxx 等内部路径: ✅ COVERED — negative assertio |
| 37 | [COMP-SYSENV-01-059](case/COMP-SYSENV-01-059.md) | ATOMGIT 系统环境变量关键变量存在性 | [正向] 关键 ATOMGIT_* 变量在日志中显示非空: ✅ COVERED — steps have real logic; [负向]  |
| 38 | [COMP-SYSENV-01-060](case/COMP-SYSENV-01-060.md) | ATOMGIT 系统环境变量值正确性 | [正向] ATOMGIT_SHA 等于 atomgit.sha: ✅ COVERED — steps have real logic; [正 |
| 39 | [COMP-TIMEOUT-01-002](case/COMP-TIMEOUT-01-002.md) | 超时的 job 被强制终止并标记为 failure | [负向] 运行状态为 failure: ✅ COVERED — negative assertion in YAML assertions; |
| 40 | [COMP-TRIG-01-072](case/COMP-TRIG-01-072.md) | push 事件关键字段与过滤验证 | [正向] push 到 main 触发 workflow: ✅ COVERED — steps have real logic; [正向]  |
| 41 | [COMP-TRIG-01-074](case/COMP-TRIG-01-074.md) | workflow_dispatch 事件关键字段与 inputs 验证 | [正向] 手动触发成功创建 run: ✅ COVERED — steps have real logic; [正向] inputs 参数值在 |
| 42 | [COMP-TRIG-01-076](case/COMP-TRIG-01-076.md) | issue_comment 事件关键字段与 types 验证 | [正向] issue 评论创建时触发: ✅ COVERED — 步骤通过 ${{ atomgit.event.comment.id }} 和 |
| 43 | [COMP-TRIG-01-077](case/COMP-TRIG-01-077.md) | pull_request_comment 事件关键字段与过滤验证 | [正向] PR 评论创建时触发: ✅ COVERED — steps have real logic; [正向] event.comment |
| 44 | [COMP-UNKNOWN-01-002](case/COMP-UNKNOWN-01-002.md) | 不应静默忽略未知字段导致用户误以为配置生效 | [负向] 运行不应在未知字段被静默忽略的情况下成功完成: ✅ COVERED — negative assertion in YAML as |
| 45 | [COMP-VARREF-01-083](case/COMP-VARREF-01-083.md) | YAML 表达式与 Shell 环境变量引用方式验证 | [正向] 表达式引用与环境变量引用结果相同: ✅ COVERED — steps have real logic; [正向] atomgit |
| 46 | [COMPAT-ACTION-01-001](case/COMPAT-ACTION-01-001.md) | checkout 短名等价性——ref 参数支持 | [正向] checkout 步骤成功完成，无报错: ✅ COVERED — steps have real logic; [正向] 检出后的 |
| 47 | [COMPAT-ACTION-01-002](case/COMPAT-ACTION-01-002.md) | checkout 短名等价性——path 参数支持 | [正向] checkout 步骤成功完成，无报错: ✅ COVERED — steps have real logic; [正向] 指定子目 |
| 48 | [COMPAT-ACTIONDEV-01-001](case/COMPAT-ACTIONDEV-01-001.md) | action.yml 元数据校验与 GitHub 差异 | 不支持的 action.yml 字段不导致 workflow 失败: 覆盖 — LLM/nonfunctional assertion: 不 |
| 49 | [COMPAT-ARTIFACT-01-001](case/COMPAT-ARTIFACT-01-001.md) | upload/download-artifact 跨 job 传递等价性 | [正向] upload-artifact 步骤成功，无报错: ✅ COVERED — steps have real logic; [正向] |
| 50 | [COMPAT-ARTIFACT-01-002](case/COMPAT-ARTIFACT-01-002.md) | upload-artifact 保留期行为等价性 | [正向] 保留期内可正常下载 artifact: ✅ COVERED — steps have real logic; [正向] 超过保留期 |
| 51 | [COMPAT-CACHE-01-001](case/COMPAT-CACHE-01-001.md) | cache 行为等价性——缓存命中场景 | [正向] 第二次运行日志中出现缓存命中标识: ✅ COVERED — steps have real logic; [正向] 缓存目录内容正 |
| 52 | [COMPAT-CACHE-01-002](case/COMPAT-CACHE-01-002.md) | cache 行为等价性——fork PR 写隔离 | [负向] fork PR 不应成功覆盖主干缓存: ✅ COVERED — negative assertion in YAML assert |
| 53 | [COMPAT-COMM-01-001](case/COMPAT-COMM-01-001.md) | issue_comment types 命名差异 - GitCode 合法 type | [正向] GitCode 风格 types 命名被接受: ✅ COVERED — 步骤使用 `${{ atomgit.event_name  |
| 54 | [COMPAT-CONCUR-01-001](case/COMPAT-CONCUR-01-001.md) | concurrency cancel-in-progress false 时应排队而 | 第二次触发不应被标记为失败或取消: 覆盖 — LLM/nonfunctional assertion: 第二次触发不应被标记为失败; 第二次 |
| 55 | [COMPAT-CONCUR-01-002](case/COMPAT-CONCUR-01-002.md) | concurrency 配置越界或不支持时应给出清晰报错 | 不通过无指引的原始报错（如仅报 generic YAML error）: 覆盖 — LLM/nonfunctional assertion: |
| 56 | [COMPAT-CONCUR-01-003](case/COMPAT-CONCUR-01-003.md) | concurrency preemption enable 行为差异 | 系统接受或拒绝 preemption 配置时应给出明确提示: 覆盖 — LLM/nonfunctional assertion: 系统接受或 |
| 57 | [COMPAT-CONCUR-01-004](case/COMPAT-CONCUR-01-004.md) | concurrency preemption events 越界时行为差异 | 系统对越界值给出明确报错: 覆盖 — LLM/nonfunctional assertion: 系统对 events 越界值给出明确报错;  |
| 58 | [COMPAT-CONTAINER-01-001](case/COMPAT-CONTAINER-01-001.md) | container 字段不被支持时应明确报错而非静默忽略 | 不通过无指引的原始报错（如仅报 generic YAML error）: 覆盖 — LLM/nonfunctional assertion: |
| 59 | [COMPAT-CONTAINER-01-002](case/COMPAT-CONTAINER-01-002.md) | container 自定义镜像被拒绝时应给出替代指引 | 报错信息说明 container 自定义镜像限制: 覆盖 — LLM/nonfunctional assertion: 报错给出替代方案，如 |
| 60 | [COMPAT-CTX-01-001](case/COMPAT-CTX-01-001.md) | 使用 github.ref 上下文应报错或求值为空 | [负向] 使用 github.ref 不应被静默映射为 atomgit.ref: ✅ COVERED — negative assertio |
| 61 | [COMPAT-CTX-01-002](case/COMPAT-CTX-01-002.md) | 使用 atomgit.ref 上下文应正确返回触发引用 | [正向] 日志中 atomgit_ref 的值不为空且符合预期格式: ✅ COVERED — steps have real logic |
| 62 | [COMPAT-CTX-01-003](case/COMPAT-CTX-01-003.md) | github 上下文嵌套属性访问应报错而非返回空 | [正向] 嵌套属性访问不导致 workflow 崩溃: ✅ COVERED — steps have real logic; [正向] 返回 |
| 63 | [COMPAT-DEPR-01-001](case/COMPAT-DEPR-01-001.md) | ::set-env:: 废弃命令应被拒绝或给出迁移指引 | 不通过命令被静默忽略且 workflow 成功（用户误以为生效）: 覆盖 — LLM/nonfunctional assertion: 不应 |
| 64 | [COMPAT-DEPR-01-002](case/COMPAT-DEPR-01-002.md) | ::add-path:: 废弃命令应被拒绝或给出迁移指引 | 不通过命令被静默忽略且 workflow 成功（用户误以为生效）: 覆盖 — LLM/nonfunctional assertion: 不应 |
| 65 | [COMPAT-DIR-01-002](case/COMPAT-DIR-01-002.md) | 工作流目录差异——.github/workflows/ 不应被识别 | .github/workflows/ 下的工作流不应被触发执行: 覆盖 — LLM/nonfunctional assertion: .gi |
| 66 | [COMPAT-DIR-01-003](case/COMPAT-DIR-01-003.md) | .github/workflows 目录不应被识别且应给出迁移提示 | .github/workflows 下的 workflow 不应被触发: 覆盖 — LLM/nonfunctional assertion: |
| 67 | [COMPAT-ENV-01-001](case/COMPAT-ENV-01-001.md) | ATOMGIT_SHA 环境变量应正确返回触发提交 SHA | [正向] 日志中 ATOMGIT_SHA 的值不为空且为有效 SHA 格式: ✅ COVERED — steps have real log |
| 68 | [COMPAT-ENV-01-002](case/COMPAT-ENV-01-002.md) | GITHUB_SHA 环境变量在 GitCode 中应为空或未定义 | [负向] GITHUB_SHA 不应被静默映射为 ATOMGIT_SHA: ✅ COVERED — negative assertion i |
| 69 | [COMPAT-ENV-01-003](case/COMPAT-ENV-01-003.md) | GITHUB_ENV 环境变量不应被静默映射到 ATOMGIT_ENV | [负向] GITHUB_ENV 不等于 ATOMGIT_ENV: ✅ COVERED — negative assertion in YAM |
| 70 | [COMPAT-ENVIRON-01-002](case/COMPAT-ENVIRON-01-002.md) | environment 字段绑定 secrets 的行为差异 | 不通过 environment 字段被静默忽略: 覆盖 — LLM/nonfunctional assertion: environment |
| 71 | [COMPAT-EXPR-01-001](case/COMPAT-EXPR-01-001.md) | success 关键字在条件表达式中的可用性 | [正向] 表达式被正确解析，日志中输出预期值: ✅ COVERED — steps have real logic; [负向] 若平台拒绝该 |
| 72 | [COMPAT-EXPR-01-008](case/COMPAT-EXPR-01-008.md) | toJson 表达式输出格式差异（pretty-print vs compact） | toJson 输出合法 JSON: 覆盖 — real command in step 'Output object via toJson' |
| 73 | [COMPAT-EXPR-01-009](case/COMPAT-EXPR-01-009.md) | loose equality 跨类型强制求值差异 | 表达式求值不报错: 覆盖 — real command in step 'Compare string one and number one |
| 74 | [COMPAT-EXPR-01-010](case/COMPAT-EXPR-01-010.md) | loose equality null 与空字符串及零的等价性差异 | 表达式求值不报错: 覆盖 — real command in step 'Compare null and empty string' co |
| 75 | [COMPAT-EXPR-01-013](case/COMPAT-EXPR-01-013.md) | success() 带括号与不带括号的兼容性差异 | 若支持无括号形式，应正常求值: 覆盖 — LLM/nonfunctional assertion: 若支持无括号形式，应正常求值并执行; 若 |
| 76 | [COMPAT-EXPR-01-014](case/COMPAT-EXPR-01-014.md) | always() 带括号与不带括号的兼容性差异 | 若支持无括号形式，应正常求值: 覆盖 — LLM/nonfunctional assertion: 若支持无括号形式，应正常求值并执行; 若 |
| 77 | [COMPAT-IF-01-001](case/COMPAT-IF-01-001.md) | step 失败后后续 step 默认跳过行为 | [正向] 第二个 step 未执行，日志中无其输出: ✅ COVERED — steps have real logic; [正向] job |
| 78 | [COMPAT-IF-01-002](case/COMPAT-IF-01-002.md) | continue-on-error 标记后失败 step 不阻断后续执行 | [正向] 第二个 step 成功执行并输出消息: ✅ COVERED — steps have real logic; [正向] 第一个 s |
| 79 | [COMPAT-INPUTS-01-002](case/COMPAT-INPUTS-01-002.md) | workflow_dispatch inputs 类型限制 - string 正常通 | [正向] workflow 校验通过: ✅ COVERED — steps have real logic; [正向] string 类型  |
| 80 | [COMPAT-ISOLATE-01-001](case/COMPAT-ISOLATE-01-001.md) | Runner 环境隔离——跨 job 文件隔离 | [负向] job B 中不存在 job A 的 workspace 标记文件: ✅ COVERED — negative assertion |
| 81 | [COMPAT-ISOLATE-01-002](case/COMPAT-ISOLATE-01-002.md) | Runner 环境隔离——跨 job 环境变量隔离 | [负向] job B 中不应读取到 job A 通过 ATOMGIT_ENV 设置的值: ✅ COVERED — negative asse |
| 82 | [COMPAT-MASK-01-001](case/COMPAT-MASK-01-001.md) | 直接 echo secrets 值应在日志中被脱敏 | [负向] 日志中不含 TEST_SECRET 的原始明文值: ✅ COVERED — negative assertion in YAML  |
| 83 | [COMPAT-MASK-01-002](case/COMPAT-MASK-01-002.md) | 通过 env 注入 secret 后输出应在日志中被脱敏 | [负向] 日志中不含 TEST_SECRET 的原始明文值: ✅ COVERED — negative assertion in YAML  |
| 84 | [COMPAT-MATRIX-01-003](case/COMPAT-MATRIX-01-003.md) | matrix 三维展开不被支持时的差异 | [正向] 系统对三维 matrix 给出明确响应（接受或拒绝）: ✅ COVERED — steps have real logic; [负 |
| 85 | [COMPAT-MATRIX-01-004](case/COMPAT-MATRIX-01-004.md) | matrix include 无基础变量不被支持时的差异 | [正向] 系统接受或拒绝 include 配置时给出明确提示: ✅ COVERED — steps have real logic; [负向 |
| 86 | [COMPAT-MATRIX-01-005](case/COMPAT-MATRIX-01-005.md) | matrix exclude 全排除不被支持时的差异 | 系统对空矩阵给出明确报错: 覆盖 — LLM/nonfunctional assertion: 系统对空矩阵给出明确报错（如 matrix  |
| 87 | [COMPAT-MIGRATE-01-001](case/COMPAT-MIGRATE-01-001.md) | GitHub 风格 permissions 块迁移报错应给出可操作指引 | [负向] 不通过无指引的原始报错（如仅报 YAML 解析错误）: COVERED — negative assertion present; |
| 88 | [COMPAT-MIGRATE-01-002](case/COMPAT-MIGRATE-01-002.md) | GitHub 风格 run-name 语法迁移报错应给出可操作指引 | [负向] 不通过无指引的原始报错: COVERED — negative assertion present; [正向] 报错信息包含 `r |
| 89 | [COMPAT-OUTCOME-01-001](case/COMPAT-OUTCOME-01-001.md) | continue-on-error false 时 outcome 与 conclu | [正向] 失败 step 的 outcome 为 failure: COVERED — 2 real steps, assertions p |
| 90 | [COMPAT-OUTCOME-01-002](case/COMPAT-OUTCOME-01-002.md) | continue-on-error true 时 outcome 应为 failur | [正向] 失败 step 的 outcome 为 failure: COVERED — 2 real steps, assertions p |
| 91 | [COMPAT-OUTCOME-01-003](case/COMPAT-OUTCOME-01-003.md) | outcome 与 conclusion 在 job 条件判断中不应互换语义 | [正向] job A 的 outcome 保持为 failure: COVERED — 1 real steps, assertions p |
| 92 | [COMPAT-OUTPUT-01-001](case/COMPAT-OUTPUT-01-001.md) | 跨 Job 引用未声明 output 时返回空值的差异 | [正向] 跨 Job 引用未声明 output 时不导致 workflow 崩溃: COVERED — 2 real steps, asse |
| 93 | [COMPAT-PERM-01-003](case/COMPAT-PERM-01-003.md) | permissions 命名差异——GitHub contents 权限项应报错 | [负向] 使用 `contents` 时 workflow 解析/校验阶段应报错: COVERED — negative assertion |
| 94 | [COMPAT-PERM-01-004](case/COMPAT-PERM-01-004.md) | permissions 命名差异——GitCode repository 权限项正常 | [正向] workflow 解析阶段无报错: COVERED — 2 real steps, assertions present; [正向 |
| 95 | [COMPAT-PERM-01-005](case/COMPAT-PERM-01-005.md) | permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异 | [正向] 读操作成功: COVERED — 2 real steps, assertions present; [负向] 写操作被平台拒绝: |
| 96 | [COMPAT-PR-01-001](case/COMPAT-PR-01-001.md) | pull_request types 命名差异 - GitCode 合法 types | [正向] workflow 校验通过: COVERED — 1 real steps, assertions present; [正向] 指 |
| 97 | [COMPAT-PR-01-003](case/COMPAT-PR-01-003.md) | PR types 配置后匹配类型不触发与 GitHub 行为差异 | [负向] 不通过假阴性（PR 更新后没有对应 workflow 运行）: COVERED — negative assertion pres |
| 98 | [COMPAT-PR-01-004](case/COMPAT-PR-01-004.md) | PR types 含 merge 时不触发与 GitHub 行为差异 | [负向] 不通过仅产生 PUSH 运行而无 pull_request 运行: COVERED — negative assertion pr |
| 99 | [COMPAT-PR-01-005](case/COMPAT-PR-01-005.md) | PR paths 过滤不工作时的兼容性差异 | [负向] 不通过 PR 修改匹配路径后无 workflow 触发: COVERED — negative assertion present |
| 100 | [COMPAT-PR-01-006](case/COMPAT-PR-01-006.md) | PR 目标分支过滤行为差异 | [正向] 目标分支为 main 的 PR 应触发 workflow: COVERED — 1 real steps, assertions  |
| 101 | [COMPAT-SCHEDULE-01-001](case/COMPAT-SCHEDULE-01-001.md) | schedule cron 按 UTC 时间触发 | [正向] schedule 事件能正常触发 workflow: COVERED — 1 real steps, assertions pre |
| 102 | [COMPAT-SCHEDULE-01-003](case/COMPAT-SCHEDULE-01-003.md) | schedule 在非默认分支不触发与 GitHub 差异 | [负向] develop 分支的 schedule workflow 不应触发: COVERED — negative assertion  |
| 103 | [COMPAT-SECRET-01-005](case/COMPAT-SECRET-01-005.md) | 环境级 secrets 不支持时应明确报错而非降级为项目级 | [负向] 不通过静默降级（ENV_SECRET 不应返回 PROJECT_SECRET 的值）: COVERED — negative as |
| 104 | [COMPAT-SHELL-01-001](case/COMPAT-SHELL-01-001.md) | 默认 shell 隐式行为差异 - 未显式声明时是否为 bash | [正向] 日志包含 bash 字样: COVERED — 2 real steps, assertions present; [正向] 命令 |
| 105 | [COMPAT-SHELL-01-002](case/COMPAT-SHELL-01-002.md) | 默认工作目录隐式行为差异 - 未显式声明时是否为仓库根目录 | [正向] 当前工作目录路径与仓库根目录一致: COVERED — 1 real steps, assertions present; [正向 |
| 106 | [COMPAT-TARGET-01-001](case/COMPAT-TARGET-01-001.md) | pull_request_target 默认 checkout 应为 base 分支 | [负向] 日志中显示的 SHA 不应等于 fork PR head SHA: COVERED — negative assertion pr |
| 107 | [COMPAT-TARGET-01-002](case/COMPAT-TARGET-01-002.md) | pull_request_target 在 fork 场景下应保持 secret 隔 | [负向] 日志中不应出现 DEPLOY_TOKEN 明文: COVERED — negative assertion present; [正 |
| 108 | [COMPAT-TARGET-01-003](case/COMPAT-TARGET-01-003.md) | pull_request_target 默认 types 与 GitHub 差异 | [正向] 默认 types 下 PR open 应触发 workflow: COVERED — 1 real steps, assertio |
| 109 | [COMPAT-TOKEN-01-001](case/COMPAT-TOKEN-01-001.md) | ATOMGIT_TOKEN 应正确返回有效令牌 | [正向] API 调用返回 200，表明 TOKEN 有效: COVERED — 1 real steps, assertions pres |
| 110 | [COMPAT-TOKEN-01-003](case/COMPAT-TOKEN-01-003.md) | GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN | [负向] GITHUB_TOKEN 不等于 ATOMGIT_TOKEN: COVERED — negative assertion pres |
| 111 | [COMPAT-VARS-01-001](case/COMPAT-VARS-01-001.md) | vars 上下文若支持应正确返回值 | [正向] vars.TEST_VAR 返回配置值: COVERED — 1 real steps, assertions present |
| 112 | [COMPAT-VARS-01-003](case/COMPAT-VARS-01-003.md) | vars 项目级覆盖组织级的优先级差异 | [正向] 若支持 vars，项目级值覆盖组织级值: COVERED — 1 real steps, assertions present;  |
| 113 | [COMPAT-VARS-01-004](case/COMPAT-VARS-01-004.md) | vars 与 env 同名时的优先级差异 | [正向] 若支持 vars，env 优先级高于 vars: COVERED — 1 real steps, assertions prese |
| 114 | [COMPAT-VARS-01-005](case/COMPAT-VARS-01-005.md) | vars 在条件表达式 if 中的可用性差异 | [正向] 若支持 vars，if 条件正确求值并控制步骤执行: COVERED — 1 real steps, assertions pre |
| 115 | [COMPAT-VARS-01-006](case/COMPAT-VARS-01-006.md) | vars 在 Action 中的可用性差异 | [正向] 若支持 vars，Action 的 with 参数正确接收值: COVERED — 1 real steps, assertion |
| 116 | [REL-ART-01-041](case/REL-ART-01-041.md) | 超大 artifact——100 MB artifact 上传后下游 job 应成功 | [正向] upload 成功: COVERED — 2 real steps, assertions present; [正向] downl |
| 117 | [REL-ARTCONC-01-063](case/REL-ARTCONC-01-063.md) | 制品并发写一致性——多 job 同时 upload-artifact 同名 arti | [正向] 下载内容确定: COVERED — 2 real steps, assertions present; [负向] 不应出现 ABA |
| 118 | [REL-ARTPERF-01-053-V2](case/REL-ARTPERF-01-053-V2.md) | 制品传输性能——1GB artifact 上传下载耗时 | [正向] 上传≤300s: COVERED — 2 real steps, assertions present; [正向] 下载≤300s |
| 119 | [REL-ARTPERF-01-053](case/REL-ARTPERF-01-053.md) | 制品传输性能——100MB artifact 上传下载耗时 | [正向] 上传≤30s: COVERED — 2 real steps, assertions present; [正向] 下载≤30s:  |
| 120 | [REL-CANCEL-01-028](case/REL-CANCEL-01-028.md) | 手动取消 workflow——运行中取消时 always() cleanup ste | [正向] 非 always step 被终止: COVERED — 1 real steps, assertions present; [正 |
| 121 | [REL-FAULT-01-035](case/REL-FAULT-01-035.md) | 故障注入——artifact 下载服务 503 不可用时 job 应失败并报依赖服务 | [正向] download-artifact step 状态=failure: COVERED — 1 real steps, assert |
| 122 | [REL-LOGPERF-01-051-V2](case/REL-LOGPERF-01-051-V2.md) | 日志加载性能——200MB 日志下载与查看耗时 | [正向] 下载≤120s: COVERED — 1 real steps, assertions present; [正向] 大小/行数 1 |
| 123 | [REL-MATRIX-01-039](case/REL-MATRIX-01-039.md) | 大规模 matrix——50 个组合应全部生成并正确调度 | [正向] 50 个 jobs 全部生成: COVERED — 1 real steps, assertions present; [正向]  |
| 124 | [REL-RETAIN-01-047](case/REL-RETAIN-01-047.md) | artifact 保留期 90 天边界——第 91 天应不可下载 | 第 90 天可下载: 覆盖 — real step logic exists; 第 91 天不可下载: 覆盖 — real step log |
| 125 | [REL-STATE-01-058](case/REL-STATE-01-058.md) | Runner 状态机正确性——空闲/运行/离线转换与时序一致性 | 状态序列正确: 覆盖 — real step logic exists; idle→running≤30s: 覆盖 — 非功能断言存在(LL |
| 126 | [REL-TIMEOUT-01-009](case/REL-TIMEOUT-01-009.md) | 自定义短超时——timeout-minutes=1 时 step 运行 2 分钟应被 | job 状态=failure: 覆盖 — potential failure paths exist; 实际运行时长 60±10 秒: 覆盖 |
| 127 | [SEC-ARTF-01-001](case/SEC-ARTF-01-001.md) | fork PR 上传的 artifact 必须不可被主仓 workflow 下载或执 | [负向] 主仓 workflow 绝不应能下载到 fork PR 上传的 artifact: ✅ COVERED — 步骤真实以 fork  |
| 128 | [SEC-ARTF-01-002](case/SEC-ARTF-01-002.md) | 跨仓库 artifact 下载返回 403 或 404 | 跨仓库 artifact 下载绝不应成功: 覆盖 — log assertion without specific string check |
| 129 | [SEC-BASE-01-001](case/SEC-BASE-01-001.md) | pull_request_target 使用 base 分支的 workflow 版 | base 分支 workflow 按其定义执行，可访问 secret 与写 token: 覆盖 — log assertion withou |
| 130 | [SEC-BASE-01-002](case/SEC-BASE-01-002.md) | fork PR 改 workflow 不被 pull_request_target  | pull_request_target 绝不应执行来自不可信 fork 的 workflow 定义: 覆盖 — log assertion  |
| 131 | [SEC-CACHE-01-002](case/SEC-CACHE-01-002.md) | 主仓 cache restore 对 fork cache miss | 主仓绝不应命中 fork PR 的缓存: 覆盖 — real logic exists for negative verification; |
| 132 | [SEC-DEFPERM-01-002](case/SEC-DEFPERM-01-002.md) | job 级覆盖后权限正确收窄 | job 级收窄后不应仍保留顶层的更大权限: 覆盖 — log assertion without specific string check |
| 133 | [SEC-ENV-01-001](case/SEC-ENV-01-001.md) | 环境级 secret 必须经审批后才能被 workflow 访问 | [positive] run_status equals: success_after_approval: COVERED — 步骤含实际命 |
| 134 | [SEC-ENV-01-002](case/SEC-ENV-01-002.md) | 环境级 secret 审批前 workflow 不可读取 | [negative] run_logs must_not_contain: secret accessible unexpectedly:  |
| 135 | [SEC-FORK-01-001](case/SEC-FORK-01-001.md) | fork PR 触发 pull_request 时不可读取项目 secrets | [负向] 日志不含 DEPLOY_TOKEN 明文: ✅ COVERED — 步骤1 使用 `${{ secrets.DEPLOY_TOKE |
| 136 | [SEC-FORK-01-002](case/SEC-FORK-01-002.md) | fork PR 中 secrets 引用返回空值且 job 不崩溃 | [负向] 环境变量 API_KEY 为空或未定义: ✅ COVERED — 步骤通过 `if [ -z "$API_KEY" ]` 真实检测 |
| 137 | [SEC-MASK-01-002](case/SEC-MASK-01-002.md) | Secret 值在 step summary 和错误堆栈中必须被脱敏 | [negative] step_summary must_not_contain_secret: API_KEY: COVERED — ta |
| 138 | [SEC-NAME-01-001](case/SEC-NAME-01-001.md) | Secret/变量名含特殊字符时不可导致意外求值或权限绕过 | [negative] run_logs must_not_contain_secret: MY-VAR: COVERED — 步骤使用了 M |
| 139 | [SEC-PRTGT-01-001](case/SEC-PRTGT-01-001.md) | pull_request_target 下显式 checkout 不可信 PR 时  | [负向] 运行日志中不应出现 DEPLOY_TOKEN 明文: ✅ COVERED — 步骤1 使用 `uses: checkout` +  |
| 140 | [SEC-PRTGT-01-002](case/SEC-PRTGT-01-002.md) | pull_request_target 无审批不执行 fork PR 代码 | [负向] 未审批时不应让 job 直接执行 fork PR 代码: ✅ COVERED — 断言 target=run_status mus |
| 141 | [SEC-SIDE-01-001](case/SEC-SIDE-01-001.md) | Secret 不经 output 侧信道绕过脱敏外泄 | [negative] run_logs must_not_contain_secret: API_KEY: COVERED — 步骤使用了  |
| 142 | [SEC-SIDE-01-002](case/SEC-SIDE-01-002.md) | Secret 不经 artifact 侧信道绕过脱敏外泄 | [negative] artifact_content must_not_contain_secret: DEPLOY_TOKEN: COV |
| 143 | [SEC-SUPPLY-01-001](case/SEC-SUPPLY-01-001.md) | 第三方 Action 引用应支持完整 commit hash 固定 | [positive] run_status equals: success_or_action_executed: COVERED — 步骤 |
| 144 | [SEC-SUPPLY-01-002](case/SEC-SUPPLY-01-002.md) | commit hash 不匹配时第三方 Action 应被拒绝执行 | [negative] run_status must_not_equal: success: COVERED — 步骤含实际命令/actio |
| 145 | [SEC-SUPPLY-01-003](case/SEC-SUPPLY-01-003.md) | 第三方 Action 来源应具备信任边界（typosquatting 限制） | [negative] run_status must_not_equal: success: COVERED — 步骤含实际命令/actio |
| 146 | [SEC-TOCTOU-01-002](case/SEC-TOCTOU-01-002.md) | 评论触发不应绕过代码固定与 PR 审批 | [负向] 新 commit 绝不应被该次特权运行自动执行: ✅ COVERED — 断言 target=run_logs must_not_ |
| 147 | [SEC-TOKEN-01-001](case/SEC-TOKEN-01-001.md) | fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须 | [正向] ATOMGIT_TOKEN 可成功执行 clone 等读操作: ✅ COVERED — 断言 target=run_logs eq |
| 148 | [SEC-TOKEN-01-002](case/SEC-TOKEN-01-002.md) | fork PR 中 ATOMGIT_TOKEN 写操作被平台拒绝 | [负向] 写操作绝不应成功: ✅ COVERED — 断言 target=run_logs equals "push_denied_or_4 |
| 149 | [SEC-WCMD-01-002](case/SEC-WCMD-01-002.md) | 跨运行 artifact 必须被视为不可信数据 | [negative] run_logs must_not_contain: auto_executed: COVERED — 期望值可能来自 |
| 150 | [USE-ACT-01-001](case/USE-ACT-01-001.md) | 使用裸插件名 checkout 时正常拉取官方 Action | [positive] run_status equals: COMPLETED: COVERED — 步骤含实际命令或 action，运行状 |
| 151 | [USE-ANNOT-01-001](case/USE-ANNOT-01-001.md) | workflow 命令 ::error:: 与 ::warning:: 在日志中保留 | 日志中包含 ::error:: 原始文本: 覆盖 — produced by step 'emit error and warning':  |
| 152 | [USE-CONC-01-001](case/USE-CONC-01-001.md) | concurrency.max 配置 0 或 10 时报错应提示有效范围 1-5 | 不应静默截断为边界值: 覆盖 — negative status assertion; 报错中是否包含 1、5、范围等关键词: 覆盖 — 非 |
| 153 | [USE-CONC-01-002](case/USE-CONC-01-002.md) | concurrency.max 配置 -1 时报错应提示有效范围 | 不应静默截断: 覆盖 — negative status assertion; 报错中是否包含有效范围说明: 覆盖 — 非功能断言存在(LL |
| 154 | [USE-CTX-01-002](case/USE-CTX-01-002.md) | 使用 github 上下文时报错应提示 atomgit 替代 | 不应静默求值为空字符串: 覆盖 — negative status assertion; 报错信息中应同时出现 github 与 atomg |
| 155 | [USE-DISP-01-001](case/USE-DISP-01-001.md) | workflow_dispatch 必填参数未提供时应给出明确校验错误 | 不应在缺少必填参数时触发运行: 覆盖 — negative status assertion; 报错中是否指出具体缺少的字段名: 覆盖 —  |
| 156 | [USE-ENV-01-001](case/USE-ENV-01-001.md) | 使用 ATOMGIT_SHA 环境变量时正常取值 | [positive] run_logs contains: sha=: COVERED — 步骤 [echo ATOMGIT_SHA] 执行 |
| 157 | [USE-INPT-01-001](case/USE-INPT-01-001.md) | 使用 string 类型 input 时正常通过校验 | 运行可手动触发: 覆盖 — status assertion: COMPLETED; 输入参数正常传递: 覆盖 — status asser |
| 158 | [USE-INPT-01-002](case/USE-INPT-01-002.md) | 使用 boolean 类型 input 时报错应提示仅支持 string | 不应静默降级为 string: 覆盖 — negative status assertion; 报错中应包含 string 与类型转换相关提 |
| 159 | [USE-LBL-01-001](case/USE-LBL-01-001.md) | runs-on 标签完全不匹配时应给出明确失败原因与可用标签列表 | 不应无限 queued 且无提示: 覆盖 — negative status assertion; 错误信息中是否包含用户指定的标签文本:  |
| 160 | [USE-LBL-01-002](case/USE-LBL-01-002.md) | runs-on 标签因容量不足排队时应提示排队状态而非无可用 runner | 状态或日志中是否出现排队/等待字样: 覆盖 — 非功能断言存在(LLM评估); 错误信息是否区分无匹配与容量不足: 覆盖 — 非功能断言存在 |
| 161 | [USE-NEST-01-001](case/USE-NEST-01-001.md) | workflow_call 嵌套 3 层时报错应明确提示上限为 2 层 | 不应静默失败或卡死: 覆盖 — negative status assertion; 报错中是否包含 workflow_call、嵌套、2  |
| 162 | [USE-PERM-01-001](case/USE-PERM-01-001.md) | 使用 GitCode 权限域命名时正常生效 | [positive] run_status equals: COMPLETED: COVERED — 步骤含实际命令或 action，运行状 |
| 163 | [USE-RUN-01-001](case/USE-RUN-01-001.md) | 使用三段式标签时 job 正常调度 | 运行成功完成: 覆盖 — status assertion: COMPLETED; job 日志显示在对应 runner 上执行: 覆盖 — |
| 164 | [USE-RUN-01-002](case/USE-RUN-01-002.md) | 使用单标签 ubuntu-latest 时报错应给出三段式格式指引 | 不应无限 queued 且无提示: 覆盖 — negative status assertion; 报错中应包含三段式或 default 等 |
| 165 | [USE-SEARCH-01-001](case/USE-SEARCH-01-001.md) | 日志搜索与下载功能可用且交互流畅 | 搜索后匹配行被高亮: 覆盖 — produced by step 'generate log content': executes real |
| 166 | [USE-SECNAME-01-001](case/USE-SECNAME-01-001.md) | Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误 | 不应仅报 Secret not found: 覆盖 — negative status assertion; 报错中是否包含 Secret  |
| 167 | [USE-SECNAME-01-002](case/USE-SECNAME-01-002.md) | Secret 名称以数字开头时应给出命名规则错误 | 不应仅报 Secret not found: 覆盖 — negative status assertion; 报错中是否包含命名格式说明:  |
| 168 | [USE-STAT-01-001](case/USE-STAT-01-001.md) | 使用 always() 带括号时若被接受则正常执行 | step 日志出现执行记录: 覆盖 — produced by step 'cleanup with always': uses ${{ } |
| 169 | [USE-STAT-01-002](case/USE-STAT-01-002.md) | 使用 success() 带括号时报错应提示 GitCode 括号差异 | 不应静默通过校验: 覆盖 — negative status assertion; 报错中应包含括号差异提示: 覆盖 — 非功能断言存在(L |
| 170 | [USE-TYPE-01-001](case/USE-TYPE-01-001.md) | 使用 GitCode types 命名时正常触发 | [正向] PR 创建或更新时触发运行: ✅ COVERED — 断言 target=run_status equals COMPLETED， |

## 部分不符 — 验证点与步骤产出部分不一致（171 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-ATOMGIT-01-047](case/COMP-ATOMGIT-01-047.md) | atomgit 核心上下文属性可访问性 | [正向] 各核心属性输出不为空: ✅ COVERED — 步骤1 echo 15个属性，断言 SHA=/REF=/REPO= 均有值; [正向] at |
| 2 | [COMP-ATOMGIT-01-048](case/COMP-ATOMGIT-01-048.md) | atomgit 事件相关属性可访问性 | [正向] event.ref 与 atomgit.ref 一致: ✅ COVERED — 断言 EVENT_REF=refs/，与 atomgit.r |
| 3 | [COMP-ATOMGIT-01-049](case/COMP-ATOMGIT-01-049.md) | atomgit 边界格式校验 | [正向] sha 长度等于 40: ✅ COVERED — 断言 must_contain: SHA_LEN=40; [正向] ref 以 refs/ |
| 4 | [COMP-BOUND-01-084](case/COMP-BOUND-01-084.md) | 路径与分支过滤组合及否定模式边界验证 | [正向] branches + paths 组合过滤生效: ✅ — push 到匹配分支+路径触发 workflow，断言 run_status=su |
| 5 | [COMP-BOUND-01-086](case/COMP-BOUND-01-086.md) | 矩阵构建 include exclude 与单值边界验证 | [正向] include 添加的组合在 step 中可访问: ✅ COVERED — 矩阵有 [1, 2, 3] 三值（含 include 的 ver |
| 6 | [COMP-BOUND-01-087](case/COMP-BOUND-01-087.md) | 步骤输出与跨 job 传递边界验证 | [正向] ATOMGIT_OUTPUT 写入后同 job 可读取: ✅ COVERED — 步骤2 通过 steps.writer.outputs.k |
| 7 | [COMP-BOUND-01-088](case/COMP-BOUND-01-088.md) | 工作流命令 set-env add-path 与文件写入边界验证 | [正向] ATOMGIT_ENV 写入后后续 step 可读取: ✅ COVERED — 断言 must_contain: MY_ENV=from_e |
| 8 | [COMP-CALL-01-001](case/COMP-CALL-01-001.md) | 2 层 workflow_call 嵌套正常执行 | [正向] 运行状态成功: ✅ COVERED — 断言 run_status=success，但成功仅证明 echo 步骤执行; [正向] 子 wor |
| 9 | [COMP-CTX-01-052](case/COMP-CTX-01-052.md) | 上下文在条件表达式 if 中注入验证 | [正向] atomgit.ref 条件正确匹配时步骤执行: ✅ COVERED — job 级 if 使用 ${{ atomgit.ref == 'r |
| 10 | [COMP-ENVCTX-01-050](case/COMP-ENVCTX-01-050.md) | env 优先级链 step 大于 job 大于 workflow | [正向] 最终输出值为 step 级定义的值: ✅ COVERED — step 级 env MY_VAR=step_value，断言 MY_VAR= |
| 11 | [COMP-EXPR-01-054](case/COMP-EXPR-01-054.md) | 字符串函数 contains startsWith endsWith 边界行 | [正向] contains 匹配子串返回真: ✅ COVERED — if: ${{ contains(atomgit.ref_name, 'main |
| 12 | [COMP-EXPR-01-055](case/COMP-EXPR-01-055.md) | hashFiles 函数边界行为 | [正向] 单文件 hashFiles 输出 64 位 hex: ❌ TRIVIAL — 步骤 echo HASH_SINGLE= 但断言仅检查 = 存 |
| 13 | [COMP-EXPR-01-056](case/COMP-EXPR-01-056.md) | toJson 函数边界行为 | [正向] toJson(atomgit.event) 输出以 { 开头: ✅ COVERED — 断言 must_contain: EVENT_JSO |
| 14 | [COMP-EXPR-01-058](case/COMP-EXPR-01-058.md) | 表达式运算符与优先级边界行为 | [正向] == 和 != 运算正确: ✅ COVERED — 步骤1 == 运算，步骤2 != 运算，断言 eq_passed, ne_passed; |
| 15 | [COMP-ISOLATION-01-001](case/COMP-ISOLATION-01-001.md) | 同一 workflow 先后 job 的文件系统相互隔离 | [负向] job 2 不应访问到 job 1 的文件: ✅ COVERED — negative assertion: must_not_contai |
| 16 | [COMP-JOB-01-066](case/COMP-JOB-01-066.md) | job 必填字段 name runs-on steps 验证 | [正向] 完整 job 定义通过校验并执行: ✅ COVERED — job 含 name+runs-on+steps，run_status=succ |
| 17 | [COMP-PRTARGET-01-001](case/COMP-PRTARGET-01-001.md) | pull_request_target 默认使用 base 分支 workf | [正向] 执行的 step 内容与 base 分支 workflow 一致: ⚠️ TRIVIAL — 步骤仅 `echo "BASE_VERSION |
| 18 | [COMP-PRTARGET-01-002](case/COMP-PRTARGET-01-002.md) | 显式 checkout head.sha 后执行不可信代码的风险可控 | [正向] checkout head.sha 成功: ✅ COVERED — 步骤使用 `uses: checkout` action 配合 `ref |
| 19 | [COMP-PUSH-01-001](case/COMP-PUSH-01-001.md) | 匹配 branches 的 push 正确触发 workflow | [正向] 运行记录存在且 event 为 push: ⚠️ PARTIAL — steps exist but all trivial (echo o |
| 20 | [COMP-PUSH-01-003](case/COMP-PUSH-01-003.md) | paths 过滤匹配前 300 个变更文件行为符合预期 | 运行列表中不存在该 push 触发的运行: 空洞 — no real logic, negative assertion may be vacuous |
| 21 | [COMP-RERUN-01-002](case/COMP-RERUN-01-002.md) | 第 4 次 rerun 应被系统拒绝 | [负向] 第 4 次 rerun 不应创建新运行: ✅ COVERED — negative assertion in YAML assertions |
| 22 | [COMP-RERUN-01-003](case/COMP-RERUN-01-003.md) | 超过 6 小时的运行不可 rerun | 超 6h 的运行的 rerun 不应成功: 空洞 — no real logic, negative assertion may be vacuous |
| 23 | [COMP-STAGES-01-003](case/COMP-STAGES-01-003.md) | post.run_always true 时 workflow 失败仍执行  | post 阶段步骤日志存在: 覆盖 — deliberate failure step exists; post 阶段步骤输出出现在运行详情页: 覆盖 |
| 24 | [COMP-STATUS-01-001](case/COMP-STATUS-01-001.md) | 运行状态机 queued 到 completed 转换正确 | [正向] 状态转换序列符合预期: ⚠️ PARTIAL — steps exist but all trivial (echo only); [正向] |
| 25 | [COMP-STEP-01-071](case/COMP-STEP-01-071.md) | step 执行控制 shell working-directory cont | [正向] shell bash 和 sh 均可执行: ⚠️ PARTIAL — steps exist but all trivial (echo o |
| 26 | [COMP-TIMEOUT-01-001](case/COMP-TIMEOUT-01-001.md) | 未声明 timeout-minutes 的 job 在 360 分钟内正常完 | [正向] 运行状态为 success: ⚠️ PARTIAL — steps exist but all trivial (echo only); [ |
| 27 | [COMP-TRIG-01-073](case/COMP-TRIG-01-073.md) | pull_request 事件关键字段与 types 验证 | [正向] PR 创建时触发 workflow: ✅ COVERED — 步骤通过 ${{ atomgit.event.pull_request.num |
| 28 | [COMP-TRIG-01-075](case/COMP-TRIG-01-075.md) | schedule 事件关键字段与 cron 格式验证 | [正向] 数组格式 schedule 通过校验: ✅ COVERED — workflow 的 on.schedule 使用了数组格式 [{cron: |
| 29 | [COMP-TRIG-01-078](case/COMP-TRIG-01-078.md) | 多事件组合与分支路径过滤验证 | [正向] 多事件组合通过校验: ⚠️ PARTIAL — steps exist but all trivial (echo only); [正向]  |
| 30 | [COMP-TRIG-01-079](case/COMP-TRIG-01-079.md) | 触发事件 types 取值与过滤边界验证 | [正向] 合法 types 通过校验: ⚠️ PARTIAL — steps exist but all trivial (echo only); [ |
| 31 | [COMP-UNKNOWN-01-001](case/COMP-UNKNOWN-01-001.md) | 包含未知顶层字段的 workflow 触发 YAML 校验失败 | [正向] workflow 提交后触发校验失败: ⚠️ PARTIAL — steps exist but all trivial (echo onl |
| 32 | [COMP-WFLOW-01-061](case/COMP-WFLOW-01-061.md) | workflow name 与 on 字段必填与类型验证 | [正向] 含 name 的 workflow 被正确显示: ⚠️ PARTIAL — steps exist but all trivial (ech |
| 33 | [COMP-WFLOW-01-062](case/COMP-WFLOW-01-062.md) | workflow env 与 defaults 字段验证 | [正向] workflow env 在 step 中可访问: ⚠️ PARTIAL — steps exist but all trivial (ec |
| 34 | [COMP-WFLOW-01-063](case/COMP-WFLOW-01-063.md) | workflow concurrency 并发控制字段验证 | [正向] 合法 concurrency 配置通过校验: ⚠️ PARTIAL — steps exist but all trivial (echo  |
| 35 | [COMP-WFLOW-01-064](case/COMP-WFLOW-01-064.md) | workflow stages 阶段结构字段验证 | [正向] stages map 格式通过校验: ❌ NOT_COVERED — no steps found; [正向] 单 stage 可缺省 st |
| 36 | [COMP-WFLOW-01-065](case/COMP-WFLOW-01-065.md) | workflow post 后处理阶段字段验证 | [正向] post 步骤在成功时执行: ⚠️ PARTIAL — steps exist but all trivial (echo only); [ |
| 37 | [COMPAT-DIR-01-001](case/COMPAT-DIR-01-001.md) | 工作流目录差异——.gitcode/workflows/ 正常识别 | .gitcode/workflows/*.yml 被正确识别: 覆盖 — status assertion: completed_success; 对 |
| 38 | [COMPAT-ENVIRON-01-001](case/COMPAT-ENVIRON-01-001.md) | 含 environment 字段的 job 应被报错或警告 | 不应被静默接受: 未覆盖 — 缺少负向断言; 报错信息应提示 environment 字段不支持及替代方案: 覆盖 — 非功能断言存在(LLM评估) |
| 39 | [COMPAT-EXPR-01-002](case/COMPAT-EXPR-01-002.md) | success() 函数的处理行为差异 | [正向] 若支持，表达式返回布尔结果: ✅ COVERED — steps have real logic; [负向] 若不支持，应有表达式解析错误或 |
| 40 | [COMPAT-EXPR-01-003](case/COMPAT-EXPR-01-003.md) | failure() 与 failed 关键字的处理行为差异 | [正向] 若支持，可在失败后获取到正确的状态值: ✅ COVERED — steps have real logic; [负向] 若不支持，应有表达式 |
| 41 | [COMPAT-EXPR-01-004](case/COMPAT-EXPR-01-004.md) | contains 表达式大小写敏感边界 | [正向] 大小写匹配时返回 true: ✅ COVERED — steps have real logic; [正向] 大小写不匹配时返回 false |
| 42 | [COMPAT-EXPR-01-005](case/COMPAT-EXPR-01-005.md) | contains 表达式空值与空字符串边界 | [正向] 空字符串包含任意非空子串返回 false: ✅ COVERED — steps have real logic; [正向] 任意字符串包含空 |
| 43 | [COMPAT-EXPR-01-006](case/COMPAT-EXPR-01-006.md) | hashFiles 表达式无匹配路径边界 | [正向] 无匹配时返回空字符串: ✅ COVERED — steps have real logic; [负向] 无匹配时不应抛出异常导致 step  |
| 44 | [COMPAT-EXPR-01-007](case/COMPAT-EXPR-01-007.md) | hashFiles 表达式多路径组合边界 | [正向] 多路径匹配时返回非空哈希字符串: ✅ COVERED — steps have real logic; [正向] 修改任一匹配文件后哈希值发 |
| 45 | [COMPAT-EXPR-01-011](case/COMPAT-EXPR-01-011.md) | join() 函数缺失时的降级行为 | 不支持函数不应静默通过并返回意外值: 覆盖 — log assertion without specific string check; 错误信息应足 |
| 46 | [COMPAT-EXPR-01-012](case/COMPAT-EXPR-01-012.md) | fromJSON() 函数缺失时的降级行为 | 不支持函数不应静默通过并返回意外值: 覆盖 — log assertion without specific string check; 错误信息应足 |
| 47 | [COMPAT-FIELD-01-001](case/COMPAT-FIELD-01-001.md) | 含 run-name 字段的 workflow 应被报错或警告 | [负向] 不应被静默接受: ❌ UNVERIFIABLE — single dispatch cannot prove negation; [非功能] |
| 48 | [COMPAT-FIELD-01-002](case/COMPAT-FIELD-01-002.md) | 含 services 字段的 job 应被报错或警告 | [负向] 不应被静默接受: ❌ UNVERIFIABLE — single dispatch cannot prove negation; [非功能] |
| 49 | [COMPAT-FIELD-01-003](case/COMPAT-FIELD-01-003.md) | 未知顶层字段不应被静默忽略而应给出警告 | [负向] 不通过未知字段被静默忽略: ✅ COVERED — negative assertion in YAML assertions; [正向]  |
| 50 | [COMPAT-INPUTS-01-001](case/COMPAT-INPUTS-01-001.md) | workflow_dispatch inputs 类型限制 - boolea | [负向] boolean 类型不应被静默接受: ✅ COVERED — negative assertion in YAML assertions;  |
| 51 | [COMPAT-NEST-01-002](case/COMPAT-NEST-01-002.md) | workflow_call 嵌套层数 - 3 层越界应报错 | [负向] 3 层嵌套不应被静默接受: COVERED — negative assertion present; [正向] 错误信息应明确指出嵌套层数 |
| 52 | [COMPAT-PATHS-01-001](case/COMPAT-PATHS-01-001.md) | paths 过滤器 300 条边界测试 | [正向] workflow 校验通过: WEAK — assertions present but all steps trivial; [正向] 匹 |
| 53 | [COMPAT-PATHS-01-002](case/COMPAT-PATHS-01-002.md) | paths 过滤器 301 条越界测试 | [负向] 超出上限的 paths 不应被静默接受: COVERED — negative assertion present; [正向] 错误信息应明 |
| 54 | [COMPAT-PERM-01-001](case/COMPAT-PERM-01-001.md) | 未声明 permissions 时默认 TOKEN 读操作权限范围 | [正向] checkout step 成功完成: COVERED — 1 real steps, assertions present; [正向] 读 |
| 55 | [COMPAT-PERM-01-002](case/COMPAT-PERM-01-002.md) | 未声明 permissions 时 fork PR 写操作隔离 | [负向] 写操作（如 git push 或 API 写调用）失败或被阻止: COVERED — negative assertion present; |
| 56 | [COMPAT-PR-01-002](case/COMPAT-PR-01-002.md) | pull_request types 命名差异 - GitHub 风格 ty | [负向] GitHub 风格 types 不应被静默接受: COVERED — negative assertion present; [正向] 错误 |
| 57 | [COMPAT-RUNNER-01-001](case/COMPAT-RUNNER-01-001.md) | runner.os 在 Linux Runner 上应返回 Linux | [正向] 日志中 runner.os 的值为 Linux: COVERED — 1 real steps, assertions present; [ |
| 58 | [COMPAT-RUNNER-01-002](case/COMPAT-RUNNER-01-002.md) | runner.arch 在 x86_64 Runner 上应返回 X64 | [正向] 日志中 runner.arch 的值为 X64: COVERED — 1 real steps, assertions present; [ |
| 59 | [COMPAT-RUNNER-01-003](case/COMPAT-RUNNER-01-003.md) | self-hosted 标签不被支持时应明确报错 | [正向] 系统对不支持的 self-hosted 标签给出明确报错: WEAK — assertions present but all steps  |
| 60 | [COMPAT-RUNNER-01-004](case/COMPAT-RUNNER-01-004.md) | 自定义特征标签不被支持时应给出可用标签列表 | [正向] 报错信息说明标签不匹配: WEAK — assertions present but all steps trivial; [正向] 报错给 |
| 61 | [COMPAT-RUNNER-01-005](case/COMPAT-RUNNER-01-005.md) | 内网环境 Runner 不支持时的差异 | [正向] 系统对内网标签给出明确报错: WEAK — assertions present but all steps trivial; [负向] 不 |
| 62 | [COMPAT-RUNNER-01-006](case/COMPAT-RUNNER-01-006.md) | Runner 未预装 Java 工具链与 GitHub 差异 | [正向] 系统对缺失的 Java 工具链给出明确提示: WEAK — assertions present but all steps trivial |
| 63 | [COMPAT-RUNSON-01-001](case/COMPAT-RUNSON-01-001.md) | runs-on 标签体系——三段式数组正常匹配 | [正向] 工作流成功启动并执行: WEAK — assertions present but all steps trivial; [正向] 日志中显 |
| 64 | [COMPAT-RUNSON-01-002](case/COMPAT-RUNSON-01-002.md) | runs-on 标签体系——单标签字符串应报错 | [负向] 单标签字符串格式在解析/校验阶段报错: COVERED — negative assertion present; [正向] 错误信息应明确 |
| 65 | [COMPAT-SCHEDULE-01-002](case/COMPAT-SCHEDULE-01-002.md) | schedule 不支持 timezone 字段差异 | [负向] 不应因 timezone 字段导致不可预期的行为: COVERED — negative assertion present; [正向] 错 |
| 66 | [COMPAT-SHELL-01-003](case/COMPAT-SHELL-01-003.md) | Windows runner 默认 shell 差异 | [正向] 默认 shell 正确执行 Windows 命令: WEAK — assertions present but all steps triv |
| 67 | [COMPAT-TOKEN-01-002](case/COMPAT-TOKEN-01-002.md) | GITHUB_TOKEN 在 GitCode 中应为空且不应被静默映射 | [负向] GITHUB_TOKEN 不应被静默映射为 ATOMGIT_TOKEN: COVERED — negative assertion pres |
| 68 | [COMPAT-VARS-01-002](case/COMPAT-VARS-01-002.md) | vars 上下文若不支持应报错而非静默为空 | [负向] 不应静默求值为空: COVERED — negative assertion present; [非功能] 报错信息应说明 vars 上下文 |
| 69 | [COMPAT-WCMD-01-001](case/COMPAT-WCMD-01-001.md) | ::add-mask:: 不被支持时应静默降级而非报错 | [正向] workflow 不因 add-mask 命令而失败: WEAK — assertions present but all steps tr |
| 70 | [COMPAT-WCMD-01-002](case/COMPAT-WCMD-01-002.md) | ::group:: 不被支持时应静默降级而非报错 | [正向] workflow 不因 group 命令而失败: WEAK — assertions present but all steps trivi |
| 71 | [COMPAT-WCMD-01-003](case/COMPAT-WCMD-01-003.md) | ::stop-commands:: 不被支持时应静默降级而非报错 | [正向] workflow 不因 stop-commands 而失败: WEAK — assertions present but all steps |
| 72 | [REL-API-01-065](case/REL-API-01-065.md) | API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据 | [正向] 200 占比=100%: WEAK — assertions present but all steps trivial; [负向] 不应出 |
| 73 | [REL-BIGRUNNER-01-066](case/REL-BIGRUNNER-01-066.md) | 大规格资源调度稳定性——xlarge/2xlarge 反复编译成功率 | [正向] 成功率≥90%: WEAK — assertions present but all steps trivial; [正向] 失败归因明确: |
| 74 | [REL-CACHE-01-046](case/REL-CACHE-01-046.md) | 缓存 LRU 淘汰压力——连续写入 10 个大缓存后最旧缓存应被正确淘汰 | [正向] 最新 key 状态=hit: COVERED — 1 real steps, assertions present; [正向] 最旧 key |
| 75 | [REL-CACHEPERF-01-054](case/REL-CACHEPERF-01-054.md) | 缓存加速比——cache 命中 vs 未命中构建耗时对比 | [正向] 加速比≥2x: WEAK — 2 real steps but no assertions; [负向] cache 命中后不应仍执行完整安装 |
| 76 | [REL-CANCELREL-01-061](case/REL-CANCELREL-01-061.md) | 取消操作可靠性——queued/running/post 各阶段取消状态正确 | [正向] 各阶段取消终态稳定: COVERED — 1 real steps, assertions present; [非功能] 取消到终态稳定时间 |
| 77 | [REL-CHILDSTATE-01-064-V2](case/REL-CHILDSTATE-01-064-V2.md) | 子任务状态传播——workflow_call 未拉起时父 workflow  | [正向] 父 workflow 状态=failure: WEAK — assertions present but all steps trivial |
| 78 | [REL-CHILDSTATE-01-064](case/REL-CHILDSTATE-01-064.md) | 子任务状态传播——workflow_call 失败时父 workflow 不 | [正向] 父 workflow 状态=failure: WEAK — assertions present but all steps trivial |
| 79 | [REL-CONC-01-001](case/REL-CONC-01-001.md) | concurrency.max=5 时同时触发 5 个运行应全部进入执行态 | [正向] 5 个运行状态均为 completed(success): WEAK — assertions present but all steps  |
| 80 | [REL-CONC-01-002](case/REL-CONC-01-002.md) | concurrency.max=6 配置应被系统拒绝 | [正向] YAML 校验失败或保存被拒: WEAK — assertions present but all steps trivial; [负向]  |
| 81 | [REL-CONTINUE-01-030](case/REL-CONTINUE-01-030.md) | continue-on-error=true——job 失败后 workfl | [正向] job_a 状态=failure: WEAK — assertions present but all steps trivial; [正向 |
| 82 | [REL-CPU-01-022](case/REL-CPU-01-022.md) | Runner CPU 饱和——small runner 运行 4 个 CPU | [正向] job 状态=success: WEAK — assertions present but all steps trivial; [非功能] |
| 83 | [REL-DISK-01-018](case/REL-DISK-01-018.md) | Runner 磁盘边界——small runner 写入 49 GB 应成功 | [正向] job 状态=success: WEAK — assertions present but all steps trivial; [负向]  |
| 84 | [REL-DISK-01-019](case/REL-DISK-01-019.md) | Runner 磁盘越界——small runner 写入 51 GB 应失败 | [正向] job 状态=failure: WEAK — assertions present but all steps trivial; [正向]  |
| 85 | [REL-FAULT-01-031](case/REL-FAULT-01-031.md) | 故障注入——job 执行中 runner 进程被 SIGKILL 后应记录失 | [正向] job 状态=failure: WEAK — assertions present but all steps trivial; [正向]  |
| 86 | [REL-FAULT-01-032](case/REL-FAULT-01-032.md) | 故障注入——artifact 上传时网络分区 30 秒后应失败并报网络错误 | [正向] upload-artifact step 状态=failure: COVERED — 1 real steps, assertions pr |
| 87 | [REL-FAULT-01-033](case/REL-FAULT-01-033.md) | 故障注入——runner 磁盘接近满时写入操作应失败并报磁盘满 | [正向] job 状态=failure: WEAK — assertions present but all steps trivial; [正向]  |
| 88 | [REL-FAULT-01-034](case/REL-FAULT-01-034.md) | 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cac | [正向] cache step 标记为 miss 或跳过: COVERED — 1 real steps, assertions present; [ |
| 89 | [REL-FLOOD-01-036](case/REL-FLOOD-01-036.md) | 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflo | [正向] 10 个运行均被创建: WEAK — assertions present but all steps trivial; [正向] 每个运行 |
| 90 | [REL-FLOOD-01-037](case/REL-FLOOD-01-037.md) | 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃 | [正向] 50 个运行均被创建: WEAK — assertions present but all steps trivial; [正向] API/ |
| 91 | [REL-IGNORE-01-004](case/REL-IGNORE-01-004.md) | concurrency IGNORE 策略——超上限运行应直接执行 | [正向] 4 个运行全部 completed(success): WEAK — assertions present but all steps tr |
| 92 | [REL-IMAGE-01-052-V2](case/REL-IMAGE-01-052-V2.md) | 镜像拉取性能——5GB 自定义 container 环境准备耗时基准 | [正向] 拉取≤600s: COVERED — 1 real steps, assertions present; [负向] 不应 pending 后 |
| 93 | [REL-IMAGE-01-052](case/REL-IMAGE-01-052.md) | 镜像拉取性能——500MB 自定义 container 环境准备耗时基准 | [正向] 拉取≤2min: COVERED — 1 real steps, assertions present; [负向] 不应 pending 1 |
| 94 | [REL-K8S-01-045](case/REL-K8S-01-045.md) | 自托管 K8s Runner 弹性伸缩——min=1/max=1 时并发 3 | [正向] Pod 数=1: WEAK — assertions present but all steps trivial; [正向] 峰值并发=1: |
| 95 | [REL-LATENCY-01-050-V2](case/REL-LATENCY-01-050-V2.md) | 调度延迟压力——并发 20 个 job 的排队延迟与完成率 | [正向] 20 个 job 全部完成: WEAK — assertions present but all steps trivial; [负向] 无 |
| 96 | [REL-LOG-01-040](case/REL-LOG-01-040.md) | 超长日志——单 job 输出 100 MB 日志应完整保留且可下载查看 | [正向] 日志总大小≈100 MB: COVERED — 1 real steps, assertions present; [正向] 首尾行可查看: |
| 97 | [REL-LOGPERF-01-051](case/REL-LOGPERF-01-051.md) | 日志加载性能——50MB 日志下载与查看耗时 | [正向] 下载≤30s: COVERED — 1 real steps, assertions present; [正向] 大小/行数 100% 一致 |
| 98 | [REL-LOGSTABLE-01-059](case/REL-LOGSTABLE-01-059.md) | 日志系统稳定性——6 万行日志无乱序/无丢失/无截断 | [正向] 行数=60000: COVERED — 1 real steps, assertions present; [正向] 行号单调递增: COV |
| 99 | [REL-LONG-01-043](case/REL-LONG-01-043.md) | 长时运行接近 timeout 边界——350 分钟运行应成功且心跳保活正常 | [正向] job 状态=success: COVERED — 1 real steps, assertions present; [正向] 心跳日志间 |
| 100 | [REL-MATRIX-01-026](case/REL-MATRIX-01-026.md) | matrix fail-fast=true——任意 job 实例失败应立即取 | [正向] 失败 job 状态=failure: COVERED — 1 real steps, assertions present; [正向] 其余 |
| 101 | [REL-MATRIX-01-027](case/REL-MATRIX-01-027.md) | matrix max-parallel=4——9 个组合应最多同时运行 4  | [正向] 峰值并发≤4: COVERED — 1 real steps, assertions present; [正向] 9 个 jobs 全部 c |
| 102 | [REL-MATRIX-01-038](case/REL-MATRIX-01-038.md) | 大规模 matrix——20 个组合应全部生成并正确调度 | [正向] 20 个 jobs 全部生成: COVERED — 1 real steps, assertions present; [正向] 矩阵变量校 |
| 103 | [REL-MATRIXFAIR-01-056](case/REL-MATRIXFAIR-01-056.md) | 矩阵调度公平性——20 实例 matrix 配 max-parallel=4 | [正向] 20 实例全部完成: COVERED — 1 real steps, assertions present; [非功能] 最大/最小 que |
| 104 | [REL-MEM-01-020](case/REL-MEM-01-020.md) | Runner 内存边界——small runner 分配 7.5 GB 应成 | [正向] job 状态=success: WEAK — assertions present but all steps trivial; [负向]  |
| 105 | [REL-MEM-01-021](case/REL-MEM-01-021.md) | Runner 内存越界——small runner 分配 9 GB 应被 O | [正向] job 状态=failure: WEAK — assertions present but all steps trivial; [正向]  |
| 106 | [REL-NEEDS-01-025](case/REL-NEEDS-01-025.md) | needs 失败传播——上游 job 失败时下游 job 应被 skip | [正向] job_a 状态=failure: WEAK — assertions present but all steps trivial; [正向 |
| 107 | [REL-NETFAULT-01-062](case/REL-NETFAULT-01-062.md) | 网络依赖容错——workflow 中访问不可达地址的明确失败与有界超时 | [正向] 可达地址成功: COVERED — 1 real steps, assertions present; [负向] 不可达地址不应 hang> |
| 108 | [REL-OUTPUT-01-016](case/REL-OUTPUT-01-016.md) | step output 边界值——ATOMGIT_OUTPUT 写入 1 M | [正向] 下游读取内容长度=1,048,576 bytes: COVERED — 2 real steps, assertions present;  |
| 109 | [REL-OUTPUT-01-017](case/REL-OUTPUT-01-017.md) | step output 越界值——ATOMGIT_OUTPUT 写入 1 M | [正向] step 状态=failure 或日志含 1MB/超出限制: COVERED — 1 real steps, assertions pres |
| 110 | [REL-PATHS-01-014](case/REL-PATHS-01-014.md) | paths 匹配边界值——变更恰好 300 个文件时 paths 过滤应生效 | [正向] workflow 运行被创建: WEAK — assertions present but all steps trivial; [负向]  |
| 111 | [REL-PATHS-01-015](case/REL-PATHS-01-015.md) | paths 匹配越界值——第 301 个变更文件不参与 paths 匹配判断 | [正向] workflow 不触发: WEAK — assertions present but all steps trivial; [负向] 第  |
| 112 | [REL-PREEMPT-01-005](case/REL-PREEMPT-01-005.md) | preemption events 边界值——配置 10 个应正常解析 | [正向] workflow 保存成功并运行 completed(success): WEAK — assertions present but all |
| 113 | [REL-PREEMPT-01-006](case/REL-PREEMPT-01-006.md) | preemption events 越界值——配置 11 个应被拒绝 | [正向] 明确报错: WEAK — assertions present but all steps trivial; [负向] 不应静默截断: UN |
| 114 | [REL-PRESSURE-01-055](case/REL-PRESSURE-01-055.md) | 并发压测——concurrency.max=5 时触发 20 个 workf | [正向] completed=20: WEAK — assertions present but all steps trivial; [负向] ru |
| 115 | [REL-PROJLIMIT-01-067](case/REL-PROJLIMIT-01-067.md) | 项目级 workflow 并发上限——200 条同时触发时全部完成无丢失 | [正向] completed_count = 200: COVERED — 1 real steps, assertions present; [正向 |
| 116 | [REL-PROJLIMIT-01-068](case/REL-PROJLIMIT-01-068.md) | 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排 | [正向] completed_count = 201: COVERED — 1 real steps, assertions present; [正向 |
| 117 | [REL-QUEUE-01-003](case/REL-QUEUE-01-003.md) | concurrency QUEUE 策略——超上限运行应排队等待 | [正向] 4 个运行最终全部 completed(success): WEAK — assertions present but all steps  |
| 118 | [REL-RACE-01-048](case/REL-RACE-01-048.md) | 取消与 needs 条件竞态——job A 被取消时 job B(if: f | [正向] job A 状态=cancelled: WEAK — assertions present but all steps trivial; [ |
| 119 | [REL-RERUN-01-011](case/REL-RERUN-01-011.md) | rerun 边界值——单条运行连续重新运行 3 次应全部成功 | [正向] 运行编号递增: WEAK — assertions present but all steps trivial; [正向] 每次 rerun |
| 120 | [REL-RERUN-01-012](case/REL-RERUN-01-012.md) | rerun 越界值——尝试第 4 次重新运行应被系统拒绝 | [正向] 第 4 次 rerun 按钮不可用或点击后报错: WEAK — assertions present but all steps trivi |
| 121 | [REL-RERUN-01-013](case/REL-RERUN-01-013.md) | rerun 6 小时年龄限制——超期运行不可重新运行 | rerun 被拒绝: 覆盖 — real step logic exists; 不应创建新运行: 未覆盖 — 缺少负向断言 |
| 122 | [REL-RUNNER-01-049-V2](case/REL-RUNNER-01-049-V2.md) | Runner 规格真实性——xlarge/2xlarge 实际 CPU/内存 | CPU/内存/磁盘最小比率≥0.9: 覆盖 — real step logic exists; 不应因架构不匹配而随机失败: 未覆盖 — 缺少负向断言 |
| 123 | [REL-RUNNER-01-049](case/REL-RUNNER-01-049.md) | Runner 规格真实性——small/medium/large 实际 CP | CPU/内存/磁盘最小比率≥0.9: 覆盖 — real step logic exists; 实际资源不应显著低于声明: 未覆盖 — 缺少负向断言; |
| 124 | [REL-SCHED-01-057](case/REL-SCHED-01-057.md) | 资源调度状态一致性——空闲 runner 存在时 job 不应死等 | 10 次全部≤60s: 未覆盖 — 缺少正向断言; 平均≤30s: 覆盖 — 非功能断言存在(LLM评估); 不应出现 runner 空闲但 job  |
| 125 | [REL-STAGES-01-029](case/REL-STAGES-01-029.md) | stages fail_fast 机制——阶段内任一 job 失败应立即终止 | 失败 job 状态=failure: 覆盖 — deliberate failure step exists; 同阶段其余 jobs 状态∈{canc |
| 126 | [REL-STEPS-01-042](case/REL-STEPS-01-042.md) | 超多 step——单 job 内 50 个 step 应全部串行执行无丢失 | 50 个 step 全部出现在运行详情页: 空洞 — steps only echo literal strings; 每个 step 日志包含唯一标 |
| 127 | [REL-TIMEOUT-01-007](case/REL-TIMEOUT-01-007.md) | job timeout 边界值——359 分钟运行应在 360 分钟边界前完 | job 状态=success: 覆盖 — workflow can potentially fail; 不应在 358 分钟前被强制终止: 未覆盖 — |
| 128 | [REL-TIMEOUT-01-008](case/REL-TIMEOUT-01-008.md) | job timeout 越界触发——361 分钟应在 360 分钟被强制终止 | job 状态=failure: 覆盖 — potential failure paths exist; 日志含 timeout 或 超时: 覆盖 —  |
| 129 | [REL-TIMEOUT-01-010](case/REL-TIMEOUT-01-010.md) | 默认超时——未声明 timeout-minutes 运行 361 分钟应被强 | job 状态=failure: 覆盖 — potential failure paths exist; 不应无限运行: 未覆盖 — 缺少负向断言 |
| 130 | [SEC-CACHE-01-001](case/SEC-CACHE-01-001.md) | fork PR 写入的 cache 必须不可被主仓后续 workflow 读 | [负向] 主仓 workflow 在 fork PR 写入 cache 后，绝不应命中到该缓存: ✅ COVERED — 步骤以 fork 贡献者身份 |
| 131 | [SEC-COMM-01-001](case/SEC-COMM-01-001.md) | issue_comment / pull_request_comment 触 | [负向] 伪装在代码块或注释中的关键字绝不应触发 workflow: 🔄 UNVERIFIABLE — 单次已触发的 workflow 运行无法证明被 |
| 132 | [SEC-DEFPERM-01-001](case/SEC-DEFPERM-01-001.md) | ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效 | 顶层声明被各 job 继承；job 级声明覆盖顶层: 覆盖 — log assertion without specific string check |
| 133 | [SEC-DOS-01-001](case/SEC-DOS-01-001.md) | 大 artifact / 大 cache 必须受配额与边界限制 | 超过大小上限的 artifact/cache 上传绝不应成功写入: 覆盖 — negative status assertion; 超限时应给出明确报 |
| 134 | [SEC-INJ-01-001](case/SEC-INJ-01-001.md) | 不可信 PR 标题不可直接插进 run 脚本导致命令注入 | [负向] 含特殊字符的 PR 标题绝不应被解释为 shell 命令执行: ✅ COVERED — 步骤通过 `${{ atomgit.event.pu |
| 135 | [SEC-INJ-01-002](case/SEC-INJ-01-002.md) | 不可信分支名不可直接插进 run 脚本导致命令注入 | [负向] 含特殊字符的分支名绝不应被解释为 shell 命令: ✅ COVERED — 步骤通过 `${{ atomgit.head_ref }}`  |
| 136 | [SEC-INJ-01-003](case/SEC-INJ-01-003.md) | 不可信 issue/PR 评论内容不可直接插进 run 脚本导致命令注入 | [负向] 含 shell 元字符的评论内容绝不应被解释为命令执行: ✅ COVERED — 步骤通过 `${{ atomgit.event.comme |
| 137 | [SEC-INJ-01-004](case/SEC-INJ-01-004.md) | 不可信 commit message 不可直接插进 run 脚本导致命令注入 | [负向] 含反引号或分号的 commit message 绝不应被解释为命令执行: ✅ COVERED — 步骤通过 `${{ atomgit.eve |
| 138 | [SEC-INJ-01-005](case/SEC-INJ-01-005.md) | 表达式求值必须防止双重模板渲染（二次求值） | [negative] run_logs must_not_contain: 2: UNCOVERED — 期望值 [2] 未在任何步骤输出中找到; [ |
| 139 | [SEC-MASK-01-001](case/SEC-MASK-01-001.md) | Secret 值在运行日志中必须被自动脱敏为 *** | [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN: COVERED — 步骤使用了  |
| 140 | [SEC-MASK-01-003](case/SEC-MASK-01-003.md) | Secret 日志脱敏不可通过 base64 编码绕过 | [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN: COVERED — 步骤使用了  |
| 141 | [SEC-MASK-01-004](case/SEC-MASK-01-004.md) | Secret 日志脱敏不可通过字符串拼接或插值绕过 | [negative] run_logs must_not_contain_secret: API_KEY: COVERED — 步骤使用了 API_K |
| 142 | [SEC-MASK-01-005](case/SEC-MASK-01-005.md) | Secret 日志脱敏不可通过多行值输出绕过 | [negative] run_logs must_not_contain_secret: MULTI_LINE_SECRET: COVERED — 步 |
| 143 | [SEC-MASK-01-006](case/SEC-MASK-01-006.md) | Secret 日志脱敏不可通过分片输出绕过 | [negative] run_logs must_not_contain_secret: DEPLOY_TOKEN: COVERED — 步骤使用了  |
| 144 | [SEC-NAME-01-002](case/SEC-NAME-01-002.md) | 通过 printenv 或进程枚举获取 ATOMGIT_TOKEN/secr | [negative] run_logs must_not_contain_secret: API_KEY: COVERED — 步骤使用了 API_K |
| 145 | [SEC-NET-01-001](case/SEC-NET-01-001.md) | Runner 网络出站必须受控，防止 SSRF 与内网跳板 | [negative] run_logs must_not_contain: metadata_service_response: UNCOVERED  |
| 146 | [SEC-OIDC-01-001](case/SEC-OIDC-01-001.md) | OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案 | 不支持 OIDC 时，系统绝不应提供可长期复用的高权限云部署凭证作为默认方案: 空洞 — no real logic, negative assert |
| 147 | [SEC-PERM-01-001](case/SEC-PERM-01-001.md) | 显式声明的 permissions 必须在 job 级实际生效并限制 ATO | [positive] run_logs equals: read_operations_successful: UNCOVERED — 期望值 [re |
| 148 | [SEC-PERM-01-002](case/SEC-PERM-01-002.md) | permissions 声明 read 时写操作被平台拒绝 | [negative] run_logs must_not_contain: push_successful: UNCOVERED — 期望值 [pus |
| 149 | [SEC-PERM-01-003](case/SEC-PERM-01-003.md) | 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须 | [negative] run_logs must_not_contain: write_permission_granted: UNCOVERED — |
| 150 | [SEC-PERM-01-004](case/SEC-PERM-01-004.md) | 默认状态下写操作被 403 拒绝 | [negative] run_logs must_not_contain: push_successful: UNCOVERED — 期望值 [pus |
| 151 | [SEC-RUN-01-001](case/SEC-RUN-01-001.md) | Job 结束后 workspace 与临时文件必须被彻底清理 | [negative] run_logs must_not_contain: residual found: COVERED — 步骤 [Check n |
| 152 | [SEC-RUN-01-002](case/SEC-RUN-01-002.md) | Runner 环境变量与共享目录必须跨 job 隔离 | [negative] run_logs must_not_contain: isolation broken: COVERED — 步骤 [Check |
| 153 | [SEC-RUN-01-003](case/SEC-RUN-01-003.md) | 自托管 Runner 跨项目残留必须被隔离 | [negative] run_logs must_not_contain: cross project leak: COVERED — 步骤 [Che |
| 154 | [SEC-TOCTOU-01-001](case/SEC-TOCTOU-01-001.md) | 审批后推送新 commit 不应被已授权特权运行执行 | [negative] run_logs must_not_contain: unapproved_commit_executed: UNCOVERED |
| 155 | [SEC-WCMD-01-001](case/SEC-WCMD-01-001.md) | Workflow 命令（如 add-mask）的响应本身不可泄露被遮蔽前的  | [negative] run_logs must_not_contain_secret: API_KEY: COVERED — 步骤使用了 API_K |
| 156 | [SEC-WCMD-01-003](case/SEC-WCMD-01-003.md) | ATOMGIT_ENV 不被不可信输入污染提权 | [negative] run_logs must_not_contain: injection succeeded: UNCOVERED — 期望值  |
| 157 | [SEC-WCMD-01-004](case/SEC-WCMD-01-004.md) | ATOMGIT_OUTPUT 不被不可信输入污染提权 | [negative] run_logs must_not_contain: hijack succeeded: UNCOVERED — 期望值 [hi |
| 158 | [USE-ACT-01-002](case/USE-ACT-01-002.md) | 使用 actions/checkout@v4 时报错应给出迁移指引 | [negative] run_status equals: COMPLETED: COVERED — 步骤含实际命令/action，失败状态取决于真实 |
| 159 | [USE-BADGE-01-001](case/USE-BADGE-01-001.md) | workflow 运行完成后状态徽标及时回写且语义清晰 | [positive] run_status equals: COMPLETED: UNCOVERED — 所有步骤无实质逻辑/条件/action，wo |
| 160 | [USE-DEPR-01-002](case/USE-DEPR-01-002.md) | 使用 ::set-output 时应给出弃用警告与替代示例 | 不应静默生效: 未覆盖 — 缺少负向断言; 日志警告中应包含 deprecated/废弃/ATOMGIT_OUTPUT 字样: 覆盖 — 非功能断言存 |
| 161 | [USE-DIR-01-001](case/USE-DIR-01-001.md) | workflow 放置于 .gitcode/workflows/ 下可正常触 | [positive] run_status equals: COMPLETED: UNCOVERED — 所有步骤无实质逻辑/条件/action，wo |
| 162 | [USE-EXPR-01-001](case/USE-EXPR-01-001.md) | 引用不存在的上下文属性时报错应包含原始表达式与错误类型 | [negative] run_status equals: COMPLETED: COVERED — 步骤含实际命令/action，失败状态取决于真实 |
| 163 | [USE-EXPR-01-002](case/USE-EXPR-01-002.md) | 调用未知函数时报错应提示函数名错误与修正方向 | [negative] run_status equals: COMPLETED: COVERED — 存在失败路径：有 fail 命令或条件分支可产生 |
| 164 | [USE-MASK-01-001](case/USE-MASK-01-001.md) | secret 脱敏文档描述与实际行为一致并给出缓解建议 | [positive] run_logs must_not_contain_secret: TEST_SECRET: UNCOVERED — secre |
| 165 | [USE-MASK-01-002](case/USE-MASK-01-002.md) | 直接 echo secrets 值时文档描述的绕过风险与实际一致 | 若绕过确实发生，日志中可能出现明文: 未覆盖 — 缺少负向断言; 文档是否给出不要在 run 中直接 echo secrets 的缓解建议: 覆盖 — |
| 166 | [USE-MD-01-001](case/USE-MD-01-001.md) | ATOMGIT_STEP_SUMMARY 写入的 Markdown 正确渲染 | [positive] step_summary contains: Test Report: COVERED — target=step_summar |
| 167 | [USE-NEST-01-002](case/USE-NEST-01-002.md) | workflow_call 嵌套 2 层时应正常执行 | 运行成功完成: 覆盖 — status assertion: COMPLETED; 不应报嵌套超限错误: 未覆盖 — 缺少负向断言 |
| 168 | [USE-PERM-01-002](case/USE-PERM-01-002.md) | 使用 GitHub 权限域命名时报错应给出 GitCode 对照表 | [negative] run_status equals: COMPLETED: COVERED — 步骤含实际命令/action，失败状态取决于真实 |
| 169 | [USE-TYPE-01-002](case/USE-TYPE-01-002.md) | 使用 GitHub types 命名 opened/synchronize  | [负向] 不应静默通过校验并在运行时永远不被触发: ✅ COVERED — 断言 type=negative target=run_status eq |
| 170 | [USE-YAML-01-001](case/USE-YAML-01-001.md) | 缺少必填字段 on 时报错应指出具体字段名与位置 | [negative] run_status equals: COMPLETED: UNCOVERED — [负向] 未找到可能导致非成功状态的步骤，单 |
| 171 | [USE-YAML-01-002](case/USE-YAML-01-002.md) | YAML 缩进错误时报错应指出具体行号与列号 | [negative] run_status equals: COMPLETED: ✅ COVERED — workflow 含有故意缩进错误的 YAM |

## 完全不符 — 全部验证点未能由步骤产出（28 例）

| # | Case ID | 标题 | 原因 |
|---|---------|------|------|
| 1 | [COMP-BOUND-01-085](case/COMP-BOUND-01-085.md) | cron 表达式格式与位置边界验证 | [正向] 含 * 的 cron 通过校验: ❌ BLOCKED — schedule 触发无法在测试环境中即时验证; [正向] 含 , 的 cron  |
| 2 | [COMP-CACHE-01-003](case/COMP-CACHE-01-003.md) | fork PR 不应覆盖或污染主分支 cache | [负向] fork PR 不应覆盖主分支 cache: ❌ BLOCKED — untrusted_contributor 身份依赖多账号模拟 for |
| 3 | [COMP-RUNNER-01-003](case/COMP-RUNNER-01-003.md) | 不存在的标签组合导致 job 排队或失败 | job 不应成功执行: 空洞 — no failure path exists, status=success guaranteed; 系统应给出标签 |
| 4 | [COMP-SCHEDULE-01-001](case/COMP-SCHEDULE-01-001.md) | 合法 cron 在默认分支按时触发 | [正向] 运行记录存在且 event 为 schedule: ⚠️ TRIVIAL — 步骤仅 echo 字面量 "scheduled run"，无  |
| 5 | [COMP-SCHEDULE-01-002](case/COMP-SCHEDULE-01-002.md) | 非默认分支的 schedule workflow 不应触发 | [负向] 运行列表中不存在该 schedule 触发的运行: ❌ MISSING — 步骤仅 echo 字面量 "should not run"，无任 |
| 6 | [COMP-SCHEDULE-01-003](case/COMP-SCHEDULE-01-003.md) | cron 间隔短于 5 分钟时被拒绝或降级 | [负向] 不应允许每分钟触发的 schedule: 🔄 UNVERIFIABLE — 平台级校验（workflow 提交时拒绝）发生在步骤执行之前，步 |
| 7 | [COMP-STAGES-01-001](case/COMP-STAGES-01-001.md) | stages 阶段间串行、阶段内 job 并行执行 | stage 2 的 job 开始时间晚于 stage 1 所有 job 的结束时间: 空洞 — all steps trivial, status=s |
| 8 | [COMPAT-COMM-01-002](case/COMPAT-COMM-01-002.md) | issue_comment types:created 不支持时应给出降级指 | [负向] 不通过静默忽略（types 配置失效）: 🔄 UNVERIFIABLE — 步骤仅输出 `event_name=issue_comment` |
| 9 | [COMPAT-NEST-01-001](case/COMPAT-NEST-01-001.md) | workflow_call 嵌套层数 - 2 层正常执行 | [正向] 2 层嵌套 workflow 能正常触发并执行: NOT COVERED — no steps in workflow; [正向] 运行状态 |
| 10 | [REL-FAIR-01-044](case/REL-FAIR-01-044.md) | 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调 | [正向] 启动时延差≤60 秒: NOT COVERED — no real steps, no assertions; [负向] 不应出现 work |
| 11 | [REL-LATENCY-01-050](case/REL-LATENCY-01-050.md) | 调度延迟基准——queued→running P50/P95 等待时间 | [正向] P95≤60s: NOT COVERED — no real steps, no assertions; [负向] 不应出现 runner  |
| 12 | [REL-NEST-01-023](case/REL-NEST-01-023.md) | workflow_call 嵌套边界——2 层嵌套调用应成功执行 | [正向] 最外层运行状态=success: NOT COVERED — no steps in workflow; [正向] 所有子运行均 succe |
| 13 | [REL-NEST-01-024](case/REL-NEST-01-024.md) | workflow_call 嵌套越界——3 层嵌套调用应被拒绝 | [正向] 运行状态=failure: NOT COVERED — no steps in workflow; [正向] 日志明确提示嵌套超限: NOT |
| 14 | [REL-YAMLCACHE-01-060](case/REL-YAMLCACHE-01-060.md) | Workflow YAML 缓存失效——修改后无旧代码残留 | 日志打印 marker_v2: 空洞 — no step produces 'marker_v2'; 不应打印 marker_v1: 空洞 — ste |
| 15 | [USE-ANNOT-01-002](case/USE-ANNOT-01-002.md) | ::error:: 生成的 PR annotation 具备文件路径、行号与 | [非功能] annotation 是否包含准确的文件路径、行号、错误信息: 🔄 UNVERIFIABLE — 断言 type=nonfunctiona |
| 16 | [USE-CTX-01-001](case/USE-CTX-01-001.md) | 使用 atomgit 上下文时表达式正常求值 | 日志中输出当前分支引用值: 空洞 — no step produces 'ref=refs/heads/'; 运行成功完成: 空洞 — no step |
| 17 | [USE-DEPR-01-001](case/USE-DEPR-01-001.md) | 使用 ATOMGIT_OUTPUT 文件协议时正常生效 | 下游步骤通过 steps.*.outputs.key 获取到值: 空洞 — no step produces 'val=myvalue'; 运行成功完 |
| 18 | [USE-DIR-01-002](case/USE-DIR-01-002.md) | .github/workflows/ 下 workflow 未被识别时应给出 | [负向] 不应无任何提示地忽略 .github/workflows/ 下的文件: ❌ UNVERIFIABLE — workflow=null，无步骤 |
| 19 | [USE-DISP-01-002](case/USE-DISP-01-002.md) | workflow_dispatch 未提供参数但存在 default 时应使 | 运行成功完成: 空洞 — no step produces 'env=staging'; 日志中输出 default 值: 空洞 — no step  |
| 20 | [USE-DOC-01-001](case/USE-DOC-01-001.md) | stages 与 post 概念在迁移文档中具备可发现性 | [正向] 迁移相关页面有 stages/post 的入口链接: ❌ MISSING — workflow=null，无步骤产出文档内容验证; [非功能 |
| 21 | [USE-ENV-01-002](case/USE-ENV-01-002.md) | 引用 GITHUB_SHA 时日志应给出环境变量映射提示 | [负向] 不应静默输出空值后继续: ❌ UNVERIFIABLE — 步骤含 `set -u` / `$GITHUB_SHA` 引用但仅 echo；s |
| 22 | [USE-LOG-01-001](case/USE-LOG-01-001.md) | 多 step 日志按时间线组织且边界清晰 | 日志面板中 step 按定义顺序排列，step 内 shell 输出内容（如 "prepare done"）可在 run_logs 中检索到: 空洞  |
| 23 | [USE-OS-01-001](case/USE-OS-01-001.md) | runner.os 返回值与文档声明的平台支持一致 | runner.os 返回 Linux: 空洞 — no step produces 'os=Linux'; 文档中 runner.os 说明旁是否附加 |
| 24 | [USE-PATH-01-001](case/USE-PATH-01-001.md) | paths 300 文件上限在文档与行为中一致且明示 | [非功能] 文档 paths 章节有 300 文件上限提示: ❌ MISSING — workflow=null，无步骤审查文档内容; [非功能] 超 |
| 25 | [USE-RES-01-001](case/USE-RES-01-001.md) | runtime-environment-variables.md 中不应出现 | [正向] 所有独立环境变量示例使用 ATOMGIT_ 前缀: ❌ MISSING — workflow=null，无步骤扫描文档进行字符串匹配; [负 |
| 26 | [USE-UNKN-01-001](case/USE-UNKN-01-001.md) | 未知字段如 run-name 不应被静默忽略而应给出警告或错误 | [负向] 不应静默忽略未知字段: ❌ UNVERIFIABLE — workflow 含 `run-name: Build by ${{ atomgi |
| 27 | [USE-UNKN-01-002](case/USE-UNKN-01-002.md) | 未知字段报错若识别为 GitHub 特有应追加迁移提示 | [非功能] 报错中出现 GitHub Actions 特有迁移提示: ❌ TRIVIAL — 步骤仅 `echo "hello"`，无 if:/${{ |
| 28 | [USE-VARS-01-001](case/USE-VARS-01-001.md) | vars 上下文在文档与样本中的声明必须一致 | [正向] 若支持，文档示例可运行且样本注释已移除: ❌ MISSING — workflow=null，无步骤能够运行文档示例或检查样本注释; [负向 |
