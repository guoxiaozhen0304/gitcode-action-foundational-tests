# Failure Analyst 全量汇总 · run 2026-07-24-valid297-final2

## 执行概要

- **Run ID**: 2026-07-24-valid297-final2
- **总用例**: 297
- **PASS**: 131 (44.1%)
- **FAIL**: 82 (27.6%)
- **COMPILE_ERROR**: 63 (21.2%)
- **TIMEOUT**: 16 (5.4%)
- **ENV_ERROR**: 4 (1.3%)
- **INCONCLUSIVE**: 1 (0.3%)

## 归因分类分布

| 根因分类 | 数量 | 主要维度 |
|---------|------|---------|
| **产品缺陷/平台bug** | 35 | completeness, security, compatibility, reliability |
| **用例问题（断言关键词错配/脚本输出不一致）** | 15 | completeness, reliability, usability |
| **需人工判断（日志截断/证据不足）** | 20 | 各维度均有 |
| **环境问题（日志缺失严重）** | 12 | completeness, security, reliability |

## ★ 系统性缺陷发现（按严重程度排序）

### 1. Secret注入链路断裂（P0-安全严重）
**影响用例**: COMP-SECRET-01-001, SEC-MASK-01-001, SEC-MASK-01-005, SEC-WCMD-01-001 等
**现象**: config_probe确认secret已配置，但echo输出为空（`secret is `）
**归因**: 产品缺陷 — 平台在运行时secret注入链路中未正确传递secret值
**影响**: 阻塞+静默+跨维度 — CI/CD安全基础设施失效

### 2. Fork PR Secret隔离缺失（P0-安全严重）
**影响用例**: COMP-PR-01-001, SEC-FORK-01-001
**现象**: fork PR的pull_request事件成功读到项目secrets
**归因**: 产品缺陷 — 平台未正确隔离fork PR的secret访问
**影响**: 阻塞+静默+跨维度 — fork PR可读取目标仓库secrets

### 3. 平台静默接受无效配置（P1-系统性）
**影响用例**: USE-CONC-01-001, USE-CTX-01-002, USE-EXPR-01-001, USE-INPT-01-002, USE-SECNAME-01-001, COMPAT-INPUTS-01-001
**现象**: 多个负向测试期望平台拒绝，但平台全部接受并正常执行
**归因**: 产品缺陷 — 缺乏输入校验
**影响**: 非阻塞但静默 — 用户可能无感知地使用不受支持的配置

### 4. 近空日志问题（P1-诊断能力）
**影响用例**: 约25个FAIL用例日志仅1-3行（"duration check: true"），无shell脚本输出
**归因**: 环境问题/日志采集缺陷 — 大量用例无法从日志诊断失败原因
**影响**: 影响全部FAIL用例的诊断效率

### 5. Cache/Artifact功能不可用（P0-基础能力）
**影响用例**: COMP-CACHE-01-001/002, COMP-ARTIFACT-01-001/002/003, COMPAT-CACHE-01-001, COMPAT-ARTIFACT-01-001/002, REL-ART-*, REL-ARTPERF-*, REL-RETAIN-01-047
**现象**: cache所有测试FAIL，artifact上传/下载均FAIL，日志几乎为空
**归因**: 产品缺陷 — cache/artifact插件完全不工作
**影响**: 阻塞+跨维度 — CI流水线核心能力缺失

### 6. Pull_request_target安全机制可能不完整（P0-安全）
**影响用例**: SEC-BASE-01-001, SEC-BASE-01-002, SEC-PRTGT-01-001, SEC-PRTGT-01-002
**归因**: 产品缺陷 — pull_request_target隔离的多个维度FAIL
**影响**: 阻塞+跨维度+安全 — fork PR安全的基础防线

### 7. Timeout/Cancel状态标记异常
**影响用例**: COMP-TIMEOUT-01-002, REL-TIMEOUT-01-009, REL-CANCEL-01-028
**现象**: 超时被标记为CANCELLED而非FAILED；取消操作标记为COMPLETED
**归因**: 产品缺陷 — 状态机标记与预期不一致
**影响**: 非阻塞 — 但可能影响下游依赖

### 8. 断言引擎可能的误报
**影响用例**: SEC-INJ-01-005 (标记SECURITY_CRITICAL但表达式实际未求值)
**现象**: leak断言在6行日志中检测到'2'，但日志中表达式因bash错误未求值
**归因**: 需人工判断 — 可能为断言引擎在版本号/哈希中匹配到'2'
**影响**: 标记级别异常 — SECURITY_CRITICAL可能是假阳性

## 真缺陷清单（高置信度产品缺陷）

| 用例 | 缺陷描述 | 影响维度 |
|------|---------|---------|
| COMP-CACHE-01-001 | cache插件完全不工作 | completeness |
| COMP-CACHE-01-002 | restore-keys不工作 | completeness |
| COMP-ARTIFACT-01-001 | artifact跨job传递失败 | completeness |
| COMP-ARTIFACT-01-002 | artifact全量下载不可用 | completeness |
| COMP-SECRET-01-001 | secret注入链路断裂 | security |
| COMP-PR-01-001 | fork PR能读取secrets | security |
| SEC-FORK-01-001 | fork PR secret隔离缺失 | security |
| COMP-PERMS-01-002 | permissions write不生效 | completeness |
| SEC-SUPPLY-01-001 | Action fixed-hash引用失败 | security |
| COMP-CALL-01-001 | workflow_call不可用 | completeness |
| COMP-SUMMARY-01-001 | Step Summary不工作 | completeness |
| COMP-TIMEOUT-01-002 | timeout状态标记异常 | completeness |
| COMPAT-INPUTS-01-001 | 不接受input类型未报错 | compatibility |
| USE-CONC-01-001 | concurrency.max校验缺失 | usability |
| USE-CTX-01-002 | github上下文未警告 | usability |
| USE-EXPR-01-001 | 不存在上下文属性未报错 | usability |
| USE-INPT-01-002 | boolean input未报错 | usability |
| USE-SECNAME-01-001 | ATOMGIT_前缀secrets未拒绝 | usability |
| REL-CONTINUE-01-030 | continue-on-error行为异常 | reliability |
| REL-MATRIX-01-026 | fail-fast不生效 | reliability |
| REL-NEEDS-01-025 | needs失败传导不正确 | reliability |
| REL-YAMLCACHE-01-060 | workflow YAML缓存不失效 | reliability |

## 用时

- **归因开始**: 2026-07-24 22:30 CST
- **归因完成**: 2026-07-24 23:15 CST
- **总耗时**: 约45分钟（82个FAIL用例逐条分析）
