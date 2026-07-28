# COMPAT-CACHE-01-002
- **标题**: cache 行为等价性——fork PR 写隔离
- **维度**: 兼容性
- **优先级**: P0
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
删除非法断言（negative run_status equals leaked_cache_to_fork，非合法状态值，恒真无意义）；新增确定性断言 must_contain FORK_WRITE_ATTEMPTED（fork 真实写入尝试标记，步骤含 mkdir+写文件真实命令）；隔离/拒绝判定保留 llm 并加注释。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain FORK_WRITE_ATTEMPTED | ✅ GENUINE | 真实写文件后输出 |
| 2 | run_logs | negative | llm_assisted | 🔶 LLM_DEPENDENT | fork save 是否覆盖主干 cache 取决于插件行为（跳过/拒绝/隔离措辞未知） |
| 3 | run_logs | positive | llm_assisted | 🔶 LLM_DEPENDENT | 隔离/拒绝标识为平台日志内容判读 |

### 残留问题
cache 插件的隔离日志措辞未知，平台行为判读保留 llm_assisted（YAML 已注释）；非法断言已清除。
