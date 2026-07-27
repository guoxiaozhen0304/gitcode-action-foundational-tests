# COMPAT-ENV-01-004
- **标题**: ATOMGIT_ENV 覆写系统默认变量的防护（对齐 GitHub 同名禁止）
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**经环境文件写入 ATOMGIT_ 前缀系统默认变量被拒绝或忽略，覆写尝试在日志中产生警告**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-043
通过标准：
1. 后续步骤读到的变量不应是被污染值
2. 覆写尝试应有警告或拒绝痕迹
3. 普通自定义变量经环境文件正常传递
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Record original workspace | `echo "ORIG_WORKSPACE=$ATOMGIT_WORKSPACE" >> orig_marker.txt` | — | ORIG_WORKSPACE=<原始值> |
| 2 | Attempt override via env file | `echo "ATOMGIT_WORKSPACE=/tmp/override-probe" >> "$ATOMGIT_ENV"; echo "CUSTOM_PROBE=custom-ok" >> "$ATOMGIT_ENV"` | — | 写入环境文件 |
| 3 | Read values in later step | `echo "WORKSPACE_NOW=$ATOMGIT_WORKSPACE" && echo "CUSTOM_NOW=$CUSTOM_PROBE" && echo "PROBE_DONE"` | — | WORKSPACE_NOW=..., CUSTOM_NOW=..., PROBE_DONE |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs WORKSPACE_NOW 不应被污染 | negative | llm_assisted | 🔶 LLM_DEPENDENT |  |
| 2 | must_contain CUSTOM_NOW=custom-ok | positive | — | ✅ GENUINE | 步骤通过 ATOMGIT_ENV 写入并读取自定义变量，真实验证环境文件传递机制 |
| 3 | run_logs 覆写警告痕迹 | positive | llm_assisted | 🔶 LLM_DEPENDENT |  |
---
