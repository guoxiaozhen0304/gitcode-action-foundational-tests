# 风险登记册（全平台 — 决定测试火力分配）

> L0 基线之一。这是**优先级的唯一来源**——所有 intent/用例的 P0/P1/P2 都从这里取。
> 覆盖度评审的另一坐标系：每个 blocker 风险项都必须有 P0 用例覆盖，否则记为盲区。
> **本文件已按全平台扩展（Actions + 代码托管 + MR + Issues + Packages + 权限），风险项需阿蓁评审确认。**

## 优先级规则
- **P0（blocker）**：影响高 × 发生概率不低，或安全命脉——不修不能上线。
- **P1**：影响大但有 workaround。
- **P2**：体验/边角。

---

## 一、安全性（Security）

| 风险 ID | 维度 | 风险描述 | 影响 | 概率 | 优先级 | 是否 blocker | 依据 | 覆盖意图 |
|---|---|---|---|---|---|---|---|---|
| RISK-SEC-01 | 安全 | fork PR 读到仓库 secrets | 高 | 中 | P0 | 是 | 攻击面/CVE 模式 | INTENT-SEC-001 |
| RISK-SEC-02 | 安全 | 不可信输入注入命令执行（脚本注入） | 高 | 中 | P0 | 是 | Actions 高频漏洞 | INTENT-SEC-002 |
| RISK-SEC-03 | 安全 | `pull_request_target` checkout 不可信代码 | 高 | 中 | P0 | 是 | 高权限运行不可信代码 | INTENT-SEC-003 |
| RISK-SEC-04 | 安全 | cache 投毒（跨 fork/跨分支污染） | 高 | 低 | P1 | 否 | 供应链攻击模式 | INTENT-SEC-004 |
| RISK-SEC-05 | 安全 | Personal Access Token 泄露（日志/artifact） | 高 | 中 | P0 | 是 | 历史实证：token 脱敏绕过 | INTENT-SEC-005 |
| RISK-SEC-06 | 安全 | 权限越界（低权限用户访问高权限资源） | 高 | 中 | P0 | 是 | 权限模型缺陷 | INTENT-SEC-006 |
| RISK-SEC-07 | 安全 | Package 仓库被恶意覆盖/投毒 | 高 | 低 | P1 | 否 | 供应链安全 | INTENT-SEC-007 |
| RISK-SEC-08 | 安全 | Webhook secret 泄露或签名绕过 | 高 | 低 | P1 | 否 | 中间人攻击 | INTENT-SEC-008 |
| RISK-SEC-09 | 安全 | 组织成员非法提升权限（提权漏洞） | 高 | 低 | P0 | 是 | 权限继承缺陷 | INTENT-SEC-009 |

---

## 二、完备性（Completeness）

| 风险 ID | 维度 | 风险描述 | 影响 | 概率 | 优先级 | 是否 blocker | 依据 | 覆盖意图 |
|---|---|---|---|---|---|---|---|---|
| RISK-COMP-01 | 完备 | 核心 API 端点缺失或返回格式不兼容 | 高 | 中 | P0 | 是 | 平台可用性根基 | INTENT-COMP-101 |
| RISK-COMP-02 | 完备 | 默认值差异致行为静默不同（如 timeout、权限） | 中 | 高 | P1 | 否 | 兼容性差异高发 | INTENT-COMP-102 |
| RISK-COMP-03 | 完备 | 空仓库/空数据场景 API 行为异常 | 中 | 高 | P1 | 否 | 边界场景 | INTENT-COMP-103 |
| RISK-COMP-04 | 完备 | 分页参数（per_page/page）不生效或越界崩溃 | 中 | 中 | P1 | 否 | API 健壮性 | INTENT-COMP-104 |
| RISK-COMP-05 | 完备 | Package 格式支持缺失（如只支持 npm 不支持 docker） | 高 | 低 | P1 | 否 | 功能缺失 | INTENT-COMP-105 |

---

## 三、稳定性（Reliability）

