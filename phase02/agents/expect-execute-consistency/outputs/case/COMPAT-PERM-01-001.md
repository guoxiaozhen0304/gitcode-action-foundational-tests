# COMPAT-PERM-01-001
- **标题**: 未声明 permissions 时默认 TOKEN 读操作权限范围
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**未声明 permissions 时默认 TOKEN 读操作权限范围**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-002
通过标准：
1. 系统在 workflow 未声明 permissions 时，赋予默认 TOKEN 足够的读权限
2. checkout 和文件读取操作成功执行
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | read repo file | `cat README.md` | — | README 内容 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status equals success | positive | — | ✅ GENUINE | uses: checkout 和 cat README.md 均为真实操作，依赖默认 TOKEN 权限才能成功 |
| 2 | run_logs contains "README" | positive | — | ✅ GENUINE | cat README.md 的输出依赖文件存在和具读取权限，若权限不足则不含此字符串 |
---
