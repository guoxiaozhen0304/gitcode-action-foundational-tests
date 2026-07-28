# Abnormal 总结 · 2026-07-28-01

## 总体分布

| 类型 | 数量 | 占比 |
|---|---|---|
| ENV_ERROR | 12 | 27% |
| COMPILE_ERROR | 2 | 5% |
| INCONCLUSIVE | 8 | 18% |
| TIMEOUT | 22 | 50% |
| **合计** | **44** | 100% |

## 根因分类汇总

### 平台缺陷 / 能力边界（10 条）★leader 复核：原 19 条中 workflow_call 9 条移出（非平台缺陷）

| 子类 | 数量 | 说明 |
|---|---|---|
| comment 事件不响应 | 10 | issue_comment / pull_request_comment 不触发 workflow |

> ★ workflow_call 9 条已移出平台缺陷 → 重判 **NOT_CONFIGURED（缺 reusable.yml fixture）**，详见 abnormal-detail.md §1.1。被调文件从未部署（fixture 自动布置未实现），无法据此判定平台是否支持 workflow_call。

### 环境问题 — Harness 侧（8 条）

| 子类 | 数量 | 说明 |
|---|---|---|
| push 冲突 | 1 | 多仓并发导致 git pull --rebase（push-retry/Fix A 已覆盖） |

> ★ leader 复核：原列"untrusted_contributor guard 7 条 = env 变量名不匹配"**已删除**——误诊。代码读文件 `~/.gitcode-contributor-token`（存在）、不读该 env；7 条是 untrusted 无 opt-in 被 guard **正确**拦成 INCONCLUSIVE，非 bug。详见 abnormal-detail.md §2.1。故 Harness 侧真实问题仅 push 冲突 1 条。

### 用例设计 / 夹具问题（8 条）

| 子类 | 数量 | 说明 |
|---|---|---|
| paths 无变更匹配 | 3 | push 内容不匹配 paths filter |
| YAML 不合规 | 2 | runs-on 格式 / step name 非法字符 |
| dispatch inputs 校验 | 2 | payload 格式与平台不匹配 |
| 日志不可得 | 1 | 无法判定 |

### 超时 — 混合原因（9 条）

| 子类 | 数量 | 说明 |
|---|---|---|
| 边界测试设计如此 | 2 | REL-TIMEOUT 系列 600s 白名单 |
| dispatch 长时 | 2 | 不在白名单的 dispatch 用例 |
| 调度/索引慢 | 5 | 平台调度延迟 + 部分用例本身耗时 |

## 目录结构

```
failure/2026-07-28-01/abnormal/
├── abnormal-detail.md          ← 明细（含根因分析）
├── abnormal-summary.md         ← 本文件
├── ENV_ERROR/                  ← 12 条 (json + log.txt)
├── COMPILE_ERROR/              ← 2 条
├── INCONCLUSIVE/               ← 8 条
└── TIMEOUT/                    ← 22 条
```
