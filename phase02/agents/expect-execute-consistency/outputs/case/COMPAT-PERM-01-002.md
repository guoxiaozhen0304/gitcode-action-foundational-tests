# COMPAT-PERM-01-002

- 标题: 未声明 permissions 时 fork PR 写操作隔离
- 维度: 兼容性 | 优先级: P0
- 评级: 部分不符

---

## 1. 想测什么（规格）

标题: 未声明 permissions 时 fork PR 写操作隔离

- [负向] 写操作（如 git push 或 API 写调用）失败或被阻止
- [负向] 目标仓库内容未被修改
- [正向] fork 身份无法获得写权限

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | checkout source | uses: checkout | Y |
| 2 | attempt write | git config user.email "test@example.com" git config user.name "Test" echo "test" > test_file.txt git | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| negative | run_status | success |
| negative | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | fork_pr |
| 身份 | untrusted_contributor |
| 触发阻塞 | 是 (untrusted_contributor trigger) |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] 写操作（如 git push 或 API 写调用）失败或被阻止 | COVERED | negative assertion present |
| [负向] 目标仓库内容未被修改 | COVERED | negative assertion present |
| [正向] fork 身份无法获得写权限 | WEAK | 1 real steps but no assertions |

### 问题

- [正向] fork 身份无法获得写权限: 1 real steps but no assertions

---
