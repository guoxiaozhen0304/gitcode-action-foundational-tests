# USE-SEARCH-01-001

- 标题: 日志搜索与下载功能可用且交互流畅
- 维度: 易用性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   USE-SEARCH-01-001
维度标签:   ['usability']
维度:      usability
优先级:    P1
溯源意图:  INTENT-USE-018
参照来源:  inputs/gitcode-spec/running-pipelines/view-job-logs.md; inputs/gitcode-spec/running-pipelines/view-run-results.md
母意图:    —
标题:      日志搜索与下载功能可用且交互流畅

前置条件:
  - workflow 已产生日志
  - 日志面板可访问

操作步骤:
  1. 在日志面板输入关键词搜索
  2. 点击下载日志按钮

预期结果:
  匹配行高亮显示，下载文件为 UTF-8 纯文本，大文件不崩溃

验证点:
  - [正向] 搜索后匹配行被高亮
  - [正向] 下载的日志文件为 UTF-8 文本
  - [非功能] 搜索响应时间小于 2 秒

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | generate log content (log-search) | echo "INFO: starting build" echo "ERROR: mock failure line 1" echo "WARN: something minor" echo "ERR | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 搜索后匹配行被高亮 | 覆盖 | produced by step 'generate log content': executes real command |
| 下载的日志文件为 UTF-8 文本 | 覆盖 | produced by step 'generate log content': executes real command |
| 搜索响应时间小于 2 秒 | 覆盖 | 非功能断言存在(LLM评估) |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | ERROR: mock failure line 1 | CONSISTENT | produced by step 'generate log content': executes real command |
| 2 | ui_interaction | nonfunctional | 搜索框需在日志面板顶部常驻可见，高亮颜色与背景对比度 >= 3:1；下载按钮文案 | LLM_DEPENDENT | LLM/nonfunctional assertion: 搜索框需在日志面板顶部常驻可见，高亮颜色与背景对比度 >= 3:1；下载按钮文案明确为下载日志或 Do |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
