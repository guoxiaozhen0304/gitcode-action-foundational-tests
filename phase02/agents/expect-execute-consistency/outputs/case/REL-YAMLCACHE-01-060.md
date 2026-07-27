# REL-YAMLCACHE-01-060
- **标题**: Workflow YAML 缓存失效——修改后无旧代码残留
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**修改 workflow 后触发，新日志出现 marker_v2，旧 marker_v1 不残留**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-060
通过标准：
1. 新触发日志包含 marker_v2
2. 日志不包含 marker_v1
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | echo marker | `echo marker_v1` | — | marker_v1 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 日志包含 marker_v2 | positive | run_logs contains "marker_v2" | ❌ MISSING_SOURCE | YAML 步骤仅 echo marker_v1，无任何步骤产生 marker_v2；依赖外部 workflow 修改 |
| 2 | 日志不含 marker_v1 | negative | run_logs contains "marker_v1" | ✅ GENUINE | 步骤 echo marker_v1 会输出该字符串，断言检查修改后缓存失效是否残留；依赖平台缓存行为 |
### 问题
断言 1 MISSING_SOURCE：依赖外部 workflow 修改产生 marker_v2，但 YAML 中无对应源步骤。
---