| 风险 ID | 维度 | 风险描述 | 影响 | 概率 | 优先级 | 是否 blocker | 依据 | 覆盖意图 |
|---|---|---|---|---|---|---|---|---|
| RISK-REL-01 | 稳定 | 并发洪泛下排队/公平性失效 | 中 | 中 | P1 | 否 | 容量规格 | INTENT-REL-001 |
| RISK-REL-02 | 稳定 | needs 依赖的 matrix job 全成功但上游 job 初始化失败时无声失败 | 高 | 中 | P0 | 是 | 历史实证 #101 | INTENT-REL-069 |
| RISK-REL-03 | 稳定 | API 速率限制未正确返回 429/Retry-After | 中 | 中 | P1 | 否 | 客户端无法自适应退避 | INTENT-REL-002 |
| RISK-REL-04 | 稳定 | Webhook 投递失败无重试或重试风暴 | 中 | 中 | P1 | 否 | 集成可靠性 | INTENT-REL-003 |
| RISK-REL-05 | 稳定 | Git 大文件克隆/推送超时或内存溢出 | 中 | 中 | P1 | 否 | Runner/网关容量 | INTENT-REL-004 |
| RISK-REL-06 | 稳定 | Package 上传大文件中断后无法断点续传 | 中 | 低 | P2 | 否 | 用户体验 | INTENT-REL-005 |

---

## 四、兼容性（Compatibility）

| 风险 ID | 维度 | 风险描述 | 影响 | 概率 | 优先级 | 是否 blocker | 依据 | 覆盖意图 |
|---|---|---|---|---|---|---|---|---|
| RISK-COMPAT-01 | 兼容 | GitHub Actions workflow 迁移到 GitCode 后静默行为变更 | 中 | 高 | P1 | 否 | 语法/语义差异 | INTENT-COMPAT-001 |
| RISK-COMPAT-02 | 兼容 | API v5 与 GitHub API v3 字段命名/类型不一致 | 中 | 高 | P1 | 否 | 客户端迁移成本 | INTENT-COMPAT-002 |
| RISK-COMPAT-03 | 兼容 | Git 客户端版本兼容性问题（如 sparse-checkout） | 低 | 低 | P2 | 否 | 边缘场景 | INTENT-COMPAT-003 |
| RISK-COMPAT-04 | 兼容 | Package 仓库协议与标准 registry 不兼容（如 npmrc 配置） | 中 | 中 | P1 | 否 | 工具链集成 | INTENT-COMPAT-004 |

---

## 五、易用性（Usability）

| 风险 ID | 维度 | 风险描述 | 影响 | 概率 | 优先级 | 是否 blocker | 依据 | 覆盖意图 |
|---|---|---|---|---|---|---|---|---|
| RISK-USE-01 | 易用 | 迁移报错不指明 GitCode 差异（用户照抄失败） | 中 | 高 | P1 | 否 | 迁移摩擦 | INTENT-USE-001 |
| RISK-USE-02 | 易用 | 官方文档承诺与实现不一致 / 核心迁移路径文档错误 | 高 | 高 | P0 | 是 | TC-533/TC-273 等实证 | INTENT-USE-031/032/033/046/050 |
| RISK-USE-03 | 易用 | API 错误信息不返回具体字段或业务语义 | 低 | 高 | P2 | 否 | 开发者体验 | INTENT-USE-002 |
| RISK-USE-04 | 易用 | MR/Issue 缺少邮件/站内通知或通知延迟 | 中 | 中 | P1 | 否 | 协作体验 | INTENT-USE-003 |
| RISK-USE-05 | 易用 | Package 版本冲突提示不清晰 | 低 | 中 | P2 | 否 | 开发者体验 | INTENT-USE-004 |

---

## 火力分配建议

- **安全维度**：单列 blocker，从严；建议配懂 CI/CD 攻击面的人复审。P0 项必须全部覆盖。
- **完备性维度**：API 可用性是根基，空数据/分页/越界场景优先。
- **稳定性维度**：并发、速率限制、大文件、Webhook 可靠性为核心。
- **兼容性维度**：GitHub 迁移差异是本次核心资产，默认值/隐式行为差异优先。
- **易用性维度**：文档一致性、错误信息质量、通知可靠性为重点。

> **填写建议**：阿蓁可基于内部历史问题（P0 生产事故、高频客诉）调整「概率」和「优先级」。每确认一个风险项，回写「覆盖意图」列。
