# SEC-TOKEN-01-001
- **标题**: fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限
- **维度**: 安全性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**fork PR 触发 pull_request 时 ATOMGIT_TOKEN 必须仅拥有 read 权限**
- 触发事件: `pull_request`
- 规格引用: INTENT-SEC-003
通过标准：
1. ATOMGIT_TOKEN 可成功执行 clone 等读操作
2. 尝试写操作应返回 403 或失败

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Clone with token | `git clone https://x-access-token:${{ atomgit.token }}@...` | - | git clone 输出（Cloning into... 或错误） |
| 2 | Attempt write via API | `curl -s -o /dev/null -w "%{http_code}" -X POST ...` | - | HTTP 状态码（如 200/403） |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals: "clone_successful" | ❌ MISSING_SOURCE | git clone 不输出该字符串，curl 也不输出。无步骤 echo 该标记 |
| 2 | run_logs | negative | must_not_contain: "write_permission_granted" | ❌ MISSING_SOURCE | curl 仅输出 HTTP 状态码（如 200 或 403），不输出该字符串。无论如何该字符串均不出现——断言空洞为真 |

### 问题
**断言 1 — MISSING_SOURCE**: git clone 和 curl 步骤执行了真实操作（clone + API write），但无步骤输出 "clone_successful" 字符串。
**断言 2 — MISSING_SOURCE**: curl 步骤仅输出 HTTP 数字状态码，不产生 "write_permission_granted" 字符串。即使写操作被错误允许（返回 200），该字符串也不会出现在日志中，断言永远为真。
---
