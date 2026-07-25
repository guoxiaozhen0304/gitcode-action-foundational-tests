# COMPAT-PERM-01-004

- 标题: permissions 命名差异——GitCode repository 权限项正常生效
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: permissions 命名差异——GitCode repository 权限项正常生效

- [正向] workflow 解析阶段无报错
- [正向] 工作流成功执行仓库读取操作
- [正向] repository 权限项语义与 GitCode 平台预期一致

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) checkout with repository read | uses: checkout | Y |
| 2 | (TC) verify repo access | if [ -f "README.md" ]; then   echo "REPOSITORY_PERM_OK" else   echo "REPOSITORY_PERM_FAILED"   exit  | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_status | completed_success |
| positive | run_logs |  |
| negative | run_logs |  |
| negative | workflow_parse |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] workflow 解析阶段无报错 | COVERED | 2 real steps, assertions present |
| [正向] 工作流成功执行仓库读取操作 | COVERED | 2 real steps, assertions present |
| [正向] repository 权限项语义与 GitCode 平台预期一致 | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
