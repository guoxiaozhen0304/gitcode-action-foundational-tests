# USE-SEARCH-01-001
- **标题**: 日志搜索与下载功能可用且交互流畅
- **维度**: usability
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**日志搜索与下载功能可用且交互流畅**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-018
通过标准：
1. 搜索后匹配行被高亮
2. 下载的日志文件为 UTF-8 文本
3. 搜索响应时间小于 2 秒

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | generate log content | 5 次 `echo` 输出不同日志行 | 无 | 日志内容含 ERROR/WARN 行 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs contains "ERROR: mock failure line 1" | positive | 纯 echo 硬编码字符串 | ⚠️ STATUS_GUARANTEED | 步骤纯 echo 无平台行为依赖，字符串必然输出 |
| 2 | ui_interaction eval=llm_assisted | nonfunctional | LLM 判定搜索框、高亮、下载按钮等 UI 交互 | 🔶 LLM_DEPENDENT | 需 LLM 辅助判定 UI 交互 |

### 问题
断言 1 为纯 echo 硬编码，trivially guaranteed；断言 2 依赖 LLM 判定 UI。
---
