# SEC-DEFPERM-01-002

- 标题: job 级覆盖后权限正确收窄
- 维度: 安全性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-DEFPERM-01-002
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-036
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    SEC-DEFPERM-01-001
标题:      job 级覆盖后权限正确收窄

前置条件:
  - 仓库声明了顶层 permissions: repository: write

操作步骤:
  1. 提交一个 workflow，顶层声明 repository: write，job 级覆盖为 repository: read
  2. 触发 workflow 并验证 job 实际权限

预期结果:
  - job 级收窄后不应仍保留顶层的更大权限
  - token 实际权限应与 job 级声明一致

验证点:
  - [负向] job 级收窄后不应仍保留顶层的更大权限
  - [正向] 各权限域实测与有效声明一致，越权写被拒

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Attempt write after override (override-test) | curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/$ | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| job 级收窄后不应仍保留顶层的更大权限 | 覆盖 | log assertion without specific string check |
| 各权限域实测与有效声明一致，越权写被拒 | 覆盖 | log assertion without specific string check |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | CONSISTENT | log assertion without specific string check |
| 2 | run_logs | positive | 403_or_permission_denied | CONSISTENT | log assertion without specific string check |

### 问题

- 所有验证点均被覆盖，步骤与断言一致

---
