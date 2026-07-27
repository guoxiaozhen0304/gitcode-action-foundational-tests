# COMPAT-PATHS-01-001
- **标题**: paths 过滤器 300 条边界测试
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**paths 过滤器 300 条边界测试**
- 触发事件: `push` (triggered on branch main)
- 规格引用: INTENT-COMPAT-012
通过标准：
1. workflow 应被平台接受，不报错
2. 匹配路径的 push 事件应正常触发 workflow
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo paths ok | `echo "PATHS_300_OK"` | — | PATHS_300_OK |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | positive | — | ✅ GENUINE | workflow 含 300 条 paths 配置，触发和成功执行依赖平台解析能力 |
| 2 | run_logs must_contain "PATHS_300_OK" | positive | — | ⚠️ STATUS_GUARANTEED | echo "PATHS_300_OK" 是纯字面输出，无 if/uses/${{ }} |
### 问题
- 断言2 为 STATUS_GUARANTEED（纯 echo）
---
