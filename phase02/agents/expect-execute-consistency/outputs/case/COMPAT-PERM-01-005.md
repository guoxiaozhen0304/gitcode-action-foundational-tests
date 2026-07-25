# COMPAT-PERM-01-005

- 标题: permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异
- 维度: 兼容性 | 优先级: P0
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: permissions 空对象时 ATOMGIT_TOKEN 默认权限范围差异

- [正向] 读操作成功
- [负向] 写操作被平台拒绝

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | Try read with token | curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $ATOMGIT_TOKEN" "$ATOMGIT_API_URL/u | Y |
| 2 | Try write with token | curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer $ATOMGIT_TOKEN" -X POST "$ATOMGIT_A | Y |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | run_logs |  |
| negative | run_logs |  |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 读操作成功 | COVERED | 2 real steps, assertions present |
| [负向] 写操作被平台拒绝 | COVERED | negative assertion present |

### 问题

无重大问题。

---
