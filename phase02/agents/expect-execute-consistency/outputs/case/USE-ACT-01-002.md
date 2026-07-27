# USE-ACT-01-002
- **标题**: 使用 actions/checkout@v4 时报错应给出迁移指引
- **维度**: 易用性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**使用 actions/checkout@v4 时报错应给出迁移指引**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-007
通过标准：
1. 不应静默失败或报泛化的 Action 不存在
2. 报错中应包含 checkout 短名提示

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout with github style | uses: actions/checkout@v4 | - | GitHub 风格 action 引用，平台应拒绝并报错 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | ✅ GENUINE | `uses: actions/checkout@v4` 为 GitHub 风格引用，在 GitCode 应解析失败，运行不应完成 |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 非功能断言，需 LLM 判定报错文本是否包含迁移指引 |
---
