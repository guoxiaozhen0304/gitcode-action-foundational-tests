# SEC-DEFPERM-01-001

- 标题: ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效
- 维度: 安全性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-DEFPERM-01-001
维度标签:   [security]
维度:      安全性
优先级:    P0
溯源意图:  INTENT-SEC-036
参照来源:  inputs/security-knowledge/issues.md; inputs/github-reference/security/
母意图:    —
标题:      ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效

前置条件:
  - 仓库未声明或声明了部分 permissions

操作步骤:
  1. 提交一个 workflow，顶层声明 repository: read，job 级覆盖为 repository: write
  2. 触发 workflow 并验证实际权限

预期结果:
  - 顶层声明被各 job 继承
  - job 级声明覆盖顶层

验证点:
  - [正向] 顶层声明被各 job 继承；job 级声明覆盖顶层
  - [非功能] 权限范围与覆盖关系可被观测判定

清理:      重置 fixture 仓库
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Attempt write (inherit-test) | curl -s -o /dev/null -w "%{http_code}" -X POST \n            "https://api.gitcode.com/api/v5/repos/$ | GENUINE |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 顶层声明被各 job 继承；job 级声明覆盖顶层 | 覆盖 | log assertion without specific string check |
| 权限范围与覆盖关系可被观测判定 | 未覆盖 | 缺少非功能断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative |  | CONSISTENT | log assertion without specific string check |
| 2 | run_logs | positive | 403_or_permission_denied | CONSISTENT | log assertion without specific string check |

### 问题

- 验证点 `权限范围与覆盖关系可被观测判定` → 未覆盖: 缺少非功能断言

---
