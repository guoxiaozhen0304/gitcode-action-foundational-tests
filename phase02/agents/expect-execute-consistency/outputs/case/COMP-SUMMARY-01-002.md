# COMP-SUMMARY-01-002
- **标题**: summary 中不应暴露系统内部路径
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**summary 中不应暴露系统内部路径**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-018
通过标准：
1. summary 中不出现 /tmp/runner-xxx 等内部路径（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Write safe summary | `echo "Results: OK" >> "$ATOMGIT_STEP_SUMMARY"` | - | 安全内容写入 summary |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_summary | negative | must_not_contain: /tmp/runner | ✅ GENUINE | 步骤写入 $ATOMGIT_STEP_SUMMARY 平台功能，harness 验证 summary 渲染内容不含 Runner 内部路径 |
| 2 | step_summary | negative | must_not_contain: /opt/actions | ✅ GENUINE | 同上，验证 summary 不含系统内部路径 |
---
